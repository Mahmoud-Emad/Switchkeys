// ------------------------------------------------------------------------------------------------------------------------------------------
//
// [DEVELOPERS] Attention please: Before adding any helper method, ask yourself these three important questions:
//
// ------------------------------------------------------------------------------------------------------------------------------------------
//
// ###################################
//  1. What does this method do?
//  2. What is the actual need for it?
//  3. Where should it be located?
// ###################################
//
// ------------------------------------------------------------------------------------------------------------------------------------------
//
// Overview of `SwitchKeysEnvironment`:
// The `SwitchKeysEnvironment` class is designed to load a specific environment.
// Imagine you have multiple environments; you need to load a specific one to work with it.
// In such cases, you use the `load` method to retrieve the environment along with its associated data,
// such as the project and organization details.
//
// Example Usage:
//
// If you have a valid environment key, you first need to login and then use the key to load the environment.
//
// ```typescript
// const environmentKey = "16e78bfa-fa85-4313-8bc2-1bd09db34642";
// await switchkeys.auth.login({
//   email: "email@example.com",
//   password: "password"
// });
//
// // Now, you can load the environment directly
// const environment = await switchkeys.environments.load(environmentKey);
// ```
//
// By default, the `load` method returns an instance of the `SwitchKeysEnvironmentServices` class,
// which provides various methods to interact with the environment.
//
// Example Usage:
//
// List all environment features:
// ```typescript
// const features = environment.features;
// console.log(features);
// ```
//
// Adding a new feature:
// ```typescript
// const addedFeature = await environment.addFeature({
//   name: "debug",
//   value: "false"
// });
// console.log("Added Feature:", addedFeature);
// ```
//
// Updating an existing feature:
// ```typescript
// const updatedFeature = await environment.updateFeature({
//   name: "debug",
//   newName: "debugMode",
//   newValue: "true"
// });
// console.log("Updated Feature:", updatedFeature);
// ```
//
// Checking if the environment has a specific feature:
// ```typescript
// const hasDebugFeature = environment.hasFeature("debugMode");
// console.log("Has 'debugMode' feature:", hasDebugFeature);
// ```
//
// Adding a user to the environment:
// ```typescript
// const newUser = await environment.addUser({
//   username: "newuser",
//   device: {
//     version: "1.0",
//     deviceType: "mobile"
//   }
// });
// console.log("Added User:", newUser);
// ```
// ------------------------------------------------------------------------------------------------------------------------------------------
//
// Before implementing anything, please:
// 1. Read the documentation first.
// 2. Review the existing code to understand the context.
// 3. Proceed with adding or modifying the code.
//
// Happy coding! xD
// @Mahmoud-Emad
// ------------------------------------------------------------------------------------------------------------------------------------------

import {
  SwitchKeysRecordNotFoundError,
  SwitchKeysValidationError,
} from "../../core/exceptions";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import {
  ISwitchKeysAddEnvironmentUserData,
  ISwitchKeysEnvironmentFeatureData,
  ISwitchKeysUpdateEnvironmentFeatureData,
} from "../request/types";
import {
  EnvironmentFeaturesResponse,
  EnvironmentResponse,
  EnvironmentUserResponse,
} from "../response/response";
import UUIDValidators from "uuid-validate";
import {
  ISwitchKeysEnvironmentFeaturesResponse,
  ISwitchKeysEnvironmentResponse,
  ISwitchKeysEnvironmentUserResponse,
  ISwitchKeysOrganizationResponse,
  ISwitchKeysProjectResponse,
} from "../response/types";

/**
 * Class representing a SwitchKeys Environment.
 */
class SwitchKeysEnvironment {
  protected environmentRoutes = SwitchKeysApiRoutes.environments;
  protected request: SwitchKeysRequest = new SwitchKeysRequest();

  /**
   * Loads the environment details using the provided environment key.
   * @param environmentKey - The UUID key of the environment.
   * @returns A Promise that resolves to a SwitchKeysEnvironmentServices instance.
   * @throws SwitchKeysValidationError if the environment key is not a valid UUID.
   */
  async load(environmentKey: string): Promise<SwitchKeysEnvironmentServices> {
    const isValidUUID = UUIDValidators(environmentKey);

    if (!isValidUUID) {
      throw new SwitchKeysValidationError(
        `'${environmentKey}' is not a valid UUID.`
      );
    }

    const url = this.environmentRoutes.load(environmentKey);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleResponse(response);
  }

  /**
   * Deletes the environment using the provided environment key.
   * @param environmentKey - The UUID key of the environment.
   * @returns A Promise that resolves to a null.
   * @throws SwitchKeysValidationError if the environment key is not a valid UUID.
   */
  async delete(environmentKey: string): Promise<SwitchKeysEnvironmentServices> {
    const isValidUUID = UUIDValidators(environmentKey);

    if (!isValidUUID) {
      throw new SwitchKeysValidationError(
        `'${environmentKey}' is not a valid UUID.`
      );
    }

    const url = this.environmentRoutes.delete(environmentKey);
    return await this.request.call(url, SwitchKeysRequestMethod.DELETE);
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns The parsed environment response.
   */
  protected handleResponse(response: any): SwitchKeysEnvironmentServices {
    const environmentResponse = new EnvironmentResponse();
    const _response = response
      ? environmentResponse.parse(response)
      : environmentResponse.init();

    return new SwitchKeysEnvironmentServices(_response);
  }
}

/**
 * Class representing the services available for a SwitchKeys Environment.
 */
class SwitchKeysEnvironmentServices {
  private environmentRoutes = SwitchKeysApiRoutes.environments;
  private request: SwitchKeysRequest = new SwitchKeysRequest();
  private environment: ISwitchKeysEnvironmentResponse;

  constructor(environment: ISwitchKeysEnvironmentResponse) {
    this.environment = environment;
  }

  /**
   * @return The environment key
   */
  get environmentKey(): string {
    return this.environment.environmentKey;
  }

  /**
   * @return The environment project
   */
  get project(): ISwitchKeysProjectResponse {
    return this.environment.project;
  }

  /**
   * @return The environment organization
   */
  get organization(): ISwitchKeysOrganizationResponse {
    return this.environment.project.organization;
  }

  /**
   * @return The environment name
   */
  get name(): string {
    return this.environment.project.name;
  }

  /**
   * @return The environment features
   */
  get features(): ISwitchKeysEnvironmentFeaturesResponse[] {
    return this.environment.features;
  }

  /**
   * @return The environment users
   */
  get users(): ISwitchKeysEnvironmentUserResponse[] {
    return this.environment.users;
  }

  /**
   * Gets the user details using the provided username.
   * @param username - The String username of the user.
   * @returns A Promise that resolves to a ISwitchKeysEnvironmentUserResponse instance.
   * @throws SwitchKeysRecordNotFoundError if the user is not found.
   */
  getUser(username: string): ISwitchKeysEnvironmentUserResponse {
    const user = this.environment.users.filter(
      (_user) => _user.username === username
    );
    if (user.length) {
      return user[0];
    }
    throw new SwitchKeysRecordNotFoundError("User not found");
  }

  /**
   * Gets the feature details using the provided feature name.
   * @param featrueName - The String name of the feature.
   * @returns A Promise that resolves to a ISwitchKeysEnvironmentFeaturesResponse instance.
   * @throws SwitchKeysRecordNotFoundError if the featrue is not found.
   */
  getFeature(featrueName: string): ISwitchKeysEnvironmentFeaturesResponse {
    const feat = this.environment.features.filter(
      (_feat) => _feat.name === featrueName
    );
    if (feat.length) {
      return feat[0];
    }
    throw new SwitchKeysRecordNotFoundError("Featrue not found");
  }

  /**
   * Checks if the environment has a specific feature.
   * @param featureName - The name of the feature.
   * @returns True if the environment has the feature, false otherwise.
   */
  hasFeature(featureName: string): boolean {
    return this.environment.features.some((feat) => feat.name === featureName);
  }

  /**
   * Adds a feature to the environment.
   * @param options - The feature data to add.
   * @returns A Promise that resolves to the added feature's response.
   */
  async addFeature(
    options: ISwitchKeysEnvironmentFeatureData
  ): Promise<ISwitchKeysEnvironmentFeaturesResponse> {
    const url = this.environmentRoutes.addFeature(this.environmentKey);
    const payload = {
      name: options.name,
      value: options.value,
    };

    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.POST,
      payload
    );

    const featureResponse = new EnvironmentFeaturesResponse();
    const feature = response
      ? featureResponse.parse(response)
      : featureResponse.init();

    if (feature.id) {
      this.environment.features.push(feature);
    }
    return feature;
  }

  /**
   * Adds a user to the environment.
   * @param options - The user data to add.
   * @returns A Promise that resolves to the added user's response.
   */
  async addUser(
    options: ISwitchKeysAddEnvironmentUserData
  ): Promise<ISwitchKeysEnvironmentUserResponse> {
    const url = this.environmentRoutes.addUser(this.environmentKey);
    const payload = {
      username: options.username,
      device: {
        version: options.device.version,
        device_type: options.device.deviceType,
      },
    };

    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.PUT,
      payload
    );

    const userResponse = new EnvironmentUserResponse();
    const user = response ? userResponse.parse(response) : userResponse.init();

    if (user.id) {
      this.environment.users.push(user);
    }
    return user;
  }

  /**
   * Updates a feature in the environment.
   * @param options - The feature data to update.
   * @returns A Promise that resolves to the updated feature's response.
   */
  async updateFeature(
    options: ISwitchKeysUpdateEnvironmentFeatureData
  ): Promise<ISwitchKeysEnvironmentFeaturesResponse> {
    const url = this.environmentRoutes.updateFeature(
      this.environmentKey,
      options.name
    );
    const payload = {
      name: options.newName,
      value: options.newValue,
    };

    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.PUT,
      payload
    );

    const featureResponse = new EnvironmentFeaturesResponse();
    const feature = response
      ? featureResponse.parse(response)
      : featureResponse.init();

    if (feature.id) {
      const index = this.environment.features.findIndex(
        (_feature) => _feature.id === feature.id
      );
      if (index !== -1) {
        this.environment.features[index] = feature;
      }
    }
    return feature;
  }

  /**
   * Adds a user to the environment.
   * @param options - The user data to add.
   * @returns A Promise that resolves to the added user's response.
   */
  async removeUser(
    username: string
  ): Promise<ISwitchKeysEnvironmentUserResponse[]> {
    const url = this.environmentRoutes.removeUser(this.environmentKey);

    await this.request.call(url, SwitchKeysRequestMethod.PUT, { username });

    this.environment.users = this.environment.users.filter(
      (user) => user.username !== username
    );

    return this.environment.users;
  }
}

export default SwitchKeysEnvironment;
