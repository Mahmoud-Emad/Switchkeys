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

class SwitchKeyUserEnvironmentFeatures {
  String name;
  String value;
  bool isEnabled;

  SwitchKeyUserEnvironmentFeatures({
    required this.name,
    required this.value,
    required this.isEnabled,
  });

  // Method to convert SwitchKeyUserEnvironmentFeatures to a JSON-compatible map
  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'value': value,
      'is_enabled': isEnabled,
    };
  }

  // Factory method to create SwitchKeyUserEnvironmentFeatures from JSON map
  factory SwitchKeyUserEnvironmentFeatures.fromJson(Map<String, dynamic> json) {
    return SwitchKeyUserEnvironmentFeatures(
      name: json['name'],
      value: json['value'],
      isEnabled: json['isEnabled'],
    );
  }
}
