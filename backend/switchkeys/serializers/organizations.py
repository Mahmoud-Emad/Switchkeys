from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    IntegerField,
)

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


class OrganizationAddMemberSerializer(ModelSerializer):
    """
    ``Serializer`` for adding a user on an ``Organization`` .
    """

    owner = SerializerMethodField()
    members = SerializerMethodField()
    member_id = IntegerField()

    class Meta:
        model = Organization
        fields = (
            "member_id",
            "id",
            "name",
            "owner",
            "members",
            "created",
            "modified",
        )
        read_only_fields = ("id", "name", "members", "created", "modified", "owner")

    def get_owner(self, obj: Organization):
        return OrganizationUserSerializer(obj.owner).data

    def get_members(self, obj: Organization):
        return OrganizationUserSerializer(obj.members, many=True).data
