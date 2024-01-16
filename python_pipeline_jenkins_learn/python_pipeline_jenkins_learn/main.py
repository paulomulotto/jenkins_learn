from fastapi import FastAPI, HTTPException
from python_pipeline_jenkins_learn.math_operations import add, sub, mul, div

app = FastAPI()


@app.get("/add")
def add_handler(x: int, y: int):
    return {"result": add(x, y)}


@app.get("/sub")
def sub_handler(x: int, y: int):
    return {"result": sub(x, y)}


@app.get("/mul")
def mul_handler(x: int, y: int):
    return {"result": mul(x, y)}


@app.get("/div")
def div_handler(x: int, y: int):
    try:
        return {"result": div(x, y)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
