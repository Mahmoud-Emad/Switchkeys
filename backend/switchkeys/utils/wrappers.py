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
        "fields": {
            field_name: "This field is unique"
        },
    }
