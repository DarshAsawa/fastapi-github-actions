"""
This module contains a FastAPI application that provides basic arithmetic operations
through API endpoints. The supported operations are addition, subtraction, multiplication,
and division.
"""
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Operation(BaseModel):
    """Model representing an arithmetic operation with two operands."""
    a: float
    b: float

@app.get("/healthz")
async def health_check():
    # You can add logic here to check the health of dependent services if necessary
    return JSONResponse(content={"status": "Healthy"}, status_code=200)

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
    