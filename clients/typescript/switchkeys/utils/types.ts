// Use this enum to send/check the user type.
enum SwitchKeysUserType {
  user = "user",
  administrator = "administrator",
}

interface SwitchKeysAuthTokens {
  accessToken?: string;
  refreshToken?: string;
}

export {
  SwitchKeysUserType,
  SwitchKeysAuthTokens
}