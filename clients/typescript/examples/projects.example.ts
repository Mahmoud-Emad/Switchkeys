// Import the SwitchKeys class from the client library.
import SwitchKeys from "../src/core/base";
import { SwitchKeysUserType } from "../src/utils/types";

/**
 * `projectExample` demonstrates the usage of organization services.
 * This example guides users and developers on how to interact with the
 * SwitchKeys projects, including getting, creating, deleting a project, and more.
 */
export async function projectExample() {
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
    await switchkeys.auth.login({
      email: userEmail,
      password: "0000",
    });
    console.log("[+] Logged in successfully.");

    // --------------------------------------------------------------------------------------------------------------------
    // Creating a new organization
    // --------------------------------------------------------------------------------------------------------------------
    // Second, create a new organization.
    // PS: If you have a valid project ID, you can get it directly and skip this step.
    const organization = await switchkeys.organizations.create({
      name: "SwitchKeys4",
    });

    // Now you can create a project in the created organization.
    const project1 = await organization.createProject({
      name: "StoryMith",
    });

    console.log("[+] Created Project:", project1);

    // --------------------------------------------------------------------------------------------------------------------
    // Getting a created project
    // --------------------------------------------------------------------------------------------------------------------
    // Retrieve an existing project by its ID.
    const project2 = await organization.projects.get(project1.id);

    console.log("[+] Retrieved Project:", project2);

    // Load the environment using the project's development environment key.
    const environmentKey = project2.environments.development.environmentKey;
    const environment = await switchkeys.environments.load(environmentKey);

    // Now you can interact with the environment, e.g., list all users.
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
