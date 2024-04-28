from django.contrib import admin
from django.urls import path, include
from views.home import display_urls
import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", display_urls),
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("auth/", include("switchkeys.urls.auth")),
                path("users/", include("switchkeys.urls.users")),
                path("organizations/", include("switchkeys.urls.organizations")),
                path("projects/", include("switchkeys.urls.projects")),
                path("groups/", include("switchkeys.urls.groups")),
                path("environments/", include("switchkeys.urls.environments")),
            ]
        ),
    ),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)


if settings.DEBUG:
    import debug_toolbar
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Api Documentation",
            default_version="v1",
        ),
        public=False,
    )

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path("__debug__/", include(debug_toolbar.urls)),
        # Swagger
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        # noqa: DJ05
    ] + urlpatterns
