import 'dart:convert';
import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'package:http/http.dart' as http;
import 'package:switchkeys/src/utils/parser.dart';

/// Class for managing SwitchKeys environments.
class SwitchKeysEnvironments {
  final config = SwitchKeysTokensConfig();
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
    var tokens = config.readTokens();
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
    var tokens = config.readTokens();
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

class SwitchKeysEnvironmentUsers {
  final config = SwitchKeysTokensConfig();

  SwitchKeysEnvironmentUsers();

  /// Adds a user to an environment.
  ///
  /// Returns a [SwitchKeysEnvironmentsUserResponse] containing information about the added user.
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

      if (response.statusCode < 400) {
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
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError(
          "Failed to add user due: $message ${data0['error'] ?? ''}",
        );
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  /// removes a user from an environment.
  ///
  /// Returns a [SwitchKeysEnvironmentsUserResponse] containing information about the added user.

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

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        var user = parseEnvironmentUser(data["results"]);
        for (var i = 0; i < environment.users.length; i++) {
          if (environment.users[i].id == user.id) {
            // Remove the user from the environment.users list
            environment.users.removeAt(i);
            break;
          }
        }
        return user;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError(
          "Failed to add user due: $message ${data0['error'] ?? ''}",
        );
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }

  /// Add user feature on an environment, in case there .
  ///
  /// Returns a [SwitchKeysEnvironmentsUserFeatureResponse] containing information about the added user feature.

  Future<List<SwitchKeyUserEnvironmentFeatures>> addFeature({
    required String username,
    required SwitchKeyUserEnvironmentFeatures feature,
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

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseFeatures(data["results"]);
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError(
          "Failed to set user feature due: $message ${data0['error'] ?? ''}",
        );
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }
}
