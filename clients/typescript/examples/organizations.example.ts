// Import the SwitchKeys class from the client library.
import SwitchKeys from "../src/core/base";
import { SwitchKeysUserType } from "../src/utils/types";

/**
 * `organizationExample` demonstrates the usage of organization services.
 * This example guides users and developers on how to interact with the
 * SwitchKeys organizations, including getting, creating, deleting an environment, and more.
 */
export async function organizationExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();
  const userEmail = "testing@switchkeys.com";

  // --------------------------------------------------------------------------------------------------------------------
  // Check if the user is already created
  // --------------------------------------------------------------------------------------------------------------------
  console.log(`[+] Check if user with email ${userEmail} is registered.`);
  const userCreated = await switchkeys.users.isUserCreated({
    email: userEmail,
  });

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  if (!userCreated) {
    // If you haven't created account yet, unlock the register method.
    await switchkeys.auth.register({
      email: userEmail,
      password: "0000",
      firstName: "Testing",
      lastName: "Account",
      memberType: SwitchKeysUserType.Administrator,
    });
    console.log("[+] Registered successfully.");
  } else {
    console.log(`[!] User with email ${userEmail} is already registered.`);
    const user = await switchkeys.auth.login({
      email: userEmail,
      password: "0000",
    });
    console.log("[+] Logged in successfully.");

    // --------------------------------------------------------------------------------------------------------------------
    // Creating a new organization
    // --------------------------------------------------------------------------------------------------------------------
    // Create a new organization named "SwitchKeys".
    const organization = await switchkeys.organizations.create({
      name: "SwitchKeys5",
    });

    console.log("[+] Created Organization:", organization);

    // --------------------------------------------------------------------------------------------------------------------
    // Adding members to an organization
    // --------------------------------------------------------------------------------------------------------------------
    // You can easily add a new member to the created organization
    await organization.addMember({
      memberId: user.id,
    });

    console.log("[+] Organization members:", organization.getMembers());

    // Also, remove member.
    await organization.removeMember({
      memberId: user.id,
    });

    console.log("[+] Organization members:", organization.getMembers());

    // --------------------------------------------------------------------------------------------------------------------
    // Creating a new project within the organization
    // --------------------------------------------------------------------------------------------------------------------
    // Now you can create a project within the created organization.
    const project = await organization.createProject({
      name: "StoryMith",
    });

    console.log("[+] Created Project:", project);

    // --------------------------------------------------------------------------------------------------------------------
    // Loading an environment from the created project
    // --------------------------------------------------------------------------------------------------------------------
    // Load any of the project's environments.
    // Each created project will have three different environments: 'development', 'staging', 'production'.
    const environmentKey = project.environments.staging.environmentKey;
    const environment = await switchkeys.environments.load(environmentKey);

    // Interact with the environment, e.g., list all users in the staging environment.
    const environmentUsers = environment.users;
    console.log("[+] Environment users: ", environmentUsers);

    // --------------------------------------------------------------------------------------------------------------------
    // Deleting the created organization
    // --------------------------------------------------------------------------------------------------------------------
    // This will also delete all associated projects and environments.
    await switchkeys.organizations.delete(organization.id);

    console.log(
      "[+] Organization and all its associated projects and environments have been deleted."
    );
    // --------------------------------------------------------------------------------------------------------------------
    // Demonstrate other authenticated operations here
    // --------------------------------------------------------------------------------------------------------------------
    // For example, you can now perform operations that require authentication, such as accessing user data,
    // loading environments, or managing projects and organizations.

    // --------------------------------------------------------------------------------------------------------------------
    // Logging out of SwitchKeys
    // --------------------------------------------------------------------------------------------------------------------
    // Finally, log out of SwitchKeys.
    switchkeys.auth.logout();
    console.log("[+] Logged out successfully.");
  }
}
