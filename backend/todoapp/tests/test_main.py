from backend.todoapp.tests import client


def test_create_user(user):
    response = client.post("/users/", json=user)
    assert response.status_code == 200

    data = response.json()

    assert data["username"] == user["username"]
    assert data["display_name"] == user["display_name"]
    assert "id" in data
    assert data["id"] == 1


def test_read_user(user):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == user["username"]
    assert data["display_name"] == user["display_name"]


def test_create_note_for_user(user, note):
    response = client.post("/users/1/notes/", json=note)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == note["title"]
    assert data["text"] == note["text"]


def test_modify_note(modify_note):
    response = client.post("/notes/1/modify", json=modify_note)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == modify_note["title"]
    assert data["text"] == modify_note["text"]


def test_delete_note():
    response = client.post("/notes/1/delete")
    assert response.status_code == 200

    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["notes_count"] == 0


def test_change_username(user, username_change):
    response = client.post("/users/1/change-username", json=username_change)
    assert response.status_code == 200

    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == username_change["new_username"]


def test_change_display_name(display_name_change):
    response = client.post("/users/1/change-display-name", json=display_name_change)
    assert response.status_code == 200

    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["display_name"] == display_name_change["new_display_name"]


def test_delete_user():
    response = client.post(f"/users/1/delete")
    assert response.status_code == 200

    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data[0]["deleted"]
