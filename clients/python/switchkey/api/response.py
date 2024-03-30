
class SwitchKeyResponseType(type):
    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        return obj


class SwitchKeyResponse(metaclass=SwitchKeyResponseType):

    def __init__(
        self,
        status_code: int,
        data=[],
        error_message: str | None = None,
        message: str | None = None,
    ):
        self.status_code = status_code
        self.data = data
        self.error_message = error_message
        self.message = message

    def __repr__(self):
        is_error = self.error_message is None
        self.message = self.message if self.message is not None else None
        self.data = self.data if self.data is not None else None
        self.error_message = (
            self.error_message if self.error_message is not None else None
        )

        return f"SwitchKeyResponse(status_code={self.status_code}, data={self.data}, message={self.message}, error={is_error}, error_message={self.error_message})"

    def get_error_message(self):
        return self.error_message

    def get_data(self):
        return self.data

    def get_message(self):
        return self.message

    def get_status_code(self):
        return self.status_code
