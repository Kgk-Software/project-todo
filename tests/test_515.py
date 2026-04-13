```python
import os
import unittest

class TestProjectDirectoryStructure(unittest.TestCase):
    def setUp(self):
        # Define the expected project root directory path here,
        # adjust as needed to point to the actual project root for tests.
        # For demonstration, using current working directory.
        self.project_root = os.getcwd()

        # Expected directory and file structure relative to project root
        self.expected_dirs = [
            "app",
            "app/api",
            "app/core",
            "app/models",
            "app/routes",
            "tests"
        ]

        self.expected_files = [
            "app/main.py",
            "app/api/__init__.py",
            "app/core/config.py",
            "app/models/__init__.py",
            "app/routes/__init__.py",
            "tests/__init__.py",
            "requirements.txt",
            "README.md"
        ]

    def test_directories_exist(self):
        """Test that all expected directories exist in the project structure."""
        for directory in self.expected_dirs:
            dir_path = os.path.join(self.project_root, directory)
            with self.subTest(directory=directory):
                self.assertTrue(os.path.isdir(dir_path), f"Directory missing: {directory}")

    def test_files_exist(self):
        """Test that all expected files exist in the project structure."""
        for file_path in self.expected_files:
            full_path = os.path.join(self.project_root, file_path)
            with self.subTest(file=file_path):
                self.assertTrue(os.path.isfile(full_path), f"File missing: {file_path}")

    def test_no_unexpected_files_or_dirs_in_app(self):
        """
        Optional: Test that app directory does not contain unexpected files or folders 
        other than expected ones (can be customized or omitted if project is evolving).
        """
        allowed_app_dirs = {d.split('/')[-1] for d in self.expected_dirs if d.startswith("app/") and len(d.split('/'))==2}
        allowed_app_dirs.add("__pycache__")  # often automatically created

        allowed_app_files = {f.split('/')[-1] for f in self.expected_files if f.startswith("app/") and len(f.split('/'))==2}
        # You can add more allowed files here if necessary

        app_path = os.path.join(self.project_root, "app")
        for entry in os.listdir(app_path):
            entry_path = os.path.join(app_path, entry)
            if os.path.isdir(entry_path):
                self.assertIn(entry, allowed_app_dirs, f"Unexpected directory in app/: {entry}")
            else:
                self.assertIn(entry, allowed_app_files, f"Unexpected file in app/: {entry}")


if __name__ == "__main__":
    unittest.main()
```