import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from typing import List
from sqlalchemy.orm import Session
from starlette.authentication import AuthenticationError

from todoapp import crud
from todoapp.database import SessionLocal
from todoapp import schemas

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


@app.post("/users/", name="create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    return crud.create_user(db, user)


@app.post("/users/{user_id}/delete")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user or db_user.deleted:
        raise HTTPException(status_code=400, detail="El usuario no existe")
    crud.delete_user(db, user_id)
    return {"message": "Usuario eliminado exitosamente"}


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@app.get("/users/{user_id}", response_model=schemas.BasicUser)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    db_user.notes_count = crud.get_user_notes_count(db, db_user.id)
    return db_user


@app.post("/users/{user_id}/change-password")
def change_password(
    user_id: int, password_data: schemas.PasswordChange, db: Session = Depends(get_db)
):
    try:
        crud.change_password(
            db, user_id, password_data.current_password, password_data.new_password
        )
    except AuthenticationError:
        return HTTPException(status_code=401, detail="Contrasena incorrecta")
    return {"message": "Contrasena cambiado satisfactoriamente"}


@app.post("/users/{user_id}/change-display-name")
def change_display_name(
    user_id: int,
    new_display_name: schemas.DisplayNameChange,
    db: Session = Depends(get_db),
):
    crud.change_display_name(db, user_id, new_display_name.new_display_name)
    return {"message": "Display name cambiado satisfactoriamente"}


@app.post("/users/{user_id}/change-username")
def change_username(
    user_id: int, new_username: schemas.UserNameChange, db: Session = Depends(get_db)
):
    crud.change_display_name(db, user_id, new_username.new_username)
    return {"message": "Nombre de usuario cambiado satisfactoriamente"}


@app.post("/users/{user_id}/notes/", response_model=schemas.Note)
def create_note_for_user(
    user_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)
):
    return crud.create_user_note(db, note, user_id)


@app.get("/notes/", response_model=List[schemas.Note])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_notes(db, skip, limit)


@app.post("/notes/{note_id}/modify")
def modify_note(
    note_id: int, edited_note: schemas.NoteEdit, db: Session = Depends(get_db)
):
    db_note = crud.get_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="La nota no existe")
    return crud.modify_note(db, note_id, edited_note.title, edited_note.text)


@app.post("/notes/{note_id}/delete")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.get_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="La nota no existe")
    crud.delete_note(db, note_id)
    return {"message": "Note eliminada satisfactoriamente"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
