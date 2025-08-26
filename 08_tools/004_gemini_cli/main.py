from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/abc")
def read_abc():
    return 1

@app.get("/bcd")
def read_bcd():
    return 2
