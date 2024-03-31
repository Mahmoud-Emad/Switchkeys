"""
Global SwitchKey exception and warning classes.
"""

# --------------------------------------------------------------------
# Exceptions

##
# Base class for all kinds of client-side errors.


class Error(Exception):
    """Base class for client errors."""

    __str__ = object.__str__


class ResponseError(Error):
    """Indicates a broken response package."""

    pass


class FeatureNotEnabled(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
