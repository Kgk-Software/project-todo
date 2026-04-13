```python
import os

def create_project_directory_structure(base_path: str = "."):
    directories = [
        "app",
        "app/api",
        "app/api/v1",
        "app/core",
        "app/models",
        "app/repositories",
        "app/services",
        "app/schemas",
        "app/tests"
    ]

    for directory in directories:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

if __name__ == "__main__":
    create_project_directory_structure()
```