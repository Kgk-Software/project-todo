```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient

from app.api import app, get_hello_service
from app.services.hello_service import HelloService

@pytest.fixture
def hello_service_mock():
    class MockHelloService:
        def get_greeting(self) -> str:
            return "Hello, Test!"
    return MockHelloService()

@pytest.fixture
def client(hello_service_mock):
    app.dependency_overrides[get_hello_service] = lambda: hello_service_mock
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
```

```python
# tests/test_hello.py
def test_hello_endpoint(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Test!"}
```

```python
# app/api.py
from fastapi import FastAPI, Depends
from app.services.hello_service import HelloService

app = FastAPI()

def get_hello_service() -> HelloService:
    return HelloService()

@app.get("/hello")
def hello(service: HelloService = Depends(get_hello_service)):
    return {"message": service.get_greeting()}
```

```python
# app/services/hello_service.py
class HelloService:
    def get_greeting(self) -> str:
        return "Hello, World!"
```