\# FDA Notes App



\## Project Structure



fda-notes-app/

│

├── exercise1/        # FDA API exploration

├── exercise2/        # User + Notes API

├── final\_app/        # Combined application

│

├── requirements.txt

└── README.md





---



\## Exercise 1



\- Explore openFDA API

\- Use requests library

\- Query parameters (search, limit)

\- Pagination (skip)

\- Extract useful JSON fields (reactionmeddrapt)

\- Handle empty results



Run:



cd exercise1

python run\_exercise1.py





---



\## Exercise 2



\- Create user

\- Get user by ID

\- Add notes

\- Get notes

\- Return 409 if username exists



Run:



cd exercise2

uvicorn app.main:app --reload





---



\## Final App



Combine Exercise 1 + 2



New feature:



POST /users/{user\_id}/search-and-save



This will:

\- Call openFDA API

\- Extract side effects

\- Save them as user notes



Run:



cd final\_app

uvicorn app.main:app --reload





Open browser:



http://127.0.0.1:8000/docs

