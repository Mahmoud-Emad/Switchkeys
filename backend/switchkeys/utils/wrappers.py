from typing import Any


def unique_field_error(field_name: str):
    """
    Generate a unique field error response for API requests.

    Args:
        field_name (str): The name of the unique field causing the error.

    Returns:
        dict: A dictionary representing the unique field error response.

    Example:
        >>> unique_field_error("name")
        {
            "message": "Please note that you have passed a unique field.",
            "fields": {
                "name": "This field is unique"
            }
        }
    """
    return {
        "message": "Please note that you have passed a unique field.",
        "fields": {field_name: "This field is unique"},
    }


def value_not_accepted_error(
    field_name: str, user_value: Any, default_value: Any
) -> dict:
    """
    Generate a field value error response for API requests.

    Args:
        field_name (str): The name of the field causing the error.
        user_value (Any): The value that the user sent.
        default_value (Any): The value that the field accepts.

    Returns:
        dict: A dictionary representing the field error response.

    Example:
        >>> field_value_error("device_type", "Google", ["Android", "IPhone"])
        {
            "message": "Please note that you have sent a value that is not accepted by the field.",
            "fields": {
                "device_type": "You have sent 'Google' and this field accepts ['Android', 'IPhone']"
            }
        }
    """
    return {
        "message": "Please note that you have sent a value that is not accepted by the field.",
        "fields": {
            field_name: f"You have sent '{user_value}' and this field accepts '{default_value}'."
        },
    }
