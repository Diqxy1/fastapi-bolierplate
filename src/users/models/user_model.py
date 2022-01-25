from pydantic import BaseModel
from typing import Optional

class CreateUserModel(BaseModel):
    id: Optional[int]
    name: str
    password: str

    class Config:
        orm_mode = True

class UserModel(BaseModel):
    name: str
    password: str