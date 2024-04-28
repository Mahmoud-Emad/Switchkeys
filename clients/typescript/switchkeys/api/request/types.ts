import { SwitchKeysUserType } from "../../utils/types";

/**
 * Interface for the data required to register a new member.
 */
interface ISwitchKeysAuthRegisterData {
  /**
   * Member's email address.
   */
  email: string;
  
  /**
   * Member's password.
   */
  password: string;
  
  /**
   * Member's first name.
   */
  firstName: string;
  
  /**
   * Member's last name.
   */
  lastName: string;
  
  /**
   * Member's type (optional). Defaults to 'member' if not provided.
   */
  memberType?: SwitchKeysUserType;
}

/**
 * Interface for the data required to log in a member.
 */
interface ISwitchKeysAuthLoginData {
  /**
   * Member's email address.
   */
  email: string;
  
  /**
   * Member's password.
   */
  password: string;
}

interface IUpdateMemberData {
  /**
   * Member's email address.
   */
  email?: string;
  
  /**
   * Member's password.
   */
  password?: string;
  
  /**
   * Member's first name.
   */
  firstName?: string;
  
  /**
   * Member's last name.
   */
  lastName?: string;
  
  /**
   * Member's type (optional). Defaults to 'member' if not provided.
   */
  memberType?: SwitchKeysUserType;
}

export {
  ISwitchKeysAuthRegisterData,
  ISwitchKeysAuthLoginData,
  IUpdateMemberData
};
