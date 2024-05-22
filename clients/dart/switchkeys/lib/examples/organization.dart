import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for organization-related operations.
Future<void> organizationsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchkeys = SwitchKeys();

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  await switchkeys.auth
      .login(
        email: "testing@switchkeys.com",
        password: "0000",
      )
      .then(
        (user) => print("Logged in successfully: ${user.email}"),
      )
      .catchError(
        (e) => print("Error logging in: $e"),
      );
  // If you haven't created account yet, unlock the register method.
  /**
  await switchkeys.auth
    .register(
      firstName: "Testing",
      lastName: "Account",
      email: "testing@switchkeys.com",
      password: "0000",
      memberType: UserTypeEnum.administrator,
    )
    .then(
      (user) => print("User registered successfully: ${user.email}"),
    )
    .catchError(
      (e) => print("Error registering user: $e"),
    );
  */

  // --------------------------------------------------------------------------------------------------------------------
  // Creating a new organization
  // --------------------------------------------------------------------------------------------------------------------
  // Create a new organization named "SwitchKeys".
  var organization = await switchkeys.organizations.create(
    name: "Sonono2",
  );

  print(organization.name); // Print the organization object

  var project = await organization.createProject(projectName: "FlayAway");

  print(project.name); // Print the project object.
  print(project.organization?.name); // Print the project organization.

  // Adding a member into an organization.
  var member = await organization.addMember(memberID: 1);
  print(member);
}
