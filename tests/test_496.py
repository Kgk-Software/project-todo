```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Assume the /hello endpoint is implemented as follows for testing purpose:
app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello"}

client = TestClient(app)

def test_hello_status_code():
    response = client.get("/hello")
    assert response.status_code == 200

def test_hello_response_json():
    response = client.get("/hello")
    assert response.json() == {"message": "Hello"}

def test_hello_content_type():
    response = client.get("/hello")
    assert response.headers["content-type"] == "application/json"
```