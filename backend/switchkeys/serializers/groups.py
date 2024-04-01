from rest_framework.serializers import ModelSerializer

from switchkeys.models.management import OrganizationProjectGroup


class OrganizationProjectGroupSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization project group`` .
    """

    class Meta:
        model = OrganizationProjectGroup
        fields = ("id", "name", "created", "modified", "project", "members")
        read_only_fields = ("id", "created", "modified")
