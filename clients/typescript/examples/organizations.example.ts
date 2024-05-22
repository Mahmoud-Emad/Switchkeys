// Import the SwitchKeys class from the client library.
import SwitchKeys from "../src/core/base";

/**
 * `organizationExample` demonstrates the usage of organization services.
 * This example guides users and developers on how to interact with the
 * SwitchKeys organizations, including getting, creating, deleting an environment, and more.
 */
export async function organizationExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();

  // First, log in to SwitchKeys with valid credentials.
  const user = await switchkeys.auth.login({
    email: "testing@switchkeys.com",
    password: "0000",
  });

  // --------------------------------------------------------------------------------------------------------------------
  // Creating a new organization
  // --------------------------------------------------------------------------------------------------------------------
  // Create a new organization named "SwitchKeys".
  const organization = await switchkeys.organizations.create({
    name: "SwitchKeys",
  });

  console.log("Created Organization:", organization);

  // --------------------------------------------------------------------------------------------------------------------
  // Adding members to an organization
  // --------------------------------------------------------------------------------------------------------------------
  // You can easily add a new member to the created organization
  await organization.addMember({
    memberId: user.id
  })

  console.log("Organization members:", organization.getMembers());

  // Also, remove member.
  await organization.removeMember({
    memberId: user.id
  })

  console.log("Organization members:", organization.getMembers());

  // --------------------------------------------------------------------------------------------------------------------
  // Creating a new project within the organization
  // --------------------------------------------------------------------------------------------------------------------
  // Now you can create a project within the created organization.
  const project = await organization.createProject({
    name: "StoryMith",
  });

  console.log("Created Project:", project);

  // --------------------------------------------------------------------------------------------------------------------
  // Loading an environment from the created project
  // --------------------------------------------------------------------------------------------------------------------
  // Load any of the project's environments.
  // Each created project will have three different environments: 'development', 'staging', 'production'.
  const environmentKey = project.environments.staging.environmentKey;
  const environment = await switchkeys.environments.load(environmentKey);

  // Interact with the environment, e.g., list all users in the staging environment.
  const environmentUsers = environment.users;
  console.log({ environmentUsers });

  // --------------------------------------------------------------------------------------------------------------------
  // Deleting the created organization
  // --------------------------------------------------------------------------------------------------------------------
  // This will also delete all associated projects and environments.
  await switchkeys.organizations.delete(organization.id);

  console.log("Organization and all its associated projects and environments have been deleted.");
}
