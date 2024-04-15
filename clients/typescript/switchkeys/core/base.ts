import SwitchKeysAuth from "../api/models/auth.model";
import SwitchKeysOrganization from "../api/models/organization.model";

/**
 * Main class for managing interactions with the SwitchKeys system.
 * Provides access to authentication and organization functionalities.
 */
class SwitchKeys {
  /** Instance of SwitchKeysAuth for managing authentication operations. */
  auth: SwitchKeysAuth = new SwitchKeysAuth();

  /** Instance of SwitchKeysOrganization for managing organization-related operations. */
  organization: SwitchKeysOrganization = new SwitchKeysOrganization();
}

export default SwitchKeys;
