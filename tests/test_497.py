```python
from fastapi import FastAPI
import pytest

def test_fastapi_import():
    # Verify that FastAPI is imported and available
    assert callable(FastAPI)

def test_app_instance_creation():
    # Test that the FastAPI app instance can be created successfully
    app = FastAPI()
    assert app is not None
    # Check that app is an instance of FastAPI
    assert isinstance(app, FastAPI)

def test_app_has_routes_property():
    app = FastAPI()
    # New FastAPI app should have routes attribute (list)
    assert hasattr(app, "routes")
    assert isinstance(app.routes, list)

def test_app_startup_and_shutdown_events():
    app = FastAPI()
    startup_triggered = []
    shutdown_triggered = []

    @app.on_event("startup")
    async def on_startup():
        startup_triggered.append(True)

    @app.on_event("shutdown")
    async def on_shutdown():
        shutdown_triggered.append(True)

    # Using TestClient to trigger events
    from fastapi.testclient import TestClient
    with TestClient(app) as client:
        pass
    # After exiting client context startup and shutdown should be triggered once
    assert startup_triggered == [True]
    assert shutdown_triggered == [True]
```