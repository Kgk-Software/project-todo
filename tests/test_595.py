```python
import os
import shutil
import tempfile
import pytest
from your_module import setup_initial_structure  # Replace with actual import


@pytest.fixture
def temp_project_dir():
    """
    Creates a temporary directory for the project root.
    Cleans up after the test runs.
    """
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_initial_folder_structure_created(temp_project_dir):
    """
    Test that the initial folder and file structure for the FastAPI project is created successfully.
    Assumes setup_initial_structure creates a predefined set of folders and files.
    """
    setup_initial_structure(temp_project_dir)

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

    # Verify directories exist
    for d in expected_dirs:
        dir_path = os.path.join(temp_project_dir, d)
        assert os.path.isdir(dir_path), f"Directory '{d}' should be created"

    # Verify files exist
    for f in expected_files:
        file_path = os.path.join(temp_project_dir, f)
        assert os.path.isfile(file_path), f"File '{f}' should be created"


def test_structure_is_idempotent(temp_project_dir):
    """
    Running the setup_initial_structure multiple times should not cause errors or change the structure.
    """
    setup_initial_structure(temp_project_dir)
    # Capture initial state
    initial_dir_contents = {
        root: sorted(files + dirs)
        for root, dirs, files in os.walk(temp_project_dir)
    }

    # Run again
    setup_initial_structure(temp_project_dir)

    # Capture second state
    second_dir_contents = {
        root: sorted(files + dirs)
        for root, dirs, files in os.walk(temp_project_dir)
    }

    assert initial_dir_contents == second_dir_contents, "Structure should remain unchanged after repeated setup"


def test_files_not_empty(temp_project_dir):
    """
    Some essential files like README.md, main.py should not be empty if the setup creates boilerplate code.
    """
    setup_initial_structure(temp_project_dir)

    files_to_check = [
        "README.md",
        "app/main.py",
    ]

    for f in files_to_check:
        file_path = os.path.join(temp_project_dir, f)
        assert os.path.isfile(file_path), f"File '{f}' should exist"
        assert os.path.getsize(file_path) > 0, f"File '{f}' should not be empty"
```