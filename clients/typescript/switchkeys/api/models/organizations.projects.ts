import { IProjectResponse } from "../../utils/types";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { ProjectResponse } from "../response/response";
import SwitchKeysEnvironment from "./projects.environments";

/**
 * Interface for project request data.
 */
interface IProjectRequest {
  name: string;
  organizationId: number;
}

/**
 * Represents a service for interacting with projects.
 */
class SwitchKeysProject {
  private projectRoutes = SwitchKeysApiRoutes.projects;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  /**
   * Instance of `SwitchKeysEnvironment` for managing environment-related operations.
   */
  environments: SwitchKeysEnvironment = new SwitchKeysEnvironment();

  /**
   * Creates a new project.
   * @param data - Project data.
   * @returns A promise that resolves to the created project.
   */
  async create(data: IProjectRequest): Promise<IProjectResponse> {
    const requestData = { name: data.name, organization_id: data.organizationId };
    const url = this.projectRoutes.create;
    const response = await this.request.call(url, SwitchKeysRequestMethod.POST, requestData);
    return this.handleResponse(response);
  }

  /**
   * Updates an existing project.
   * @param projectId - The ID of the project to update.
   * @param data - Updated project data.
   * @returns A promise that resolves to the updated project.
   */
  async update(projectId: number, data: IProjectRequest): Promise<IProjectResponse> {
    const requestData = { name: data.name, organization_id: data.organizationId };
    const url = this.projectRoutes.getById(projectId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.PUT, requestData);
    return this.handleResponse(response);
  }

  /**
   * Retrieves a project by its ID.
   * @param projectId - The ID of the project to retrieve.
   * @returns A promise that resolves to the retrieved project.
   */
  async getById(projectId: number): Promise<IProjectResponse> {
    const url = this.projectRoutes.getById(projectId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleResponse(response);
  }

  /**
   * Deletes a project by its ID.
   * @param projectId - The ID of the project to delete.
   * @returns A promise that resolves to a success message or an error.
   */
  async delete(projectId: number): Promise<string | Error> {
    const url = this.projectRoutes.getById(projectId);
    return await this.request.call(url, SwitchKeysRequestMethod.DELETE);
  }

  /**
   * Retrieves all projects belonging to a specific organization.
   * @param organizationId - The ID of the organization.
   * @returns A promise that resolves to an array of projects.
   */
  async all(organizationId: number): Promise<IProjectResponse[]> {
    const url = this.projectRoutes.getAllOrganizationProjects(organizationId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleAllResponse(response);
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns The parsed project response.
   */
  private handleResponse(response: any): IProjectResponse {
    const projectResponse = new ProjectResponse();
    return response ? projectResponse.parse(response) : projectResponse.init();
  }

  /**
   * Parses and handles the response for multiple projects from the API.
   * @param response - The response from the API.
   * @returns An array of parsed project responses.
   */
  private handleAllResponse(response: any): IProjectResponse[] {
    const projectResponse = new ProjectResponse();
    return response ? projectResponse.parseAll(response) : [];
  }
}

export default SwitchKeysProject;
