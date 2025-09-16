# 🗃️ Chat with Your Database
## 🚀 Live Demo: [Click Here](https://chat-db-harsh-pilania.streamlit.app/)

A powerful Streamlit application that allows you to interact with your MySQL database using natural language queries powered by AI. Simply ask questions in plain English and get instant results from your database!

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=flat&logo=mysql&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=flat&logo=chainlink&logoColor=white)

## 🚀 Features

- **Natural Language Queries**: Ask questions about your data in plain English
- **Real-time Streaming**: Get responses as they're generated
- **Memory Support**: Maintains conversation context for follow-up questions
- **Secure Connection**: Encrypted password input for database security
- **Error Handling**: Comprehensive error messages for troubleshooting
- **Easy-to-use Interface**: Clean and intuitive Streamlit UI

## 🛠️ Technologies Used

<div align="center">

| Technology | Purpose | Logo |
|------------|---------|------|
| **Streamlit** | Web Application Framework | <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="40"> |
| **LangChain** | AI Agent Framework | <img src="https://python.langchain.com/img/brand/wordmark.png" width="80"> |
| **MySQL** | Database Management | <img src="https://labs.mysql.com/common/logos/mysql-logo.svg" width="60"> |
| **Groq** | AI Language Model | <img src="https://groq.com/wp-content/uploads/2024/03/PBG-mark1-color.svg" width="40"> |
| **SQLAlchemy** | Database ORM | <img src="https://www.sqlalchemy.org/img/sqla_logo.png" width="60"> |

</div>

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Python 3.8+** installed on your system
2. **MySQL Server** running locally or remotely
3. **Groq API Key** (free tier available at [Groq Console](https://console.groq.com/))
4. A **MySQL database** with some data to query

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/database-chat-app.git
   cd database-chat-app
   ```

2. **Install required packages**
   ```bash
   pip install streamlit langchain langchain-groq sqlalchemy mysql-connector-python
   ```

3. **Set up Groq API Key**
   
   Create a `.streamlit/secrets.toml` file in your project directory:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

## 🚀 Usage

### Step 1: Start the Application
```bash
streamlit run app.py
```

### Step 2: Configure Database Connection

When the application opens, you'll see the sidebar with database connection fields:

![Database Connection Example](https://via.placeholder.com/400x300/2E3440/FFFFFF?text=Database+Connection+Sidebar)

Fill in your MySQL connection details:

- **MySQL Host**: Your database server address
  - For local MySQL: `localhost` or `127.0.0.1:3306`
  - For remote MySQL: `your-server-ip:3306`
- **MySQL User**: Your database username (e.g., `root`)
- **MySQL Password**: Your database password
- **MySQL Database**: Name of your database

#### Example Configuration:
```
MySQL Host: localhost:3306
MySQL User: root  
MySQL Password: ••••••••
MySQL Database: company_db
```

### Step 3: Start Chatting!

Once connected, you can start asking questions about your database:

#### Example Queries:
- "How many employees do we have?"
- "Show me the top 5 highest paid employees"
- "What's the average salary by department?"
- "List all customers from California"
- "Find products with stock less than 10"

#### Follow-up Questions:
The app remembers context, so you can ask follow-up questions:
- First: "Who is the oldest employee?"
- Then: "What's their salary?" *(remembers the oldest employee)*

### Step 4: View Results

The AI will:
1. Understand your question
2. Generate appropriate SQL queries
3. Execute them on your database
4. Present results in a readable format


## 🔒 Security Notes

- Database passwords are masked in the UI
- Connection details are not stored permanently
- Use environment variables for production deployments
- Ensure your MySQL server has proper access controls

## ⚠️ Common Issues & Solutions

### Connection Issues
- **Error**: "Database connection failed"
  - **Solution**: Verify MySQL server is running and credentials are correct
  - Check if MySQL is listening on the specified port (default: 3306)

### Permission Issues
- **Error**: "Access denied for user"
  - **Solution**: Ensure the MySQL user has SELECT privileges on the database

### Package Issues
- **Error**: "Module not found"
  - **Solution**: Install missing packages using pip install
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues:

1. Check the [Common Issues](#-common-issues--solutions) section
2. Open an issue on GitHub
3. Provide your error logs and configuration (without sensitive data)


<div align="center">

**Made with ❤️ using Streamlit and LangChain**

[⭐ Star this repo](https://github.com/yourusername/database-chat-app) if you found it helpful!

</div>
