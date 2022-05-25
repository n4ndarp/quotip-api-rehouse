from sqlalchemy.orm import Session
from . import model, schema

def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()

def get_user_username(db: Session, username: str):
    return db.query(model.User).filter(model.User.username == username).first()

def get_user_story(db: Session, user_id: int):
    return db.query(model.Story).filter(model.Story.user_id == user_id).first()

def make_user(db: Session, user: schema.UserCreate):
    hashed_password = user.password + "bapakkaus4lt0"
    db_user = model.User(username=user.username, hashed_password=hashed_password, name=user.name, biography=user.biography)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_story(db: Session, story: schema.StoryCreate, user_id: int): #currently broken
    db_story = model.Story(story=story.story, user_id=user_id)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story
