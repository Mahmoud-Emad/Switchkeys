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
  android,
  // ignore: constant_identifier_names
  iphone,
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

class SwitchKeysFeatureData {
  String name;
  String value;

  SwitchKeysFeatureData({
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

  // Factory method to create SwitchKeyUserEnvironmentFeatures from JSON map
  factory SwitchKeysFeatureData.fromJson(Map<String, dynamic> json) {
    return SwitchKeysFeatureData(
      name: json['name'],
      value: json['value'],
    );
  }
}
