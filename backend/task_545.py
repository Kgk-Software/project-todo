```python
import os

def create_project_structure():
    dirs = [
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
            "from fastapi import FastAPI\n\n"
            "def create_app() -> FastAPI:\n"
            "    app = FastAPI(\n"
            "        title=\"Clean Architecture FastAPI App\",\n"
            "        description=\"FastAPI application structured with clean architecture, repository pattern, and service layer\",\n"
            "        version=\"1.0.0\"\n"
            "    )\n\n"
            "    # TODO: Include routers here as they are implemented\n"
            "    # Example:\n"
            "    # from app.api.v1 import api_router\n"
            "    # app.include_router(api_router, prefix=\"/api/v1\")\n\n"
            "    return app\n\n"
            "app = create_app()\n"
        ),
        "app/api/v1/__init__.py": "",
        "app/core/__init__.py": "",
        "app/models/__init__.py": "",
        "app/repositories/__init__.py": "",
        "app/services/__init__.py": "",
        "app/schemas/__init__.py": "",
        "app/tests/__init__.py": "",
    }

    for d in dirs:
        os.makedirs(d, exist_ok=True)

    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    create_project_structure()
```