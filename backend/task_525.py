```python
import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock

from app.api import app
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.schemas import UserOut


@pytest.fixture
def mock_user_repo():
    repo = AsyncMock(spec=UserRepository)
    return repo


@pytest.fixture
def user_service(mock_user_repo):
    service = UserService(user_repository=mock_user_repo)
    return service


@pytest.fixture
def client(user_service, monkeypatch):
    # patch the dependency override so the app uses our service with mock repo
    app.dependency_overrides[UserService] = lambda: user_service
    return TestClient(app)


@pytest.mark.asyncio
async def test_successful_get_user_response(client, mock_user_repo):
    # Arrange
    user_id = 1
    expected_user = UserOut(id=user_id, name="John Doe", email="john@example.com")

    mock_user_repo.get_user_by_id.return_value = expected_user

    # Act
    response = client.get(f"/users/{user_id}")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_user.dict()
    mock_user_repo.get_user_by_id.assert_awaited_once_with(user_id)
```
