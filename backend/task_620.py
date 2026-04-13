```python
import getpass
from typing import Optional


class UserRepository:
    """
    Repository pattern abstraction for user data source.
    Here we simulate fetching user data from a system or external service.
    """
    def get_current_system_username(self) -> Optional[str]:
        """
        Attempts to fetch the current system user name.

        Returns:
            Optional[str]: The current system user name or None if unavailable
        """
        try:
            username = getpass.getuser()
            if username and username.strip():
                return username.strip()
        except Exception:
            return None
        return None


class UserService:
    """
    Service layer to encapsulate business logic related to users.
    """

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_current_user_name(self) -> Optional[str]:
        """
        Get current user's name from system or user service.

        Returns:
            Optional[str]: Name of the current user or None if not found
        """
        username = self.user_repository.get_current_system_username()
        return username


# Example usage:
if __name__ == "__main__":
    user_repo = UserRepository()
    user_service = UserService(user_repo)
    current_username = user_service.get_current_user_name()
    print(f"Current user: {current_username if current_username else 'Unknown user'}")
```