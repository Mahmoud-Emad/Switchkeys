from typing import ClassVar
from switchkey.core.exceptions import FeatureNotEnabled as FeatureNotEnabledError

class ModelBase(type): ...


class SwitchKeyFeatures():
    def has(self, feature: str):
        return True
  
    def get(self, feature: str):
        pass
  
    def create(self, feature: str, value: str):
        pass

    def is_enabled(self, feature: str) -> bool:
        return False

class SwitchKey(metaclass=ModelBase):
    def __init__(self, environment_id: str) -> None:
        self.FeatureNotEnabled = FeatureNotEnabledError
        self.environment_id = environment_id
        self.features = SwitchKeyFeatures()