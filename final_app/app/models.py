from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str


class DrugSearch(BaseModel):
    drug_name: str