// import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for organization-related operations.
Future<void> organizationsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchkeys = SwitchKeys();

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  var user = await switchkeys.auth.login(
    email: "testing@switchkeys.com",
    password: "0000",
  );
  print("Logged in successfully: ${user.email}");

  // If you haven't created account yet, unlock the register method.
  /**
  var user = await switchkeys.auth.register(
    firstName: "Testing",
    lastName: "Account",
    email: "testing@switchkeys.com",
    password: "0000",
    memberType: UserTypeEnum.administrator,
  );
  print("Registered successfully: ${user.email}");
  */

  // --------------------------------------------------------------------------------------------------------------------
  // Creating a new organization
  // --------------------------------------------------------------------------------------------------------------------
  // Create a new organization named "SwitchKeys".
  // var organization = await switchkeys.organizations.create(
  //   name: "Sonono2",
  // );

  // print(organization.name); // Print the organization object

  // var project = await organization.createProject(projectName: "FlayAway");

  // print(project.name); // Print the project object.
  // print(project.organization?.name); // Print the project organization.

  // // Adding a member into an organization.
  // var member = await organization.addMember(memberID: user.id);
  // print(member);
}
