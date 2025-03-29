from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import SessionLocal, User
from app.auth import authenticate_user, create_token, get_db
from app.routes import router
import bcrypt
from pydantic import BaseModel

app = FastAPI()
app.include_router(router)

class RegisterRequest(BaseModel):
    username: str
    password: str

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_token(user.username), "token_type": "bearer"}


@app.post("/register")
def register(user_data: RegisterRequest, db: Session = Depends(get_db)):
    try:
        if db.query(User).filter(User.username == user_data.username).first():
            raise HTTPException(status_code=400, detail="Username already exists")
        hashed_pw = bcrypt.hashpw(user_data.password.encode(), bcrypt.gensalt()).decode()
        new_user = User(username=user_data.username, hashed_password=hashed_pw)
        db.add(new_user)
        db.commit()
        return {"message": "User registered successfully"}
    except Exception as e:
        return e
