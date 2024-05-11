from fastapi import FastAPI

app = FastAPI()


@app.get("/greeting")
async def say_greet():
    return "Hello, have a wonderful day"
