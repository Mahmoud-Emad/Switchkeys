from switchkeys.models.environments import UserFeature
from switchkeys.models.users import ProjectEnvironmentUser, User
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class OrganizationUserSerializer(ModelSerializer):
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
        read_only_feilds = [
            "joining_at",
            "background_color",
            "full_name",
            "is_active",
        ]


class ProjectEnvironmentUserSerializer(ModelSerializer):
    """
    This class will be used to get all project users.
    """

    device = SerializerMethodField()
    features = SerializerMethodField()

    class Meta:
        model = ProjectEnvironmentUser
        fields = [
            "id",
            "username",
            "device",
            "features",
        ]
        read_only_feilds = [
            "features",
        ]

    def get_device(self, obj: ProjectEnvironmentUser):
        from switchkeys.serializers.environments import EnvironmentUserDeviceSerializer

        return EnvironmentUserDeviceSerializer(obj.device).data

    def get_features(self, obj: ProjectEnvironmentUser):
        from switchkeys.serializers.environments import SwitchKeysFeatureSerializer
        features = UserFeature.objects.filter(user=obj)
        serialized_features = []

        for feature in features:
            feature.feature.value = feature.feature_value
            serialized_features.append(
                SwitchKeysFeatureSerializer(feature.feature).data
            )
        
        return serialized_features
