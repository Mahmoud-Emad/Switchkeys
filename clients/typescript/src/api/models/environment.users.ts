import { SwitchKeysFeatureDoesNotExistError } from "../../core/exceptions";
import {} from "../../utils/types";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import SwitchKeysEnvironment from "./projects.environments";
import { EnvironmentFeaturesResponse } from "../response/response";
import {
  ISwitchKeysEnvironmentFeaturesResponse,
  ISwitchKeysEnvironmentUserResponse,
} from "../response/types";

/**
 * Class for managing environment user operations.
 */
class SwitchKeysEnvironmentUser {
  /**
   * Retrieves an environment user based on username or ID.
   * @param environmentKey The environment key.
   * @param options Object containing username or ID for user lookup.
   * @returns A promise resolving to the environment user response, if found.
   * @throws SwitchKeysValidationError if neither username nor ID is provided.
   */
  // async get(
  //   environmentKey: string,
  //   options: { username?: string; id?: number }
  // ): Promise<SwitchKeysEnvironmentUserServices> {
  //   if (!options.username && !options.id) {
  //     throw new SwitchKeysValidationError(
  //       "You have to send the user username or even the user ID."
  //     );
  //   }
  //   const environment = new SwitchKeysEnvironment();
  //   const users = await environment.getUsers(environmentKey);
  //   for (const user of users) {
  //     if (
  //       (options.username && user.username === options.username) ||
  //       (options.id && user.id === options.id)
  //     ) {
  //       return new SwitchKeysEnvironmentUserServices({
  //         id: user.id,
  //         username: user.username,
  //         device: user.device,
  //         features: user.features,
  //         environment,
  //         environmentKey,
  //       });
  //     }
  //   }
  //   throw new SwitchKeysRecordNotFoundError(
  //     `The user with ${
  //       options.username
  //         ? `username '${options.username}'`
  //         : `id '${options.id}'`
  //     } is not found.`
  //   );
  // }
}

// Remove export later.
export class SwitchKeysEnvironmentUserServices {
  private user: ISwitchKeysEnvironmentUserResponse;
  private environmentKey: string;
  private environment: SwitchKeysEnvironment;

  // private environmentRoutes = SwitchKeysApiRoutes.environments;
  private environmentUserRoutes = SwitchKeysApiRoutes.environmentUsers;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  constructor(
    options: ISwitchKeysEnvironmentUserResponse & {
      environment: SwitchKeysEnvironment;
      environmentKey: string;
    }
  ) {
    this.user = {
      id: options.id,
      username: options.username,
      device: options.device,
      features: options.features,
    };

    this.environment = options.environment;
    this.environmentKey = options.environmentKey;
  }

  get features() {
    return this.user.features;
  }

  get device() {
    return this.user.device;
  }

  // TODO: Make action classes for all class managements.

  async addFeature(feature: { name: string; value: any }) {
    const url = this.environmentUserRoutes.addFeature(
      this.environmentKey,
      this.user.username
    );
    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.PUT,
      feature
    );
    return this.handleResponse(response);
  }

  getFeature(featureName: string): ISwitchKeysEnvironmentFeaturesResponse {
    if (this.hasFeature(featureName)) {
      const feature = this.user.features.filter(
        (feature) => feature.name === featureName
      );
      return feature[0];
    }
    throw new SwitchKeysFeatureDoesNotExistError(
      `The feature 'featureName' does not exit for user '${this.user.username}'.`
    );
  }

  hasFeature(featureName: string): boolean {
    return this.user.features.map((feature) => featureName === feature.name)[0];
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns The parsed project response.
   */
  private handleResponse(
    response: any
  ): ISwitchKeysEnvironmentFeaturesResponse {
    const userFeature = new EnvironmentFeaturesResponse();
    return response ? userFeature.parse(response) : userFeature.init();
  }
}

export default SwitchKeysEnvironmentUser;
