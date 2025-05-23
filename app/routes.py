import torch
from fastapi import APIRouter, Depends, HTTPException
from transformers import T5Tokenizer, T5ForConditionalGeneration
from app.auth import get_current_user  # Assuming you have authentication set up
from pydantic import BaseModel

class SQLQueryRequest(BaseModel):
    natural_language: str
    
router = APIRouter()

# Load the tokenizer and model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('cssupport/t5-small-awesome-text-to-sql').to(device)
model.eval()

def generate_sql(input_prompt: str) -> str:
    """Generates an SQL query from a natural language input."""
    try:
        inputs = tokenizer(input_prompt, padding=True, truncation=True, return_tensors="pt").to(device)

        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=512)

        generated_sql = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_sql

    except Exception as e:
        raise Exception(f"Error generating SQL: {str(e)}")



@router.post("/query")
def generate_sql_endpoint(request: SQLQueryRequest, user: str = Depends(get_current_user)):
    try:
        input_prompt = f"""
tables:
CREATE TABLE students (
    student_id VARCHAR PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    enrollment_date DATE
);

CREATE TABLE courses (
    course_id VARCHAR PRIMARY KEY,
    course_name VARCHAR(100),
    instructor VARCHAR(100),
    credits INT
);

CREATE TABLE student_course_attendance (
    attendance_id SERIAL PRIMARY KEY,
    student_id VARCHAR REFERENCES students(student_id) ON DELETE CASCADE,
    course_id VARCHAR REFERENCES courses(course_id) ON DELETE CASCADE,
    attendance_date DATE,
    status VARCHAR(20) CHECK (status IN ('Present', 'Absent', 'Late'))
);

query for: {request.natural_language}
"""


        sql_query = generate_sql(input_prompt)
        return {"sql_query": sql_query}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))