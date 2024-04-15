import { ISwitchKeysAuthTokens } from "../../utils/types";

/**
 * Interface for SwitchKeys authentication register response.
 */
interface ISwitchKeysUserAuthResponse {
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  joiningAt: string;
  accessToken: string;
  refreshToken: string;
}

/**
 * Interface for SwitchKeys user info response.
 */
interface ISwitchKeysUserInfoResponse {
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  joiningAt: string;
  isActive?: boolean;
}

/**
 * Represents the response containing authentication tokens.
 */
class SwitchKeysTokensResponse implements ISwitchKeysAuthTokens {
  accessToken: string | undefined;
  refreshToken: string | undefined;

  constructor(accessToken?: string, refreshToken?: string) {
    this.accessToken = accessToken;
    this.refreshToken = refreshToken;
  }
}



export {
  SwitchKeysTokensResponse,
  ISwitchKeysUserAuthResponse,
  ISwitchKeysUserInfoResponse,
};
