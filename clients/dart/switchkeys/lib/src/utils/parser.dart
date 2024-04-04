import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/api/response/types.dart';

SwitchKeysAuthResponse parseAuth(Map<String, dynamic> authData) {
  return SwitchKeysAuthResponse(
    id: authData['id'],
    firstName: authData['first_name'],
    lastName: authData['last_name'],
    email: authData['email'],
    password: authData['password'],
    joiningAt: authData['joining_at'],
    userType: authData['user_type'],
    accessToken: authData['access_token'],
    refreshToken: authData['refresh_token'],
  );
}

SwitchKeysOrganizationResponse parseOrganization(
    Map<String, dynamic> organizationData) {
  return SwitchKeysOrganizationResponse(
    id: organizationData['id'],
    name: organizationData['name'],
    owner: parseUser(organizationData['owner']),
    members: parseUsers(organizationData['members']),
    created: organizationData['created'],
    modified: organizationData['modified'],
  );
}

SwitchKeysUserResponse parseUser(Map<String, dynamic> userData) {
  return SwitchKeysUserResponse(
    id: userData['id'],
    backgroundColor: userData['background_color'],
    email: userData['email'],
    firstName: userData['first_name'],
    lastName: userData['last_name'],
    fullName: userData['full_name'],
    isActive: userData['is_active'],
    joiningAt: userData['joining_at'],
  );
}

List<SwitchKeysUserResponse> parseUsers(List<dynamic> usersData) {
  List<SwitchKeysUserResponse> users = [];
  for (var i = 0; i < usersData.length; i++) {
    users.add(SwitchKeysUserResponse(
      id: usersData[i]['id'],
      backgroundColor: usersData[i]['background_color'],
      email: usersData[i]['email'],
      firstName: usersData[i]['first_name'],
      lastName: usersData[i]['last_name'],
      fullName: usersData[i]['full_name'],
      isActive: usersData[i]['is_active'],
      joiningAt: usersData[i]['joining_at'],
    ));
  }

  return users;
}

SwitchKeysProjectResponse parseProject(Map<String, dynamic> projectData) {
  return SwitchKeysProjectResponse(
    id: projectData['id'],
    name: projectData['name'],
    organization: parseOrganization(projectData['organization']),
    created: projectData['created'],
    modified: projectData['modified'],
  );
}

List<SwitchKeysProjectResponse> parseProjects(
  List<dynamic> projectsData,
) {
  List<SwitchKeysProjectResponse> projects = [];
  for (var i = 0; i < projectsData.length; i++) {
    projects.add(SwitchKeysProjectResponse(
      created: projectsData[i]['created'],
      modified: projectsData[i]['modified'],
      id: projectsData[i]['id'],
      name: projectsData[i]['name'],
    ));
  }

  return projects;
}

SwitchKeysEnvironmentResponse parseEnvironment(
  Map<String, dynamic> environmentData,
) {
  return SwitchKeysEnvironmentResponse(
    id: environmentData['id'],
    name: environmentData['name'],
    environmentKey: environmentData['environment_key'],
    project: parseProject(environmentData['project']),
    users: parseEnvironmentUsers(environmentData['users']),
    created: environmentData['created'],
    modified: environmentData['modified'],
  );
}

SwitchKeyDevice parseDevice(
  Map<String, dynamic> deviceData,
) {
  return SwitchKeyDevice(
    deviceType: deviceData['device_type'] == 'IPhone'
        ? SwitchKeyDeviceType.IPhone
        : SwitchKeyDeviceType.Android,
    version: deviceData['version'],
  );
}

List<SwitchKeyUserEnvironmentFeatures> parseFeatures(
  List<dynamic> featuresData,
) {
  List<SwitchKeyUserEnvironmentFeatures> features = [];

  for (var i = 0; i < featuresData.length; i++) {
    features.add(
      SwitchKeyUserEnvironmentFeatures(
        isEnabled: featuresData[i]['is_enabled'],
        name: featuresData[i]['name'],
        value: featuresData[i]['value'],
      ),
    );
  }
  return features;
}

SwitchKeysEnvironmentsUserResponse parseEnvironmentUser(
  Map<String, dynamic> userData,
) {
  return SwitchKeysEnvironmentsUserResponse(
    id: userData['id'],
    username: userData['username'],
    device: parseDevice(userData['device']),
    features: parseFeatures(userData['features']),
  );
}

List<SwitchKeysEnvironmentsUserResponse> parseEnvironmentUsers(
  List<dynamic> usersData,
) {
  List<SwitchKeysEnvironmentsUserResponse> users = [];

  for (var i = 0; i < usersData.length; i++) {
    users.add(
      SwitchKeysEnvironmentsUserResponse(
        id: usersData[i]['id'],
        username: usersData[i]['username'],
        device: parseDevice(usersData[i]['device']),
        features: parseFeatures(usersData[i]['features']),
      ),
    );
  }
  return users;
}
