import axios, { AxiosResponse } from "axios";
import SwitchKeysConfig from "../../utils/config";
import { SwitchKeysLogger } from "../../utils/logger";
import {
  SwitchKeysAuthTokens,
} from "../../utils/types";
import { SwitchKeysApiRoutes } from "../request/request";
import { SwitchKeysAuthLoginData, SwitchKeysAuthRegisterData } from "../request/types";
import { SwitchKeysAuthRegisterResponse } from "../response/types";

enum SwitchKeysRequestMethod {
  POST,
  GET,
  PUT,
  DELETE,
}

class SwitchKeysRequest {
  private logger: SwitchKeysLogger = new SwitchKeysLogger();

  /**
   * Makes an HTTP request to the specified URL using the provided method and data.
   * @param url The URL to make the request to.
   * @param method The HTTP method to use for the request.
   * @param data Optional data to send with the request.
   * @returns The response data if the request is successful, or an error message if it fails.
   */
  async call(url: string, method: SwitchKeysRequestMethod, data?: any) {
    let response;

    try {
      if (method === SwitchKeysRequestMethod.POST) {
        response = await axios.post(url, data);
      } else if (method === SwitchKeysRequestMethod.PUT) {
        response = await axios.put(url, data);
      } else if (method === SwitchKeysRequestMethod.GET) {
        response = await axios.get(url);
      } else if (method === SwitchKeysRequestMethod.DELETE) {
        response = await axios.delete(url);
      } else {
        this.logger.error("Unknown request method.");
        return;
      }

      return this.readResponse(response);
    } catch (error: any) {
      return this.readResponse(error.response);
    }
  }

  /**
   * Reads the response from the HTTP request and handles errors.
   * @param response The AxiosResponse object containing the response data.
   * @returns The response data if the request is successful, or an error message if it fails.
   */
  private readResponse(response: AxiosResponse) {
    const status = response.status;
    const data = response.data;
    const message = data.message;
    const error = data.error;

    if (error || status >= 400) {
      return this.displayError(message, error);
    } else {
      return this.wrapResults(data.results);
    }
  }

  /**
   * Displays error messages in the console.
   * @param message The error message to display.
   * @param error Optional additional error details.
   */
  private displayError(message: string, error?: any) {
    if (error) {
      let errorMessage = `${message}\nError Details:`;
      for (const key of Object.keys(error)) {
        errorMessage += `\n- ${key}: ${error[key]}`;
      }
      this.logger.error(errorMessage);
    } else {
      this.logger.error(message);
    }
  }

  /**
   * Wraps results.
   * @param results The results to wrapped.
   */
  private wrapResults(results: any) {
    return results
  }
}

class SwitchKeysAuth {
  private tokens: SwitchKeysAuthTokens = { accessToken: "", refreshToken: "" };
  private config = new SwitchKeysConfig();
  private authRoutes = SwitchKeysApiRoutes.auth;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  /**
   * Registers a new user with the SwitchKeys authentication service.
   * @param data The registration data for the new user.
   */
  async register(data: SwitchKeysAuthRegisterData): Promise<SwitchKeysAuthRegisterResponse>{
    const url = this.authRoutes.registerURL;
    const requestBody = {
      email: data.email,
      password: data.password,
      first_name: data.firstName,
      last_name: data.lastName,
      user_type: data.userType,
    }

    let userData = await this.request.call(url, SwitchKeysRequestMethod.POST, requestBody);

    if (data){
      const switchKeysAuthRegisterResponse = new SwitchKeysAuthRegisterResponse()
      userData = switchKeysAuthRegisterResponse.parseAuth(data)
    }

    return userData
  }

  /**
   * Logs in an existing user with the SwitchKeys authentication service.
   * @param data The login credentials for the user.
   */
  async login(data: SwitchKeysAuthLoginData) {
    // Implement login functionality here
  }
}

export default SwitchKeysAuth;
