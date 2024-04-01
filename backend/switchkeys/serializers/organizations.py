from rest_framework.serializers import ModelSerializer, SerializerMethodField

from switchkeys.serializers.users import OrganizationUserSerializer
from switchkeys.models.management import Organization


class OrganizationSerializer(ModelSerializer):
    """
    ``Serializer`` for ``Organization`` .
    """

    owner = SerializerMethodField()
    members = SerializerMethodField()

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

    def get_owner(self, obj: Organization):
        return OrganizationUserSerializer(obj.owner).data

    def get_members(self, obj: Organization):
        return OrganizationUserSerializer(obj.members, many=True).data
