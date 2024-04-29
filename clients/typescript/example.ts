import { authExample } from "./examples/auth.example";
import { environmenthExample } from "./examples/environments.example";
import { organizationExample } from "./examples/organizations.example";
import { projectExample } from "./examples/projects.example";

/**
 * Main function demonstrating the usage of the SwitchKeys client.
 */
async function main() {
  // await organizationExample();
  // await projectExample();
  // await authExample();
  await environmenthExample();
}

main();
