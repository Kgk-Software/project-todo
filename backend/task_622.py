```python
def output_hello_world():
    """
    Service layer method to encapsulate the logic of producing 'Hello world!' message.
    """
    return "Hello world!"


def print_hello_world():
    """
    Console application entry point that retrieves the message from the service
    and prints it to the console, maintaining separation of concerns.
    """
    message = output_hello_world()
    print(message)


if __name__ == "__main__":
    print_hello_world()
```