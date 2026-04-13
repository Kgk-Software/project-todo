```python
from fastapi.testclient import TestClient
from fastapi import FastAPI

# Assuming the route handler is defined as follows:
app = FastAPI()

@app.get("/hello")
async def read_hello():
    return {"message": "Hello"}

# Tests for the /hello endpoint

def test_hello_status_code():
    client = TestClient(app)
    response = client.get("/hello")
    assert response.status_code == 200

def test_hello_response_content():
    client = TestClient(app)
    response = client.get("/hello")
    assert response.json() == {"message": "Hello"}

def test_hello_response_content_type():
    client = TestClient(app)
    response = client.get("/hello")
    assert response.headers["content-type"] == "application/json"

```