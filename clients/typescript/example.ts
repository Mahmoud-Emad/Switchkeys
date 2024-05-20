import { authExample } from "./examples/auth.example";
import { organizationExample } from "./examples/organizations.example";
import { projectExample } from "./examples/projects.example";
import { environmentExample } from "./examples/environments.example";

/**
 * Main function demonstrating the usage of the SwitchKeys client.
 */
async function main() {
  await authExample();
  await organizationExample();
  await projectExample();
  await environmentExample();
}
main();
