// import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for project-related operations.
Future<void> environmentsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchkeys = SwitchKeys();

  print('\n------------------------------------------------------------------');
  print('### Running the environments example ###');
  print('------------------------------------------------------------------\n');

  // --------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  try {
    // If you haven't created account yet, unlock the register method.
    var user = await switchkeys.auth.register(
      firstName: "Testing",
      lastName: "Account",
      email: "testing@switchkeys.com",
      password: "0000",
      memberType: UserTypeEnum.administrator,
    );
    print("[+] Registered successfully: ${user.email}");
  } catch (e) {
    var user = await switchkeys.auth.login(
      email: "testing@switchkeys.com",
      password: "0000",
    );
    print("[+] Logged in successfully: ${user.email}");

    // ------------------------------------------------------------------------
    // Creating a new organization
    // ------------------------------------------------------------------------
    // Create a new organization named "SwitchKeys".
    var organization = await switchkeys.organizations.create(
      name: "SwitchKeys10",
    );
    print("[+] Created organization name: ${organization.name}");

    // ------------------------------------------------------------------------
    // Creating a new project on the created organization
    // ------------------------------------------------------------------------
    // Create a new project named "FlayAway" on the created organization.
    var project = await switchkeys.projects.create(
      name: "FlayAway",
      organizationID: organization.id,
    );
    print("[+] Created project name: ${project.name}");

    // ------------------------------------------------------------------------
    // Updating the created project
    // ------------------------------------------------------------------------
    await project.update(
      name: "StoryMith",
      organizationID: organization.id,
    );
    print("[+] Updated project name: ${project.name}");

    // ------------------------------------------------------------------------
    // Load project environment.
    // ------------------------------------------------------------------------
    // Load the environment using the project's development environment key.
    var environmentKey = project.environments.development.environmentKey;
    var environment = await switchkeys.environments.load(
      environmentKey: environmentKey,
    );

    print("[+] Loaded environment key: ${environment.environmentKey}");

    // ------------------------------------------------------------------------
    // Add/remove user to/from the environment.
    // ------------------------------------------------------------------------
    // First, you need to send the `SwitchKeysEnvironmentsUser` user.
    var environmentUser = SwitchKeysEnvironmentsUser(
      username: "Mahmoud",
      device: SwitchKeyUserDevice(
        deviceType: SwitchKeyUserDeviceType.android,
        version: "v142.54.5158s.54w",
      ),
    );

    var pName = environment.project.name;
    var envName = environment.name;

    var addedUser = await environment.addUser(user: environmentUser);
    var username = addedUser.username;

    print(
      "[+] User '$username' has been added to the '$pName/$envName' environment",
    );

    // ------------------------------------------------------------------------
    // Add/remove feature to/from the environment.
    // ------------------------------------------------------------------------
    // Log the environment features
    print("[+] Environment features: ${environment.features.toList()}");

    var feature = await environment.addFeature(
      feature: SwitchKeysFeatureData(name: "theme", value: "dark"),
    );
    print(
      "[+] Feature '${feature.name}' has been added to the '${environment.name}' environment, Value => '${feature.value}'.",
    );

    print("[+] Environment features: ${environment.features.toList()}");

    feature = await environment.updateFeature(
      featureName: "theme",
      feature: SwitchKeysFeatureData(name: "theme", value: "light"),
    );
    print(
      "[+] Feature '${feature.name}' has been updated with new value: '${feature.value}'.",
    );

    print("[+] Environment features: ${environment.features.toList()}");

    await environment.deleteFeature(
      featureName: "theme",
    );

    print(
      "[-] Feature '${feature.name}' deleted!",
    );

    print("[+] Environment features: ${environment.features.toList()}");

    // ------------------------------------------------------------------------
    // Get/Select environment user.
    // ------------------------------------------------------------------------
    var envUser = environment.users.getUser(username: username);
    print("[+] User ${envUser.username} selected.");
    print("[+] User ${envUser.username} features are ${envUser.features}.");

    // ------------------------------------------------------------------------
    // Get, Check, and set a feature for an environment user.
    // ------------------------------------------------------------------------
    const featureName = "design";

    if (envUser.hasFeature(featureName: featureName)) {
      print("[+] ${envUser.username} has the '$featureName' feature.");

      var envUserFeat = envUser.getFeature(
        featureName: featureName,
      );

      print(
        "[+] User ${envUser.username} $featureName feature value is: ${envUserFeat.value}.",
      );
    } else {
      SwitchKeysFeatureData featrue = SwitchKeysFeatureData(
        name: featureName,
        value: "v1.2.5",
      );
      var userFeat = await envUser.setFeature(feature: featrue);
      print(
        "[+] User ${envUser.username} ${userFeat.name} feature value is: ${userFeat.value}.",
      );
    }

    // ------------------------------------------------------------------------
    // Delete the created organization
    // ------------------------------------------------------------------------
    // You can also delete a different organization by providing its ID.
    await switchkeys.organizations.delete(organizationID: organization.id);
    print("[+] Deleted organization: ${organization.name}");

    // ------------------------------------------------------------------------
    // Get the deleted organization: Error!
    // ------------------------------------------------------------------------
    try {
      await switchkeys.organizations.getById(organizationID: organization.id);
      // await switchkeys.organizations.getByName(
      //   organizationName: organization.name,
      // );
    } catch (e) {
      print("[-] $e");
    }
  } finally {
    // ------------------------------------------------------------------------
    // Logging out of SwitchKeys
    // ------------------------------------------------------------------------
    // Finally, log out of SwitchKeys.
    await switchkeys.auth.logout();
    print("[+] Logged out successfully");
  }
}
