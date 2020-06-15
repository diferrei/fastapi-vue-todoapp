from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from todoapp.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), unique=True, index=True)
    display_name = Column(String(32))
    password = Column(String(255))


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32))
    text = Column(String(255))
    creation_datetime = Column(DateTime)
    completion_datetime = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    owner = relationship(User, backref="notes")
