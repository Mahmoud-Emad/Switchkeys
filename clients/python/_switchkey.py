from switchkey.core.base import SwitchKey


switch_key = SwitchKey(environment_key="1931ca88-f3d8-4aac-8019-a45e78f38d19")
switch_key.connect()
print(switch_key.environment.users[1].features)
# environment.parsed_data().organization

# switch_key.__routes
# feature = 'debug'

# if switch_key.features.has(feature):
#     if switch_key.features.is_enabled(feature):
#         feature_value = switch_key.features.get(feature)
#     else:
#         raise switch_key.FeatureNotEnabled(f"Feature '{feature}' is not enabled.")

