import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'package:switchkeys/src/utils/parser.dart';

/// Class for managing SwitchKeys environments.
class SwitchKeysEnvironments {
  final _config = SwitchKeysTokensConfig();
  final users = SwitchKeysEnvironmentUsers();
  SwitchKeysEnvironments();

  /// Creates a new environment.
  ///
  /// Returns a [SwitchKeysEnvironmentResponse] containing information about the created environment.
  Future<SwitchKeysEnvironmentResponse> create({
    required String name,
    required int projectID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.environments);
    Map<String, dynamic> body = {
      "name": name,
      "project_id": projectID,
    };
    var tokens = _config.readTokens();
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      http.Response response = await http.post(
        Uri.parse(apiUrl),
        headers: headers,
        body: jsonEncode(body),
      );

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseEnvironment(data["results"]);
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Environment creation failed due: $message");
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  /// Loads an environment using its unique key.
  ///
  /// Returns a [SwitchKeysEnvironmentResponse] containing information about the loaded environment.
  Future<SwitchKeysEnvironmentResponse> load({
    required String environmentKey,
  }) async {
    String apiUrl =
        SwitchKeysRoutes.getRoute(EndPoints.environmentsKey, [environmentKey]);
    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      http.Response response = await http.get(
        Uri.parse(apiUrl),
        headers: headers,
      );

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseEnvironment(data["results"]);
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Failed to get environment due: $message");
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  /// Gets an environment by its ID.
  ///
  /// Returns a [SwitchKeysEnvironmentResponse] containing information about the environment.
  Future<SwitchKeysEnvironmentResponse> getByID({
    required int environmentId,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.environmentsId, [environmentId.toString()]);
    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      http.Response response = await http.get(
        Uri.parse(apiUrl),
        headers: headers,
      );

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseEnvironment(data["results"]);
      } else {
        Map<String, dynamic> data = jsonDecode(response.body);
        String message = data['message'] ?? data['detail'];
        throw ResponseError("Failed to get the environment due: $message");
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  /// Deletes an environment by its ID.
  ///
  /// Returns `true` if the environment is successfully deleted.
  Future<bool> delete({
    required int environmentId,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.environmentsId, [environmentId.toString()]);
    var tokens = _config.readTokens();
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      http.Response response = await http.delete(
        Uri.parse(apiUrl),
        headers: headers,
      );

      if (response.statusCode < 400) {
        return true;
      } else {
        Map<String, dynamic> data = jsonDecode(response.body);
        String message = data['message'] ?? data['detail'];
        throw ResponseError("Failed to delete the environment due: $message");
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  /// Updates an environment by its ID.
  ///
  /// Returns a [SwitchKeysEnvironmentResponse] containing information about the updated environment.
  Future<SwitchKeysEnvironmentResponse> update({
    required String name,
    required int projectID,
    required int environmentId,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.environmentsId, [environmentId.toString()]);
    Map<String, dynamic> body = {
      "name": name,
      "project_id": projectID,
    };
    var tokens = _config.readTokens();
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      http.Response response = await http.put(
        Uri.parse(apiUrl),
        headers: headers,
        body: jsonEncode(body),
      );

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseEnvironment(data["results"]);
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Environment update failed due: $message");
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }
}

/// A class that provides methods for managing users in SwitchKeys environments.
///
/// This class allows you to add and remove users from environments, as well as add and remove features for a specific user in an environment.
/// It also provides methods for handling error responses from API calls.
///
/// Example usage:
/// ```dart
/// SwitchKeysEnvironmentUsers users = SwitchKeysEnvironmentUsers();
///
/// // Add a user to an environment
/// SwitchKeysEnvironmentsUserResponse addedUser = await users.addUser(
///   user: SwitchKeysEnvironmentsUser(
///     username: 'john_doe',
///     device: SwitchKeyDevice(
///       deviceType: SwitchKeyDeviceType.Android,
///       version: '10.0',
///     ),
///   ),
///   environment: SwitchKeysEnvironmentResponse(
///     environmentKey: 'env123',
///     users: [],
///   ),
/// );
///
/// // Remove a user from an environment
/// SwitchKeysEnvironmentsUserResponse removedUser = await users.removeUser(
///   user: addedUser,
///   environment: SwitchKeysEnvironmentResponse(
///     environmentKey: 'env123',
///     users: [],
///   ),
/// );
///
/// // Add a feature for a user in an environment
/// List<SwitchKeyUserEnvironmentFeatures> addedFeatures = await users.addFeature(
///   username: 'john_doe',
///   feature: SwitchKeyUserEnvironmentFeatures(
///     name: 'feature1',
///     value: true,
///   ),
///   environment: SwitchKeysEnvironmentResponse(
///     environmentKey: 'env123',
///     users: [],
///   ),
/// );
///
/// // Bulk create features for a user in an environment
/// List<SwitchKeyUserEnvironmentFeatures> bulkCreatedFeatures = await users.bulkCreateFeature(
///   username: 'john_doe',
///   features: [
///     SwitchKeyUserEnvironmentFeatures(
///       name: 'feature1',
///       value: true,
///     ),
///     SwitchKeyUserEnvironmentFeatures(
///       name: 'feature2',
///       value: false,
///     ),
///   ],
///   environment: SwitchKeysEnvironmentResponse(
///     environmentKey: 'env123',
///     users: [],
///   ),
/// );
/// ```
class SwitchKeysEnvironmentUsers {
  final config = SwitchKeysTokensConfig();

  SwitchKeysEnvironmentUsers();

  Future<SwitchKeysEnvironmentsUserResponse> addUser({
    required SwitchKeysEnvironmentsUser user,
    required SwitchKeysEnvironmentResponse environment,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsKeyAddUser,
      [
        environment.environmentKey.toString(),
      ],
    );
    String deviceType = (user.device?.deviceType == SwitchKeyDeviceType.Android)
        ? 'Android'
        : 'IPhone';
    Map<String, dynamic> body = {
      "username": user.username,
      "device": {
        "device_type": deviceType,
        "version": user.device?.version,
      },
    };

    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      http.Response response = await http.put(
        Uri.parse(apiUrl),
        headers: headers,
        body: jsonEncode(body),
      );

      if (_isResponseSuccessful(response)) {
        Map<String, dynamic> data = jsonDecode(response.body);
        var user = parseEnvironmentUser(data["results"]);
        var isUserInEnvironment = false;

        for (var i = 0; i < environment.users.length; i++) {
          if (environment.users[i].id == user.id) {
            isUserInEnvironment = true;
          }
        }

        if (!isUserInEnvironment) {
          environment.users.add(user);
        }

        return user;
      } else {
        throw ResponseError(_handleErrorResponseMessage(response));
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  Future<List<SwitchKeysEnvironmentsUserResponse>> addUsers({
    required List<SwitchKeysEnvironmentsUser> users,
    required SwitchKeysEnvironmentResponse environment,
  }) async {
    final apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsKeyAddUsers,
      [environment.environmentKey.toString()],
    );

    final List<Map<String, dynamic>> payload = users.map((user) {
      String deviceType =
          (user.device?.deviceType == SwitchKeyDeviceType.Android)
              ? 'Android'
              : 'IPhone';
      return {
        "username": user.username,
        "device": {
          "device_type": deviceType,
          "version": user.device?.version,
        },
      };
    }).toList();

    Map<String, dynamic> body = {"users": payload};

    final headers = {
      "Content-Type": "application/json",
    };

    try {
      final response = await http.put(
        Uri.parse(apiUrl),
        headers: headers,
        body: jsonEncode(body),
      );

      if (_isResponseSuccessful(response)) {
        final Map<String, dynamic> data = jsonDecode(response.body);
        final List<SwitchKeysEnvironmentsUserResponse> parsedUsers =
            parseEnvironmentUsers(
          data["results"],
        );

        for (final user in parsedUsers) {
          if (!environment.users.any((u) => u.id == user.id)) {
            environment.users.add(user);
          }
        }

        return environment.users;
      } else {
        throw ResponseError(_handleErrorResponseMessage(response));
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysEnvironmentsUserResponse> removeUser({
    required SwitchKeysEnvironmentsUser user,
    required SwitchKeysEnvironmentResponse environment,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsKeyRemoveUser,
      [
        environment.environmentKey.toString(),
      ],
    );

    Map<String, dynamic> body = {"username": user.username};

    var tokens = config.readTokens();
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      http.Response response = await http.put(
        Uri.parse(apiUrl),
        headers: headers,
        body: jsonEncode(body),
      );

      if (_isResponseSuccessful(response)) {
        Map<String, dynamic> data = jsonDecode(response.body);
        var user = parseEnvironmentUser(data["results"]);
        for (var i = 0; i < environment.users.length; i++) {
          if (environment.users[i].id == user.id) {
            environment.users.removeAt(i);
            break;
          }
        }
        return user;
      } else {
        throw ResponseError(_handleErrorResponseMessage(response));
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  Future<List<SwitchKeyUserEnvironmentFeatures>> addFeature({
    required String username,
    required SwitchKeyUserEnvironmentFeatures feature,
    required SwitchKeysEnvironmentResponse environment,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentUserAddFeature,
      [
        environment.environmentKey.toString(),
      ],
    );

    Map<String, dynamic> body = {
      "username": username,
      "feature": feature.toJson(),
    };

    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      http.Response response = await http.post(
        Uri.parse(apiUrl),
        headers: headers,
        body: jsonEncode(body),
      );

      if (_isResponseSuccessful(response)) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseFeatures(data["results"]);
      } else {
        throw ResponseError(_handleErrorResponseMessage(response));
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  Future<List<SwitchKeyUserEnvironmentFeatures>> bulkCreateFeature({
    required String username,
    required List<SwitchKeyUserEnvironmentFeatures> features,
    required SwitchKeysEnvironmentResponse environment,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentUserAddFeatures,
      [
        environment.environmentKey.toString(),
      ],
    );

    Map<String, dynamic> body = {
      "username": username,
      "features": features,
    };

    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      http.Response response = await http.post(
        Uri.parse(apiUrl),
        headers: headers,
        body: jsonEncode(body),
      );

      if (_isResponseSuccessful(response)) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseFeatures(data["results"]);
      } else {
        throw ResponseError(_handleErrorResponseMessage(response));
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeyUserEnvironmentFeatures> getFeature({
    required String username,
    required String featureName,
    required SwitchKeysEnvironmentResponse environment,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentUserGetFeature,
      [environment.environmentKey.toString(), featureName, username],
    );

    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      http.Response response = await http.get(
        Uri.parse(apiUrl),
        headers: headers,
      );

      if (_isResponseSuccessful(response)) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseFeature(data["results"]);
      } else {
        throw ResponseError(_handleErrorResponseMessage(response));
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  // featureIsEnabled({
  //   required String username,
  //   required String featureName,
  // }) async {}

  String _handleErrorResponseMessage(http.Response response) {
    Map<String, dynamic> data = jsonDecode(response.body);
    String message = data['message'] ?? data['detail'];
    return "Failed due: $message ${data['error'] ?? ''}";
  }

  bool _isResponseSuccessful(http.Response response) {
    return response.statusCode < 400;
  }
}
