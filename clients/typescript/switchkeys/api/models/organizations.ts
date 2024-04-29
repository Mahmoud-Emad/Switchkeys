import {
  IOrganizationMemberRequest,
  IOrganizationRequest,
  IOrganizationResponse,
} from "../../utils/types";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { OrganizationResponse } from "../response/response";
import SwitchKeysOrganizationMember from "./organizations.members";
import SwitchKeysProject from "./organizations.projects";

/**
 * Class representing operations related to organizations.
 */
class SwitchKeysOrganizations {
  private organizationRoutes = SwitchKeysApiRoutes.organizations;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  /** Instance of `SwitchKeysOrganizationMember` for managing `member-related` operations. */
  members: SwitchKeysOrganizationMember = new SwitchKeysOrganizationMember();

  /**
   * Creates a new organization.
   * @param data The organization data.
   * @returns The response containing the organization details.
   */
  async create(data: IOrganizationRequest): Promise<IOrganizationResponse> {
    const url = this.organizationRoutes.create;
    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.POST,
      data
    );
    return this.handleResponse(response);
  }

  /**
   * Retrieves an organization by its ID.
   * @param orgId The ID of the organization.
   * @returns The response containing the organization details.
   */
  async getById(orgId: number): Promise<IOrganizationResponse> {
    const url = this.organizationRoutes.getById(orgId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleResponse(response);
  }

  /**
   * Updates an organization.
   * @param orgId The ID of the organization to update.
   * @param data The organization data.
   * @returns The response containing the updated organization details.
   */
  async update(orgId: number, data: IOrganizationRequest) {
    const url = this.organizationRoutes.getById(orgId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.PUT, data);
    return this.handleResponse(response);
  }

  /**
   * Adds a member to an organization.
   * @param orgId The ID of the organization.
   * @param data The member data.
   * @returns The response containing the updated organization details.
   */
  async addMember(orgId: number, data: IOrganizationMemberRequest) {
    const url = this.organizationRoutes.addMember(orgId);
    const _data = {
      member_id: data.memberId,
    };
    const response = await this.request.call(url, SwitchKeysRequestMethod.PUT, _data);
    return this.handleResponse(response);
  }

  /**
   * Removes a member from an organization.
   * @param orgId The ID of the organization.
   * @param data The member data.
   * @returns The response containing the updated organization details.
   */
  async removeMember(orgId: number, data: IOrganizationMemberRequest) {
    const url = this.organizationRoutes.removeMember(orgId);
    const _data = {
      member_id: data.memberId,
    };
    const response = await this.request.call(url, SwitchKeysRequestMethod.PUT, _data);
    return this.handleResponse(response);
  }

  /**
   * Deletes an organization.
   * @param orgId The ID of the organization to delete.
   */
  async delete(orgId: number): Promise<string | Error> {
    const url = this.organizationRoutes.getById(orgId);
    return await this.request.call(url, SwitchKeysRequestMethod.DELETE);
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns The parsed organization response.
   */
  private handleResponse(response: any): IOrganizationResponse {
    const organizationResponse = new OrganizationResponse();
    return response
      ? organizationResponse.parse(response)
      : organizationResponse.init();
  }
}

export default SwitchKeysOrganizations;
