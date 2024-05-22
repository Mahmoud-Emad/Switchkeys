import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:switchkeys/src/api/request/request.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'package:switchkeys/src/utils/parser.dart';

class SwitchKeysOrganizations {
  final _config = SwitchKeysTokensConfig();
  SwitchKeysOrganizations();

  // Future<SwitchKeysOrganizationResponse> create({required String name}) async {
  Future<SwitchKeysOrganizationServices> create({required String name}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.organizations);
    Map<String, dynamic> payload = {"name": name};

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.post,
      payload,
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    var data = response.data;
    return __parse(data);
  }

  SwitchKeysOrganizationServices __parse(dynamic data) {
    SwitchKeysOrganizationResponse organization = parseOrganization(data);
    return SwitchKeysOrganizationServices(organization, organization);
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

  Future<SwitchKeysOrganizationResponse> getById(
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
}

class SwitchKeysOrganizationServices {
  final SwitchKeysOrganizationResponse __organization;

  // ignore: no_leading_underscores_for_local_identifiers
  const SwitchKeysOrganizationServices(organization, this.__organization);

  /// The organization name.
  String get name {
    return __organization.name;
  }

  /// The organization ID.
  int get id {
    return __organization.id;
  }

  /// The organization members.
  List<SwitchKeysUserResponse> get members {
    return __organization.members;
  }

  /// The organization created at datetime.
  String get created {
    return __organization.created;
  }

  /// The organization modified at datetime.
  String get modified {
    return __organization.modified;
  }

  /// The organization modified at datetime.
  SwitchKeysUserResponse get owner {
    return __organization.owner;
  }

  Future<SwitchKeysProjectResponse> createProject({
    required String projectName,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.projects);
    Map<String, dynamic> payload = {
      "name": projectName,
      "organization_id": __organization.id,
    };

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.post,
      payload,
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    var data = response.data;
    SwitchKeysProjectResponse projectResponse = parseProject(data);
    return projectResponse;
  }

  Future<SwitchKeysUserResponse> addMember({required int memberID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsIdAddMember,
      [
        __organization.id.toString(),
      ],
    );

    Map<String, dynamic> payload = {
      "member_id": memberID,
    };

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.put,
      payload,
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    print("response.data ${response.data}");
    var data = response.data;
    SwitchKeysUserResponse memberResponse = parseUser(data);
    return memberResponse;
  }

  Future<SwitchKeysUserResponse> removeMember({required int memberID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsIdRemoveMember,
      [
        __organization.id.toString(),
      ],
    );

    Map<String, dynamic> payload = {
      "member_id": memberID,
    };

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.put,
      payload,
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    var data = response.data;
    SwitchKeysUserResponse memberResponse = parseUser(data);
    return memberResponse;
  }
}
