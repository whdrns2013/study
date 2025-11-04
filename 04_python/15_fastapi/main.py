from fastapi import FastAPI
from app.api.v1.router import routers as v1_routers
from app.core.settings import settings
from tests import dummy_test

app = FastAPI(
    title="FastAPI study",
    version="1.0.0"
)

app.include_router(v1_routers,
                   prefix=settings.ENDPOINT.PREFIX)

def run_test():
    dummy_test.test()

if __name__ == '__main__':
    run_test()
    import uvicorn
    uvicorn.run("main:app", host=str(settings.SERVICE.BIND), port=int(settings.SERVICE.PORT))