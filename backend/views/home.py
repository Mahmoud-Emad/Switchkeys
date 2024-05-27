from django.urls import get_resolver
from django.http import JsonResponse
from components import config


def display_urls(request):
    """
    View function to display all available URL patterns in the Django project.

    Args:
        request: HttpRequest object representing the incoming request.

    Returns:
        JSON response containing information about the server version and available URL patterns.
    """
    # Get the resolver for the current Django project
    resolver = get_resolver()

    # Extract URL patterns and their corresponding view functions or classes
    url_patterns = []
    for url_pattern in resolver.url_patterns:
        url_name = url_pattern.name if hasattr(url_pattern, "name") else None
        url_path = str(url_pattern.pattern)
        url_view = getattr(url_pattern.callback, "__name__", str(url_pattern.callback))
        url_patterns.append({"name": url_name, "path": url_path, "view": url_view})

    # Return the list of URL patterns as JSON response
    return JsonResponse(
        {
            "server": "backend",
            "version": config("SWITCHKEYS_VERSION"),
            "urls": url_patterns,
        }
    )
