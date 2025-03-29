FastAPI Text-to-SQL API with Authentication

This is a FastAPI-based application that converts natural language queries into SQL using a pre-trained Hugging Face model. The project includes authentication and database execution functionalities.

Features

User authentication using JWT tokens.

Convert natural language queries to SQL.

Execute generated SQL queries on a SQLite database.

Secure API endpoints with authentication.

Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/fastapi-text2sql.git
cd fastapi-text2sql

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up the Database

Run the following command to create the SQLite database:

python database.py

5. Run the FastAPI Server

uvicorn app.main:app --reload

Server will be running at:
📍 http://127.0.0.1:8000

Authentication

Register or manually add a user to the database.

Obtain a token by sending a POST request to /token with username and password.

Use the token for authentication when calling protected endpoints.

Example: Getting a Token (Using httpie)

http -f POST http://127.0.0.1:8000/token username=test_user password=password

API Endpoints

1. Authentication

Method

Endpoint

Description

POST

/token

Generates JWT token

2. Query Processing

Method

Endpoint

Description

POST

/query

Convert natural language to SQL

3. SQL Execution

Method

Endpoint

Description

POST

/execute

Execute generated SQL query

Deployment on Deta.sh

Install Deta CLI

curl -fsSL https://get.deta.dev/cli.sh | sh

Login to Deta

deta login

Deploy the Application

deta new fastapi-text2sql
deta deploy

Your API will be live at https://your-app-name.deta.dev

License

This project is licensed under the MIT License.

