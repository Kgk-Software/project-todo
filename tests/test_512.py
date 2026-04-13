```python
import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Simulate the basic FastAPI app configuration for testing purposes.
def create_basic_app():
    app = FastAPI()

    @app.get("/ping")
    async def ping():
        return {"ping": "pong"}

    return app


class TestBasicFastAPIAppConfiguration(unittest.TestCase):
    def setUp(self):
        self.app = create_basic_app()
        self.client = TestClient(self.app)

    def test_app_instance_creation(self):
        """Test that the FastAPI app instance is created successfully."""
        from fastapi import FastAPI
        self.assertIsInstance(self.app, FastAPI)

    def test_default_openapi_route_exists(self):
        """Test that the OpenAPI docs route is available by default."""
        response = self.client.get("/openapi.json")
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn("openapi", json_response)
        self.assertIn("info", json_response)

    def test_ping_endpoint_returns_expected_response(self):
        """Test that the /ping endpoint returns the expected JSON response."""
        response = self.client.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ping": "pong"})

    def test_docs_ui_available(self):
        """Test that the automatic docs UI is available at /docs."""
        response = self.client.get("/docs")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])

    def test_redoc_ui_available(self):
        """Test that the ReDoc UI is available at /redoc."""
        response = self.client.get("/redoc")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])


if __name__ == "__main__":
    unittest.main()
```