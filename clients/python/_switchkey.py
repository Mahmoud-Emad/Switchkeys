from switchkey.core.base import SwitchKey

switch_key = SwitchKey(environment_id="test_key")
feature = 'debug'

if switch_key.features.has(feature):
    if switch_key.features.is_enabled(feature):
        feature_value = switch_key.features.get(feature)
    else:
        raise switch_key.FeatureNotEnabled(f"Feature '{feature}' is not enabled.")
