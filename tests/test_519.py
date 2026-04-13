```python
import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient

# Simulate FastAPI app with the endpoint route setup for testing
def create_app():
    app = FastAPI()

    @app.get("/sample-route")
    async def sample_route():
        return {"message": "This is a sample route"}

    return app


class TestEndpointRouteSetup(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = TestClient(self.app)

    def test_route_exists(self):
        """Test that the /sample-route endpoint exists and returns 200."""
        response = self.client.get("/sample-route")
        self.assertEqual(response.status_code, 200)

    def test_route_response_content(self):
        """Test that /sample-route returns the expected JSON content."""
        response = self.client.get("/sample-route")
        self.assertEqual(response.json(), {"message": "This is a sample route"})

    def test_route_method_not_allowed(self):
        """Test that HTTP methods other than GET are not allowed on /sample-route."""
        response_post = self.client.post("/sample-route")
        self.assertIn(response_post.status_code, (405, 404))
        response_put = self.client.put("/sample-route")
        self.assertIn(response_put.status_code, (405, 404))
        response_delete = self.client.delete("/sample-route")
        self.assertIn(response_delete.status_code, (405, 404))


if __name__ == "__main__":
    unittest.main()
```