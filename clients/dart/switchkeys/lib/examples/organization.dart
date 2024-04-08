// This Dart script demonstrates how to use the SwitchKeys organizations API.
// It first creates an organization with the provided organization name and members,
// handling any errors that may occur during the process.
// Then, it gets an existing organization with the specified details,
// Again, error handling is included to manage any errors that may occur during the creation/deletion/updating/getting processes.

import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for organization-related operations.
void organizationsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchKeys = SwitchKeys();

  // Login the user. This step is required if the saved token is expired.
  await switchKeys.auth.login(email: "", password: "");

  // Variable to hold organization information
  SwitchKeysOrganizationResponse organization;

  try {
    // Create a new organization. Ensure the organization name is unique.
    // organization =
    //     await switchKeys.organizations.create(name: "Cloud for students", members: []);
    // print("Organization ID: ${organization.id}");

    // Get an organization based on its name since the name is unique for the user.
    organization = await switchKeys.organizations.getByName(
      organizationName: 'Cloud for students',
    );

    print("Organization name: ${organization.name}");

    // We can add members to an organization by passing the memberID.
    organization = await switchKeys.organizations.addMember(
      organizationID: organization.id,
      memberID: 2,
    );

    // As we used the `addMember` method to add a member on the organization, also we can remove the added member or any member from the organization.
    organization = await switchKeys.organizations.removeMember(
      organizationID: organization.id,
      memberID: 2,
    );

    print("Members ${organization.members[0].fullName}");

    // Update an existing organization by specifying its ID.
    // organization = await switchKeys.organizations.update(
    //   organizationID: organization.id,
    //   newName: "EGClouds",
    //   newMembers: [],
    // );

    // print("Organization name: ${organization.name}");

    // Delete the organization based on its ID, returns `true` if the organization is deleted.
    // final isDeleted = await switchKeys.organizations.delete(
    //   organizationID: organization.id,
    // );

    // print("Is the organization deleted: $isDeleted");
  } catch (e) {
    // Handle any errors that may occur during organization operations.
    print(e);
  }
}
