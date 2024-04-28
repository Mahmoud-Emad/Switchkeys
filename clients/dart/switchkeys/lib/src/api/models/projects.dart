import 'dart:convert';

import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'package:http/http.dart' as http;
import 'package:switchkeys/src/utils/parser.dart';

class SwitchKeysProjects {
  final _config = SwitchKeysTokensConfig();
  SwitchKeysProjects();

  Future<SwitchKeysProjectResponse> create(
      {required String name, required int organizationID}) async {
    // API endpoint for creating organization
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.projects);
    // Request body
    Map<String, dynamic> body = {
      "name": name,
      "organization_id": organizationID,
    };

    // Get the tokens
    var tokens = _config.readTokens();

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      // Make POST request
      http.Response response = await http.post(Uri.parse(apiUrl),
          headers: headers, body: jsonEncode(body));

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysProjectResponse projectResponse =
            parseProject(data["results"]);
        return projectResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Project creation failed due: $message");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysProjectResponse> getById({required int projectID}) async {
    String apiUrl =
        SwitchKeysRoutes.getRoute(EndPoints.projectsId, [projectID.toString()]);

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      // Make GET request
      http.Response response =
          await http.get(Uri.parse(apiUrl), headers: headers);

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysProjectResponse projectResponse =
            parseProject(data["results"]);
        return projectResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Cannot get the organization due: $message");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysProjectResponse> update(
      {required String name,
      required int organizationID,
      required int projectID}) async {
    // API endpoint for creating organization
    String apiUrl =
        SwitchKeysRoutes.getRoute(EndPoints.projectsId, [projectID.toString()]);
    // Request body
    Map<String, dynamic> body = {
      "name": name,
      "organization_id": organizationID,
    };

    // Get the tokens
    var tokens = _config.readTokens();

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      // Make PUT request
      http.Response response = await http.put(Uri.parse(apiUrl),
          headers: headers, body: jsonEncode(body));

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysProjectResponse projectResponse =
            parseProject(data["results"]);
        return projectResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Failed to update project due: $message");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<bool> delete({required int projectID}) async {
    String apiUrl =
        SwitchKeysRoutes.getRoute(EndPoints.projectsId, [projectID.toString()]);

    // Get the tokens
    var tokens = _config.readTokens();

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      // Make DELETE request
      http.Response response =
          await http.delete(Uri.parse(apiUrl), headers: headers);

      if (response.statusCode < 400) {
        return true;
      } else {
        Map<String, dynamic> data = jsonDecode(response.body);
        String message = data['message'] ?? data['detail'];
        throw ResponseError("Failed to delete the project due: $message");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }
}
