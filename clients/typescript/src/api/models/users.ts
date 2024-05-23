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
// Overview of `SwitchKeysUsers`:
// The `SwitchKeysUsers` class is designed to manage a specific user, or even list all of them.
//
// Example Usage:
//
// ```typescript
// await switchkeys.users.getByEmail({
//   email: "email@example.com",
// });
// ```
//
// By default, the `get` method returns an instance of the `SwitchKeysUserServices` class,
// which provides various methods to interact with the user.
//
// Example Usage:
//
// Get the user email:
// ```typescript
// const email = user.email;
// console.log({ email });
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
import { ISwitchKeysGetUserByEmail } from "../request/types";
import { SwitchKeysMemberResponse } from "../response/response";
import { ISwitchKeysMemberResponse } from "../response/types";

/**
 * Class representing operations related to users.
 */
class SwitchKeysUsers {
  private userRoutes = SwitchKeysApiRoutes.users;
  private request: SwitchKeysRequest = new SwitchKeysRequest();

  /**
   * Checks if a user with the specified email is created.
   * @param options - The options containing the user's email.
   * @returns A promise that resolves to true if the user exists, false otherwise.
   */
  async isUserCreated(options: ISwitchKeysGetUserByEmail): Promise<boolean> {
    try {
      await this.getByEmail(options);
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Retrieves a user by their email.
   * @param options - The options containing the user's email.
   * @returns A promise that resolves to an instance of `SwitchKeysUserServices`.
   */
  async getByEmail(options: ISwitchKeysGetUserByEmail): Promise<SwitchKeysUserServices> {
    const url = this.userRoutes.getByEmail(options.email);
    const response = await this.request.call(
      url,
      SwitchKeysRequestMethod.GET,
      options
    );
  
    return this.handleResponse(response);
  }

  /**
   * Parses and handles the response from the API.
   * @param response - The response from the API.
   * @returns An instance of `SwitchKeysUserServices`.
   * @throws SwitchKeysRecordNotFoundError if the user is not found.
   */
  private handleResponse(response: any): SwitchKeysUserServices {
    const userResponse = new SwitchKeysMemberResponse();
    const user = response
      ? userResponse.parse(response)
      : userResponse.init();

    if (!user.id) {
      throw new SwitchKeysRecordNotFoundError("User not found.");
    }

    return new SwitchKeysUserServices(user);
  }
}

/**
 * Class representing services related to a specific user.
 */
class SwitchKeysUserServices {
  user: ISwitchKeysMemberResponse;

  /**
   * Creates an instance of `SwitchKeysUserServices`.
   * @param user - The user response data.
   */
  constructor(user: ISwitchKeysMemberResponse) {
    this.user = user;
  }
}

export default SwitchKeysUsers;
