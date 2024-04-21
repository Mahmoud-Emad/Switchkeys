import SwitchKeysAuth from "../api/models/auth";
import SwitchKeysOrganizations from "../api/models/organizations";
import SwitchKeysOrganizationMember from "../api/models/organizations.members";

/**
 * Main class for managing interactions with the `SwitchKeys` system.

 * Provides access to `authentication`, `users`, and `organizations` functionalities.
 */
class SwitchKeys {
  /** Instance of `SwitchKeysAuth` for managing `authentication` operations. */
  auth: SwitchKeysAuth = new SwitchKeysAuth();

  /** Instance of `SwitchKeysOrganization` for managing `organization-related` operations. */
  organizations: SwitchKeysOrganizations = new SwitchKeysOrganizations();
}

export default SwitchKeys;
