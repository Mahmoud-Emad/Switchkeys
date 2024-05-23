import 'package:dotenv/dotenv.dart';

enum EndPoints {
  // Endpoints without parameters
  signUp,
  login,
  changePassword,
  refreshToken,
  users,
  usersId,

  // organizations
  organizations,
  organizationsId,
  organizationsIdAddMember,
  organizationsIdRemoveMember,
  organizationsName,
  organizationsIdAllProjects,

  // environments
  environments,
  environmentsKey,
  environmentsId,
  environmentsKeyAddUser,
  environmentsKeyRemoveUser,
  environmentAddFeature,
  environmentUpdateFeature,
  environmentDeleteFeature,

  // Projects
  projects,
  projectsId,

  // Groups
  groups,
  groupsId,
}

abstract class SwitchKeysRoutes {
  static final env = DotEnv()..load();
  static final String baseUrl = env['BASE_URL'] ?? "";

  static String getRoute(EndPoints endpoint, [List<String>? args]) {
    switch (endpoint) {
      // Auth, Users.
      case EndPoints.signUp:
        return "${baseUrl}auth/signup/";
      case EndPoints.login:
        return "${baseUrl}auth/login/";
      case EndPoints.users:
        return "${baseUrl}auth/users/";
      case EndPoints.changePassword:
        return "${baseUrl}auth/change-password/";
      case EndPoints.refreshToken:
        return "${baseUrl}auth/token/refresh/";
      case EndPoints.usersId:
        return "${baseUrl}users/${args![0]}/";

      // Organizations
      case EndPoints.organizations:
        return "${baseUrl}organizations/";
      case EndPoints.organizationsId:
        return "${baseUrl}organizations/${args![0]}/";
      case EndPoints.organizationsIdAddMember:
        return "${baseUrl}organizations/${args![0]}/add-member/";
      case EndPoints.organizationsIdRemoveMember:
        return "${baseUrl}organizations/${args![0]}/remove-member/";
      case EndPoints.organizationsName:
        return "${baseUrl}organizations/name/${args![0]}/";
      case EndPoints.organizationsIdAllProjects:
        return "${baseUrl}organizations/${args![0]}/projects/";

      // Environments
      case EndPoints.environments:
        return "${baseUrl}environments/";
      case EndPoints.environmentsKey:
        return "${baseUrl}environments/key/${args![0]}/";
      case EndPoints.environmentsKeyAddUser:
        return "${baseUrl}environments/key/${args![0]}/add-user/";
      case EndPoints.environmentsKeyRemoveUser:
        return "${baseUrl}environments/key/${args![0]}/remove-user/";
      case EndPoints.environmentsId:
        return "${baseUrl}environments/${args![0]}/";
      case EndPoints.environmentAddFeature:
        return "${baseUrl}environments/${args![0]}/features/";
      case EndPoints.environmentUpdateFeature:
        return "${baseUrl}environments/${args![0]}/features/update/${args[1]}/";
      case EndPoints.environmentDeleteFeature:
        return "${baseUrl}environments/${args![0]}/features/delete/${args[1]}/";

      // Projects
      case EndPoints.projects:
        return "${baseUrl}projects/";
      case EndPoints.projectsId:
        return "${baseUrl}projects/${args![0]}/";

      // Groups
      case EndPoints.groups:
        return "${baseUrl}groups/";
      case EndPoints.groupsId:
        return "${baseUrl}groups/${args![0]}/";

      default:
        throw ArgumentError("Invalid endpoint: $endpoint");
    }
  }
}
