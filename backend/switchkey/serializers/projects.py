from rest_framework.serializers import ModelSerializer

from switchkey.models.management import OrganizationProject


class OrganizationProjectSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project`` .
    """

    class Meta:
        model = OrganizationProject
        fields = ("id", "name", "created", "modified", "organization")
        read_only_fields = ("id", "created", "modified")
