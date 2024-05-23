import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for organization-related operations.
Future<void> organizationsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchkeys = SwitchKeys();

  print('\n------------------------------------------------------------------');
  print('[+] Running the organizations example.');
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
      name: "SwitchKeys",
    );
    print("[+] Created organization name: ${organization.name}");

    // ------------------------------------------------------------------------
    // Creating a new project on the created organization
    // ------------------------------------------------------------------------
    // Create a new project named "FlayAway" on the created organization.
    var project = await organization.createProject(projectName: "FlayAway");
    print("[+] Created project name: ${project.name}");

    // ------------------------------------------------------------------------
    // List all organization projects
    // ------------------------------------------------------------------------
    // You can list all of the organization projects,
    // including the new created "FlayAway" project.
    var projects = await organization.getAllProjects();
    print("[+] Organization projects: $projects");

    // ------------------------------------------------------------------------
    // Adding members to an organization
    // ------------------------------------------------------------------------
    // You can easily add a new member to the created organization
    await organization.addMember(memberID: user.id);
    print("[+] Organization members: ${organization.members}");
    // Also, remove member.
    await organization.removeMember(memberID: user.id);
    print("[+] Organization members: ${organization.members}");

    // ------------------------------------------------------------------------
    // Updating the organization
    // ------------------------------------------------------------------------
    await organization.update(newName: "FlagsBoard", newMembers: []);
    print("[+] Updated organization name: ${organization.name}");

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
