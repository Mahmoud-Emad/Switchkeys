from django.db import models
from switchkeys.models.users import ProjectEnvironmentUser, User
from switchkeys.models.abstracts import TimeStampedModel
import uuid


class Organization(TimeStampedModel):
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
        return f"{self.owner} | {self.name}"

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        unique_together = (
            "name",
            "owner",
        )


class OrganizationProject(TimeStampedModel):
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


class OrganizationProjectGroup(TimeStampedModel):
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


class ProjectEnvironment(TimeStampedModel):
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
