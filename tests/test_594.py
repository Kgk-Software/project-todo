```python
import pytest
from fastapi import FastAPI
from your_module import create_app  # Assuming the function to initialize FastAPI app is called create_app


def test_app_instance_created():
    """
    Test that the create_app function returns a FastAPI instance.
    """
    app = create_app()
    assert isinstance(app, FastAPI), "The app instance should be a FastAPI object"


def test_app_routes_exist():
    """
    Test that the app has at least the expected default routes.
    Adjust expected routes based on actual implementation.
    """
    app = create_app()
    routes = [route.path for route in app.routes]

    # Common default routes that FastAPI apps have (adjust as necessary)
    # For example, if there is a root endpoint defined, test its existence:
    expected_paths = ["/"]

    # Check each expected path is in the routes
    for path in expected_paths:
        assert path in routes, f"Route {path} should be registered in the app"


def test_app_metadata():
    """
    Optional: If your create_app function sets metadata like title or version,
    verify those attributes exist and have expected values.
    """
    app = create_app()
    # Example checks, adjust according to your implementation:
    assert hasattr(app, "title"), "App should have a title attribute"
    assert isinstance(app.title, str), "App title should be a string"
    assert app.title != "", "App title should not be empty"
```
