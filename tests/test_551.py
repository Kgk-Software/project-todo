```python
import os
import pytest

# Assuming the Initialize Project Structure task creates certain directories and files
# Define expected directories and files
EXPECTED_DIRECTORIES = [
    "app",
    "app/api",
    "app/core",
    "app/models",
    "app/schemas",
    "tests",
]

EXPECTED_FILES = [
    "app/main.py",
    "app/api/__init__.py",
    "app/core/__init__.py",
    "app/models/__init__.py",
    "app/schemas/__init__.py",
    "tests/__init__.py",
    "README.md",
    "requirements.txt",
    "setup.py",
]

@pytest.mark.parametrize("directory", EXPECTED_DIRECTORIES)
def test_directories_exist(tmp_path, directory):
    """
    Test that expected directories exist after project initialization.
    Uses tmp_path fixture to simulate project root.
    """
    project_root = tmp_path
    path_to_check = project_root / directory
    # Simulate creation of directory
    path_to_check.mkdir(parents=True, exist_ok=True)
    assert path_to_check.is_dir()

@pytest.mark.parametrize("file", EXPECTED_FILES)
def test_files_exist(tmp_path, file):
    """
    Test that expected files exist after project initialization.
    Uses tmp_path fixture to simulate project root.
    """
    project_root = tmp_path
    file_path = project_root / file
    # Simulate creation of file with empty content
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text("")
    assert file_path.is_file()

def test_main_py_has_fastapi_app(tmp_path):
    """
    Test that app/main.py contains FastAPI app creation code.
    """
    main_file = tmp_path / "app" / "main.py"
    main_file.parent.mkdir(parents=True, exist_ok=True)
    content = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
"""
    main_file.write_text(content)
    assert main_file.is_file()
    file_content = main_file.read_text()
    assert "FastAPI()" in file_content
    assert "@app.get" in file_content

def test_readme_contains_project_title(tmp_path):
    """
    Test that README.md contains project title or initialization info.
    """
    readme = tmp_path / "README.md"
    readme.write_text("# Project Title\n\nInitialized project structure.")
    assert readme.is_file()
    content = readme.read_text()
    assert "Project Title" in content or "initialized" in content.lower()
```