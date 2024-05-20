import SwitchKeysAuth from "../api/models/auth";
import SwitchKeysOrganizations from "../api/models/organizations";
import SwitchKeysProject from "../api/models/organizations.projects";
import SwitchKeysEnvironment from "../api/models/projects.environments";

/**
 * Main class for managing interactions with the `SwitchKeys` system.
 * Provides access to `authentication`, `users`, and `organizations` functionalities.
 */
class SwitchKeys {
  /** Instance of `SwitchKeysAuth` for managing `authentication` operations. */
  auth: SwitchKeysAuth = new SwitchKeysAuth();
  /** Instance of `SwitchKeysOrganization` for managing `organization-related` operations. */
  organizations: SwitchKeysOrganizations = new SwitchKeysOrganizations();
  /** Instance of `SwitchKeysProject` for managing `project-related` operations. */
  projects: SwitchKeysProject = new SwitchKeysProject();
  /** Instance of `SwitchKeysEnvironment` for managing environment-related operations. */
  environments: SwitchKeysEnvironment = new SwitchKeysEnvironment();
}

export default SwitchKeys;
