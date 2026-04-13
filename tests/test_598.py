```python
import pytest
from fastapi.testclient import TestClient
from your_module import create_app  # Replace with your actual app factory import


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_hello_endpoint_status_code(client):
    """
    Test that GET /hello returns status code 200
    """
    response = client.get("/hello")
    assert response.status_code == 200, "GET /hello should return status code 200"


def test_hello_endpoint_response_content(client):
    """
    Test that GET /hello returns the expected JSON content
    """
    response = client.get("/hello")
    assert response.headers["content-type"] == "application/json"
    json_data = response.json()
    assert isinstance(json_data, dict), "Response JSON should be a dictionary"
    assert "message" in json_data, "Response JSON must contain 'message' key"
    assert json_data["message"] == "Hello, World!", "Response 'message' should be 'Hello, World!'"


def test_hello_endpoint_method_not_allowed(client):
    """
    Test that other HTTP methods are not allowed on /hello endpoint
    """
    response = client.post("/hello")
    assert response.status_code == 405, "POST /hello should return status code 405 Method Not Allowed"
```