import streamlit as st
from pathlib import Path
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.agents import initialize_agent
from sqlalchemy.exc import SQLAlchemyError

Groq_api_key = st.secrets["GROQ_API_KEY"]

st.set_page_config(page_title="Chat with Your DB")
st.title("Chat with Your Database")
st.markdown("Use this agent to chat with your MySQL local database")

st.sidebar.title("Database Connection")
mysql_host = st.sidebar.text_input("Provide MySQL Host", placeholder=" for eg :- localhost:3306")
mysql_user = st.sidebar.text_input("MySQL User", placeholder=" for eg :- root")
mysql_password = st.sidebar.text_input("MySQL Password", type="password")
mysql_db = st.sidebar.text_input("MySQL Database", placeholder= "Database name")

llm = ChatGroq(
    groq_api_key=Groq_api_key,
    model_name="llama-3.3-70b-versatile",
    streaming=True,
    #prompt="You are a helpful SQL agent that helps people query the database.Use your memory if the user asked without context.",
    temperature=0.3
)

@st.cache_resource(ttl="2h")
def configure_db(mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    try:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error(" Please provide all MySQL connection details.")
            st.stop()

        engine = create_engine(
            f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"
        )
        return SQLDatabase(engine)

    except SQLAlchemyError as e:
        st.error(f" Database connection failed: {str(e)}")
        st.stop()
    except Exception as e:
        st.error(f" Unexpected error while connecting to DB: {str(e)}")
        st.stop()

try:
    db = configure_db(mysql_host, mysql_user, mysql_password, mysql_db)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools=toolkit.get_tools(),
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory
    )
    if "messages" not in st.session_state or st.sidebar.button("Clear Chat"):
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        memory.clear()  


    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # User input
    user_query = st.chat_input(placeholder="Ask anything from the database")
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        with st.chat_message("assistant"):
            try:
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.write(response)
            except SQLAlchemyError as e:
                st.error(f" Database error: {str(e)}")
            except Exception as e:
                st.error(f"Something went wrong while processing your query: {str(e)}")

except Exception as e:
    st.error(f" Fatal error initializing app: {str(e)}")
