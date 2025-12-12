from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class PostDummyBody(BaseModel):
    param_1: int
    param_2: int

@app.get("/sync_get")
def sync_get():
    return {"message" : "sync_get success"}

@app.get("/async_get")
async def async_get():
    return {"message" : "async_get success"}

@app.post("/sync_post")
def sync_post(body: PostDummyBody):
    return {"message" : f"sync_post succerss\nparam1 : {body.param_1}, param2 : {body.param_2}"}

@app.post("/async_post")
async def async_post(body: PostDummyBody):
    return {"message" : f"async_post succerss\nparam1 : {body.param_1}, param2 : {body.param_2}"}

if __name__ == "__main__":
    uvicorn.run(
        "dummy_api:app",
        # host="0.0.0.0",
        host="localhost",
        port=18000,
        workers=4,
        reload=True
    )