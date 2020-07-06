import pytest
import os


@pytest.fixture()
def user():
    return {"username": "test", "display_name": "Test User", "password": "test"}


@pytest.fixture()
def note():
    return {"title": "hola", "text": "ASASASASA"}


@pytest.fixture()
def modify_note():
    return {"title": "aloh", "text": "modifeid"}


@pytest.fixture()
def username_change():
    return {"user_id": 1, "new_username": "test"}


@pytest.fixture()
def display_name_change():
    return {"new_display_name": "test"}


@pytest.fixture(scope="session", autouse=True)
def delete_db():
    yield
    os.remove("test.db")
