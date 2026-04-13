```python
import os
import unittest

class TestFastAPIProjectStructure(unittest.TestCase):
    def setUp(self):
        # Assuming tests run at the project root directory
        self.project_root = os.getcwd()

        # Expected directories within the project
        self.expected_dirs = [
            "app",
            "app/api",
            "app/core",
            "app/models",
            "app/routes",
            "tests"
        ]

        # Expected files within the project
        self.expected_files = [
            "app/main.py",
            "app/api/__init__.py",
            "app/core/__init__.py",
            "app/models/__init__.py",
            "app/routes/__init__.py",
            "tests/__init__.py",
            "requirements.txt",
            "README.md"
        ]

    def test_directories_exist(self):
        """Test that all expected directories exist"""
        for directory in self.expected_dirs:
            dir_path = os.path.join(self.project_root, directory)
            with self.subTest(directory=directory):
                self.assertTrue(os.path.isdir(dir_path), f"Expected directory missing: {directory}")

    def test_files_exist(self):
        """Test that all expected files exist"""
        for file_rel_path in self.expected_files:
            file_path = os.path.join(self.project_root, file_rel_path)
            with self.subTest(file=file_rel_path):
                self.assertTrue(os.path.isfile(file_path), f"Expected file missing: {file_rel_path}")

    def test_no_unexpected_files_in_app(self):
        """Optional: Verify no unexpected files are present in app/ root directory (excluding known files)."""
        app_dir = os.path.join(self.project_root, "app")
        allowed_files = {f.split('/')[-1] for f in self.expected_files if f.startswith("app/") and len(f.split('/')) == 2}
        allowed_files.add("__pycache__")
        if os.path.exists(app_dir):
            for entry in os.listdir(app_dir):
                entry_path = os.path.join(app_dir, entry)
                if os.path.isfile(entry_path):
                    self.assertIn(entry, allowed_files, f"Unexpected file in app/: {entry}")


if __name__ == "__main__":
    unittest.main()
```