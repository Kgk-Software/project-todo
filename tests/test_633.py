```python
import unittest
from io import StringIO
import sys

# Assuming the implementation to test looks like this:
#
# def print_hello_world():
#     print("Hello World")

from your_module import print_hello_world  # Replace 'your_module' with the actual module name


class TestHelloWorldOutput(unittest.TestCase):
    def test_print_hello_world_outputs_correct_message(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print_hello_world()

        sys.stdout = sys.__stdout__  # Restore original stdout
        self.assertEqual(captured_output.getvalue(), "Hello World\n")

    def test_print_hello_world_output_not_empty(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print_hello_world()

        sys.stdout = sys.__stdout__
        self.assertTrue(len(captured_output.getvalue()) > 0)

    def test_print_hello_world_output_exact_text(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print_hello_world()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Hello World")

    def test_print_hello_world_output_with_extra_spaces(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print_hello_world()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        # Ensure no leading or trailing spaces besides expected newline
        self.assertTrue(output == "Hello World\n")

    def test_print_hello_world_is_callable(self):
        self.assertTrue(callable(print_hello_world))


if __name__ == "__main__":
    unittest.main()
```