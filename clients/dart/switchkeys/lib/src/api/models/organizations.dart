import 'package:switchkeys/src/api/request/request.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/parser.dart';

class SwitchKeysOrganizations {
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

  Future<SwitchKeysOrganizationServices> getById({
    required int organizationID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsId,
      [
        organizationID.toString(),
      ],
    );

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.get,
      {},
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    var data = response.data;
    return __parse(data);
  }

  Future<SwitchKeysOrganizationServices> getByName(
      {required String organizationName}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsName,
      [
        organizationName,
      ],
    );

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.get,
      {},
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    var data = response.data;
    return __parse(data);
  }

  Future<Null> delete({
    required int organizationID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsId,
      [
        organizationID.toString(),
      ],
    );

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.delete,
      {},
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    return null;
  }
}

class SwitchKeysOrganizationServices {
  SwitchKeysOrganizationResponse __organization;
  SwitchKeysOrganizationServices(organization, this.__organization);

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

  Future<SwitchKeysOrganizationResponse> addMember(
      {required int memberID}) async {
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

    var data = response.data;
    SwitchKeysOrganizationResponse orgResponse = parseOrganization(data);

    if (orgResponse.id == 0) {
      throw SwitchKeysRecordNotFoundError("Organization not found.");
    }

    __organization = orgResponse;
    return orgResponse;
  }

  Future<SwitchKeysOrganizationResponse> removeMember(
      {required int memberID}) async {
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
    SwitchKeysOrganizationResponse orgResponse = parseOrganization(data);

    if (orgResponse.id == 0) {
      throw SwitchKeysRecordNotFoundError("Organization not found.");
    }

    __organization = orgResponse;
    return orgResponse;
  }

  Future<List<SwitchKeysProjectResponse>> getAllProjects() async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsIdAllProjects,
      [
        __organization.id.toString(),
      ],
    );

    var response = await SwitchKeysRequest.call(
      apiUrl,
      SwitchKeysRequestMethod.get,
      {},
      false,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    var data = response.data;
    List<SwitchKeysProjectResponse> projectsResponse = parseProjects(data);
    return projectsResponse;
  }

  Future<SwitchKeysOrganizationResponse> update({
    required String newName,
    required List<int>? newMembers,
  }) async {
    // API endpoint for updating organization
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsId,
      [
        __organization.id.toString(),
      ],
    );

    // Request body
    Map<String, dynamic> payload = {
      "name": newName,
      "members": newMembers ?? [],
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
    SwitchKeysOrganizationResponse orgResponse = parseOrganization(data);

    if (orgResponse.id == 0) {
      throw SwitchKeysRecordNotFoundError("Organization not found.");
    }

    __organization = orgResponse;
    return orgResponse;
  }
}
