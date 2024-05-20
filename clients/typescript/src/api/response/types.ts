// ----------------------------------------------------------------------------------------------------------------------------------------------------------
//
// [DEVELOPERS] Attention please: Before adding any new type here, You need to know that this file should only contain the (HTTP response) types/interfaces.
//
// ----------------------------------------------------------------------------------------------------------------------------------------------------------

import { DeviceTypeSelection } from "../../utils/types";

/** Interface representing authentication tokens used in the SwitchKeys system */
interface ISwitchKeysAuthTokensResponse {
  /** Member access token: Used for login */
  accessToken?: string;
  /** Member refresh token: Used for refreshing the access token when expires */
  refreshToken?: string;
}

interface ISwitchKeysMemberResponse {
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
interface ISwitchKeysUserAuthResponse
  extends ISwitchKeysMemberResponse,
    ISwitchKeysAuthTokensResponse {}

/**
 * Interface for SwitchKeys organization info response.
 */
interface ISwitchKeysOrganizationResponse {
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

/** Interface for the environment features or environment user features. */
interface ISwitchKeysEnvironmentFeaturesResponse {
  /** Feature ID */
  id: number;
  /** Feature name */
  name: string;
  /** Feature value */
  value: string;
  /** Feature initial value */
  initialValue: string;
  /** Crated at date time */
  created: string;
  /** Modified at date time */
  modified: string;
}

/** The user device information */
interface ISwitchKeysUserDeviceType {
  version: string;
  deviceType: DeviceTypeSelection;
}

interface ISwitchKeysProjectResponse {
  /** Project ID */
  id: number;
  /** Project name */
  name: string;
  /** The organization details */
  organization: ISwitchKeysOrganizationResponse;
  /** The organization ID */
  organizationId: number;
  /** The environments details */
  environments: ISwitchKeysDefaultEnvironmentsResponse;
  /** Crated at date time */
  created: string;
  /** Modified at date time */
  modified: string;
}

/** Interface for the environment users, features, username, device info and some other fields. */
interface ISwitchKeysEnvironmentUserResponse {
  /** User ID */
  id: number;
  /** The user username */
  username: string;
  /** The user device */
  device: ISwitchKeysUserDeviceType;
  /** The user features */
  features: ISwitchKeysEnvironmentFeaturesResponse[];
}

/** Interface for the whole environment data including the organization, project and users */
interface ISwitchKeysEnvironmentResponse {
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
  project: ISwitchKeysProjectResponse;
  /** Environment Key */
  environmentKey: string;
  /** Environment users */
  users: ISwitchKeysEnvironmentUserResponse[];
  /** Environment features */
  features: ISwitchKeysEnvironmentFeaturesResponse[];
}

/**  The default env response contains only three envs [development, staging, production] each containing only the name and the key. */
interface ISwitchKeysDefaultEnvironmentResponse {
  /** Environment name */
  name: string;
  /** Environment Key */
  environmentKey: string;
}

interface ISwitchKeysDefaultEnvironmentsResponse {
  /** Development environment data | Auto created */
  development: ISwitchKeysDefaultEnvironmentResponse;
  /** Staging environment data | Auto created */
  staging: ISwitchKeysDefaultEnvironmentResponse;
  /** Production environment data | Auto created */
  production: ISwitchKeysDefaultEnvironmentResponse;
}

export {
  ISwitchKeysMemberResponse,
  ISwitchKeysUserDeviceType,
  ISwitchKeysProjectResponse,
  ISwitchKeysUserAuthResponse,
  ISwitchKeysAuthTokensResponse,
  ISwitchKeysEnvironmentResponse,
  ISwitchKeysOrganizationResponse,
  ISwitchKeysEnvironmentUserResponse,
  ISwitchKeysEnvironmentFeaturesResponse,
  ISwitchKeysDefaultEnvironmentsResponse,
};
