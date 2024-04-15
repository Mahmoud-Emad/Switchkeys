import SwitchKeysConfig from "../../utils/config";
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

    const request = await this.request.call(url, SwitchKeysRequestMethod.POST, requestBody);
    const response = new SwitchKeysAuthRegisterResponse();
    let userData: ISwitchKeysAuthRegisterResponse = response.init();

    if (request) {
      userData = response.parseAuth(request);
      if (userData.accessToken && userData.refreshToken) {
        this.tokens.accessToken = userData.accessToken;
        this.tokens.refreshToken = userData.refreshToken;
        this.config.write(this.tokens);
      }
    }

    return userData;
  }

  /**
   * Logs in an existing user with the SwitchKeys authentication service.
   * @param data The login credentials for the user.
   */
  async login(data: SwitchKeysAuthLoginData) {
    // Implement login functionality here
    console.log("this.config.load()", this.config.load());
  }
}

export default SwitchKeysAuth;
