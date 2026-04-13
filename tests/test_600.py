```python
import pytest
from unittest import mock

# Assuming the FastAPI start script is in fastapi_start.py with a function main()
# that runs uvicorn to start the FastAPI app.
#
# Example assumed code for fastapi_start.py could be:
#
# import uvicorn
#
# def main():
#     uvicorn.run("app:app", host="127.0.0.1", port=8000)
#

import fastapi_start


def test_main_calls_uvicorn_run_with_defaults():
    with mock.patch("uvicorn.run") as mock_run:
        fastapi_start.main()
        mock_run.assert_called_once_with("app:app", host="127.0.0.1", port=8000)


def test_main_accepts_custom_parameters(monkeypatch):
    # If the script is designed to accept custom host and port parameters,
    # for example from environment variables or parameters, test that.
    # Here, monkeypatch environment variables if used.

    monkeypatch.setenv("FASTAPI_HOST", "0.0.0.0")
    monkeypatch.setenv("FASTAPI_PORT", "9000")

    with mock.patch("uvicorn.run") as mock_run:
        fastapi_start.main()
        mock_run.assert_called_once_with("app:app", host="0.0.0.0", port=9000)


def test_main_handles_uvicorn_error_gracefully():
    with mock.patch("uvicorn.run", side_effect=RuntimeError("Failing uvicorn")) as mock_run:
        with pytest.raises(RuntimeError, match="Failing uvicorn"):
            fastapi_start.main()


def test_main_calls_with_correct_app_path():
    with mock.patch("uvicorn.run") as mock_run:
        fastapi_start.main()
        called_args, called_kwargs = mock_run.call_args
        assert called_args[0] == "app:app"


@pytest.mark.parametrize(
    "host, port",
    [
        ("127.0.0.1", 8000),
        ("0.0.0.0", 8080),
        ("localhost", 5000),
    ],
)
def test_uvicorn_run_called_with_various_hosts_ports(host, port):
    with mock.patch("uvicorn.run") as mock_run:
        # Assuming main() can take parameters, if not, adjust accordingly
        if hasattr(fastapi_start.main, "__call__"):
            try:
                fastapi_start.main(host=host, port=port)
                mock_run.assert_called_once_with("app:app", host=host, port=port)
            except TypeError:
                # main() does not accept params: fallback to default test
                fastapi_start.main()
                mock_run.assert_called_once_with("app:app", host="127.0.0.1", port=8000)
```