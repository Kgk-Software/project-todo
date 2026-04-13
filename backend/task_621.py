```python
from typing import Optional

class GreetingService:
    """
    Service layer class responsible for generating greeting messages.
    """

    @staticmethod
    def get_hello_message(user_name: Optional[str] = None) -> str:
        """
        Return a greeting message. If user_name is given, include it in the greeting.

        Args:
            user_name (Optional[str]): Name of the user to greet.

        Returns:
            str: Personalized or generic hello message.
        """
        if user_name and user_name.strip():
            return f"Hello world! Welcome, {user_name}!"
        return "Hello world!"


def print_hello_message(user_name: Optional[str] = None):
    """
    Console output function that prints the greeting message including optional user name.

    Args:
        user_name (Optional[str]): Name of the user to greet.
    """
    message = GreetingService.get_hello_message(user_name)
    print(message)


if __name__ == "__main__":
    # Example usage with a hardcoded user name; in real app could come from input or args
    print_hello_message("Alice")
```