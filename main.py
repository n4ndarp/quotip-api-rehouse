from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import crud, model, schema
from database.db import SessionLocal, engine


app = FastAPI()
model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schema.User)
def post_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.make_user(db, user=user)

@app.get("/user/{berak}", response_model=schema.UserGet)
def get_user(berak: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=berak)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    return db_user

@app.post("/user/{user_id}/story") #currently broken
def post_user_story(user_id: int, story: schema.StoryCreate, db: Session = Depends(get_db)):
    return crud.create_user_story(db=db, story=story.story, user_id=user_id)