```python
import os

def create_folder_structure(base_path: str = "."):
    folders = [
        "app",
        "app/api",
        "app/api/v1",
        "app/core",
        "app/models",
        "app/repositories",
        "app/services",
        "app/schemas",
        "app/tests",
    ]

    files = {
        "app/main.py": (
            'from fastapi import FastAPI\n\n'
            'def create_app() -> FastAPI:\n'
            '    app = FastAPI(\n'
            '        title="My Clean Architecture FastAPI Application",\n'
            '        description="API built with FastAPI following clean architecture principles",\n'
            '        version="1.0.0"\n'
            '    )\n'
            '    return app\n\n'
            'app = create_app()\n'
        ),
        "app/core/config.py": (
            "# Configuration settings go here\n\n"
            "class Settings:\n"
            "    # example: database_url: str = \"sqlite:///./test.db\"\n"
            "    pass\n\n"
            "settings = Settings()\n"
        ),
        "app/api/v1/__init__.py": "",
        "app/models/__init__.py": "",
        "app/repositories/__init__.py": "",
        "app/services/__init__.py": "",
        "app/schemas/__init__.py": "",
        "app/tests/__init__.py": "",
        "app/tests/test_sample.py": (
            "def test_example():\n"
            "    assert True\n"
        ),
    }

    # Create folders
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)

    # Create files with initial content
    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)
        if not os.path.exists(full_path):
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    create_folder_structure()
```