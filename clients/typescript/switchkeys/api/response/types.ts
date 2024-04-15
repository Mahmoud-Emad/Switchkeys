import { SwitchKeysAuthTokens } from "../../utils/types";

/**
 * Interface for SwitchKeys authentication register response.
 */
interface ISwitchKeysAuthRegisterResponse {
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  joiningAt: string;
  accessToken: string;
  refreshToken: string;
}

/**
 * Represents the response containing authentication tokens.
 */
class SwitchKeysTokensResponse implements SwitchKeysAuthTokens {
  accessToken: string | undefined;
  refreshToken: string | undefined;

  constructor(accessToken?: string, refreshToken?: string) {
    this.accessToken = accessToken;
    this.refreshToken = refreshToken;
  }
}

/**
 * Represents the response for registering a user with SwitchKeys authentication.
 */
class SwitchKeysAuthRegisterResponse
  implements ISwitchKeysAuthRegisterResponse
{
  id: number = 0;
  firstName: string = "";
  lastName: string = "";
  email: string = "";
  joiningAt: string = "";
  accessToken: string = "";
  refreshToken: string = "";

  /**
   * Parses authentication data and sets the properties of the response object.
   * @param authData The authentication data to parse.
   * @returns The parsed authentication response object.
   */
  parseAuth(authData: any): ISwitchKeysAuthRegisterResponse {
    this.id = authData["id"];
    this.firstName = authData["first_name"];
    this.lastName = authData["last_name"];
    this.joiningAt = authData["joining_at"];
    this.accessToken = authData["access_token"];
    this.refreshToken = authData["refresh_token"];

    return {
      id: this.id,
      email: this.email,
      accessToken: this.accessToken,
      refreshToken: this.refreshToken,
      firstName: this.firstName,
      lastName: this.lastName,
      joiningAt: this.joiningAt,
    };
  }

  /**
   * Represents the response containing authentication tokens.
   */
  init(): ISwitchKeysAuthRegisterResponse {
    return {
      id: 0,
      email: "",
      accessToken: "",
      refreshToken: "",
      firstName: "",
      lastName: "",
      joiningAt: "",
    };
  }
}

export {
  SwitchKeysTokensResponse,
  SwitchKeysAuthRegisterResponse,
  ISwitchKeysAuthRegisterResponse,
};
