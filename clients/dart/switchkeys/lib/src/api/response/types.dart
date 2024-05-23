import 'dart:ffi';

import 'package:switchkeys/src/api/request/types.dart';

class SwitchKeysEnvironmentUserResponse {
  final int id;
  final String username;
  final SwitchKeyDevice device;
  final List<SwitchKeysFeature> features;

  SwitchKeysEnvironmentUserResponse({
    required this.id,
    required this.username,
    required this.device,
    required this.features,
  });
}

class SwitchKeysEnvironmentResponse {
  final int id;
  final String created;
  final String modified;
  final String environmentKey;
  List<SwitchKeysFeature> features;
  final SwitchKeysProjectResponse project;
  List<SwitchKeysEnvironmentUserResponse> users;

  SwitchKeysEnvironmentResponse({
    required this.id,
    required this.created,
    required this.modified,
    required this.project,
    required this.environmentKey,
    required this.users,
    required this.features,
  });
}

class SwitchKeysDefaultEnvironmentResponse {
  String name;
  String environmentKey;
  SwitchKeysDefaultEnvironmentResponse({
    required this.name,
    required this.environmentKey,
  });
}

class SwitchKeysDefaultEnvironmentsResponse {
  final SwitchKeysDefaultEnvironmentResponse development;
  final SwitchKeysDefaultEnvironmentResponse staging;
  final SwitchKeysDefaultEnvironmentResponse production;

  SwitchKeysDefaultEnvironmentsResponse({
    required this.development,
    required this.staging,
    required this.production,
  });
}

class SwitchKeysProjectResponse {
  final int id;
  final String name;
  final String created;
  final String modified;
  final SwitchKeysDefaultEnvironmentsResponse environments;
  final SwitchKeysOrganizationResponse? organization;

  SwitchKeysProjectResponse({
    required this.id,
    required this.name,
    required this.created,
    required this.modified,
    required this.environments,
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
  final String memberType;
  final String accessToken;
  final String refreshToken;

  SwitchKeysAuthResponse({
    required this.id,
    required this.firstName,
    required this.lastName,
    required this.email,
    this.password,
    this.joiningAt,
    required this.memberType,
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

class SwitchKeysFeature {
  final int id;
  final String name;
  final String value;
  final String initialValue;
  final Bool isDefault;
  final String created;
  final String modified;

  SwitchKeysFeature({
    required this.id,
    required this.name,
    required this.value,
    required this.initialValue,
    required this.isDefault,
    required this.created,
    required this.modified,
  });
}
