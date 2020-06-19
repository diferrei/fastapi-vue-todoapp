from datetime import datetime

from sqlalchemy.orm import Session

from todoapp import schemas
from todoapp.auth import hash_password
import todoapp.models


def get_user(db: Session, user_id: int):
    return (
        db.query(todoapp.models.User).filter(todoapp.models.User.id == user_id).first()
    )


def get_user_by_username(db: Session, username: str):
    return (
        db.query(todoapp.models.User)
        .filter(todoapp.models.User.username == username)
        .first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(todoapp.models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = todoapp.models.User(
        username=user.username, display_name=user.display_name, password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(todoapp.models.Note).offset(skip).limit(limit).all()


def create_user_note(db: Session, note: schemas.NoteCreate, user_id: int):
    db_note = todoapp.models.Note(
        **note.dict(), owner_id=user_id, creation_datetime=datetime.now()
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
