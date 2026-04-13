```python
import os
import shutil
import tempfile
import pytest
from your_module import create_project_structure  # Replace with actual import


@pytest.fixture
def temp_project_dir():
    """
    Create a temporary directory to serve as the project root.
    Clean up after test finishes.
    """
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_project_structure_created(temp_project_dir):
    """
    Test that the project directory structure is created correctly.
    Assumes the create_project_structure function takes a root path argument.
    """

    # Call the function to create project structure
    create_project_structure(temp_project_dir)

    # Define expected directories and files based on typical project structure
    expected_dirs = [
        "app",
        "app/api",
        "app/core",
        "app/models",
        "app/schemas",
        "app/services",
        "tests",
    ]
    expected_files = [
        "README.md",
        "requirements.txt",
        "app/main.py",
        "app/__init__.py",
        "app/api/__init__.py",
        "tests/__init__.py",
    ]

    # Check directories exist
    for d in expected_dirs:
        dir_path = os.path.join(temp_project_dir, d)
        assert os.path.isdir(dir_path), f"Expected directory '{d}' to be created"

    # Check files exist
    for f in expected_files:
        file_path = os.path.join(temp_project_dir, f)
        assert os.path.isfile(file_path), f"Expected file '{f}' to be created"
```