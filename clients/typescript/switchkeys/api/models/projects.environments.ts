import { SwitchKeysValidationError } from "../../core/exceptions";
import { IEnvironmentFeaturesResponse, IEnvironmentResponse, IEnvironmentUserResponse, IOrganizationResponse, IProjectResponse } from "../../utils/types";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { EnvironmentResponse } from "../response/response";
import SwitchKeysEnvironmentUser from "./environment.users";
import SwitchKeysEnvironmentFeatures from "./envoronment.features";
import UUIDValidators from 'uuid-validate';


class SwitchKeysEnvironment{
  private environmentRoutes = SwitchKeysApiRoutes.environments;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  features: SwitchKeysEnvironmentFeatures = new SwitchKeysEnvironmentFeatures()
  users: SwitchKeysEnvironmentUser = new SwitchKeysEnvironmentUser()

  async load(environmentKey: string): Promise<IEnvironmentResponse>{
    const isValidUUID = UUIDValidators(environmentKey)

    if(!isValidUUID){
      throw new SwitchKeysValidationError(`'${environmentKey}' is not a valid UUID.`)
    }

    const url = this.environmentRoutes.load(environmentKey);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleResponse(response);
  }

  async getProject(environmentKey: string): Promise<IProjectResponse>{
    const environemt = await this.load(environmentKey);
    return environemt.project
  }

  async getOrganization(environmentKey: string): Promise<IOrganizationResponse>{
    const environemt = await this.load(environmentKey);
    return environemt.project.organization;
  }

  async getUsers(environmentKey: string): Promise<IEnvironmentUserResponse[]>{
    const environemt = await this.load(environmentKey);
    return environemt.users;
  }

  async getFeatures(environmentKey: string): Promise<IEnvironmentFeaturesResponse[]>{
    const environemt = await this.load(environmentKey);
    return environemt.features;
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns The parsed organization response.
   */
  private handleResponse(response: any): IEnvironmentResponse {
    const environmentResponse = new EnvironmentResponse();
    return response
      ? environmentResponse.parse(response)
      : environmentResponse.init();
  }
}

export default SwitchKeysEnvironment;