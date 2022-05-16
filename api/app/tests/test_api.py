from datetime import datetime
from urllib import response
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

# TODO Crear Modelos y Migraciones para una base de datos test
# TODO Obtener identificadores de la base de datos para hacer tests dinamicos

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# First use case
def test_create_new_user():
    id = 1
    response = client.post(
        "/users",
        json={"email": "user_test@test.com", "name": "UserTest", "avatar": "https://randomuser.me/api/portraits/lego/6.jpg"}
    )
    assert response.status_code == 201
    assert response.json() == {"id": id + 1}

# Second use case
def test_change_name():
    response = client.patch(
        "/users",
        json={"name": "PilloElHumilde"}
    )
    assert response.status_code == 204

# Third use case
def test_change_avatar():
    response = client.patch(
        "/users",
        json={"avatar": "12"}
    )
    assert response.status_code == 204

# Fourth use case
def test_create_new_group():
    # TODO Obtener el último id de la tabla de grupos
    id = 1
    response = client.post(
        "/groups",
        json={"user_id": "1", "name": "Daily", "description": "Mi primer grupo"}
    )
    assert response.status_code == 201
    assert response.json() == {"id": id + 1}

# Fifth use case
def test_create_new_task():
    # TODO Obtener el último id de la tabla de tareas
    id = 1
    response = client.post(
        "/tasks",
        json={"group_id": "1", "title": "Mi primera taraea", "descripton": "Esta es mi primera tarea"}
    )
    assert response.status_code == 201
    assert response.json() == {"id": id + 1}

# Sixth use case
def test_check_task():
    response = client.patch(
        "/tasks",
        json={"task_id": "1", "fecha_terminado": datetime.now}
    )
    assert response.status_code == 204

def test_uncheck_task():
    response = client.patch(
        "/tasks",
        json={"task_id": "1", "fecha_terminado": None}
    )
    assert response.status_code == 204

# Seventh use case
def test_delete_task():
    response = client.delete(
        "/tasks",
        json={"task_id": "1"}
    )
    assert response.status_code == 204

# Eighth use case
def test_delete_group():
    response = client.delete(
        "/tasks",
        json={"group_id"}
    )
    assert response.status_code == 204