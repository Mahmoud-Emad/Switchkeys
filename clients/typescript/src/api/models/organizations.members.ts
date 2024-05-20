import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { SwitchKeysMemberResponse } from "../response/response";
import { ISwitchKeysMemberResponse } from "../response/types";

/**
 * Class responsible for handling member-related operations.
 */
class SwitchKeysOrganizationMember {
  private memberRoutes = SwitchKeysApiRoutes.members;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  /**
   * Retrieves member information by member ID.
   * @param memberId The ID of the member to retrieve.
   * @returns A promise that resolves to the member information.
   */
  async getById(memberId: number): Promise<ISwitchKeysMemberResponse> {
    const url = this.memberRoutes.getById(memberId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleResponse(response);
  }

  /**
   * Retrieves member information by email.
   * @param memberEmail The email of the member to retrieve.
   * @returns A promise that resolves to the member information.
   */
  async getByEmail(memberEmail: string): Promise<ISwitchKeysMemberResponse> {
    const url = this.memberRoutes.getByEmail(memberEmail);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);
    return this.handleResponse(response);
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns The parsed member response.
   */
  private handleResponse(response: any): ISwitchKeysMemberResponse {
    const member = new SwitchKeysMemberResponse();
    return response ? member.parse(response) : member.init();
  }
}

export default SwitchKeysOrganizationMember;
