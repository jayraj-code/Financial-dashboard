from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from typing import Optional 

# Temporary in-memory database (will be replaced by PostgreSQL later)
expenses_db = [
    {"id": 1, "description": "Lunch", "amount": 12.5, "category": "food"},
    {"id": 2, "description": "Uber", "amount": 7.0, "category": "transport"},
]

app = FastAPI()

@app.get("/expenses")
async def get_expense(
    category : Optional[str] = None,
    min_amount : Optional[float] = None,
    max_amount : Optional[float] = None,

):
    result = expenses_db
    if category is not None:
        result = [e for e in result if e["category"] == category]
    if min_amount is not None:
        result = [e for e in result if e["amount"] >= min_amount]
    if max_amount is not None: 
        result = [e for e in result if e["amount"] <= max_amount]
    return result

@app.get("/expenses/{expense_id}")
async def get_expense(expense_id: int):
    for expense in expenses_db:
        if expense["id"] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")

@app.get("/expense/search")
async def get_expenses_search(
    q : Optional[str] = None
):
    result = expenses_db
    if q is None :
        return result
    
    q_lower = q.lower()
    if q is not None: 
        result = [e for e in result if q_lower in e["description"].lower()]
    return result


@app.get("/health")
async def get_health():
    return ["status : okay"]
    