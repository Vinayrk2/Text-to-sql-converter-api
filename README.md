# FastAPI Text-to-SQL API with Authentication

This is a FastAPI-based application that converts natural language queries into SQL using a pre-trained Hugging Face model. The project includes authentication and database execution functionalities.

## Features

- User authentication using JWT tokens.
- Convert natural language queries to SQL.
- Execute generated SQL queries on a SQLite database.
- Secure API endpoints with authentication.

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/fastapi-text2sql.git
cd fastapi-text2sql
```

### 2. Create a Virtual Environment (Optional but Recommended)

```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set Up the Database

Run the following command to create the SQLite database:

```
python database.py
```

### 5. Run the FastAPI Server

```
uvicorn app.main:app --reload
```

Server will be running at: 📍 [**http://127.0.0.1:8000**](http://127.0.0.1:8000)

## Authentication

1. Obtain a token by sending a **POST** request to `/token` with username and password.
2. Use the token for authentication when calling protected endpoints.

### Example: Getting a Token (Using `httpie`)

```
http -f POST http://127.0.0.1:8000/token username=test_user password=password
```

- Or can check all the endpoints from the test.rest file.
- [optional] just install the 'REST Client' extension on the VS Code. And Run Server and Click on 'Send Request' for the response.

## API Endpoints

### 1. Authentication

| Method | Endpoint | Description         |
| ------ | -------- | ------------------- |
| POST   | `/register` | For the new user |
| POST   | `/token` | Generates JWT token |

### 2. Query Processing

| Method | Endpoint | Description                     |
| ------ | -------- | ------------------------------- |
| POST   | `/query` | Convert natural language to SQL |

### 3. SQL Execution

| Method | Endpoint   | Description                 |
| ------ | ---------- | --------------------------- |
| POST   | `/execute` | Execute generated SQL query |

## Deployment on Deta.sh

1. **Install Deta CLI**
   ```
   curl -fsSL https://get.deta.dev/cli.sh | sh
   ```
2. **Login to Deta**
   ```
   deta login
   ```
3. **Deploy the Application**
   ```
   deta new fastapi-text2sql
   deta deploy
   ```

Your API will be live at `https://your-app-name.deta.dev`

## License

This project is licensed under the MIT License.

