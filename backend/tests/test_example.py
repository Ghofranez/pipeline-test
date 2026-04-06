from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)

# Test 1 — route principale
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI fonctionne (ghofrane) "}

# Test 2 — route hello avec un nom
def test_hello():
    response = client.get("/hello/Ghofrane")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour Ghofrane"}

# Test 3 — route hello avec un autre nom
def test_hello_autre_nom():
    response = client.get("/hello/Ali")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour Ali"}

# Test 4 — route inexistante
def test_route_inexistante():
    response = client.get("/inexistant")
    assert response.status_code == 404