import { SwitchKeysUserType } from "../../utils/types";

/**
 * Interface for the data required to register a new user.
 */
interface SwitchKeysAuthRegisterData {
  /**
   * User's email address.
   */
  email: string;
  
  /**
   * User's password.
   */
  password: string;
  
  /**
   * User's first name.
   */
  firstName: string;
  
  /**
   * User's last name.
   */
  lastName: string;
  
  /**
   * User's type (optional). Defaults to 'user' if not provided.
   */
  userType?: SwitchKeysUserType;
}

/**
 * Interface for the data required to log in a user.
 */
interface SwitchKeysAuthLoginData {
  /**
   * User's email address.
   */
  email: string;
  
  /**
   * User's password.
   */
  password: string;
}

export {
  SwitchKeysAuthRegisterData,
  SwitchKeysAuthLoginData,
};
