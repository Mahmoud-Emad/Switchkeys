import SwitchKeysConfig from "../../utils/config";
import { SwitchKeysLogger } from "../../utils/logger";
import { SwitchKeysAuthTokens } from "../../utils/types";
import { SwitchKeysApiRoutes, SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysAuthLoginData, SwitchKeysAuthRegisterData } from "../request/types";
import { ISwitchKeysAuthRegisterResponse, SwitchKeysAuthRegisterResponse } from "../response/types";

/**
 * Class for managing authentication operations with the SwitchKeys system.
 */
class SwitchKeysAuth {
  private tokens: SwitchKeysAuthTokens = { accessToken: "", refreshToken: "" };
  private config = new SwitchKeysConfig();
  private authRoutes = SwitchKeysApiRoutes.auth;
  private request: SwitchKeysRequest = new SwitchKeysRequest();
  private logger: SwitchKeysLogger = new SwitchKeysLogger();
  private configFile: string = 'config.ini';

  /**
   * Registers a new user with the SwitchKeys authentication service.
   * @param data The registration data for the new user.
   * @returns A promise that resolves to the registered user's data.
   */
  async register(data: SwitchKeysAuthRegisterData): Promise<ISwitchKeysAuthRegisterResponse> {
    const url = this.authRoutes.registerURL;
    const requestBody = {
      email: data.email,
      password: data.password,
      first_name: data.firstName,
      last_name: data.lastName,
      user_type: data.userType,
    };

    const response = await this.request.call(url, SwitchKeysRequestMethod.POST, requestBody);
    const switchKeysAuthRegisterResponse = new SwitchKeysAuthRegisterResponse();
    let userData: ISwitchKeysAuthRegisterResponse = switchKeysAuthRegisterResponse.init();

    if (response) {
      userData = switchKeysAuthRegisterResponse.parseAuth(response);
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
   * Logs in an existing user with the SwitchKeys authentication service.
   * @param data The login credentials for the user.
   * @returns A promise that resolves to the logged in user's data.
   */
  async login(data: SwitchKeysAuthLoginData): Promise<ISwitchKeysAuthRegisterResponse> {
    const url = this.authRoutes.loginURL;
    const response = await this.request.call(url, SwitchKeysRequestMethod.POST, data);

    const switchKeysAuthRegisterResponse = new SwitchKeysAuthRegisterResponse();
    let userData: ISwitchKeysAuthRegisterResponse = switchKeysAuthRegisterResponse.init();

    if (response) {
      userData = switchKeysAuthRegisterResponse.parseAuth(response);
      if (userData.accessToken && userData.refreshToken) {
        this.tokens.accessToken = userData.accessToken;
        this.tokens.refreshToken = userData.refreshToken;
        this.config.write(this.tokens);
      }
    }

    return userData;
  }
}

export default SwitchKeysAuth;
