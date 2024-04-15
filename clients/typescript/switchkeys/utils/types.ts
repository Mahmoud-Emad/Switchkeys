/**
 * Enum representing different user types in the SwitchKeys system.
 */
enum SwitchKeysUserType {
  /**
   * Regular user type.
   */
  User = "user",

  /**
   * Administrator user type.
   */
  Administrator = "administrator",
}

/**
 * Interface representing authentication tokens used in the SwitchKeys system.
 */
interface SwitchKeysAuthTokens {
  /**
   * Access token for authentication.
   */
  accessToken?: string;

  /**
   * Refresh token for authentication.
   */
  refreshToken?: string;
}

export { SwitchKeysUserType, SwitchKeysAuthTokens };
