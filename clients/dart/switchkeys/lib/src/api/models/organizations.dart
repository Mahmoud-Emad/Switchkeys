import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'package:switchkeys/src/utils/parser.dart';

class SwitchKeysOrganizations {
  final _config = SwitchKeysTokensConfig();
  SwitchKeysOrganizations();

  Future<SwitchKeysOrganizationResponse> create(
      {required String name, required List<int>? members}) async {
    // API endpoint for creating organization
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.organizations);
    // Request body
    Map<String, dynamic> body = {
      "name": name,
      "members": members ?? [],
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
        SwitchKeysOrganizationResponse organizationResponse =
            parseOrganization(data["results"]);
        return organizationResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Organization creation failed due: $message");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysOrganizationResponse> update(
      {required int organizationID,
      required String newName,
      required List<int>? newMembers}) async {
    // API endpoint for updating organization
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.organizationsId, [organizationID.toString()]);

    // Request body
    Map<String, dynamic> body = {
      "name": newName,
      "members": newMembers ?? [],
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
      http.Response response = await http.put(Uri.parse(apiUrl),
          headers: headers, body: jsonEncode(body));

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysOrganizationResponse organizationResponse =
            parseOrganization(data["results"]);
        return organizationResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Organization updating failed due: $message");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysOrganizationResponse> getByID(
      {required int organizationID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.organizationsId, [organizationID.toString()]);

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      // Make POST request
      http.Response response =
          await http.get(Uri.parse(apiUrl), headers: headers);

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysOrganizationResponse organizationResponse =
            parseOrganization(data["results"]);
        return organizationResponse;
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

  Future<SwitchKeysOrganizationResponse> getByName(
      {required String organizationName}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.organizationsName, [organizationName]);

    // Get the tokens
    var tokens = _config.readTokens();

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      // Make GET request
      http.Response response =
          await http.get(Uri.parse(apiUrl), headers: headers);

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysOrganizationResponse organizationResponse =
            parseOrganization(data["results"]);
        return organizationResponse;
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

  Future<List<SwitchKeysProjectResponse>> getAllProjects(
      {required int organizationID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.organizationsIdAllProjects, [organizationID.toString()]);

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
        List<SwitchKeysProjectResponse> projectsResponse =
            parseProjects(data["results"]);
        return projectsResponse;
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

  Future<bool> delete({required int organizationID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.organizationsId, [organizationID.toString()]);

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
        throw ResponseError("Failed to delete organization due: $message");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysOrganizationResponse> addMember(
      {required int organizationID, required int memberID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.organizationsIdAddMember, [organizationID.toString()]);

    // Request body
    Map<String, dynamic> body = {
      "member_id": memberID,
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
        SwitchKeysOrganizationResponse organizationResponse =
            parseOrganization(data["results"]);
        return organizationResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError(
            "Failed to add member to organization due: $message ${data0['error'] ?? ''}");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysOrganizationResponse> removeMember(
      {required int organizationID, required int memberID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
        EndPoints.organizationsIdRemoveMember, [organizationID.toString()]);

    // Request body
    Map<String, dynamic> body = {
      "member_id": memberID,
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
        SwitchKeysOrganizationResponse organizationResponse =
            parseOrganization(data["results"]);
        return organizationResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError(
            "Failed to remove member from an organization due: $message ${data0['error'] ?? ''}");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }
}
