```python
import getpass
from typing import Optional


class UserRepository:
    """
    Repository pattern abstraction for user data source.
    Responsible for retrieving user-related data from the system or other sources.
    """

    def get_current_system_username(self) -> Optional[str]:
        """
        Retrieve the current system user's name.

        Returns:
            Optional[str]: Username if available, otherwise None.
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
    Service layer for handling user-related business logic.
    """

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_current_user_name(self) -> Optional[str]:
        """
        Fetch the current user's name using the user repository.

        Returns:
            Optional[str]: The current user's name or None if not found.
        """
        return self.user_repository.get_current_system_username()


# Example usage
if __name__ == "__main__":
    user_repository = UserRepository()
    user_service = UserService(user_repository)
    current_user_name = user_service.get_current_user_name()
    if current_user_name:
        print(f"Current user name: {current_user_name}")
    else:
        print("Current user name could not be retrieved.")
```