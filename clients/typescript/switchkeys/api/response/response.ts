import { UUID } from "crypto";
import { DeviceTypeSelection } from "../../utils/types";
import {
  ISwitchKeysDefaultEnvironmentsResponse,
  ISwitchKeysEnvironmentFeaturesResponse,
  ISwitchKeysEnvironmentResponse,
  ISwitchKeysEnvironmentUserResponse,
  ISwitchKeysMemberResponse,
  ISwitchKeysOrganizationResponse,
  ISwitchKeysProjectResponse,
  ISwitchKeysUserDeviceType,
} from "./types";

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
    };
  }
}

/**
 * Class for parsing organization response data.
 */
class OrganizationResponse implements ISwitchKeysOrganizationResponse {
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
  init(): ISwitchKeysOrganizationResponse {
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
      },
    };
  }

  /**
   * Parses raw data into organization response data.
   * @param data Raw data to parse.
   * @returns Parsed organization response data.
   */
  parse(data: any): ISwitchKeysOrganizationResponse {
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
class ProjectResponse implements ISwitchKeysProjectResponse {
  id: number = 0;
  name: string = "";
  organization: ISwitchKeysOrganizationResponse = new OrganizationResponse();
  organizationId: number = 0;
  environments: ISwitchKeysDefaultEnvironmentsResponse = {
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
  init(): ISwitchKeysProjectResponse {
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
  parse(data: any): ISwitchKeysProjectResponse {
    const development = data?.environments.filter(
      (e: { name: string; environment_key: UUID }) => e.name === "development"
    )[0];
    const staging = data?.environments.filter(
      (e: { name: string; environment_key: UUID }) => e.name === "staging"
    )[0];
    const production = data?.environments.filter(
      (e: { name: string; environment_key: UUID }) => e.name === "production"
    )[0];
    const environments: ISwitchKeysDefaultEnvironmentsResponse = {
      development: {
        environmentKey: development.environment_key,
        name: development.name,
      },
      production: {
        environmentKey: production.environment_key,
        name: production.name,
      },
      staging: {
        environmentKey: staging.environment_key,
        name: staging.name,
      },
    };

    return {
      id: data["id"] || 0,
      name: data["name"] || "",
      created: data["created"] || "",
      modified: data["modified"] || "",
      organizationId: data["organization_id"] || 0,
      organization: new OrganizationResponse().parse(data["organization"]),
      environments: environments,
    };
  }

  /**
   * Parses raw data into projects response data.
   * @param data Raw data to parse.
   * @returns Parsed projects response data.
   */
  parseAll(data: any): ISwitchKeysProjectResponse[] {
    return Array.isArray(data)
      ? data.map((projectData: any) => this.parse(projectData))
      : [];
  }
}

/**
 * Class for parsing environment response data.
 */
class EnvironmentResponse implements ISwitchKeysEnvironmentResponse {
  id: number = 0;
  name: string = "";
  created: string = "";
  modified: string = "";
  projectId: number = 0;
  project: ISwitchKeysProjectResponse = new ProjectResponse();
  environmentKey: string = "";
  users: ISwitchKeysEnvironmentUserResponse[] = [];
  features: ISwitchKeysEnvironmentFeaturesResponse[] = [];

  /**
   * Initializes default environment response data.
   */
  constructor() {}

  /**
   * Initializes default environment response data.
   * @returns Default environment response data.
   */
  init(): ISwitchKeysEnvironmentResponse {
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
  parse(data: any): ISwitchKeysEnvironmentResponse {
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
      features: data["features"] || [],
    };
  }
}

/**
 * Class for parsing environment feature response data.
 */
class EnvironmentFeaturesResponse
  implements ISwitchKeysEnvironmentFeaturesResponse
{
  id: number = 0;
  name: string = "";
  value: string = "";
  initialValue: string = "";
  created: string = "";
  modified: string = "";

  constructor() {}

  /**
   * Initializes default environment feature response data.
   * @returns Default environment feature response data.
   */
  init(): ISwitchKeysEnvironmentFeaturesResponse {
    return {
      id: 0,
      created: "",
      modified: "",
      name: "",
      value: "",
      initialValue: "",
    };
  }

  /**
   * Parses raw data into environment feature response data.
   * @param data Raw data to parse.
   * @returns Parsed environment feature response data.
   */
  parse(data: any): ISwitchKeysEnvironmentFeaturesResponse {
    return {
      id: data["id"] || 0,
      created: data["created"] || "",
      modified: data["modified"] || "",
      name: data["name"] || "",
      value: data["value"] || "",
      initialValue: data["initial_value"] || "",
    };
  }
}

/**
 * Class for parsing environment user response data.
 */
class EnvironmentUserResponse implements ISwitchKeysEnvironmentUserResponse {
  id: number = 0;
  username: string = "";
  device: ISwitchKeysUserDeviceType = {
    deviceType: DeviceTypeSelection.ANDROID,
    version: "",
  };
  features: ISwitchKeysEnvironmentFeaturesResponse[] = [];

  /**
   * Initializes default environment user response data.
   */
  constructor() {}

  /**
   * Initializes default environment user response data.
   * @returns Default environment user response data.
   */
  init(): ISwitchKeysEnvironmentUserResponse {
    return {
      id: 0,
      username: "",
      device: {
        deviceType: DeviceTypeSelection.ANDROID,
        version: "",
      },
      features: [],
    };
  }

  /**
   * Parses raw data into environment user response data.
   * @param data Raw data to parse.
   * @returns Parsed environment user response data.
   */
  parse(data: any): ISwitchKeysEnvironmentUserResponse {
    return {
      id: data["id"] || 0,
      username: data["username"] || "",
      features: data["features"] || [],
      device: {
        version: data["device"]["version"],
        deviceType: data["device"]["device_type"],
      },
    };
  }
}

export {
  OrganizationResponse,
  SwitchKeysMemberResponse,
  ProjectResponse,
  EnvironmentResponse,
  EnvironmentFeaturesResponse,
  EnvironmentUserResponse,
};
