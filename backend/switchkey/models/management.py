from django.db import models
from switchkey.models.users import ProjectEnvironmentUser, User
from switchkey.models.abstracts import TimeStamp
import uuid


class Organization(TimeStamp):
    owner = models.ForeignKey(
        User, related_name="organization_owner", on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=20,
    )
    members = models.ManyToManyField(
        User, related_name="organization_members", blank=True
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        unique_together = (
            "name",
            "owner",
        )


class OrganizationProject(TimeStamp):
    name = models.CharField(
        max_length=20,
    )
    organization = models.ForeignKey(
        Organization,
        related_name="project_organization",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name} | {self.organization.name}"

    class Meta:
        verbose_name = "Organization Project"
        verbose_name_plural = "Organization Projects"
        unique_together = (
            "name",
            "organization",
        )


class OrganizationProjectGroup(TimeStamp):
    project = models.ForeignKey(
        OrganizationProject,
        related_name="project_groups",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, related_name="organization_groups")

    class Meta:
        verbose_name = "Organization Project Group"
        verbose_name_plural = "Organization Project Groups"
        unique_together = (
            "name",
            "project",
        )

    def __str__(self):
        return f"{self.project.name} | {self.name}"


class ProjectEnvironment(TimeStamp):
    project = models.ForeignKey(
        OrganizationProject,
        related_name="environment_project",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50)
    environment_key = models.UUIDField(default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(
        ProjectEnvironmentUser, related_name="environment_users", blank=True
    )

    def __str__(self):
        return f"{self.name} | {self.project.name}"


class FeatureStorage(TimeStamp):
    environment = models.ForeignKey(
        ProjectEnvironment,
        related_name="environment_keys",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    key = models.CharField(max_length=20)
    value = models.TextField(max_length=750)
    tag = models.CharField(max_length=20, null=True, blank=True)
    tag_color = models.CharField(max_length=25, null=True, blank=True)

    description = models.TextField(max_length=750, null=True, blank=True)
    enabled_by_default = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    last_used = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.key} | {self.environment.name} :: Project = {self.environment.project.name}"  # Changed to return key instead of name

    class Meta:
        verbose_name = "Feature Storage"
        verbose_name_plural = "Features Storage"
        unique_together = (
            "environment",
            "key",
        )
