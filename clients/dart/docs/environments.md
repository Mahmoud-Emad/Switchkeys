# SwitchKeys Environments Operations

This document provides an overview and usage examples of operations related to SwitchKeys environments.

## Overview

The script demonstrates various operations that can be performed on SwitchKeys environments using the SwitchKeys SDK. These operations include loading an environment, adding users to an environment, adding features to a user in an environment, bulk creating features for a user, and getting the value of a specific feature for a user in an environment.

## Usage

Ensure you have the SwitchKeys SDK installed in your Dart project. You can install it using:

```bash
dart pub add switchkeys
```

### Script Execution

To execute the script, you can call the `environmentsMain()` function:

```dart
environmentsMain();
```

### Operations

1. **Load an Environment**: 
   - Loads an environment using its key.

2. **Add a User to the Environment**:
   - Adds a user to the environment.

3. **Add a Feature to a User**:
   - Adds a feature to a specific user in the environment.

4. **Bulk Create Features for a User**:
   - Bulk creates features for a user in the environment.

5. **Get the Value of a Feature for a User**:
   - Retrieves the value of a specific feature for a user in the environment.

## Usage Examples

```dart
// Load an environment using its key.
var environment = await switchKeys.environments.load(
  environmentKey: '0246204d-c567-4089-add2-a1155657ecac', // Production
);

// Add a user to the environment.
final userDevice = SwitchKeyDevice(
  deviceType: SwitchKeyDeviceType.Android,
  version: "v1.1-0x54s",
);
final user = SwitchKeysEnvironmentsUser(
  username: "Adham",
  device: userDevice,
);
await switchKeys.environments.users.addUser(
  user: user,
  environment: environment,
);

// Add a feature to the user.
var feature = SwitchKeyUserEnvironmentFeatures(
  name: "Theme",
  value: "dark",
);
await switchKeys.environments.users.addFeature(
  username: "Mahmoud",
  feature: feature,
  environment: environment,
);

// Bulk create features for a user.
List<SwitchKeyUserEnvironmentFeatures> features = [];
features.add(
  SwitchKeyUserEnvironmentFeatures(
    name: "version",
    value: "v0.2",
  ),
);
features.add(
  SwitchKeyUserEnvironmentFeatures(
    name: "debug",
    value: "true",
  ),
);
await switchKeys.environments.users.bulkCreateFeature(
  features: features,
  environment: environment,
  username: 'Adham',
);

// Get the value of a specific feature for a user.
feature = await switchKeys.environments.users.getFeature(
  featureName: "debug",
  username: "Adham",
  environment: environment,
);

print("Name: ${feature.name}");
print("Value: ${feature.value}");
```

## Dependencies

- `switchkeys`: The SwitchKeys SDK for Dart.
