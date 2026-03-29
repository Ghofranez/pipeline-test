from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ✅ Test 1 : Route principale
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Backend is working!"}

# ✅ Test 2 : Route health check
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# ✅ Test 3 : Route inexistante
def test_not_found():
    response = client.get("/route-inexistante")
    assert response.status_code == 404