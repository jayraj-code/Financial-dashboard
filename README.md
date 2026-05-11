# Financial Dashboard
A full‑stack personal financial dashboard for tracking expenses, investments, and savings goals. 

## Tech Stack (Planned)
- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** React 
- **Database:** PostgreSQL 
- **Performance:** C++ extensions via pybind11 (planned)
- **ML:** scikit‑learn for transaction categorization (planned)

## Current Features
- REST API for expenses (CRUD)
- In‑memory storage (to be replaced by PostgreSQL)
- Expense filtering by category, amount range

## Setup
1. Clone the repo: `git clone <url>`
2. Create a virtual environment: `python -m venv venv`
3. Activate it and install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn main:app --reload`
5. Visit `http://localhost:8000/docs` for interactive API docs.
