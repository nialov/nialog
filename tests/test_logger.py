"""
Test logger.py.
"""

import logging

import pytest

from nialog import logger

VALID_LEVELS = (
    logging.DEBUG,
    logging.INFO,
    logging.WARNING,
    logging.ERROR,
    logging.CRITICAL,
)


@pytest.mark.parametrize("json_indent", [1, 2, 3, 10])
@pytest.mark.parametrize("logging_level_int", VALID_LEVELS)
def test_setup_module_logging(logging_level_int: int, json_indent: int, caplog, capsys):
    """
    Test setup_module_logging.
    """
    with caplog.at_level(logging.DEBUG):
        result = logger.setup_module_logging(logging_level_int, json_indent=json_indent)

    assert len(caplog.records) > 0
    for record in caplog.records:
        assert record.levelno == logging.INFO
    assert "Set up logging level." in caplog.text

    assert result is None

    captured = capsys.readouterr()
    captured_stderr = captured.err
    captured_stdout = captured.out

    assert "logger.py" in captured_stderr
    assert "logging_level_int" in captured_stderr

    assert len(captured_stdout) == 0


def test_logging_level_enums():
    """
    Test LoggingLevel.
    """
    for logging_level in logger.LoggingLevel:
        assert hasattr(logging, logging_level.value)
        assert isinstance(getattr(logging, logging_level.value), int)
