import axios, { AxiosResponse } from 'axios';
import * as dotenv from 'dotenv';
import { SwitchKeysLogger } from '../../utils/logger';

dotenv.config(); // Load environment variables from .env file

/**
 * Represents authentication routes for making API requests.
 */
class SwitchKeysAuthRoutes {
  private BASE_URL: string;

  /**
   * Constructs a new SwitchKeysAuthRoutes instance.
   */
  constructor() {
    this.BASE_URL = process.env.BASE_URL || '';
  }

  /**
   * Gets the URL for user registration.
   * @returns The URL for user registration.
   */
  get registerURL(): string {
    return `${this.BASE_URL}/api/auth/signup/`;
  }

  /**
   * Gets the URL for user login.
   * @returns The URL for user login.
   */
  get loginURL(): string {
    return `${this.BASE_URL}/api/auth/login/`;
  }
}

/**
 * Represents API routes for making requests.
 */
class SwitchKeysApiRoutes {
  static auth: SwitchKeysAuthRoutes = new SwitchKeysAuthRoutes();
}

/**
 * Enum representing HTTP request methods.
 */
enum SwitchKeysRequestMethod {
  POST = 'POST',
  GET = 'GET',
  PUT = 'PUT',
  DELETE = 'DELETE',
}

/**
 * Handles making HTTP requests to the API.
 */
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
    try {
      const response = await axios.request({
        url,
        method,
        data,
      });

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
    if (!response){
      return this.logger.error("Server might be down or your connection is a bit slow, Please check your connection/server connection.")
    }

    const { status, data } = response;

    if (status >= 400 || data.error) {
      return this.displayError(data.message, data.error);
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
    let errorMessage = `${message}\nError Details:`;

    if (error) {
      for (const key of Object.keys(error)) {
        errorMessage += `\n- ${key}: ${error[key]}`;
      }
    }

    this.logger.error(errorMessage);
  }

  /**
   * Wraps results.
   * @param results The results to wrapped.
   */
  private wrapResults(results: any) {
    return results;
  }
}

export { SwitchKeysApiRoutes, SwitchKeysRequest, SwitchKeysRequestMethod };
