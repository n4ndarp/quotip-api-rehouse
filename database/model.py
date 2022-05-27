from email.policy import default
from sqlalchemy import TEXT, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base
import uuid

def genUUID():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(45), unique=True, nullable=False)
    hashed_password = Column(String(45), nullable=False)
    name = Column(String(45), nullable=False)
    biography = Column(String(250), nullable=False)
    story = relationship("Story")


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    story = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    quote_id = Column(Integer, ForeignKey("quotes.id"))
    quote = relationship("Quote", back_populates="story")
    #quote = relationship("Quote", back_populates="story")
    #user = relationship("User", back_populates="story")

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(45), nullable=False)
    story = relationship("Story", back_populates="quote")