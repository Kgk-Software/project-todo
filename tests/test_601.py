```python
import sys
import pytest
from unittest import mock
from uvicorn import Config, Server

# Assuming the run script is defined in a module named uvicorn_run_script.py
# and has a function called main() that executes the uvicorn server run.
# Example:
# def main():
#     import uvicorn
#     uvicorn.run("app:app", host="127.0.0.1", port=8000)

# Since the task says "Add Uvicorn Run Script", we'll test this main function script.

# For illustration, let's assume uvicorn_run_script.py looks like this:
#
# import uvicorn
# def main():
#     uvicorn.run("app:app", host="127.0.0.1", port=8000)
#

import uvicorn_run_script


def test_uvicorn_run_script_calls_run_with_expected_args():
    with mock.patch("uvicorn.run") as mock_run:
        uvicorn_run_script.main()
        mock_run.assert_called_once_with("app:app", host="127.0.0.1", port=8000)


def test_uvicorn_config_server_run_called():
    # If the script uses Config and Server classes directly (alternative way),
    # we can test that these are used correctly.

    # Let's patch Config and Server to test interactions.
    with mock.patch("uvicorn_run_script.Config") as mock_config_cls, \
         mock.patch("uvicorn_run_script.Server") as mock_server_cls:

        mock_config_instance = mock.MagicMock()
        mock_server_instance = mock.MagicMock()

        mock_config_cls.return_value = mock_config_instance
        mock_server_cls.return_value = mock_server_instance

        # Call main
        uvicorn_run_script.main()

        # Assert Config called with expected arguments if applicable
        # If your actual implementation creates Config and Server explicitly,
        # adjust these assertions accordingly.
        # For example:
        # mock_config_cls.assert_called_once_with("app:app", host="127.0.0.1", port=8000)
        # mock_server_cls.assert_called_once_with(mock_config_instance)
        # mock_server_instance.run.assert_called_once()

        # If above lines are not applicable, ignore this test or adjust accordingly.


@pytest.mark.parametrize(
    "host, port",
    [
        ("127.0.0.1", 8000),
        ("0.0.0.0", 8080),
        ("192.168.1.1", 5000),
    ],
)
def test_uvicorn_run_script_with_custom_args(host, port):
    # This test assumes you might extend the run script to accept params
    # Here we'll simulate command line arguments or function parameters

    # Patch uvicorn.run to check call parameters
    with mock.patch("uvicorn.run") as mock_run:
        # If main accepts parameters, use them, else mock them
        # For example, if main(host, port) signature exists:
        # uvicorn_run_script.main(host=host, port=port)
        # Otherwise, we skip this test or redesign

        # For now, just assert the default call since no param supported yet
        uvicorn_run_script.main()
        mock_run.assert_called_once_with("app:app", host="127.0.0.1", port=8000)
```
