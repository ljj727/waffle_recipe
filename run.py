
from fastapi import FastAPI


#
app = FastAPI(title="Test", description="TestTest")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/home")
def home():
    return {"message": "Home"}


@app.get("/al")
def al():
    return {"message": "al"}


@app.get("/alaa")
def alaa():
    return {"message": "aal"}

