# FDA Notes App

A backend API project that allows users to:
- Search adverse drug events from the openFDA API
- Extract useful JSON fields (e.g., side effects)
- Save results as user notes


---

## 📂 Project Structure
fda-notes-app/
│
├── exercise1/ # FDA API exploration
├── exercise2/ # User + Notes API
├── final_app/ # Combined application
├── requirements.txt
└── README.md


---

## 🚀 Quick Start

1. Clone the repo
git clone https://github.com/HongruZeng/fda-notes-app.git

cd fda-notes-app

2. Install dependencies
pip install -r requirements.txt


---

## 🧪 Exercise 1

Explore the openFDA API using Python.
cd exercise1
python run_exercise1.py


---

## 🧰 Exercise 2

FastAPI user & notes API:


cd exercise2
uvicorn app.main:app --reload


---

## 📌 Final App

This combines both functionalities. To run:


cd final_app
uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs


---

## 🛠 API Examples

**1) Create User**


POST /users
{ "username": "grandma" }


**2) Search & Save**


POST /users/1/search-and-save
{ "drug_name": "aspirin" }


**3) Get Notes**


GET /users/1/notes


---

## 📌 Requirements

This project uses:

fastapi
uvicorn
requests

...as listed in `requirements.txt`.
