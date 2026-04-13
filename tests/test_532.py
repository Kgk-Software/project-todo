```python
import unittest
from unittest.mock import patch
from my_module import my_function  # replace with actual module and function names

class TestMyFunctionSuccess(unittest.TestCase):
    @patch('my_module.external_dependency')  # mock external calls if any
    def test_successful_response(self, mock_external):
        # Arrange
        mock_external.return_value = {
            'status': 'success',
            'data': {'id': 123, 'name': 'Test Item'}
        }

        expected_result = {'id': 123, 'name': 'Test Item'}
        
        # Act
        result = my_function()

        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_result)
        self.assertEqual(mock_external.call_count, 1)

if __name__ == '__main__':
    unittest.main()
```