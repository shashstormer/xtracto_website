import xtracto
from fastapi import FastAPI

uvicorn_kwargs = {
    "host": "0.0.0.0",
    "port": 5333,

}
app = FastAPI()
xtracto.App(app, uvicorn_kwargs=uvicorn_kwargs, auto_run=False)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, **uvicorn_kwargs)

