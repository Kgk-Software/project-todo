```python
import unittest
from io import StringIO
import sys

# Assuming the backend code to test has a function like:
# def display_hello_world():
#     print("Hello world!")

from your_module import display_hello_world  # Replace 'your_module' with actual module name


class TestDisplayHelloWorld(unittest.TestCase):
    def test_display_hello_world_prints_exact_message(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        display_hello_world()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello world!\n")

    def test_display_hello_world_output_is_not_empty(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        display_hello_world()

        sys.stdout = sys.__stdout__
        self.assertTrue(len(captured_output.getvalue()) > 0)

    def test_display_hello_world_output_strip(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        display_hello_world()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Hello world!")

    def test_display_hello_world_function_is_callable(self):
        self.assertTrue(callable(display_hello_world))


if __name__ == "__main__":
    unittest.main()
```