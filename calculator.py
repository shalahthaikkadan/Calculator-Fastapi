from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


class Calculator(BaseModel):
    x: float
    y: float
    opr: str


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/calculate")
def calculate(data: Calculator):

    x = data.x
    y = data.y
    opr = data.opr

    if opr == "+":
        result = addition(x, y)

    elif opr == "-":
        result = subtraction(x, y)

    elif opr == "*":
        result = multiplication(x, y)

    elif opr == "/":
        if y == 0:
            return {"error": "Cannot divide by zero"}

        result = division(x, y)

    else:
        return {"error": "Invalid operator"}

    return {
        "x": x,
        "y": y,
        "operator": opr,
        "result": result
    }