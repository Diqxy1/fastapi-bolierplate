from sqlalchemy import Column, String , Integer
from src.config.database import Base

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25))
    password = Column(String(25))