// Import the SwitchKeys class from the client library.
import SwitchKeys from "../switchkeys/core/base";

/**
 * `projectExample` demonstrates the usage of organization services.
 * This example guides users and developers on how to interact with the
 * SwitchKeys projects, including getting, creating, deleting a project, and more.
 */
export async function projectExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();

  // First, log in to SwitchKeys with valid credentials.
  await switchkeys.auth.login({
    email: "admin@gmail.com",
    password: "0000",
  });

  // --------------------------------------------------------------------------------------------------------------------
  // Creating a new project
  // --------------------------------------------------------------------------------------------------------------------
  // Second, create a new organization. 
  // PS: If you have a valid project ID, you can get it directly and skip this step.
  const organization = await switchkeys.organizations.create({
    name: "SwitchKeys",
  });

  // Now you can create a project in the created organization.
  const project1 = await organization.createProject({
    name: "StoryMith",
  });

  console.log("Created Project:", project1);

  // --------------------------------------------------------------------------------------------------------------------
  // Getting a created project
  // --------------------------------------------------------------------------------------------------------------------
  // Retrieve an existing project by its ID.
  const project2 = await organization.projects.get(project1.id);

  console.log("Retrieved Project:", project2);

  // Load the environment using the project's development environment key.
  const environmentKey = project2.environments.development.environmentKey;
  const environment = await switchkeys.environments.load(environmentKey);

  // Now you can interact with the environment, e.g., list all users.
  const environmentUsers = environment.users;
  console.log({ environmentUsers });

  // --------------------------------------------------------------------------------------------------------------------
  // Deleting the created organization
  // --------------------------------------------------------------------------------------------------------------------
  // This will also delete all associated projects and environments.
  await switchkeys.organizations.delete(organization.id);

  console.log("Organization and all its associated projects and environments have been deleted.");
}
