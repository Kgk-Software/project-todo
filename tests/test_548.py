```python
import pytest
from fastapi.testclient import TestClient

# Assume the FastAPI app was defined in a module named 'app_module'
from app_module import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    # Assuming the root returns a JSON welcome message or similar
    assert response.headers["content-type"] == "application/json"
    json_data = response.json()
    assert isinstance(json_data, dict)
    # Example expected key check - adjust according to actual implementation
    assert "message" in json_data

def test_healthcheck_endpoint():
    # If a health check endpoint exists, e.g. /health
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data == {"status": "ok"}

def test_non_existent_route():
    response = client.get("/non-existent-route")
    assert response.status_code == 404

# If the FastAPI app has any startup event, you might want to cover that too,
# but typically TestClient initializes app and startup automatically.

# Additional test example if there's a /items endpoint:
# def test_get_items():
#     response = client.get("/items")
#     assert response.status_code == 200
#     json_data = response.json()
#     assert isinstance(json_data, list)

# Since this is the basic setup task, minimal endpoint tests suffice.
```
