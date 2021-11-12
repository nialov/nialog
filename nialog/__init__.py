"""
nialog.

JSON logging setup for Python.
"""

__version__ = "0.0.2.post2.dev0+e1f6c83"

from nialog.logger import LoggingLevel, setup_module_logging

assert callable(setup_module_logging)

assert isinstance(LoggingLevel.WARNING.value, str)
