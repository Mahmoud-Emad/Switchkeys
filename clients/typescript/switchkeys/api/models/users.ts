import SwitchKeysConfig from "../../utils/config";
import { SwitchKeysLogger } from "../../utils/logger";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { ISwitchKeysUserInfoResponse } from "../response/types";

/**
 * Class responsible for handling user-related operations.
 */
class SwitchKeysUsers {
  private config = new SwitchKeysConfig();
  private userRoutes = SwitchKeysApiRoutes.users;
  private request: SwitchKeysRequest = new SwitchKeysRequest();
  private logger: SwitchKeysLogger = new SwitchKeysLogger();

  /**
   * Retrieves user information by ID.
   * @param userId The ID of the user to retrieve.
   * @returns A promise that resolves to the user information.
   */
  async getByID(userId: number): Promise<ISwitchKeysUserInfoResponse> {
    const url = this.userRoutes.getByID(userId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);

    const user = new SwitchKeysUserResponse();
    let userData: ISwitchKeysUserInfoResponse = user.init();

    if (response) {
      userData = user.parse(response);
    }

    return userData;
  }

  async getByEmail(email: string): Promise<ISwitchKeysUserInfoResponse> {
    const url = this.userRoutes.getByEmail(email);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);

    const user = new SwitchKeysUserResponse();
    let userData: ISwitchKeysUserInfoResponse = user.init();

    if (response) {
      userData = user.parse(response);
    }

    return userData;
  }

  async create() {}
  async update() {}
  async delete() {}
}

/**
 * Class representing user response data.
 */
class SwitchKeysUserResponse implements ISwitchKeysUserInfoResponse {
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  joiningAt: string;
  isActive?: boolean | undefined;

  /**
   * Initializes default user response data.
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
   * Initializes default user response data.
   * @returns Default user response data.
   */
  init(): ISwitchKeysUserInfoResponse {
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
   * Parses raw data into user response data.
   * @param data Raw data to parse.
   * @returns Parsed user response data.
   */
  parse(data: any): ISwitchKeysUserInfoResponse {
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

export default SwitchKeysUsers;
