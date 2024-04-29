/** Enum representing different user types in the SwitchKeys system */
export enum SwitchKeysUserType {
  /** Regular user type */
  User = "user",
  /** Administrator user type */
  Administrator = "administrator",
}

/** Enum representing user device type */
export enum DeviceTypeSelection {
  ANDROID = "Android",
  IPHONE = "IPhone",
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
export interface IUserAuthResponse
  extends IMemberResponse,
    ISwitchKeysAuthTokens {}

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

/** Interface for the environment features or environment user features. */
export interface IEnvironmentFeaturesResponse {
  /** User ID */
  id: number;
  /** Features name */
  name: string;
  /** Features value */
  value: string;
  /** Crated at date time */
  created: string;
  /** Modified at date time */
  modified: string;
}

/** The user device information */
export interface IUserDeviceResponse {
  version: string;
  deviceType: DeviceTypeSelection;
}

/** Interface for the environment users, features, username, device info and some other fields. */
export interface IEnvironmentUserResponse {
  /** User ID */
  id: number;
  /** The user username */
  username: string;
  device: IUserDeviceResponse;
  features: IEnvironmentFeaturesResponse[]
}

/** Interface for the whole environment data including the organization, project and users */
export interface IEnvironmentResponse {
  /** Environment ID */
  id: number;
  /** Environment name */
  name: string;
  /** Project ID */
  projectId: number;
  /** Crated at date time */
  created: string;
  /** Modified at date time */
  modified: string;
  /** project details */
  project: IProjectResponse;
  /** Environment Key */
  environmentKey: string;
  /** Environment users */
  users: IEnvironmentUserResponse[];
  /** Environment features */
  features: IEnvironmentFeaturesResponse[]
}

/**  The default env response contains only three envs [development, staging, production] each containing only the name and the key. */
export interface IDefaultEnvironmentResponse {
  /** Environment name */
  name: string;
  /** Environment Key */
  environmentKey: string;
}

export interface IDefaultEnvironmentsResponse {
  /** Development environment data | Auto created */
  development: IDefaultEnvironmentResponse;
  /** Staging environment data | Auto created */
  staging: IDefaultEnvironmentResponse;
  /** Production environment data | Auto created */
  production: IDefaultEnvironmentResponse;
}

export interface IProjectResponse {
  /** Project ID */
  id: number;
  /** Project name */
  name: string;
  /** The organization details */
  organization: IOrganizationResponse;
  /** The organization ID */
  organizationId: number;
  /** The environments details */
  environments: IDefaultEnvironmentsResponse;
  /** Crated at date time */
  created: string;
  /** Modified at date time */
  modified: string;
}
