from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sympy import quo
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

@app.post("/register", response_model=schema.User) #register users
def post_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.make_user(db, user=user)

@app.get("/user/{user_id}", response_model=schema.UserGet) #get a user's details
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    return db_user

@app.post("/user/{user_id}/story", response_model=schema.StoryDef) #post story for a user
def post_user_story(user_id, story: schema.StoryCreate, db: Session = Depends(get_db)):
    return crud.create_user_story(db=db, story=story, user_id=user_id)

@app.get("/user/{user_id}/story") #returns all of a user's story (use query parameter last=True to return newest story)
def get_all_user_story(user_id, last: bool = False, db: Session = Depends(get_db)):
    db_story = crud.get_all_user_story(db, user_id=user_id, last=last)
    if db_story is None:
        raise HTTPException(status_code=404, detail="No story exists")
    return db_story

@app.post("/post/quote", response_model=schema.Quote)
def post_quote(quote: schema.QuoteCreate, db: Session = Depends(get_db)):
    return crud.make_quote(db, quote=quote)

@app.get("/get/quote")
def get_quotes(db: Session = Depends(get_db)):
    return crud.get_quotes(db)