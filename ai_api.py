from fastapi import FastAPI
import uvicorn # server for fastapi.

app = FastAPI()

@app.get("/")
async def hello():
    return "Welcome!"

# To run use >  uvicorn ai_api:app --reload

@app.get("/{name}")
async def hello(name):
    return f"Welcome! {name}"