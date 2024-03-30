from rest_framework.serializers import ModelSerializer, SerializerMethodField

from switchkey.serializers.organizations import OrganizationSerializer
from switchkey.models.management import OrganizationProject


class OrganizationProjectSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project`` .
    """

    organization = SerializerMethodField()

    class Meta:
        model = OrganizationProject
        fields = ("id", "name", "created", "modified", "organization")
        read_only_fields = ("id", "created", "modified")

    def get_organization(self, obj: OrganizationProject):
        return OrganizationSerializer(obj.organization).data
