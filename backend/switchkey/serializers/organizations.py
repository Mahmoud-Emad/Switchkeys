from rest_framework.serializers import ModelSerializer

from switchkey.models.management import Organization


class OrganizationSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization`` .
    """

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "owner",
            "members",
            "created",
            "modified",
        )
        read_only_fields = ("id", "members", "created", "modified", "owner")
