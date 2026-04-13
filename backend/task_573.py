```python
# Since the task is to create basic directory and file structure for a new FastAPI project,
# here is a Python script that creates the directories and empty files for this clean architecture setup
# with repository pattern and service layer.

import os

def create_project_structure(base_dir: str = "fastapi_project"):
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

    def create_items(path, items):
        for name, content in items.items():
            full_path = os.path.join(path, name)
            if isinstance(content, dict):
                os.makedirs(full_path, exist_ok=True)
                create_items(full_path, content)
            else:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)

    create_items(".", structure)

if __name__ == "__main__":
    create_project_structure()
```

This script will create the following directory structure with empty files:

```
fastapi_project/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── greeting_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── greeting_service.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_greeting.py
├── requirements.txt
└── README.md
```