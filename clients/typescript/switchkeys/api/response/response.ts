// This file containes all response parser classes

import {
  IDefaultEnvironmentsResponse,
  IOrganizationResponse,
  IProjectResponse,
  ISwitchKeysMemberResponse,
} from "../../utils/types";

/**
 * Class representing member response data.
 */
class SwitchKeysMemberResponse implements ISwitchKeysMemberResponse {
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  joiningAt: string;
  isActive?: boolean | undefined;

  /**
   * Initializes default member response data.
   */
  constructor() {
    const defaultData = this.init();
    this.id = defaultData.id;
    this.email = defaultData.email;
    this.firstName = defaultData.firstName;
    this.lastName = defaultData.lastName;
    this.joiningAt = defaultData.joiningAt;
  }

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
    this.id = data["id"];
    this.firstName = data["first_name"];
    this.lastName = data["last_name"];
    this.joiningAt = data["joining_at"];
    if (data["is_active"]) {
      this.isActive = data["is_active"];
    }

    return {
      id: this.id,
      email: this.email,
      firstName: this.firstName,
      lastName: this.lastName,
      joiningAt: this.joiningAt,
      isActive: this.isActive,
    };
  }
}

/**
 * Class representing organization response data.
 */
class OrganizationResponse implements IOrganizationResponse {
  id: number;
  owner: ISwitchKeysMemberResponse;
  name: string;
  members: ISwitchKeysMemberResponse[];
  created: string;
  modified: string;

  /**
   * Initializes default organization response data.
   */
  constructor() {
    const defaultData = this.init();
    this.id = defaultData.id;
    this.owner = defaultData.owner;
    this.name = defaultData.name;
    this.members = defaultData.members;
    this.created = defaultData.created;
    this.modified = defaultData.modified;
  }

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
        email: "",
        firstName: "",
        lastName: "",
        id: 0,
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
    const member = new SwitchKeysMemberResponse();
    return {
      id: data["id"],
      created: data["created"],
      modified: data["modified"],
      members: data["members"],
      name: data["name"],
      owner: member.parse(data["owner"]),
    };
  }
}

class EnvironmentsResponse {
  init(): IDefaultEnvironmentsResponse {
    return {
      development: {
        name: "",
        environmentKey: "",
      },
      staging: {
        name: "",
        environmentKey: "",
      },
      production: {
        name: "",
        environmentKey: "",
      },
    };
  }

  parse(data: any[]): IDefaultEnvironmentsResponse {
    const parsedData = {
      development: {
        name: data[0]['name'],
        environmentKey: data[0]["environment_key"],
      },
      staging: {
        name: data[1]['name'],
        environmentKey: data[1]["environment_key"],
      },
      production: {
        name: data[2]['name'],
        environmentKey: data[2]["environment_key"],
      },
    };
    return parsedData
  }
}

/**
 * Class representing organization project response data.
 */
class ProjectResponse implements IProjectResponse {
  id: number;
  name: string;
  organization: IOrganizationResponse;
  organizationId: number;
  environments: IDefaultEnvironmentsResponse;
  created: string;
  modified: string;

  /**
   * Initializes default project response data.
   */
  constructor() {
    const defaultData = this.init();
    this.id = defaultData.id;
    this.name = defaultData.name;
    this.organization = defaultData.organization;
    this.organizationId = defaultData.organizationId;
    this.environments = defaultData.environments;
    this.created = defaultData.created;
    this.modified = defaultData.modified;
  }

  /**
   * Initializes default project response data.
   * @returns Default project response data.
   */
  init(): IProjectResponse {
    const organization = new OrganizationResponse();
    const environments = new EnvironmentsResponse();

    return {
      id: 0,
      created: "",
      modified: "",
      name: "",
      environments: environments.init(),
      organizationId: 0,
      organization: organization.init(),
    };
  }

  /**
   * Parses raw data into project response data.
   * @param data Raw data to parse.
   * @returns Parsed project response data.
   */
  parse(data: any): IProjectResponse {
    const organization = new OrganizationResponse();
    const environments = new EnvironmentsResponse();

    return {
      id: data["id"],
      created: data["created"],
      modified: data["modified"],
      name: data["name"],
      organizationId: data["organization_id"],
      organization: organization.parse(data["organization"]),
      environments: environments.parse(data["environments"]),
    };
  }

  /**
   * Parses raw data into projects response data.
   * @param data Raw data to parse.
   * @returns Parsed projects response data.
   */
  parseAll(data: any): IProjectResponse[] {
    const projects: IProjectResponse[] = []

    for(const project of data){
      projects.push(this.parse(project))
    }

    return projects
  }
}

export { SwitchKeysMemberResponse, OrganizationResponse, ProjectResponse };
