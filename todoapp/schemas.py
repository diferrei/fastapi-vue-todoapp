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


class UserBase(BaseModel):
    username: str
    display_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    notes: List[Note] = []

    class Config:
        orm_mode = True
