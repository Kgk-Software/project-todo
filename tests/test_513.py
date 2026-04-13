```python
import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Assuming the FastAPI app is created in a module like:
#
# from your_app import app
#
# For this test, we'll create a minimal FastAPI app simulating the configuration.

def create_app():
    app = FastAPI(title="Test FastAPI Server", version="0.1.0", description="Test configuration")

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}

    return app


class TestFastAPIServerConfiguration(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = TestClient(self.app)

    def test_app_instance(self):
        """Test that the app instance is created and is a FastAPI instance"""
        from fastapi import FastAPI
        self.assertIsInstance(self.app, FastAPI)

    def test_app_metadata(self):
        """Test that app metadata (title, version, description) is set correctly"""
        self.assertEqual(self.app.title, "Test FastAPI Server")
        self.assertEqual(self.app.version, "0.1.0")
        self.assertEqual(self.app.description, "Test configuration")

    def test_health_endpoint_exists(self):
        """Test that /health endpoint exists and returns 200 with expected content"""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_openapi_json_available(self):
        """Test that OpenAPI JSON is available at /openapi.json"""
        response = self.client.get("/openapi.json")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIn("openapi", json_data)
        self.assertEqual(json_data["info"]["title"], "Test FastAPI Server")
        self.assertEqual(json_data["info"]["version"], "0.1.0")

if __name__ == "__main__":
    unittest.main()
```