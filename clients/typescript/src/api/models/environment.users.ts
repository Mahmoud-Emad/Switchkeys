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
// Overview of `SwitchKeysEnvironmentUsers`:
// The `SwitchKeysEnvironmentUsers` class is designed to manage the environment users, or even list all of them.
//
// Example Usage:
//
// Load the environment using the environment key.
// ```ts
// const environment = await switchkeys.environments.load(environmentKey);
// console.log("[+] Loaded Environment:", environment);
// ```
//
// Add a user to the environment.
// ```ts
// const username1 = "user1";
// await environment.addUser({
//   device: {
//     deviceType: DeviceTypeSelection.ANDROID,
//     version: "v15s.521.s",
//   },
//   username: username1,
// });
// console.log(`[+] Added user: ${username1}`, {
//   user1Features: environment.users.get(username1)?.features,
// });
// ```
// 
// Check and add a feature for any user inside the environment with a different value.
// ```ts
// const envUser = environment.users.get(username1);
// const featureName = "theme";
// if (envUser.hasFeature(featureName)) {
//   console.log(
//     `[+] User has the '${envUser.getFeature(featureName).name}' feature, the value is: '${envUser.getFeature(featureName).value}'.`
//   );
// } else {
//   envUser.setFeature({
//     name: featureName,
//     value: "dark"
//   })
//   console.log(`[+] Feature ${featureName} has been added to the user, th value is '${envUser.getFeature(featureName).value}'.`)
// }
// ```
// 
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


import { SwitchKeysFeatureDoesNotExistError, SwitchKeysRecordNotFoundError } from "../../core/exceptions";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { EnvironmentFeaturesResponse } from "../response/response";
import {
  ISwitchKeysEnvironmentFeaturesResponse,
  ISwitchKeysEnvironmentResponse,
  ISwitchKeysEnvironmentUserResponse,
} from "../response/types";

/**
 * Class for managing environment user operations.
 */
class SwitchKeysEnvironmentUsers {
  private environment: ISwitchKeysEnvironmentResponse;

  constructor(environment: ISwitchKeysEnvironmentResponse){
    this.environment = environment;
  }

  /**
   * Gets the environment users.
   * @returns A Promise that resolves to a `ISwitchKeysEnvironmentUserResponse[]` instance.
   */
  all(): ISwitchKeysEnvironmentUserResponse[]{
    return this.environment.users;
  }

  /**
   * Gets the user details using the provided username.
   * @param username - The String username of the user.
   * @returns A Promise that resolves to a SwitchKeysEnvironmentUserServices instance.
   * @throws SwitchKeysRecordNotFoundError if the user is not found.
   */
  get(username: string): SwitchKeysEnvironmentUserServices{
    const user = this.all().filter(
      (_user) => _user.username === username
    );
    if (user.length) {
      return new SwitchKeysEnvironmentUserServices(this.environment, user[0]);
    }
    throw new SwitchKeysRecordNotFoundError("User not found");
  }
}

class SwitchKeysEnvironmentUserServices {
  private user: ISwitchKeysEnvironmentUserResponse;
  private environment: ISwitchKeysEnvironmentResponse;

  private environmentUserRoutes = SwitchKeysApiRoutes.environmentUsers;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  constructor(environment: ISwitchKeysEnvironmentResponse, user: ISwitchKeysEnvironmentUserResponse) {
    this.environment = environment
    this.user = user
  }

  get features() {
    return this.user.features;
  }

  get device() {
    return this.user.device;
  }

  // TODO: Make action classes for all class managements.

  async setFeature(feature: { name: string; value: any }) {
    const url = this.environmentUserRoutes.addFeature(
      this.environment.environmentKey,
      this.user.username
    );
    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.PUT,
      feature
    );

    const feat = this.handleResponse(response);
    if(feat.id != 0){
      this.user.features.push(feat);
      return feat;
    }
    throw new SwitchKeysRecordNotFoundError("Feature not found");
  }

  getFeature(featureName: string): ISwitchKeysEnvironmentFeaturesResponse {
    if (this.hasFeature(featureName)) {
      const feature = this.user.features.filter(
        (feature) => feature.name === featureName
      );
      return feature[0];
    }
    throw new SwitchKeysFeatureDoesNotExistError(
      `The feature '${featureName}' does not exit for user '${this.user.username}'.`
    );
  }

  hasFeature(featureName: string): boolean {
    return this.user.features.some((feat) => feat.name === featureName);
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

export default SwitchKeysEnvironmentUsers;