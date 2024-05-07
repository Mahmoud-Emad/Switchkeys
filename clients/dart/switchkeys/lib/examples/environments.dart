import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for environment-related operations.
void environmentsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchKeys = SwitchKeys();

  // Load an environment using its key.
  var environment = await switchKeys.environments.load(
    environmentKey: 'a525176d-3344-4ce0-abd9-7e6b04eff0b8', // Production
    // environmentKey: 'a502139e-3e21-4c61-ae41-2b467d19ace4', // Development
  );

  // Add a user to the environment.
  final userDevice = SwitchKeyDevice(
    deviceType: SwitchKeyDeviceType.Android,
    version: "v1.1-0x54s",
  );

  final user = SwitchKeysEnvironmentsUser(
    username: "Mahmoud",
    device: userDevice,
  );

  final addedUser = await switchKeys.environments.users.addUser(
    user: user,
    environment: environment,
  );

  print(addedUser.device);

  // Add a feature to the user.
  var feature = SwitchKeyUserEnvironmentFeatureRequest(
    name: "Theme",
    value: "dark",
  );

  final userFeature = await switchKeys.environments.users.addFeature(
    username: user.username,
    feature: feature,
    environment: environment,
  );

  print(userFeature.name);

  // Get the value of a specific feature of a user.
  final getUserFeature = await switchKeys.environments.users.getFeature(
    featureName: "debug",
    username: "Adham",
    environment: environment,
  );

  print(getUserFeature.name);

  // Get all of user features.
  final getAllUserFeature = await switchKeys.environments.users.getAllFeatures(
    featureName: "debug",
    username: "Adham",
    environment: environment,
  );

  print(getAllUserFeature);

  // print("Name: ${feature.name}");
  // print("Value: ${feature.value}");
}
