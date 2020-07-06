from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    text: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    owner_id: int
    creation_datetime: datetime
    completion_datetime: Optional[datetime]

    class Config:
        orm_mode = True


class NotesCount(BaseModel):
    notes_count: int


class UserBase(BaseModel):
    username: str
    display_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    deleted: bool
    notes: List[Note] = []

    class Config:
        orm_mode = True


class BasicUser(UserBase):
    notes_count: int

    class Config:
        orm_mode = True


class PasswordChange(BaseModel):
    current_password: str
    new_password: str


class NoteEdit(NoteBase):
    pass


class UserNameChange(BaseModel):
    new_username: str


class DisplayNameChange(BaseModel):
    new_display_name: str
