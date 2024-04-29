enum EndPoints {
  // Endpoints without parameters
  changePassword,
  refreshToken,
  organizations,
  environments,
  projects,
  groups,
  signUp,
  login,
  users,

  // Endpoints with parameters
  // organizations
  organizationsId,
  organizationsIdAddMember,
  organizationsIdRemoveMember,
  organizationsIdAllProjects,
  organizationsName,

  // environments
  environmentsKey,
  environmentsSet,
  environmentsId,
  environmentsKeyAddUser,
  environmentsKeyAddUsers,
  environmentsKeyRemoveUser,
  environmentUserAddFeature,
  environmentUserAddFeatures,
  environmentUserGetFeature,

  projectsId,
  groupsId,
  usersId,
}

class SwitchKeysRoutes {
  static const String baseUrl = "http://127.0.0.1:8000/api/";

  static String getRoute(EndPoints endpoint, [List<String>? args]) {
    switch (endpoint) {
      case EndPoints.changePassword:
        return "${baseUrl}auth/change-password/";
      case EndPoints.refreshToken:
        return "${baseUrl}auth/token/refresh/";
      case EndPoints.organizations:
        return "${baseUrl}organizations/";
      case EndPoints.environments:
        return "${baseUrl}environments/";
      case EndPoints.projects:
        return "${baseUrl}projects/";
      case EndPoints.groups:
        return "${baseUrl}groups/";
      case EndPoints.signUp:
        return "${baseUrl}auth/signup/";
      case EndPoints.login:
        return "${baseUrl}auth/login/";
      case EndPoints.users:
        return "${baseUrl}auth/users/";
      case EndPoints.organizationsId:
        return "${baseUrl}organizations/${args![0]}/";
      case EndPoints.organizationsIdAddMember:
        return "${baseUrl}organizations/${args![0]}/add-member/";
      case EndPoints.organizationsIdRemoveMember:
        return "${baseUrl}organizations/${args![0]}/remove-member/";
      case EndPoints.organizationsIdAllProjects:
        return "${baseUrl}organizations/${args![0]}/projects/";
      case EndPoints.organizationsName:
        return "${baseUrl}organizations/name/${args![0]}/";
      case EndPoints.environmentsKey:
        return "${baseUrl}environments/key/${args![0]}/";
      case EndPoints.environmentsKeyAddUser:
        return "${baseUrl}environments/key/${args![0]}/add-user/";
      case EndPoints.environmentsKeyAddUsers:
        return "${baseUrl}environments/key/${args![0]}/add-users/";
      case EndPoints.environmentsKeyRemoveUser:
        return "${baseUrl}environments/key/${args![0]}/remove-user/";
      case EndPoints.environmentUserAddFeature:
        return "${baseUrl}environments/key/${args![0]}/user/add-feature/";
      case EndPoints.environmentUserAddFeatures:
        return "${baseUrl}environments/key/${args![0]}/user/add-features/";
      case EndPoints.environmentUserGetFeature:
        return "${baseUrl}environments/key/${args![0]}/user/get-feature/?feature_name=${args[1]}&username=${args[2]}"; // index 1 = feature name, index 2 = username.
      case EndPoints.environmentsSet:
        return "${baseUrl}environments/key/${args![0]}/user/set/?user_id=${args[1]}";
      case EndPoints.environmentsId:
        return "${baseUrl}environments/${args![0]}/";
      case EndPoints.projectsId:
        return "${baseUrl}projects/${args![0]}/";
      case EndPoints.groupsId:
        return "${baseUrl}groups/${args![0]}/";
      case EndPoints.usersId:
        return "${baseUrl}users/${args![0]}/";
      default:
        throw ArgumentError("Invalid endpoint: $endpoint");
    }
  }
}
