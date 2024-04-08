import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// Main function for project-related operations.
void projectsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchKeys = SwitchKeys();

  // Login the user. This step is required if the saved token is expired.
  await switchKeys.auth.login(email: "", password: "");

  try {
    // Get the organization where the project will be created
    final SwitchKeysOrganizationResponse organization =
        await switchKeys.organizations.getByName(
      organizationName: 'Cloud for students',
    );

    print("Organization name: ${organization.name}");
    print("Organization ID: ${organization.id}");

    // Create a new project under the retrieved organization
    // project = await switchKeys.projects
    //     .create(name: "TFGrid", organizationID: organization.id);
    // print("Project name: ${project.name}");

    // Get an existing project by its ID
    final SwitchKeysProjectResponse project = await switchKeys.projects.getByID(
      projectID: 2,
    );

    print("Project name: ${project.name}");

    // Update the existing project with new data
    // The `organizationID` can be changed to another organization or remain the same.
    final updatedProject = await switchKeys.projects.update(
      name: 'TFGrid Hub',
      organizationID: organization.id,
      projectID: project.id,
    );

    print("Updated project name: ${updatedProject.name}");

    // Delete the project
    final isDeleted = await switchKeys.projects.delete(
      projectID: updatedProject.id,
    );

    print("Is the project deleted: $isDeleted");
  } catch (e) {
    // Handle any errors that may occur during project operations.
    print("Error occurred: $e");
  }
}
