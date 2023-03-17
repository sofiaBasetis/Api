from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_mensaje():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello":"World"}



def test_login():
    response = client.get("/login")
    assert response.status_code == 200
    assert response.json() == "Ingrese sus datos"


def test_create_existing_item():
    response = client.post(
        "/students",
        json={
            "id": "000f",
            "name": "Sofia",
            "clase": 10
            }
    )
    if response.status_code == 200: 
        assert response.json() == "Estudiante registrado"
    else:
        assert response.json() == "Estudiante registrado"
        