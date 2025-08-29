from fastapi.testclient import TestClient
from services.tasks.app import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['service'] == 'tasks'
