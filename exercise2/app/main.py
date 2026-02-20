from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List


app = FastAPI()

users: Dict[int, dict] = {}
notes: Dict[int, List[str]] = {}


class UserCreate(BaseModel):
    username: str


class NoteCreate(BaseModel):
    text: str


@app.post("/users")
def create_user(user: UserCreate):

    for u in users.values():
        if u["username"] == user.username:
            raise HTTPException(status_code=409, detail="Username already exists")

    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "username": user.username}
    notes[user_id] = []

    return users[user_id]


@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(status_code=404)

    return users[user_id]


@app.post("/users/{user_id}/notes")
def add_note(user_id: int, note: NoteCreate):

    if user_id not in users:
        raise HTTPException(status_code=404)

    notes[user_id].append(note.text)

    return {"message": "Note added"}


@app.get("/users/{user_id}/notes")
def get_notes(user_id: int):

    if user_id not in users:
        raise HTTPException(status_code=404)

    return notes[user_id]