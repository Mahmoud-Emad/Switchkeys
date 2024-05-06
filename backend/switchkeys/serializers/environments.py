from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    SerializerMethodField,
    IntegerField,
    CharField,
)

from switchkeys.models.users import ProjectEnvironmentUser
from switchkeys.serializers.users import ProjectEnvironmentUserSerializer
from switchkeys.models.management import ProjectEnvironment
from switchkeys.models.environments import (
    EnvironmentFeature,
    SwitchKeysFeature,
    UserFeature,
)


class EnvironmentUserDeviceSerializer(Serializer):
    """
    Serializer for environment user device information.
    """

    version = CharField()
    device_type = CharField()


class ProjectEnvironmentSerializer(ModelSerializer):
    """
    Serializer for Organization project environment.
    """

    project = SerializerMethodField()
    project_id = IntegerField(write_only=True)  # Used to know which project
    users = SerializerMethodField()
    features = SerializerMethodField()

    class Meta:
        model = ProjectEnvironment
        fields = (
            "id",
            "name",
            "created",
            "modified",
            "environment_key",
            "features",
            "project",
            "project_id",
            "users",
        )

        read_only_fields = ("id", "created", "modified", "environment_key")

    def get_project(self, obj: ProjectEnvironment):
        """
        Retrieve serialized project data.
        """
        from switchkeys.serializers.projects import OrganizationProjectSerializer

        return OrganizationProjectSerializer(obj.project).data

    def get_users(self, obj: ProjectEnvironment):
        """
        Retrieve serialized user data associated with the environment.
        """
        return ProjectEnvironmentUserSerializer(obj.users, many=True).data

    def get_features(self, obj: ProjectEnvironment):
        """
        Retrieve serialized features associated with the environment.
        """
        features = EnvironmentFeature.objects.filter(environment=obj)
        serialized_features = []

        for feature in features:
            serialized_features.extend(
                SwitchKeysFeatureSerializer(feature.features.all(), many=True).data
            )

        return serialized_features


class SwitchKeysFeatureSerializer(ModelSerializer):
    """
    Serializer for environment features.
    """

    class Meta:
        fields = "__all__"
        model = SwitchKeysFeature


class AddEnvironmentUserSerializer(Serializer):
    """
    Serializer to add user to an environment.
    """

    device = EnvironmentUserDeviceSerializer()
    username = CharField()
    features = SerializerMethodField()

    class Meta:
        model = ProjectEnvironmentUser
        fields = (
            "username",
            "device",
            "features",
        )

    def get_features(self, user: ProjectEnvironmentUser):
        """
        Retrieve serialized features associated with the environment.
        """
        # If the user object is not an instance, retrieve it by username
        if not isinstance(user, ProjectEnvironmentUser):
            user = ProjectEnvironmentUser.objects.get(username=user.get("username"))

        # Fetch user features and their corresponding feature values
        user_features = UserFeature.objects.filter(user=user)
        user_features_data = {
            feature.feature.id: feature.feature_value for feature in user_features
        }

        # Fetch SwitchKeysFeature objects based on user features
        features = SwitchKeysFeature.objects.filter(id__in=user_features_data.keys())

        # Replace the feature value with the user feature value
        for feature in features:
            feature.value = user_features_data.get(feature.id)

        return SwitchKeysFeatureSerializer(features, many=True).data

class RemoveEnvironmentUserSerializer(Serializer):
    """
    Serializer to remove user from an environment.
    """

    username = CharField()



class EnvironmentFeatureSerialize(ModelSerializer):
    """
    Serializer for Organization project environment features.
    """

    name = CharField(write_only=True)
    value = CharField(write_only=True)
    features = SerializerMethodField()

    class Meta:
        model = EnvironmentFeature
        fields = [
            "id",
            "created",
            "modified",
            "features",
            "name",
            "value",
        ]

        read_only_fields = (
            "id",
            "created",
            "modified",
            "features",
        )

        write_only_fields = (
            "name",
            "value",
        )

    def get_features(self, obj: ProjectEnvironment):
        """
        Retrieve serialized features associated with the environment.
        """
        return SwitchKeysFeatureSerializer(obj.features.all(), many=True).data

class EnvironmentFeatureSerializer(Serializer):
    """
    Serializer for an environment feature.
    """

    name = CharField(write_only=True)
    value = CharField(write_only=True)

class UserFeatureSerializers(ModelSerializer):
    """
    Serializer to get user features.
    """
    name = SerializerMethodField()
    value = SerializerMethodField()

    class Meta:
        model = UserFeature
        fields = [
            "id",
            "name",
            "value",
            "created",
            "modified",
        ]

    def get_name(self, obj: UserFeature):
        return obj.feature.name

    def get_value(self, obj: UserFeature):
        return obj.feature_value