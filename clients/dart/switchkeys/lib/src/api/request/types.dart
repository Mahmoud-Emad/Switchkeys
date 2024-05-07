import 'package:switchkeys/src/api/response/types.dart';

class SwitchKeysOrganizationRequest {
  final String name;
  final List<SwitchKeysUserResponse> members;

  SwitchKeysOrganizationRequest({
    required this.name,
    required this.members,
  });
}

class SwitchKeysEnvironmentsUser {
  final String username;
  final SwitchKeyDevice? device;

  SwitchKeysEnvironmentsUser({
    required this.username,
    this.device,
  });
}

enum SwitchKeyDeviceType {
  // ignore: constant_identifier_names
  Android,
  // ignore: constant_identifier_names
  IPhone,
}

class SwitchKeyDevice {
  final SwitchKeyDeviceType deviceType;
  final String version;

  SwitchKeyDevice({
    required this.deviceType,
    required this.version,
  });
}

class SwitchKeyUserEnvironmentFeatureRequest {
  String name;
  String value;

  SwitchKeyUserEnvironmentFeatureRequest({
    required this.name,
    required this.value,
  });

  // Method to convert SwitchKeyUserEnvironmentFeatures to a JSON-compatible map
  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'value': value,
    };
  }
}

class SwitchKeyUserEnvironmentFeatures {
  int id;
  String name;
  String created;
  String modified;
  String value;
  String initialValue;
  bool isDefault;

  SwitchKeyUserEnvironmentFeatures({
    required this.id,
    required this.name,
    required this.created,
    required this.modified,
    required this.value,
    required this.initialValue,
    required this.isDefault,
  });

  // Method to convert SwitchKeyUserEnvironmentFeatures to a JSON-compatible map
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'created': created,
      'modified': modified,
      'value': value,
      'initial_value': initialValue,
      'is_default': isDefault,
    };
  }

  // Factory method to create SwitchKeyUserEnvironmentFeatures from JSON map
  factory SwitchKeyUserEnvironmentFeatures.fromJson(Map<String, dynamic> json) {
    return SwitchKeyUserEnvironmentFeatures(
      id: json['id'],
      initialValue: json['initial_value'],
      isDefault: json['is_default'],
      created: json['created'],
      modified: json['modified'],
      name: json['name'],
      value: json['value'],
    );
  }
}
