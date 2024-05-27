import os
from django.core.management.base import BaseCommand
from switchkeys.models.users import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Use this command only in development mode."""
        superuser_email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        superuser_password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        if not User.objects.filter(email=superuser_email).exists():
            User.objects.create_superuser(
                email=superuser_email,
                password=superuser_password,
            )
            print(f"Superuser with email {superuser_email} created.")
        else:
            print(f"Superuser with email {superuser_email} already exists.")
