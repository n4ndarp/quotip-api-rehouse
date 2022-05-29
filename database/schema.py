from typing import List, Union
from pydantic import BaseModel
from pydantic.schema import Optional

class StoryBase(BaseModel):
    story: str

class StoryCreate(StoryBase):
    pass

class Story(StoryBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class StoryOut(StoryBase):
    class Config:
        orm_mode = True

#===========================================================

class QuoteBase(BaseModel):
    text: str

class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int
    story: Optional[List[Story]] = []
    class Config:
        orm_mode = True

class QuoteGet(BaseModel):
    id: int
    text: str
    story: Optional[List[Story]] = []
    class Config:
        orm_mode = True    

class StoryDef(Story):
    quote: Optional[List[Quote]] = []
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

class UserGet(UserBase): #idk if this stuff's any different from ^ but this doesn't give me errors
    story: List[Story] = []
    class Config:
        orm_mode = True  