from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_status_pending():
    response = client.get("/status?counts=18&minimum=25")

    assert response.status_code == 200
    assert response.json()["status"] == "Pending"
    assert response.json()["missing"] == 7


def test_status_confirmed():
    response = client.get("/status?counts=30&minimum=25")

    assert response.status_code == 200
    assert response.json()["status"] == "Confirmed"
    assert response.json()["missing"] == 0


def test_status_rejects_zero_minimum():
    response = client.get("/status?counts=18&minimum=0")

    assert response.status_code == 422


def test_status_rejects_negative_counts():
    response = client.get("/status?counts=-5&minimum=25")

    assert response.status_code == 422

def test_operation_not_found():
    response = client.get("/operation/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Operation 999 not found"
    }