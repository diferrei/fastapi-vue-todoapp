from datetime import datetime

from sqlalchemy.orm import Session
from starlette.authentication import AuthenticationError

from backend.todoapp import models, schemas
from backend.todoapp.auth import check_password, hash_password
from backend.todoapp.models import Note, User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username, display_name=user.display_name, password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    delete_user_notes(db, user_id)
    user = get_user(db, user_id)
    user.deleted = True
    db.add(user)
    db.commit()


def change_password(
    db: Session, user_id: int, current_password: str, new_password: str
):
    """
    :param db: database session
    :param user_id: user pk
    :param current_password:
    :param new_password:
    :return:
    """
    user = get_user(db, user_id)
    valid_password = check_password(current_password, user.password)
    if valid_password:
        user.password = hash_password(new_password)
        db.add(user)
        db.commit()
    else:
        raise AuthenticationError()


def change_username(db: Session, user_id: int, new_username: str):
    user = get_user(db, user_id)
    user.username = new_username
    db.add(user)
    db.commit()


def change_display_name(db: Session, user_id: int, new_display_name: str):
    user = get_user(db, user_id)
    user.display_name = new_display_name
    db.add(user)
    db.commit()


def get_note(db: Session, note_id: int):
    return db.query(Note).filter(models.Note.id == note_id).first()


def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Note).offset(skip).limit(limit).all()


def get_notes_by_owner(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Note).filter(models.Note.owner_id == user_id)


def get_user_notes_count(db: Session, user_id: int):
    return db.query(Note).filter(models.Note.owner_id == user_id).count()


def create_user_note(db: Session, note: schemas.NoteCreate, user_id: int):
    db_note = Note(**note.dict(), owner_id=user_id, creation_datetime=datetime.now())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def modify_note(db: Session, note_id: int, title: str, text: str):
    db_note = get_note(db, note_id)
    db_note.title = title
    db_note.text = text
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int):
    db.query(Note).filter(models.Note.id == note_id).delete()
    db.commit()


def delete_user_notes(db: Session, user_id: int):
    db.query(Note).filter(models.Note.owner_id == user_id).delete()
