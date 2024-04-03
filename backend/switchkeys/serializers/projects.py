from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    IntegerField,
)

from switchkeys.serializers.organizations import OrganizationSerializer
from switchkeys.models.management import OrganizationProject


class OrganizationProjectSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project`` .
    """

    organization = SerializerMethodField()
    organization_id = IntegerField()

    class Meta:
        model = OrganizationProject
        fields = (
            "id",
            "name",
            "created",
            "modified",
            "organization",
            "organization_id",
        )
        read_only_fields = ("id", "created", "modified")
        write_only_fields = ("name", "organization_id")

    def get_organization(self, obj: OrganizationProject):
        return OrganizationSerializer(obj.organization).data
