import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/api/response/types.dart';

SwitchKeysAuthResponse parseAuth(Map<String, dynamic> authData) {
  return SwitchKeysAuthResponse(
    id: authData['id'] ?? 0,
    firstName: authData['first_name'] ?? "",
    lastName: authData['last_name'] ?? "",
    email: authData['email'] ?? "",
    password: authData['password'] ?? "",
    joiningAt: authData['joining_at'] ?? "",
    memberType: authData['user_type'] ?? "",
    accessToken: authData['access_token'] ?? "",
    refreshToken: authData['refresh_token'] ?? "",
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
    firstName: userData['first_name'],
    lastName: userData['last_name'],
    fullName: userData['full_name'],
    email: userData['email'],
    joiningAt: userData['joining_at'],
    backgroundColor: userData['background_color'],
    isActive: userData['is_active'],
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
    created: projectData['created'],
    modified: projectData['modified'],
    organization: parseOrganization(projectData['organization']),
    environments: parseProjectDefaultEnvironment(projectData['environments']),
  );
}

List<SwitchKeysProjectResponse> parseProjects(
  List<dynamic> projectsData,
) {
  List<SwitchKeysProjectResponse> projects = [];
  for (var i = 0; i < projectsData.length; i++) {
    projects.add(
      SwitchKeysProjectResponse(
        created: projectsData[i]['created'],
        modified: projectsData[i]['modified'],
        id: projectsData[i]['id'],
        name: projectsData[i]['name'],
        organization: parseOrganization(
          projectsData[i]['organization'],
        ),
        environments: parseProjectDefaultEnvironment(
          projectsData[i]['environments'],
        ),
      ),
    );
  }

  return projects;
}

SwitchKeysEnvironmentResponse parseEnvironment(
  Map<String, dynamic> environmentData,
) {
  return SwitchKeysEnvironmentResponse(
    id: environmentData['id'],
    environmentKey: environmentData['environment_key'],
    created: environmentData['created'],
    modified: environmentData['modified'],
    users: parseEnvironmentUsers(environmentData['users']),
    features: parseFeatures(environmentData['features']),
    project: parseProject(environmentData['project']),
  );
}

SwitchKeyDevice parseDevice(
  Map<String, dynamic> deviceData,
) {
  return SwitchKeyDevice(
    deviceType: deviceData['device_type'] == 'iphone'
        ? SwitchKeyDeviceType.iphone
        : SwitchKeyDeviceType.android,
    version: deviceData['version'],
  );
}

List<SwitchKeysFeature> parseFeatures(
  List<dynamic> featuresData,
) {
  List<SwitchKeysFeature> features = [];

  for (var i = 0; i < featuresData.length; i++) {
    features.add(
      SwitchKeysFeature(
        id: featuresData[i]['id'],
        name: featuresData[i]['name'],
        value: featuresData[i]['value'],
        initialValue: featuresData[i]['initial_value'],
        isDefault: featuresData[i]['is_default'],
        created: featuresData[i]['created'],
        modified: featuresData[i]['modified'],
      ),
    );
  }
  return features;
}

SwitchKeysFeature parseFeature(
  Map<String, dynamic> featuresData,
) {
  var feature = SwitchKeysFeature(
    id: featuresData['id'],
    name: featuresData['name'],
    value: featuresData['value'],
    initialValue: featuresData['initial_value'],
    isDefault: featuresData['is_default'],
    created: featuresData['created'],
    modified: featuresData['modified'],
  );

  return feature;
}

SwitchKeysEnvironmentUserResponse parseEnvironmentUser(
  Map<String, dynamic> userData,
) {
  return SwitchKeysEnvironmentUserResponse(
    id: userData['id'],
    username: userData['username'],
    device: parseDevice(userData['device']),
    features: parseFeatures(userData['features']),
  );
}

SwitchKeysDefaultEnvironmentsResponse parseProjectDefaultEnvironment(
  List<dynamic> envsData,
) {
  var development = SwitchKeysDefaultEnvironmentResponse(
    name: "",
    environmentKey: "",
  );

  var staging = SwitchKeysDefaultEnvironmentResponse(
    name: "",
    environmentKey: "",
  );

  var production = SwitchKeysDefaultEnvironmentResponse(
    name: "",
    environmentKey: "",
  );

  for (var i = 0; i < envsData.length; i++) {
    if (envsData[i]["name"] == "development") {
      development.name = envsData[i]["name"] ?? "";
      development.environmentKey = envsData[i]["environment_key"] ?? "";
    }

    if (envsData[i]["name"] == "staging") {
      staging.name = envsData[i]["name"] ?? "";
      staging.environmentKey = envsData[i]["environment_key"] ?? "";
    }

    if (envsData[i]["name"] == "production") {
      production.name = envsData[i]["name"] ?? "";
      production.environmentKey = envsData[i]["environment_key"] ?? "";
    }
  }

  return SwitchKeysDefaultEnvironmentsResponse(
    development: development,
    production: production,
    staging: staging,
  );
}

List<SwitchKeysEnvironmentUserResponse> parseEnvironmentUsers(
  List<dynamic> usersData,
) {
  List<SwitchKeysEnvironmentUserResponse> users = [];

  for (var i = 0; i < usersData.length; i++) {
    users.add(
      SwitchKeysEnvironmentUserResponse(
        id: usersData[i]['id'],
        username: usersData[i]['username'],
        device: parseDevice(usersData[i]['device']),
        features: parseFeatures(usersData[i]['features']),
      ),
    );
  }
  return users;
}
