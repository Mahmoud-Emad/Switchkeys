""" database user model """
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AnonymousUser

from typing import Any, Union

from switchkey.utils.generates import generate_random_color
from switchkey.models.abstracts import TimeStamp


class CshrBaseUserManger(BaseUserManager):
    """this is the main class for user manger"""

    def create_user(self, email: str, password: str) -> "User":
        """DMC method to create user"""
        if not email:
            raise ValueError("Email is required.")

        user = self.model(
            email=self.normalize_email(email),
            first_name="Switchkey",
            last_name="Admin",
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str):
        """create superuser"""
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStamp):
    """main user model"""

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    background_color = models.CharField(max_length=10, default=generate_random_color)
    email = models.EmailField(max_length=45, unique=True)
    joining_at = models.DateField(auto_now_add=True)

    USERNAME_FIELD = "email"
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CshrBaseUserManger()

    @property
    def full_name(self) -> str:
        "return the user's full name"
        return "%s %s" % (self.first_name.title(), self.last_name.title())

    def has_perm(
        self, perm: str, obj: Union[models.Model, AnonymousUser, None] = None
    ) -> bool:
        """For checking permissions. to keep it simple all admin have ALL permissions"""
        return self.is_admin

    @staticmethod
    def has_module_perms(app_label: Any) -> bool:
        """Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)"""
        return True

    def __str__(self) -> str:
        return f"{self.email}"
