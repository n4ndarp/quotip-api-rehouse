from typing import List, Union
from pydantic import BaseModel

class StoryBase(BaseModel):
    story: str
    user_id: int
    quote_id: int

class StoryCreate(StoryBase):
    pass

class Story(StoryBase):
    id: str

    class Config:
        orm_mode = True

#===========================================================

class QuoteBase(BaseModel):
    text: str

class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: str
    story: List[Story] = []

    class Config:
        orm_mode = True

#===========================================================

class UserBase(BaseModel):
    username: str
    name: str
    biography: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    story: List[Story] = []

    class Config:
        orm_mode = True

class UserGet(BaseModel): #very crude alternative. currently using this until i know what shit happened
    username: str
    name: str
    biography: str
    story: List[Story] = []

    class Config:
        orm_mode = True  