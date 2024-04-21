import axios, { AxiosRequestConfig, AxiosResponse } from "axios";
import { SwitchKeysLogger } from "../../utils/logger";
import {
  SwitchKeysConnectionError,
  SwitchKeysRecordNotFoundError,
  SwitchKeysUnauthorizedError,
} from "../../core/exceptions";
import SwitchKeysConfig from "../../utils/config";

/**
 * Enum representing HTTP request methods.
 */
enum SwitchKeysRequestMethod {
  POST = "POST",
  GET = "GET",
  PUT = "PUT",
  DELETE = "DELETE",
}

/**
 * Handles making HTTP requests to the API.
 */
class SwitchKeysRequest {
  private logger: SwitchKeysLogger = new SwitchKeysLogger();
  private config = new SwitchKeysConfig();

  /**
   * Makes an HTTP request to the specified URL using the provided method and data.
   * @param url The URL to make the request to.
   * @param method The HTTP method to use for the request.
   * @param data Optional data to send with the request.
   * @returns The response data if the request is successful, or an error message if it fails.
   */
  async call(url: string, method: SwitchKeysRequestMethod, data?: any) {
    let accessToken;
    const requestConfig: AxiosRequestConfig = {
      url,
      method,
      data,
    };

    if (method !== SwitchKeysRequestMethod.GET) {
      accessToken = this.config.load().accessToken;
      requestConfig.headers = {
        Authorization: `Bearer ${accessToken}`,
      };
    }

    try {
      const response = await axios.request(requestConfig);
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
    if (!response) {
      throw new SwitchKeysConnectionError(
        "Server might be down or your connection is a bit slow, Please check your connection/server connection."
      );
    }

    const { status, data } = response;

    if (status >= 400 || data.error) {
      return this.displayError(data.message || data.detail, data.error, status);
    } else {
      return this.wrapResults(data.results);
    }
  }

  /**
   * Displays error messages in the console.
   * @param message The error message to display.
   * @param error Optional additional error details.
   */
  private displayError(message: string, error?: any, status?: number) {
    if (status && status === 401) {
      throw new SwitchKeysUnauthorizedError(message);
    }

    if (status && status === 404) {
      throw new SwitchKeysRecordNotFoundError(message);
    }

    if (error) {
      message += `\nError Details:`;
      for (const key of Object.keys(error)) {
        message += `\n- ${key}: ${error[key]}`;
      }
    }

    this.logger.error(message);
  }

  /**
   * Wraps results.
   * @param results The results to wrapped.
   */
  private wrapResults(results: any) {
    return results;
  }
}

export { SwitchKeysRequest, SwitchKeysRequestMethod };
