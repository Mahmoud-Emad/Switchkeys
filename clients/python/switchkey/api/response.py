class SwitchKeyResponse:
    def __init__(
        self,
        status_code: int,
        data=None,
        error_message: str | None = None,
        message: str | None = None,
    ):
        """
        Initialize a SwitchKeyResponse object.

        Args:
            status_code (int): The HTTP status code of the response.
            data (Any, optional): The data returned in the response. Defaults to None.
            error_message (str | None, optional): The error message, if any. Defaults to None.
            message (str | None, optional): Additional message associated with the response. Defaults to None.
        """
        self.status_code = status_code
        self.data = data
        self.error_message = error_message
        self.message = message

    def __repr__(self):
        """
        Return a string representation of the SwitchKeyResponse object.

        Returns:
            str: String representation of the SwitchKeyResponse object.
        """
        is_error = self.error_message is None
        self.message = self.message if self.message is not None else None
        self.data = self.data if self.data is not None else None
        self.error_message = self.error_message if self.error_message is not None else None

        return f"SwitchKeyResponse(status_code={self.status_code}, data={self.data}, message={self.message}, error={is_error}, error_message={self.error_message})"

    def get_error_message(self):
        """
        Get the error message associated with the response.

        Returns:
            str | None: Error message if present, otherwise None.
        """
        return self.error_message

    def get_data(self):
        """
        Get the data associated with the response.

        Returns:
            Any: Data associated with the response.
        """
        return self.data

    def get_message(self):
        """
        Get the additional message associated with the response.

        Returns:
            str | None: Additional message if present, otherwise None.
        """
        return self.message

    def get_status_code(self):
        """
        Get the HTTP status code of the response.

        Returns:
            int: HTTP status code.
        """
        return self.status_code
