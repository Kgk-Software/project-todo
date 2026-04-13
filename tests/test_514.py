```python
import unittest
import os
import subprocess
import sys

class TestDependencyManagement(unittest.TestCase):
    def setUp(self):
        # Assume requirements.txt or pyproject.toml is in the current working directory
        self.project_root = os.getcwd()
        self.requirements_path = os.path.join(self.project_root, 'requirements.txt')
        self.pyproject_path = os.path.join(self.project_root, 'pyproject.toml')

    def test_requirements_file_exists(self):
        """Test that requirements.txt file exists."""
        self.assertTrue(os.path.isfile(self.requirements_path), "requirements.txt file is missing.")

    def test_requirements_file_not_empty(self):
        """Test that requirements.txt is not empty."""
        with open(self.requirements_path, 'r') as req_file:
            contents = req_file.read().strip()
            self.assertTrue(len(contents) > 0, "requirements.txt is empty.")

    def test_requirements_packages_installed(self):
        """
        Test that all packages listed in requirements.txt are installable and importable.

        This test will:
        - read packages from requirements.txt
        - try to import them or verify installation by invoking pip show
        """
        with open(self.requirements_path, 'r') as req_file:
            lines = req_file.readlines()

        packages = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # Extract package name from possible version specifiers
            # e.g. fastapi==0.70.0 -> fastapi
            pkg_name = line.split('==')[0].split('>=')[0].split('<=')[0].strip()
            packages.append(pkg_name)

        for package in packages:
            with self.subTest(package=package):
                # Using pip show to check if package is installed
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "show", package],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                self.assertEqual(
                    result.returncode, 0,
                    f"Package '{package}' from requirements.txt is not installed."
                )

    def test_pyproject_file_exists_if_no_requirements(self):
        """If requirements.txt does not exist, pyproject.toml should exist."""
        if not os.path.isfile(self.requirements_path):
            self.assertTrue(os.path.isfile(self.pyproject_path), "Neither requirements.txt nor pyproject.toml found.")


if __name__ == "__main__":
    unittest.main()
```