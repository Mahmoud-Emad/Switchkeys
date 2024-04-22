/** Enum representing different user types in the SwitchKeys system */
export enum SwitchKeysUserType {
  /** Regular user type */
  User = "user",
  /** Administrator user type */
  Administrator = "administrator",
}

/** Interface representing authentication tokens used in the SwitchKeys system */
export interface ISwitchKeysAuthTokens {
  /** Member access token: Used for login */
  accessToken?: string;
  /** Member refresh token: Used for refreshing the access token when expires */
  refreshToken?: string;
}

export interface IMemberResponse {
  /** Member ID */
  id: number;
  /** Member first name */
  firstName: string;
  /** Member last name */
  lastName: string;
  /** Member email */
  email: string;
  /** Member joining at */
  joiningAt: string;
}

/**
 * Interface for SwitchKeys authentication register response.
 */
export interface IUserAuthResponse extends IMemberResponse, ISwitchKeysAuthTokens {}

/**
 * Interface for SwitchKeys user info response.
 */
export interface ISwitchKeysMemberResponse extends IMemberResponse {
  isActive?: boolean;
}

/**
 * Interface for SwitchKeys organization info response.
 */
export interface IOrganizationResponse {
  /** Organization ID */
  id: number;
  /** The creator of the organization*/
  owner: ISwitchKeysMemberResponse;
  /** Organization name */
  name: string;
  /** List of members IDs */
  members: ISwitchKeysMemberResponse[];
  /** Crated at date time */
  created: string;
  /** Modified at date time */
  modified: string;
}

/**
 * Interface for SwitchKeys organization request data.
 */
export interface IOrganizationRequest {
  /** Organization name */
  name: string;
}

/**
 * Interface for SwitchKeys organization add memeber request data.
 */
export interface IOrganizationMemberRequest {
  /** Member ID */
  memberId: number; 
}