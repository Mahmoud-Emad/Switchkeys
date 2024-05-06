from django.db import models

from switchkeys.models.users import ProjectEnvironmentUser
from switchkeys.models.abstracts import TimeStampedModel
from switchkeys.models.management import ProjectEnvironment
from django.utils.translation import gettext_lazy as _

class SwitchKeysFeature(TimeStampedModel):
    """
    Model representing a feature in the SwitchKeys system.

    Features can be associated with both users and environments.
    They allow for toggling various functionalities within the system.

    ### Attributes:
        - name (`str`): The name of the feature.
        - value (`str`): The current value of the feature.
        - initial_value (`str`): The initial value of the feature.
        - is_default (`str`): if the feature is default feature.
    """
    name = models.CharField(_("Name"), max_length=50)
    value = models.TextField(_("Value"), max_length=5000)
    initial_value = models.TextField(_("Initial Value"), max_length=5000)
    is_default = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("SwitchKeys Feature")
        verbose_name_plural = _("SwitchKeys Features")

    def __str__(self) -> str:
        """
        - Returns a string representation of the environment feature.

        - Format: `{self.name}`
        """
        return f"{self.name}"
class EnvironmentFeature(TimeStampedModel):
    """
    Model representing features associated with a project environment in the SwitchKeys system.

    Each environment can have multiple features with their respective values.

    ### Attributes:
        - environment (`ProjectEnvironment`): The project environment associated with the features.
        - features (`ManyToManyField`): The features associated with the environment.
    """

    environment = models.OneToOneField(
        ProjectEnvironment,
        verbose_name=_("Environment"),
        related_name="feature_environment",
        on_delete=models.CASCADE,
        null=True
    )

    features = models.ManyToManyField(
        SwitchKeysFeature,
        verbose_name=_("Features"),
        related_name="environment_default_features",
    )

    def __str__(self) -> str:
        """
        - Returns a string representation of the environment feature.

        - Format: `{self.environment.name}` | `{self.environment.project.name}`
        """
        return f"{self.environment.name} | {self.environment.project.name}"

    class Meta:
        verbose_name = _("Environment Feature")
        verbose_name_plural = _("Environment Features")

class UserFeature(TimeStampedModel):
    """
    Model representing features associated with a user in a project environment.

    Each user can have multiple features with their respective values.

    ### Attributes:
        - user (ProjectEnvironmentUser): The user associated with the features.
        - feature (SwitchKeysFeature): The feature associated with the user.
        - feature_value (TextField): The value of the feature associated with the user.
    """

    user = models.ForeignKey(
        ProjectEnvironmentUser,
        verbose_name=_("User"),
        related_name="user_feature",
        on_delete=models.CASCADE,
    )

    feature = models.ForeignKey(
        SwitchKeysFeature,
        verbose_name=_("Feature"),
        related_name="user_feature",
        on_delete=models.CASCADE,
    )
    
    feature_value = models.TextField(
        _("Value"),
        max_length=5000,
        help_text=_("The value of the feature associated with the user."),
    )

    def __str__(self) -> str:
        """
        - Returns a string representation of the user feature.

        - Format: `{username}` | `{feature_name}` | `{feature_value}`
        """
        return f"{self.user.username} | {self.feature.name} | {self.feature_value}"

    class Meta:
        verbose_name = _("User Feature")
        verbose_name_plural = _("User Features")
        unique_together = ("user", "feature")