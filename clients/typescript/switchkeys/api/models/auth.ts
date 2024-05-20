import SwitchKeysConfig from "../../utils/config";
import { SwitchKeysLogger } from "../../utils/logger";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import {
  ISwitchKeysAuthLoginData,
  ISwitchKeysAuthRegisterData,
} from "../request/types";
import {
  ISwitchKeysAuthTokensResponse,
  ISwitchKeysUserAuthResponse,
} from "../response/types";

/**
 * Manages authentication operations with the SwitchKeys system.
 */
class SwitchKeysAuth {
  private tokens: ISwitchKeysAuthTokensResponse = {
    accessToken: "",
    refreshToken: "",
  };
  private config = new SwitchKeysConfig();
  private authRoutes = SwitchKeysApiRoutes.auth;
  private request: SwitchKeysRequest = new SwitchKeysRequest();
  private logger: SwitchKeysLogger = new SwitchKeysLogger();
  private configFile: string = "config.ini";

  /**
   * Registers a new user with the SwitchKeys authentication service.
   * @param data - Registration data for the new user.
   * @returns A promise that resolves to the registered user's data.
   */
  async register(
    data: ISwitchKeysAuthRegisterData
  ): Promise<ISwitchKeysUserAuthResponse> {
    const url = this.authRoutes.registerURL;
    const requestBody = {
      email: data.email,
      password: data.password,
      first_name: data.firstName,
      last_name: data.lastName,
      user_type: data.memberType,
    };

    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.POST,
      requestBody
    );

    const switchKeysAuthResponse = new SwitchKeysAuthResponse();
    let userData: ISwitchKeysUserAuthResponse = switchKeysAuthResponse.init();

    if (response) {
      userData = switchKeysAuthResponse.parseAuth(response);
      if (userData.accessToken && userData.refreshToken) {
        this.tokens.accessToken = userData.accessToken;
        this.tokens.refreshToken = userData.refreshToken;
        this.config.write(this.tokens);
        this.logger.info(`Tokens written to: ${this.configFile}.`);
      }
    }

    return userData;
  }

  /**
   * Logs out an existing user by removing the login credentials.
   * @returns undefined.
   */
  logout(): void {
    return this.config.write(
      {
        accessToken: "",
        refreshToken: "",
      },
      this.configFile,
      true
    );
  }

  /**
   * Logs in an existing user with the SwitchKeys authentication service.
   * @param data - Login credentials for the user.
   * @returns A promise that resolves to the logged in user's data.
   */
  async login(
    data: ISwitchKeysAuthLoginData
  ): Promise<ISwitchKeysUserAuthResponse> {
    const url = this.authRoutes.loginURL;
    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.POST,
      data
    );

    const switchKeysAuthResponse = new SwitchKeysAuthResponse();
    let userData: ISwitchKeysUserAuthResponse = switchKeysAuthResponse.init();

    if (response) {
      userData = switchKeysAuthResponse.parseAuth(response);
      if (userData.accessToken && userData.refreshToken) {
        this.tokens.accessToken = userData.accessToken;
        this.tokens.refreshToken = userData.refreshToken;
        this.config.write(this.tokens);
      }
    }

    return userData;
  }
}

/**
 * Represents the response for registering a user with SwitchKeys authentication.
 */
class SwitchKeysAuthResponse implements ISwitchKeysUserAuthResponse {
  id: number = 0;
  firstName: string = "";
  lastName: string = "";
  email: string = "";
  joiningAt: string = "";
  accessToken: string = "";
  refreshToken: string = "";

  /**
   * Parses authentication data and sets the properties of the response object.
   * @param authData - Authentication data to parse.
   * @returns The parsed authentication response object.
   */
  parseAuth(authData: any): ISwitchKeysUserAuthResponse {
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
  init(): ISwitchKeysUserAuthResponse {
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

export default SwitchKeysAuth;
