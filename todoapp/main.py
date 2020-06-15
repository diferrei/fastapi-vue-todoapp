import uvicorn
from fastapi import FastAPI

from todoapp.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def main():
    return {"message": "Hola mundo"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
