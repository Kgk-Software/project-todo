```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI

# Import the app and dependencies from your application
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
    # Override the dependency to use the mock service
    app.dependency_overrides[get_hello_service] = lambda: hello_service_mock
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
```

```python
# tests/test_hello_endpoint.py
import pytest

@pytest.mark.asyncio
def test_hello_success(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Test!"}
```

---

### Explanation

- `tests/conftest.py`:
  - Defines pytest fixtures.
  - `hello_service_mock`: a mock of the HelloService returning a fixed greeting string.
  - `client` fixture overrides the FastAPI dependency `get_hello_service` to inject the mock service, then yields a TestClient instance for testing.

- `tests/test_hello_endpoint.py`:
  - Contains a single test function using the `client` fixture to test the `/hello` endpoint responds successfully with the expected message.

---

Make sure that your FastAPI app defines a dependency provider function `get_hello_service` for `HelloService`, and the `/hello` endpoint uses this dependency, e.g.:

```python
# app/api.py example snippet

from fastapi import FastAPI, Depends
from app.services.hello_service import HelloService

app = FastAPI()

def get_hello_service() -> HelloService:
    return HelloService()

@app.get("/hello")
def hello(service: HelloService = Depends(get_hello_service)):
    return {"message": service.get_greeting()}
```

This setup allows you to override dependencies cleanly in tests following clean architecture principles.