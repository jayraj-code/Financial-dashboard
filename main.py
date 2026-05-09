from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, financial world!"}


@app.get("/hello")
async def say_hello():
    return {"greeting": "Hi there!"}


@app.get("/new_api")
async def trying_():
    return {"who is there"}


@app.get("/ping")
async def ping():
    return {2*4}
