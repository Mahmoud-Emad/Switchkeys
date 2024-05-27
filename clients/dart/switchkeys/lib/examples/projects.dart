// import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for project-related operations.
Future<void> projectsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchkeys = SwitchKeys();

  print('\n------------------------------------------------------------------');
  print('### Running the projects example ###');
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
      name: "SwitchKeys3",
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
