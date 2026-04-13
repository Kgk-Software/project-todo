```python
import os

def initialize_fastapi_project_structure(base_dir: str = "fastapi_project"):
    structure = {
        "app": {
            "__init__.py": "",
            "main.py": (
                "from fastapi import FastAPI, Depends\n\n"
                "# Service Layer\n"
                "class HelloService:\n"
                "    def say_hello(self) -> str:\n"
                "        return \"Hello, World!\"\n\n"
                "# Dependency Injector\n"
                "def get_hello_service() -> HelloService:\n"
                "    return HelloService()\n\n"
                "def create_app() -> FastAPI:\n"
                "    app = FastAPI(title=\"FastAPI Clean Architecture Project\")\n\n"
                "    @app.get(\"/hello\")\n"
                "    def hello(hello_service: HelloService = Depends(get_hello_service)):\n"
                "        return {\"message\": hello_service.say_hello()}\n\n"
                "    return app\n\n"
                "app = create_app()\n\n"
                "if __name__ == \"__main__\":\n"
                "    import uvicorn\n"
                "    uvicorn.run(\"app.main:app\", host=\"127.0.0.1\", port=8000, reload=True)\n"
            ),
            "api": {
                "__init__.py": "",
            },
            "repositories": {
                "__init__.py": "",
            },
            "services": {
                "__init__.py": "",
            },
            "models": {
                "__init__.py": "",
            },
            "core": {
                "__init__.py": "",
            },
        },
        "tests": {
            "__init__.py": "",
        },
        "requirements.txt": "fastapi\nuvicorn\n",
        "README.md": "# FastAPI Clean Architecture\n\nProject following Clean Architecture, Repository Pattern and Service Layer.",
    }

    def create_files(base_path, structure_dict):
        for name, content in structure_dict.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(path, content)
            else:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

    os.makedirs(base_dir, exist_ok=True)
    create_files(base_dir, structure)
    print(f"Initialized FastAPI project structure in '{base_dir}' directory.")

if __name__ == "__main__":
    initialize_fastapi_project_structure()
```