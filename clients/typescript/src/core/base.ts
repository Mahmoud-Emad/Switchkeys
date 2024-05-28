import SwitchKeysAuth from "../api/models/auth";
import { SwitchKeysOrganizations } from "../api/models/organizations";
import { SwitchKeysProjects } from "../api/models/organizations.projects";
import { SwitchKeysEnvironment } from "../api/models/projects.environments";
import SwitchKeysUsers from "../api/models/users";

/**
 * Main class for managing interactions with the `SwitchKeys` system.
 * Provides access to `authentication`, `users`, and `organizations` functionalities.
 */
class SwitchKeys {
  /** Instance of `SwitchKeysAuth` for managing `authentication` operations. */
  auth: SwitchKeysAuth = new SwitchKeysAuth();
  /** Instance of `SwitchKeysUsers` for managing `users` operations. */
  users: SwitchKeysUsers = new SwitchKeysUsers();
  /** Instance of `SwitchKeysOrganization` for managing `organization-related` operations. */
  organizations: SwitchKeysOrganizations = new SwitchKeysOrganizations();
  /** Instance of `SwitchKeysProjects` for managing `projects-related` operations. */
  projects: SwitchKeysProjects = new SwitchKeysProjects();
  /** Instance of `SwitchKeysEnvironment` for managing environment-related operations. */
  environments: SwitchKeysEnvironment = new SwitchKeysEnvironment();
}

export default SwitchKeys;
