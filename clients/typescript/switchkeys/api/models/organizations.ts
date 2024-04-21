import {
  IOrganizationRequest,
  IOrganizationResponse,
} from "../../utils/types";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { OrganizationResponse } from "../response/response";
import SwitchKeysOrganizationMember from "./organizations.members";
import SwitchKeysProject from "./organizations.projects";

class SwitchKeysOrganizations {
  /** Instance of `SwitchKeysOrganizationMember` for managing `member-related` operations. */
  private organizationRoutes = SwitchKeysApiRoutes.organizations;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  members: SwitchKeysOrganizationMember = new SwitchKeysOrganizationMember();
  projects: SwitchKeysProject = new SwitchKeysProject();

  async create(data: IOrganizationRequest): Promise<IOrganizationResponse> {
    const url = this.organizationRoutes.create;
    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.POST,
      data
    );

    const organizationResponse = new OrganizationResponse();
    let orgData: IOrganizationResponse = organizationResponse.init();

    if (response) {
      orgData = organizationResponse.parse(response);
    }

    return orgData;
  }

  async getById() {}
  async update() {}
  async delete() {}
}

export default SwitchKeysOrganizations;
