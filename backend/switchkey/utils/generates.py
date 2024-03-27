"""This file containes any generate functions."""
import random


def generate_random_color():
    """Genrate a random color to return it in case there is no user image selected."""
    color: str = ""
    for i in range(0, 6):
        color += str(random.randint(1, 7))
    return f"#{color}"
