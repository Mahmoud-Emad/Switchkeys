import 'package:switchkeys/src/api/request/request.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/parser.dart';

/// Class handling organization-related operations for SwitchKeys.
class SwitchKeysOrganizations {
  SwitchKeysOrganizations();

  /// Parses the organization data.
  SwitchKeysOrganizationServices __parse(dynamic data) {
    SwitchKeysOrganizationResponse organization = parseOrganization(data);
    return SwitchKeysOrganizationServices(organization);
  }

  /// Creates a new organization with the given name.
  ///
  /// Returns a [SwitchKeysOrganizationServices] instance.
  Future<SwitchKeysOrganizationServices> create({required String name}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.organizations);
    Map<String, dynamic> payload = {"name": name};

    try {
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
    } catch (e) {
      rethrow;
    }
  }

  /// Retrieves an organization by its ID.
  ///
  /// Returns a [SwitchKeysOrganizationServices] instance.
  Future<SwitchKeysOrganizationServices> getById({
    required int organizationID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsId,
      [organizationID.toString()],
    );

    try {
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
    } catch (e) {
      rethrow;
    }
  }

  /// Retrieves an organization by its name.
  ///
  /// Returns a [SwitchKeysOrganizationServices] instance.
  Future<SwitchKeysOrganizationServices> getByName({
    required String organizationName,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsName,
      [organizationName],
    );

    try {
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
    } catch (e) {
      rethrow;
    }
  }

  /// Deletes an organization by its ID.
  Future<void> delete({
    required int organizationID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsId,
      [organizationID.toString()],
    );

    try {
      var response = await SwitchKeysRequest.call(
        apiUrl,
        SwitchKeysRequestMethod.delete,
        {},
        false,
      );

      if (response.errorMessage != null) {
        throw response.error;
      }
    } catch (e) {
      rethrow;
    }
  }
}

/// Services for interacting with a specific organization.
class SwitchKeysOrganizationServices {
  SwitchKeysOrganizationResponse __organization;

  SwitchKeysOrganizationServices(this.__organization);

  /// The organization name.
  String get name => __organization.name;

  /// The organization ID.
  int get id => __organization.id;

  /// The organization members.
  List<SwitchKeysUserResponse> get members => __organization.members;

  /// The organization creation date and time.
  String get created => __organization.created;

  /// The organization modification date and time.
  String get modified => __organization.modified;

  /// The organization owner.
  SwitchKeysUserResponse get owner => __organization.owner;

  /// Creates a new project in the organization.
  ///
  /// Returns a [SwitchKeysProjectResponse] instance.
  Future<SwitchKeysProjectResponse> createProject({
    required String projectName,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.projects);
    Map<String, dynamic> payload = {
      "name": projectName,
      "organization_id": __organization.id,
    };

    try {
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
      return parseProject(data);
    } catch (e) {
      rethrow;
    }
  }

  /// Adds a member to the organization.
  ///
  /// Returns the updated [SwitchKeysOrganizationResponse].
  Future<SwitchKeysOrganizationResponse> addMember({
    required int memberID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsIdAddMember,
      [__organization.id.toString()],
    );

    Map<String, dynamic> payload = {"member_id": memberID};

    try {
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
    } catch (e) {
      rethrow;
    }
  }

  /// Removes a member from the organization.
  ///
  /// Returns the updated [SwitchKeysOrganizationResponse].
  Future<SwitchKeysOrganizationResponse> removeMember({
    required int memberID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsIdRemoveMember,
      [__organization.id.toString()],
    );

    Map<String, dynamic> payload = {"member_id": memberID};

    try {
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
    } catch (e) {
      rethrow;
    }
  }

  /// Retrieves all projects in the organization.
  ///
  /// Returns a list of [SwitchKeysProjectResponse].
  Future<List<SwitchKeysProjectResponse>> getAllProjects() async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsIdAllProjects,
      [__organization.id.toString()],
    );

    try {
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
      return parseProjects(data);
    } catch (e) {
      rethrow;
    }
  }

  /// Updates the organization's name and members.
  ///
  /// Returns the updated [SwitchKeysOrganizationResponse].
  Future<SwitchKeysOrganizationResponse> update({
    required String newName,
    required List<int>? newMembers,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.organizationsId,
      [__organization.id.toString()],
    );

    Map<String, dynamic> payload = {
      "name": newName,
      "members": newMembers ?? [],
    };

    try {
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
    } catch (e) {
      rethrow;
    }
  }
}
