from switchkey.models.users import User
from rest_framework.serializers import ModelSerializer

class GeneralUserSerializer(ModelSerializer):
    """
    This class will be used to get all info about a user
    """

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "joining_at",
            "background_color",
            "is_active",
        ]

