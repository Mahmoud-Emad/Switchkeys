import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

// This example will create all the needed objects to be ready to work in an environment.
void switchKeysFullExample() async {
  print("Running the SwitchKeys full-example.");
  // Import and take an instance from the `SwitchKeys` module
  SwitchKeys switchKeys = SwitchKeys();

  // Register new user as an `administrator`
  print("Registering a new admin user.");
  await switchKeys.auth.register(
    firstName: "Ahmed",
    lastName: "Anwar",
    email: "ahmed@gmail.com",
    password: "0000",
    memberType: UserTypeEnum.administrator,
  );

  // Register new user as a `user` to use this user later when creating an organization.
  print("Registering a new member user.");
  SwitchKeysAuthResponse member1 = await switchKeys.auth.register(
    firstName: "Khaled",
    lastName: "Mohamed",
    email: "khaled@gmail.com",
    password: "0000",
    memberType: UserTypeEnum.user,
  );

  // Now we need to login with the created user to save the user tokens
  print("Logging the created admin user.");
  await switchKeys.auth.login(email: "ahmed@gmail.com", password: "0000");

  // Create an organization
  print("Creating new organization.");
  SwitchKeysOrganizationResponse organization =
      await switchKeys.organizations.create(
    name: "Threefold",
    members: [
      member1.id,
    ],
  );

  // Create new project on the created organization.
  print("Creating new project on ${organization.name} organization.");
  SwitchKeysProjectResponse project = await switchKeys.projects.create(
    name: "TFGrid TS",
    organizationID: organization.id,
  );

  // Now we need to create new environment
  print("Creating new environment on ${project.name} project.");
  SwitchKeysEnvironmentResponse environment =
      await switchKeys.environments.create(
    name: "development",
    projectID: project.id,
  );

  // Now we need to save the `environmentKey` to use it later
  print("Environment key: ${environment.environmentKey}");
}

// Load an environment using its `environmentKey` and interact with it.
void switchKeysManagement() async {
  // The created environment data:
  // environment = {
  //  name: "development",
  //  environmentKey: "16e78bfa-fa85-4313-8bc2-1bd09db34642"
  // }

  print("Running the SwitchKeys full-example.");
  // Import and take an instance from the `SwitchKeys` module
  SwitchKeys switchKeys = SwitchKeys();

  await switchKeys.environments.load(
    environmentKey: "16e78bfa-fa85-4313-8bc2-1bd09db34642",
  );
}
