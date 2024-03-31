from functools import wraps

def check_data_type(data_type):
    """
    Decorator to check if the provided data is of the specified type.

    Args:
        data_type: The expected type of the data.

    Raises:
        TypeError: If the provided data is not an instance of the specified type.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            data = kwargs.get('data', None)
            if not isinstance(data, data_type):
                raise TypeError(
                    f"Data should be an instance of '{data_type.__name__}'."
                )
            return func(self, *args, **kwargs)
        return wrapper
    return decorator