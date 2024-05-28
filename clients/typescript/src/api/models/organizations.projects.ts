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
// Overview of `SwitchKeysProjects`:
// The `SwitchKeysProjects` class is designed to manage a specific organization project, or even list all of them.
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
import { ProjectResponse } from "../response/response";
import {
  ISwitchKeysDefaultEnvironmentsResponse,
  ISwitchKeysOrganizationResponse,
  ISwitchKeysProjectResponse,
} from "../response/types";

/**
 * Represents a service for interacting with projects.
 */
export class SwitchKeysProjects {
  private projectRoutes = SwitchKeysApiRoutes.projects;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

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

export class SwitchKeysProjectServices {
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
