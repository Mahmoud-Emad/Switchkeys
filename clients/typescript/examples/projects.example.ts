// Import the SwitchKeys class from the client library.
// import SwitchKeys from "switchkeys-ts-client";
import SwitchKeys from "../switchkeys/core/base";

/**
 * Main function demonstrating the usage of the SwitchKeys client.
 */
export async function projectExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();
  // Uncomment and replace placeholders with actual data to demonstrate project-related operations.
  // Create a project

  // const project = await switchkeys.projects.create({
  //   name: "SwitchKeys 2",
  //   organizationId: organization.id
  // })
  
  // console.log("Project name: ", project.name)
  // console.log("Environment key: ", project.environments.development.environmentKey)

  // Get an exact project by it's id
  
  // const project = await switchkeys.projects.getById(11)
  // console.log("Project name: ", project.environments.production.environmentKey)

  // Update an exact project by it's id
  // const project = await switchkeys.projects.getById(11)
  // console.log("Project name: ", project.name)
  // console.log("Project ID: ", project.id)
  
  // const updatedProject = await switchkeys.projects.update(project.id, {
  //   name: "SwitchKeys hub",
  //   organizationId: organization.id
  // })

  // console.log("Project name: ", updatedProject.name)

  // List all organization projects
  let organization = await switchkeys.organizations.getById(6);
  console.log(`Organization name: ${organization.name}`);

  const projects = await switchkeys.projects.all(organization.id)
  console.log(projects[0].name)
  // Delete an exact project by it's id
  // console.log(await switchkeys.projects.delete(12))
}
