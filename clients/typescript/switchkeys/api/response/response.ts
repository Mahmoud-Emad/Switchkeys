import {
  ISwitchKeysMemberResponse,
  IOrganizationResponse,
  IProjectResponse,
  IEnvironmentResponse,
  IEnvironmentUserResponse,
  IDefaultEnvironmentsResponse,
  IEnvironmentFeaturesResponse,
} from "../../utils/types";

/**
 * Class for parsing member response data.
 */
class SwitchKeysMemberResponse implements ISwitchKeysMemberResponse {
  id: number = 0;
  firstName: string = "";
  lastName: string = "";
  email: string = "";
  joiningAt: string = "";
  isActive?: boolean | undefined;

  /**
   * Initializes default member response data.
   */
  constructor() {}

  /**
   * Initializes default member response data.
   * @returns Default member response data.
   */
  init(): ISwitchKeysMemberResponse {
    return {
      id: 0,
      email: "",
      firstName: "",
      lastName: "",
      joiningAt: "",
      isActive: undefined,
    };
  }

  /**
   * Parses raw data into member response data.
   * @param data Raw data to parse.
   * @returns Parsed member response data.
   */
  parse(data: any): ISwitchKeysMemberResponse {
    return {
      id: data["id"] || 0,
      firstName: data["first_name"] || "",
      lastName: data["last_name"] || "",
      email: data["email"] || "",
      joiningAt: data["joining_at"] || "",
      isActive: data["is_active"] || false,
    };
  }
}

/**
 * Class for parsing organization response data.
 */
class OrganizationResponse implements IOrganizationResponse {
  id: number = 0;
  owner: ISwitchKeysMemberResponse = new SwitchKeysMemberResponse();
  name: string = "";
  members: ISwitchKeysMemberResponse[] = [];
  created: string = "";
  modified: string = "";

  /**
   * Initializes default organization response data.
   */
  constructor() {}

  /**
   * Initializes default organization response data.
   * @returns Default organization response data.
   */
  init(): IOrganizationResponse {
    return {
      id: 0,
      created: "",
      modified: "",
      members: [],
      name: "",
      owner: {
        id: 0,
        email: "",
        firstName: "",
        lastName: "",
        joiningAt: "",
        isActive: false,
      },
    };
  }

  /**
   * Parses raw data into organization response data.
   * @param data Raw data to parse.
   * @returns Parsed organization response data.
   */
  parse(data: any): IOrganizationResponse {
    return {
      id: data["id"] || 0,
      created: data["created"] || "",
      modified: data["modified"] || "",
      name: data["name"] || "",
      owner: new SwitchKeysMemberResponse().parse(data["owner"]),
      members: (data["members"] || []).map((memberData: any) =>
        new SwitchKeysMemberResponse().parse(memberData)
      ),
    };
  }
}

/**
 * Class for parsing project response data.
 */
class ProjectResponse implements IProjectResponse {
  id: number = 0;
  name: string = "";
  organization: IOrganizationResponse = new OrganizationResponse();
  organizationId: number = 0;
  environments: IDefaultEnvironmentsResponse = {
    development: { name: "", environmentKey: "" },
    staging: { name: "", environmentKey: "" },
    production: { name: "", environmentKey: "" },
  };
  created: string = "";
  modified: string = "";

  /**
   * Initializes default project response data.
   */
  constructor() {}

  /**
   * Initializes default project response data.
   * @returns Default project response data.
   */
  init(): IProjectResponse {
    return {
      id: 0,
      created: "",
      modified: "",
      name: "",
      environments: {
        development: { name: "", environmentKey: "" },
        staging: { name: "", environmentKey: "" },
        production: { name: "", environmentKey: "" },
      },
      organizationId: 0,
      organization: new OrganizationResponse().init(),
    };
  }

  /**
   * Parses raw data into project response data.
   * @param data Raw data to parse.
   * @returns Parsed project response data.
   */
  parse(data: any): IProjectResponse {
    return {
      id: data["id"] || 0,
      name: data["name"] || "",
      created: data["created"] || "",
      modified: data["modified"] || "",
      organizationId: data["organization_id"] || 0,
      organization: new OrganizationResponse().parse(data["organization"]),
      environments: {
        development: {
          name: data?.environments?.development?.name || "",
          environmentKey:
            data?.environments?.development?.environment_key || "",
        },
        staging: {
          name: data?.environments?.staging?.name || "",
          environmentKey: data?.environments?.staging?.environment_key || "",
        },
        production: {
          name: data?.environments?.production?.name || "",
          environmentKey: data?.environments?.production?.environment_key || "",
        },
      },
    };
  }

  /**
   * Parses raw data into projects response data.
   * @param data Raw data to parse.
   * @returns Parsed projects response data.
   */
  parseAll(data: any): IProjectResponse[] {
    return Array.isArray(data)
      ? data.map((projectData: any) => this.parse(projectData))
      : [];
  }
}

/**
 * Class for parsing environment response data.
 */
class EnvironmentResponse implements IEnvironmentResponse {
  id: number = 0;
  name: string = "";
  created: string = "";
  modified: string = "";
  projectId: number = 0;
  project: IProjectResponse = new ProjectResponse();
  environmentKey: string = "";
  users: IEnvironmentUserResponse[] = [];
  features: IEnvironmentFeaturesResponse[] = [];

  /**
   * Initializes default environment response data.
   */
  constructor() {}

  /**
   * Initializes default environment response data.
   * @returns Default environment response data.
   */
  init(): IEnvironmentResponse {
    return {
      id: 0,
      name: "",
      created: "",
      modified: "",
      projectId: 0,
      project: new ProjectResponse().init(),
      environmentKey: "",
      users: [],
      features: [],
    };
  }

  /**
   * Parses raw data into environment response data.
   * @param data Raw data to parse.
   * @returns Parsed environment response data.
   */
  parse(data: any): IEnvironmentResponse {
    return {
      id: data["id"] || 0,
      name: data["name"] || "",
      created: data["created"] || "",
      modified: data["modified"] || "",
      projectId: data["project_id"] || 0,
      project: new ProjectResponse().parse(data["project"]),
      environmentKey: data["environment_key"] || "",
      users: (data["users"] || []).map((userData: any) => ({
        id: userData["id"] || 0,
        username: userData["username"] || "",
        device: {
          deviceType: userData["device"]?.deviceType || "",
          version: userData["device"]?.version || "",
        },
        features: userData["features"] || [],
      })),
      features: data['features'] || []
    };
  }
}

export {
  SwitchKeysMemberResponse,
  OrganizationResponse,
  ProjectResponse,
  EnvironmentResponse,
};
