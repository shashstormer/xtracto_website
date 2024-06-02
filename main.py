import xtracto
from fastapi import FastAPI
from fastapi.responses import JSONResponse

uvicorn_kwargs = {
    "host": "0.0.0.0",
    "port": 5333,

}
app = FastAPI()


@app.get("/robots.txt")
async def NotFound():
    return JSONResponse({"detail": "not found"}, 404)


xtracto.App(app, uvicorn_kwargs=uvicorn_kwargs, auto_run=False)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, **uvicorn_kwargs)
