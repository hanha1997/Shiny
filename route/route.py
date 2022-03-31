from typing import List
from pydantic import EmailStr
from db.models.users import User
from db.repository.users import create_new_user, get_user_by_email, get_user_by_id
from fastapi import FastAPI, File, Response, UploadFile
from fastapi import Depends
from database import get_db
from schemas.users import UserCreate,ShowUser
from sqlalchemy.orm import Session
from core.hashing import Hasher
from fastapi import Response


router = FastAPI()


@router.post("/users", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.get("/user/{user_id}", response_model=ShowUser) 
def get_user(user_id:int, db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db=db)
    return user

@router.post("/login", response_model=ShowUser)
def login(email:EmailStr , password:str, db: Session = Depends(get_db)):
    user = get_user_by_email(email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user
  
@router.put("/user/{user_id}/upload")
def upload(user_id:int, file: UploadFile = File(...) , db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db=db)
    user.url_image = file.filename
    db.commit()
    db.refresh(user)
    return user

