
from pydantic import EmailStr
from core.hashing import Hasher
from db.models.users import User
from schemas.users import UserCreate
from sqlalchemy.orm import Session



def create_new_user(user: UserCreate, db: Session):
    user = User(
        name=user.name,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: EmailStr, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user

def get_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    return user