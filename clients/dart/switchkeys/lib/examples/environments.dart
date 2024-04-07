import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for environment-related operations.
void environmentsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchKeys = SwitchKeys();

  // Load an environment using its key.
  var environment = await switchKeys.environments.load(
    environmentKey: '0246204d-c567-4089-add2-a1155657ecac', // Production
    // environmentKey: 'a502139e-3e21-4c61-ae41-2b467d19ace4', // Development
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

  // Get the value of a specific feature of a user.
  feature = await switchKeys.environments.users.getFeature(
    featureName: "debug",
    username: "Adham",
    environment: environment,
  );

  print("Name: ${feature.name}");
  print("Value: ${feature.value}");
}
