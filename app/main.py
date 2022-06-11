from curses import meta
from fastapi import FastAPI
from requests import request
import meta
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:8001",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://192.168.1.181:3000",
    "http://192.168.1.181:3001",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Countdown": "Root"}

@app.get("/countdown")
async def get_countdowns() -> dict:
    countdown = meta.GetCountdown()
    return {"data" : countdown}


if __name__ == '__main__' :
    uvicorn.run("main:app", port=3002, host="0.0.0.0", reload=True)