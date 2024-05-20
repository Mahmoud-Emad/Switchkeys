import { SwitchKeysRecordNotFoundError } from "../../core/exceptions";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { ProjectResponse } from "../response/response";
import {
  ISwitchKeysDefaultEnvironmentsResponse,
  ISwitchKeysOrganizationResponse,
  ISwitchKeysProjectResponse,
} from "../response/types";

/**
 * Represents a service for interacting with projects.
 */
class SwitchKeysProject {
  private projectRoutes = SwitchKeysApiRoutes.projects;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  // /**
  //  * Updates an existing project.
  //  * @param projectId - The ID of the project to update.
  //  * @param data - Updated project data.
  //  * @returns A promise that resolves to the updated project.
  //  */
  // async update(
  //   projectId: number,
  //   data: ISwitchKeysIProjectRequest
  // ): Promise<IProjectResponse> {
  //   const requestData = {
  //     name: data.name,
  //     organization_id: data.organizationId,
  //   };
  //   const url = this.projectRoutes.getById(projectId);
  //   const response = await this.request.call(
  //     url,
  //     SwitchKeysRequestMethod.PUT,
  //     requestData
  //   );
  //   return this.handleResponse(response);
  // }

  /**
   * Retrieves a project by its ID.
   * @param projectId - The ID of the project to retrieve.
   * @returns A promise that resolves to the retrieved project.
   */
  async get(projectId: number): Promise<SwitchKeysProjectServices> {
    const url = this.projectRoutes.getById(projectId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleResponse(response);
  }

  /**
   * Retrieves all projects belonging to a specific organization.
   * @param organizationId - The ID of the organization.
   * @returns A promise that resolves to an array of projects.
   */
  async all(organizationId: number): Promise<ISwitchKeysProjectResponse[]> {
    const url = this.projectRoutes.getAllOrganizationProjects(organizationId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleAllResponse(response);
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns The parsed project response.
   */
  private handleResponse(response: any): SwitchKeysProjectServices {
    const projectResponse = new ProjectResponse();
    const project = response
      ? projectResponse.parse(response)
      : projectResponse.init();
    return new SwitchKeysProjectServices(project);
  }

  /**
   * Parses and handles the response for multiple projects from the API.
   * @param response - The response from the API.
   * @returns An array of parsed project responses.
   */
  private handleAllResponse(response: any): ISwitchKeysProjectResponse[] {
    const projectResponse = new ProjectResponse();
    return response ? projectResponse.parseAll(response) : [];
  }
}

class SwitchKeysProjectServices {
  private project: ISwitchKeysProjectResponse;
  private projectRoutes = SwitchKeysApiRoutes.projects;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  constructor(project: ISwitchKeysProjectResponse) {
    if (!project.id) {
      throw new SwitchKeysRecordNotFoundError("Project not found.");
    }

    this.project = project;
  }

  /**
   * @return The project created at datetime.
   */
  get created(): string{
    return this.project.created
  }

  /**
   * @return The project modified at datetime.
   */
  get modified(): string{
    return this.project.modified
  }

  /**
   * @return The project ID.
   */
  get id(): number{
    return this.project.id
  }

  /**
   * @return The project name.
   */
  get name(): string{
    return this.project.name
  }

  /**
   * @return The project organization.
   */
  get organization(): ISwitchKeysOrganizationResponse{
    return this.project.organization
  }

  /**
   * @return The project environments.
   */
  get environments(): ISwitchKeysDefaultEnvironmentsResponse{
    return this.project.environments
  }

  /**
   * Deletes a project by its ID.
   * @param projectId - The ID of the project to delete.
   * @returns A promise that resolves to a success message or an error.
   */
  async delete(): Promise<string | Error> {
    const url = this.projectRoutes.getById(this.project.id);
    return await this.request.call(url, SwitchKeysRequestMethod.DELETE);
  }
}

export default SwitchKeysProject;
