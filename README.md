# FDA Notes App

A backend API project built with FastAPI that allows users to:

- Search adverse drug event data from the openFDA API
- Extract useful JSON fields (e.g., side effects)
- Save results as personal notes
- Retrieve saved notes

This project demonstrates API integration, JSON parsing, pagination, error handling, and RESTful API design.

---

# 📂 Project Structure

```
fda-notes-app/
│
├── exercise1/        # FDA API exploration using Python requests
├── exercise2/        # FastAPI user & notes system
├── final_app/        # Combined application (FDA + Users)
├── requirements.txt
└── README.md
```

---

# 📝 User Stories

## Exercise 1

As a user, I want to search adverse drug events from the FDA database so that I can understand potential side effects of a medication.

## Exercise 2

As a user, I want to create an account and manage personal notes so that I can store and retrieve my own information.

## Final

As a user, I want to search FDA drug side effects and automatically save them as notes in my account so that I can keep track of important drug safety information.

---

# 🚀 Quick Start

## 1️⃣ Clone Repository

```
git clone https://github.com/HongruZeng/fda-notes-app.git
cd fda-notes-app
```

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# 🧪 Exercise 1 – FDA API Exploration

Demonstrates:

- openFDA API usage
- Query parameters (`search`, `limit`)
- Pagination (`skip`)
- Handling empty results
- Extracting useful JSON fields (`reactionmeddrapt`)
- Testing with Python `requests`
- Experimenting with curl and Postman

Run:

```
cd exercise1
python run_exercise1.py
```

---

# 🧰 Exercise 2 – User & Notes API (FastAPI)

Implements:

- Create user
- Retrieve user by ID
- Add text notes
- Retrieve notes
- Return `409` if username already exists

Run:

```
cd exercise2
uvicorn app.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

---

# 🏆 Final App – Combined Version

Combines Exercise 1 + Exercise 2.

New Endpoint:

POST `/users/{user_id}/search-and-save`

This endpoint:

1. Calls the openFDA API
2. Extracts side effects
3. Saves them as a user note
4. Returns the saved result

Run:

```
cd final_app
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 🔌 API Examples

## 1️⃣ Create User

POST `/users`

```
{
  "username": "grandma"
}
```

---

## 2️⃣ Search and Save FDA Data

POST `/users/1/search-and-save`

```
{
  "drug_name": "aspirin"
}
```

---

## 3️⃣ Get User Notes

GET `/users/1/notes`

Response:

```
[
  "FDA side effects for aspirin: [...]"
]
```

---

# 📚 Requirements

Main dependencies:

- fastapi
- uvicorn
- requests

Full list available in `requirements.txt`.

