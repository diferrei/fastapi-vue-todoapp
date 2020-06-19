from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.authentication import AuthenticationError

from todoapp import crud, schemas
from todoapp.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        return HTTPException(status_code=400, detail="El usuario ya existe")
    return crud.create_user(db, user)


@app.get(
    "/users/",
    response_model=List[schemas.User],
    description="Lee todos los usuarios",
    response_description="Lista de usuarios",
)
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return db_user


@app.post("/users/{user_id}/change-password")
def change_password(
    user_id: int, password_data: schemas.PasswordChange, db: Session = Depends(get_db),
):
    try:
        crud.change_password(db, user_id, **password_data.dict())
    except AuthenticationError:
        return HTTPException(status_code=401, detail="Contraseña actual incorrecta")
    return {"message": "Contraseña cambiada satistfactoriamente"}


@app.post("/users/{user_id}/notes/", response_model=schemas.Note)
def create_note_for_user(
    user_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)
):
    return crud.create_user_note(db, note, user_id)


@app.get("/notes/", response_model=List[schemas.Note])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_notes(db, skip, limit)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
