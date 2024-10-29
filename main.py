from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    """Model representing an arithmetic operation with two operands."""
    a: float
    b: float

@app.post("/add")
def add(operation: Operation):
    """Endpoint to add two numbers."""
    return {"result": operation.a + operation.b}

@app.post("/subtract")
def subtract(operation: Operation):
    """Endpoint to subtract the second number from the first."""
    return {"result": operation.a - operation.b}

@app.post("/multiply")
def multiply(operation: Operation):
    """Endpoint to multiply two numbers."""
    return {"result": operation.a * operation.b}

@app.post("/divide")
def divide(operation: Operation):
    """Endpoint to divide the first number by the second.

    Returns an error if the second number is zero.
    """
    if operation.b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": operation.a / operation.b}
