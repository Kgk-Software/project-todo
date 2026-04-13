```python
import unittest

# Assuming the code to test looks like this:
# class User:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_full_name(self) -> str:
#         return f"{self.first_name} {self.last_name}"

from your_module import User  # Replace 'your_module' with actual module name


class TestUserNameRetrieval(unittest.TestCase):

    def test_get_full_name_returns_correct_full_name(self):
        user = User(first_name="John", last_name="Doe")
        expected = "John Doe"
        result = user.get_full_name()
        self.assertEqual(result, expected)

    def test_get_full_name_with_empty_first_name(self):
        user = User(first_name="", last_name="Doe")
        expected = " Doe"
        result = user.get_full_name()
        self.assertEqual(result, expected)

    def test_get_full_name_with_empty_last_name(self):
        user = User(first_name="John", last_name="")
        expected = "John "
        result = user.get_full_name()
        self.assertEqual(result, expected)

    def test_get_full_name_with_both_names_empty(self):
        user = User(first_name="", last_name="")
        expected = " "
        result = user.get_full_name()
        self.assertEqual(result, expected)

    def test_get_full_name_with_whitespace_names(self):
        user = User(first_name="  Alice  ", last_name="  Smith  ")
        expected = "  Alice    Smith  "
        result = user.get_full_name()
        self.assertEqual(result, expected)

    def test_get_full_name_with_unicode_characters(self):
        user = User(first_name="Иван", last_name="Иванович")
        expected = "Иван Иванович"
        result = user.get_full_name()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
```