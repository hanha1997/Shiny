import email
from typing import Optional
from pydantic import BaseModel
from pydantic import EmailStr


# properties required during user creation
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
  


class ShowUser(BaseModel):
    id : int
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    url_image: Optional[str] = None
   


    class Config:  # to convert non dict obj to json
        orm_mode = True

class UserLogin(BaseModel):
    email:EmailStr
    password:str
