from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(operation: Operation):
    return {"result": operation.a + operation.b}

@app.post("/subtract")
def subtract(operation: Operation):
    return {"result": operation.a - operation.b}

@app.post("/multiply")
def multiply(operation: Operation):
    return {"result": operation.a * operation.b}

@app.post("/divide")
def divide(operation: Operation):
    if operation.b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": operation.a / operation.b}