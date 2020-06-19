from todoapp.tests.database import client


def test_create_user(user):
    response = client.post("/users/", json=user)
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["username"] == user["username"]
    assert data["display_name"] == user["display_name"]
    assert "id" in data


def test_create_note_for_user(user, note):
    # user_response = client.post("/users/", json=user)
    # db_user = user_response.json()

    response = client.post(f"/users/1/notes/", json=note)
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["title"] == note["title"]
    assert data["text"] == note["text"]
