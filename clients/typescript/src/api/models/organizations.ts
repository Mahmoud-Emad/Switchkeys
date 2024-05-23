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
// Overview of `SwitchKeysOrganizations`:
// The `SwitchKeysOrganizations` class is designed to manage a specific organization, or even list all of them.
//
// Example Usage:
//
// If you have a valid organization, you first need to login and then use the organization id to get the organization.
//
// ```typescript
// await switchkeys.auth.login({
//   email: "email@example.com",
//   password: "password"
// });
//
// // Now, you can get the organization directly
// const organization = await switchkeys.organizations.get({organizationID});
// ```
//
// By default, the `get` method returns an instance of the `SwitchKeysOrganizationsServices` class,
// which provides various methods to interact with the organization.
//
// Example Usage:
//
// Get the organization project:
// ```typescript
// const project = organization.project;
// console.log({ project });
// ```
//
// Creating a new project:
// ```typescript
// const project = await organization.createProject({
//   name: { projectName },
// });
// console.log("Created project:", project);
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

import { SwitchKeysRecordNotFoundError } from "../../core/exceptions";

import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import {
  ISwitchKeysOrganizationData,
  ISwitchKeysOrganizationMemberData,
  ISwitchKeysProjectData,
} from "../request/types";
import {
  OrganizationResponse,
  ProjectResponse,
} from "../response/response";
import {
  ISwitchKeysMemberResponse,
  ISwitchKeysOrganizationResponse,
  ISwitchKeysProjectResponse,
} from "../response/types";
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
   * @param options `ISwitchKeysOrganizationData` - The organization data.
   * @returns The response containing the organization details.
   */
  async create(
    options: ISwitchKeysOrganizationData
  ): Promise<SwitchKeysOrganizationsServices> {
    const url = this.organizationRoutes.create;
    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.POST,
      options
    );

    return this.handleResponse(response);
  }

  /**
   * Retrieves an organization by its ID.
   * @param orgId The ID of the organization.
   * @returns The response containing the organization details.
   */
  async get(orgId: number): Promise<SwitchKeysOrganizationsServices> {
    const url = this.organizationRoutes.getById(orgId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
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
  private handleResponse(response: any): SwitchKeysOrganizationsServices {
    const organizationResponse = new OrganizationResponse();
    const organization = response
      ? organizationResponse.parse(response)
      : organizationResponse.init();

    if (!organization.id) {
      throw new SwitchKeysRecordNotFoundError("Organization not found.");
    }

    return new SwitchKeysOrganizationsServices(organization);
  }
}

class SwitchKeysOrganizationsServices {
  private organization: ISwitchKeysOrganizationResponse;
  private organizationRoutes = SwitchKeysApiRoutes.organizations;
  private projectRoutes = SwitchKeysApiRoutes.projects;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  projects: SwitchKeysProject;
  constructor(organization: ISwitchKeysOrganizationResponse) {
    this.organization = organization;
    this.projects = new SwitchKeysProject();
  }

  /**
   * @return The organization name.
   */
  get name(): string {
    return this.organization.name;
  }

  /**
   * @return The organization created at datetime.
   */
  get created(): string {
    return this.organization.created;
  }

  /**
   * @return The organization modified at datetime.
   */
  get modified(): string {
    return this.organization.modified;
  }

  /**
   * @return The organization ID.
   */
  get id(): number {
    return this.organization.id;
  }

  /**
   * @return The organization owner.
   */
  get owner(): ISwitchKeysMemberResponse {
    return this.organization.owner;
  }

  /**
   * @return The organization modified at datetime.
   */
  getMembers(): ISwitchKeysMemberResponse[] {
    return this.organization.members;
  }

  /**
   * Creates a new project.
   * @param options - Project data.
   * @returns A promise that resolves to the created project.
   */
  async createProject(
    options: ISwitchKeysProjectData
  ): Promise<ISwitchKeysProjectResponse> {
    const requestData = {
      name: options.name,
      organization_id: this.organization.id,
    };

    const url = this.projectRoutes.create;

    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.POST,
      requestData
    );

    const projectResponse = new ProjectResponse();
    const project = response
      ? projectResponse.parse(response)
      : projectResponse.init();
    return project;
  }

  /**
   * Updates an organization.
   * @param options `ISwitchKeysOrganizationData` - The organization data.
   * @returns The response containing the updated organization details.
   */
  async update(
    options: ISwitchKeysOrganizationData
  ): Promise<ISwitchKeysOrganizationResponse> {
    const url = this.organizationRoutes.getById(this.organization.id);
    const organization = await this.request.call(
      url,
      SwitchKeysRequestMethod.PUT,
      options
    );

    this.organization = organization;
    return this.organization;
  }

  /**
   * Adds a member to an organization.
   * @param options `ISwitchKeysOrganizationMemberData` - The member data.
   * @returns The response containing the updated organization details.
   */
  async addMember(
    options: ISwitchKeysOrganizationMemberData
  ): Promise<ISwitchKeysOrganizationResponse> {
    const url = this.organizationRoutes.addMember(this.organization.id);
    const payload = {
      member_id: options.memberId,
    };

    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.PUT,
      payload
    );

    const organizationResponse = new OrganizationResponse();
    const organization = response
      ? organizationResponse.parse(response)
      : organizationResponse.init();

    if (!organization.id) {
      throw new SwitchKeysRecordNotFoundError("Organization not found.");
    }

    this.organization = organization;
    return organization;
  }

  /**
   * Removes a member from an organization.
   * @param options The member data.
   * @returns The response containing the updated organization details.
   */
  async removeMember(
    data: ISwitchKeysOrganizationMemberData
  ): Promise<ISwitchKeysOrganizationResponse> {
    const url = this.organizationRoutes.removeMember(this.organization.id);
    const payload = {
      member_id: data.memberId,
    };

    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.PUT,
      payload
    );

    const organizationResponse = new OrganizationResponse();
    const organization = response
      ? organizationResponse.parse(response)
      : organizationResponse.init();

    if (!organization.id) {
      throw new SwitchKeysRecordNotFoundError("Organization not found.");
    }

    this.organization = organization;
    return organization;
  }
}
export default SwitchKeysOrganizations;
