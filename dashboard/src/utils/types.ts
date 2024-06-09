import type { Ref } from "vue";

type Rule = (value: string) => string | boolean;

export type SignUpFormInputs = {
  vModel: Ref<string>;
  type: Ref<string>;
  icon: string;
  label: string;
  rules: Rule[];
};

export interface ISignUpResponse {
  id: number;
  access_token: string;
  refresh_token: string;
  email: string;
  first_name: string;
  last_name: string;
  password: string;
  user_type: string;
  joining_at: string;
}

export type DashboardAppType = {
  title: string;
  icon: string;
  route: string;
  description: string;
  iconColor: string;
}

export interface IOrganization {
  id: number;
  title: string;
  projects: number;
  members: number;
  createdAt: string;
  modifiedAt: string;
}

export interface IProject {
  id: number;
  title: string;
  environments: IProjectDefualtEnvironment[];
  createdAt: string;
  modifiedAt: string;
  organization: IOrganization;
}

export interface IProjectDefualtEnvironment {
  name: string;
  environmentKey: string;
  chipColor: string;
}

export interface IEnvironmentFeature {
  name: string;
  value: string;
}

export interface IEnvironmentUserDevice {
  deviceType: string;
  version: string;
}

export interface IEnvironmentUser {
  username: string;
  device: IEnvironmentUserDevice;
  features: IEnvironmentFeature[];
}

export interface IEnvironment {
  id: number;
  name: string;
  environmentKey: string;
  chipColor?: string;
  createdAt: string;
  modifiedAt: string;
  project: IProject;
  users: IEnvironmentUser[];
  features: IEnvironmentFeature[]
}