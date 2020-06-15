import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hola mundo"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
