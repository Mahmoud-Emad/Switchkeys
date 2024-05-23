// --------------------------------------------------------------------------------------------------------------------------------------------------------
//
// [DEVELOPERS] Attention please: Before adding any new type here, You need to know that this file should only contain the (HTTP request) types/interfaces.
//
// --------------------------------------------------------------------------------------------------------------------------------------------------------

import { SwitchKeysUserType } from "../../utils/types";
import { ISwitchKeysUserDeviceType } from "../response/types";

/**
 * Interface for the data required to register a new member.
 */
interface ISwitchKeysAuthRegisterData {
  /** Member's email address. */
  email: string;

  /** Member's password. */
  password: string;

  /** Member's first name. */
  firstName: string;

  /** Member's last name. */
  lastName: string;

  /** Member's type (optional). Defaults to 'member' if not provided. */
  memberType?: SwitchKeysUserType;
}

/**
 * Interface for the data required to get a user by email.
 */
interface ISwitchKeysGetUserByEmail {
  /** User email address. */
  email: string;
}

/**
 * Interface for the data required to log in a member.
 */
interface ISwitchKeysAuthLoginData {
  /** Member's email address. */
  email: string;

  /** Member's password. */
  password: string;
}

interface ISwitchKeysUpdateMemberData {
  /** Member's email address. */
  email?: string;

  /** Member's password. */
  password?: string;

  /** Member's first name. */
  firstName?: string;

  /** Member's last name. */
  lastName?: string;

  /** Member's type (optional). Defaults to 'member' if not provided. */
  memberType?: SwitchKeysUserType;
}

/**
 * Interface for the data required to set new feature on an environment.
 */
interface ISwitchKeysEnvironmentFeatureData {
  /** Feature name */
  name: string;
  /** Feature value */
  value: string;
}

/**
 * Interface for the data required to update feature on an environment.
 */
interface ISwitchKeysUpdateEnvironmentFeatureData {
  /** Feature name */
  name: string;
  /** Feature new name */
  newName: string;
  /** Feature new value */
  newValue: string;
}

/**
 * Interface for the data required to add a user on an environment.
 */
interface ISwitchKeysAddEnvironmentUserData {
  /** User username*/
  username: string;
  /** User device*/
  device: ISwitchKeysUserDeviceType;
}

/**
 * Interface for project request data.
 */
interface ISwitchKeysProjectData {
  /** Project name*/
  name: string;
}

/**
 * Interface for SwitchKeys organization request data.
 */
interface ISwitchKeysOrganizationData {
  /** Organization name */
  name: string;
}

/**
 * Interface for SwitchKeys organization add memeber request data.
 */
interface ISwitchKeysOrganizationMemberData {
  /** Member ID */
  memberId: number;
}

export {
  ISwitchKeysAuthRegisterData,
  ISwitchKeysGetUserByEmail,
  ISwitchKeysAuthLoginData,
  ISwitchKeysUpdateMemberData,
  ISwitchKeysUpdateEnvironmentFeatureData,
  ISwitchKeysEnvironmentFeatureData,
  ISwitchKeysAddEnvironmentUserData,
  ISwitchKeysProjectData,
  ISwitchKeysOrganizationData,
  ISwitchKeysOrganizationMemberData,
};
