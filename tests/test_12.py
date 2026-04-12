```python
import pytest
from your_module import create_todo, Todo, TodoError

@pytest.fixture
def valid_todo_data():
    return {
        "title": "Test Todo",
        "description": "This is a test todo item",
        "completed": False,
    }

@pytest.fixture
def invalid_todo_data():
    return {
        "title": "",  # Assuming title is required and cannot be empty
        "description": "Missing title",
        "completed": False,
    }

def test_create_todo_success(valid_todo_data):
    todo = create_todo(**valid_todo_data)
    assert isinstance(todo, Todo)
    assert todo.title == valid_todo_data["title"]
    assert todo.description == valid_todo_data["description"]
    assert todo.completed == valid_todo_data["completed"]

def test_create_todo_missing_title_raises_error(invalid_todo_data):
    with pytest.raises(TodoError):
        create_todo(**invalid_todo_data)

def test_create_todo_defaults_completed_false():
    todo = create_todo(title="New Todo", description="No completed specified")
    assert todo.completed is False

def test_create_todo_title_strip_whitespace():
    todo = create_todo(title="  Trimmed Title  ", description="Test trimming")
    assert todo.title == "Trimmed Title"

def test_create_todo_description_optional():
    todo = create_todo(title="No description")
    assert todo.description == "" or todo.description is None
```
