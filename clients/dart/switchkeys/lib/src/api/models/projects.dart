import 'package:switchkeys/src/api/request/request.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/utils/parser.dart';

/// Class handling project-related operations for SwitchKeys.
class SwitchKeysProjects {
  SwitchKeysProjects();

  /// Parses the project data.
  SwitchKeysProjectServices __parse(dynamic data) {
    SwitchKeysProjectResponse project = parseProject(data);
    return SwitchKeysProjectServices(project);
  }

  /// Creates a new project with the given name and organization ID.
  ///
  /// Returns a [SwitchKeysProjectServices] instance.
  Future<SwitchKeysProjectServices> create({
    required String name,
    required int organizationID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.projects);
    Map<String, dynamic> payload = {
      "name": name,
      "organization_id": organizationID,
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
      return __parse(data);
    } catch (e) {
      rethrow;
    }
  }

  /// Retrieves a project by its ID.
  ///
  /// Returns a [SwitchKeysProjectServices] instance.
  Future<SwitchKeysProjectServices> getById({required int projectID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.projectsId,
      [projectID.toString()],
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

  /// Deletes a project by its ID.
  Future<void> delete({required int projectID}) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.projectsId,
      [projectID.toString()],
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

/// Services for interacting with a specific project.
class SwitchKeysProjectServices {
  final SwitchKeysProjectResponse __project;
  const SwitchKeysProjectServices(this.__project);

  /// The project ID.
  int get id => __project.id;

  /// The project name.
  String get name => __project.name;

  /// The project created at datetime as string.
  String get created => __project.created;

  /// The project modified at datetime as string.
  String get modified => __project.modified;

  /// The project environments.
  SwitchKeysDefaultEnvironmentsResponse get environments =>
      __project.environments;

  /// The project organization.
  SwitchKeysOrganizationResponse? get organization => __project.organization;

  /// Updates the project details.
  ///
  /// Returns an updated [SwitchKeysProjectResponse] instance.
  Future<SwitchKeysProjectResponse> update({
    required String name,
    required int organizationID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.projectsId,
      [__project.id.toString()],
    );

    Map<String, dynamic> payload = {
      "name": name,
      "organization_id": organizationID,
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
      return parseProject(data);
    } catch (e) {
      rethrow;
    }
  }
}
