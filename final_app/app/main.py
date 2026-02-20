from fastapi import FastAPI, HTTPException
from typing import Dict, List
from app.models import UserCreate, DrugSearch
from app.fda_service import FDAService

app = FastAPI()

users: Dict[int, dict] = {}
notes: Dict[int, List[str]] = {}

fda_service = FDAService()


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


@app.get("/users/{user_id}/notes")
def get_notes(user_id: int):

    if user_id not in users:
        raise HTTPException(status_code=404)

    return notes[user_id]


@app.post("/users/{user_id}/search-and-save")
def search_and_save(user_id: int, search: DrugSearch):

    if user_id not in users:
        raise HTTPException(status_code=404)

    side_effects = fda_service.search(search.drug_name)

    if not side_effects:
        raise HTTPException(status_code=404, detail="Drug not found")

    note_text = f"FDA side effects for {search.drug_name}: {side_effects}"

    notes[user_id].append(note_text)

    return {"saved_note": note_text}