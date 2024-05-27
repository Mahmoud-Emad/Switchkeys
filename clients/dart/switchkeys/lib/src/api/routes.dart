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
  environmentUserAddFeature,

  // Projects
  projects,
  projectsId,

  // Groups
  groups,
  groupsId,
}

abstract class SwitchKeysRoutes {
  static final env = DotEnv()..load();
  static final String baseUrl =
      env['BASE_URL'] ?? "https://switchkeysbknd.gent02.dev.grid.tf/";

  static String getRoute(EndPoints endpoint, [List<String>? args]) {
    switch (endpoint) {
      // Auth, Users.
      case EndPoints.signUp:
        return "${baseUrl}/api/auth/signup/";
      case EndPoints.login:
        return "${baseUrl}/api/auth/login/";
      case EndPoints.users:
        return "${baseUrl}/api/auth/users/";
      case EndPoints.changePassword:
        return "${baseUrl}/api/auth/change-password/";
      case EndPoints.refreshToken:
        return "${baseUrl}/api/auth/token/refresh/";
      case EndPoints.usersId:
        return "${baseUrl}/api/users/${args![0]}/";

      // Organizations
      case EndPoints.organizations:
        return "${baseUrl}/api/organizations/";
      case EndPoints.organizationsId:
        return "${baseUrl}/api/organizations/${args![0]}/";
      case EndPoints.organizationsIdAddMember:
        return "${baseUrl}/api/organizations/${args![0]}/add-member/";
      case EndPoints.organizationsIdRemoveMember:
        return "${baseUrl}/api/organizations/${args![0]}/remove-member/";
      case EndPoints.organizationsName:
        return "${baseUrl}/api/organizations/name/${args![0]}/";
      case EndPoints.organizationsIdAllProjects:
        return "${baseUrl}/api/organizations/${args![0]}/projects/";

      // Environments
      case EndPoints.environments:
        return "${baseUrl}/api/environments/";
      case EndPoints.environmentsKey:
        return "${baseUrl}/api/environments/key/${args![0]}/";
      case EndPoints.environmentsKeyAddUser:
        return "${baseUrl}/api/environments/key/${args![0]}/add-user/";
      case EndPoints.environmentsKeyRemoveUser:
        return "${baseUrl}/api/environments/key/${args![0]}/remove-user/";
      case EndPoints.environmentsId:
        return "${baseUrl}/api/environments/${args![0]}/";
      case EndPoints.environmentAddFeature:
        return "${baseUrl}/api/environments/key/${args![0]}/features/";
      case EndPoints.environmentUpdateFeature:
        return "${baseUrl}/api/environments/key/${args![0]}/features/update/${args[1]}/";
      case EndPoints.environmentDeleteFeature:
        return "${baseUrl}/api/environments/key/${args![0]}/features/delete/${args[1]}/";
      case EndPoints.environmentUserAddFeature:
        return "${baseUrl}/api/environments/key/${args![0]}/users/${args[1]}/features/set/";

      // Projects
      case EndPoints.projects:
        return "${baseUrl}/api/projects/";
      case EndPoints.projectsId:
        return "${baseUrl}/api/projects/${args![0]}/";

      // Groups
      case EndPoints.groups:
        return "${baseUrl}/api/groups/";
      case EndPoints.groupsId:
        return "${baseUrl}/api/groups/${args![0]}/";

      default:
        throw ArgumentError("Invalid endpoint: $endpoint");
    }
  }
}
