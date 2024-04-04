import 'package:switchkeys/src/api/request/types.dart';

class SwitchKeysEnvironmentsUserResponse {
  final int id;
  final String username;
  final SwitchKeyDevice device;
  final List<SwitchKeyUserEnvironmentFeatures>? features;

  SwitchKeysEnvironmentsUserResponse({
    required this.id,
    required this.username,
    required this.device,
    this.features,
  });
}

class SwitchKeysEnvironmentResponse {
  final int id;
  final String name;
  final String created;
  final String modified;
  final SwitchKeysProjectResponse project;
  final String environmentKey;
  List<SwitchKeysEnvironmentsUserResponse> users;

  SwitchKeysEnvironmentResponse({
    required this.id,
    required this.name,
    required this.created,
    required this.modified,
    required this.project,
    required this.environmentKey,
    required this.users,
  });
}

class SwitchKeysProjectResponse {
  final int id;
  final String name;
  final String created;
  final String modified;
  final SwitchKeysOrganizationResponse? organization;

  SwitchKeysProjectResponse({
    required this.id,
    required this.name,
    required this.created,
    required this.modified,
    this.organization,
  });
}

class SwitchKeysAuthResponse {
  final int id;
  final String firstName;
  final String lastName;
  final String email;
  final String? password;
  final String? joiningAt;
  final String userType;
  final String accessToken;
  final String refreshToken;

  SwitchKeysAuthResponse({
    required this.id,
    required this.firstName,
    required this.lastName,
    required this.email,
    this.password,
    this.joiningAt,
    required this.userType,
    required this.accessToken,
    required this.refreshToken,
  });
}

class SwitchKeysOrganizationResponse {
  final int id;
  final String name;
  final SwitchKeysUserResponse owner;
  final List<SwitchKeysUserResponse> members;
  final String created;
  final String modified;
  SwitchKeysOrganizationResponse({
    required this.id,
    required this.name,
    required this.owner,
    required this.members,
    required this.created,
    required this.modified,
  });
}

class SwitchKeysUserResponse {
  final int id;
  final String firstName;
  final String lastName;
  final String email;
  final String fullName;
  final String backgroundColor;
  final bool isActive;
  final String joiningAt;

  SwitchKeysUserResponse({
    required this.id,
    required this.firstName,
    required this.lastName,
    required this.email,
    required this.fullName,
    required this.backgroundColor,
    required this.isActive,
    required this.joiningAt,
  });
}

enum UserTypeEnum {
  administrator,
  user,
}

extension UserTypeEnumExtension on UserTypeEnum {
  String get value {
    switch (this) {
      case UserTypeEnum.administrator:
        return 'Administrator';
      case UserTypeEnum.user:
        return 'User';
      default:
        throw Exception('Unknown user type');
    }
  }
}

class SwitchKeysEnvironmentsUserFeatureResponse {
  final int id;
  final String name;
  final String value;
  final bool isEnabled;
  final bool isDefault;
  final String created;
  final String modified;

  SwitchKeysEnvironmentsUserFeatureResponse({
    required this.id,
    required this.name,
    required this.value,
    required this.isEnabled,
    required this.isDefault,
    required this.created,
    required this.modified,
  });
}
