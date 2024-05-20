from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    IntegerField,
)

# from switchkeys.serializers.environments import EnvironmentKeyAndNameSerializer
from switchkeys.serializers.organizations import OrganizationSerializer
from switchkeys.models.management import OrganizationProject, ProjectEnvironment


class EnvironmentKeyAndNameSerializer(ModelSerializer):
    """Serializer to serialize the `ProjectEnvironment` model and return only the `[name, environment_key]` fields."""

    class Meta:
        model = ProjectEnvironment
        fields = [
            "name",
            "environment_key",
        ]

class OrganizationProjectSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project`` .
    """

    organization = SerializerMethodField()
    organization_id = IntegerField()
    environments = SerializerMethodField()

    class Meta:
        model = OrganizationProject
        fields = (
            "id",
            "name",
            "created",
            "modified",
            "organization",
            "organization_id",
            "environments",
        )
        read_only_fields = ("id", "created", "modified")
        write_only_fields = ("name", "organization_id")

    def get_organization(self, obj: OrganizationProject):
        """Return the `OrganizationSerializer` serializer"""
        return OrganizationSerializer(obj.organization).data

    def get_environments(self, obj: OrganizationProject):
        """Return the `EnvironmentKeyAndNameSerializer` serializer."""
        envs = ProjectEnvironment.objects.filter(project=obj)
        return EnvironmentKeyAndNameSerializer(envs, many=True).data
