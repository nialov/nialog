"""
nialog.

JSON logging setup for Python.
"""

__version__ = "0.0.1.post5.dev0+89e5de6"

from nialog.logger import LoggingLevel, setup_module_logging

assert callable(setup_module_logging)

assert isinstance(LoggingLevel.WARNING.value, str)
