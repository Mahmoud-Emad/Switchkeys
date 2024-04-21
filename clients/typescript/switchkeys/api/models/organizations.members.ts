import { ISwitchKeysMemberResponse } from "../../utils/types";
import { SwitchKeysRequest, SwitchKeysRequestMethod } from "../request/request";
import { SwitchKeysApiRoutes } from "../request/routes";
import { SwitchKeysMemberResponse } from "../response/response";

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
  async getByID(memberId: number): Promise<ISwitchKeysMemberResponse> {
    const url = this.memberRoutes.getByID(memberId);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);

    const member = new SwitchKeysMemberResponse();
    let memberData: ISwitchKeysMemberResponse = member.init();

    if (response) {
      memberData = member.parse(response);
    }

    return memberData;
  }

  /**
   * Retrieves member information by email.
   * @param memberEmail The email of the member to retrieve.
   * @returns A promise that resolves to the member information.
   */
  async getByEmail(memberEmail: string): Promise<ISwitchKeysMemberResponse> {
    const url = this.memberRoutes.getByEmail(memberEmail);
    const response = await this.request.call(url, SwitchKeysRequestMethod.GET);

    const member = new SwitchKeysMemberResponse();
    let memberData: ISwitchKeysMemberResponse = member.init();

    if (response) {
      memberData = member.parse(response);
    }

    return memberData;
  }

  /**
   * Updates member information by member ID.
   * @param memberId The ID of the member to update.
   * @returns A promise that resolves to the member information.
   */
  // async update(memberId: number, data: IUpdateMemberData): Promise<ISwitchKeysMemberResponse> {
  //   const url = this.memberRoutes.getByID(memberId);
  //   const response = await this.request.call(url, SwitchKeysRequestMethod.PUT, data);

  //   const member = new SwitchKeysUserResponse();
  //   let memberData: ISwitchKeysMemberResponse = member.init();

  //   if (response) {
  //     memberData = member.parse(response);
  //   }

  //   return memberData;
  // }

  // async delete() {}
}

export default SwitchKeysOrganizationMember;
