import os

import pytest


@pytest.fixture
def user():
    return {"username": "test", "display_name": "Test User", "password": "test"}


@pytest.fixture
def note():
    return {"title": "Hola", "text": "Hola Mundo!!!"}


@pytest.fixture(scope="session", autouse=True)
def delete_db():
    yield
    os.remove("test.db")
