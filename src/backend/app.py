'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-04-26 11:01:43
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-04-26 23:43:16
FilePath: \TaskTree\src\backend\app.py
Description: 李文禎
'''
import os
from fastapi import FastAPI
import uvicorn

VERSION = os.getenv("VERSION", "0.1.0")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/version")
def read_version():
    return {"version": VERSION}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)