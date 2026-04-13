```python
import os

def initialize_fastapi_project_structure(base_dir: str = "fastapi_project"):
    structure = {
        base_dir: {
            "app": {
                "api": {
                    "__init__.py": "",
                    "routes.py": "",
                },
                "core": {
                    "__init__.py": "",
                    "config.py": "",
                },
                "repositories": {
                    "__init__.py": "",
                    "greeting_repository.py": "",
                },
                "services": {
                    "__init__.py": "",
                    "greeting_service.py": "",
                },
                "main.py": "",
            },
            "tests": {
                "__init__.py": "",
                "test_greeting.py": "",
            },
            "requirements.txt": "",
            "README.md": "",
        }
    }

    def create_dir_structure(path, content):
        for name, val in content.items():
            item_path = os.path.join(path, name)
            if isinstance(val, dict):
                os.makedirs(item_path, exist_ok=True)
                create_dir_structure(item_path, val)
            else:
                # create file with content (empty string here)
                with open(item_path, "w", encoding="utf-8") as f:
                    f.write(val)

    create_dir_structure(".", structure)

if __name__ == "__main__":
    initialize_fastapi_project_structure()
```