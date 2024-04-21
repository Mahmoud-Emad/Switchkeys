// This file containes all response parser classes

import { IOrganizationResponse, ISwitchKeysMemberResponse } from "../../utils/types";


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
  parse(data: any): IOrganizationResponse{
    const member = new SwitchKeysMemberResponse();
    return {
      id: data['id'],
      created: data['created'],
      modified: data['modified'],
      members: data['members'],
      name: data['name'],
      owner: member.parse(data['owner'])
    };
  }
}

export {
  SwitchKeysMemberResponse,
  OrganizationResponse
}