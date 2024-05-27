import 'package:switchkeys/src/api/models/environment.users.dart';
import 'package:switchkeys/src/api/request/request.dart';
import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/utils/parser.dart';

/// Class for managing SwitchKeys environments.
class SwitchKeysEnvironments {
  SwitchKeysEnvironments();

  /// Parses the environment data.
  ///
  /// Takes dynamic [data] as a parameter.
  /// Returns a [SwitchKeysEnvironmentServices] instance.
  SwitchKeysEnvironmentServices __parse(dynamic data) {
    SwitchKeysEnvironmentResponse environment = parseEnvironment(data);
    final users = SwitchKeysEnvironmentUsers(environment);
    return SwitchKeysEnvironmentServices(environment, users);
  }

  /// Creates a new environment.
  ///
  /// Takes a [name] and a [projectID] as required parameters.
  /// Returns a [SwitchKeysEnvironmentServices] instance.
  Future<SwitchKeysEnvironmentServices> create({
    required String name,
    required int projectID,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.environments);
    Map<String, dynamic> payload = {
      "name": name,
      "project_id": projectID,
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

  /// Loads an environment by its key.
  ///
  /// Takes an [environmentKey] as a required parameter.
  /// Returns a [SwitchKeysEnvironmentServices] instance.
  Future<SwitchKeysEnvironmentServices> load({
    required String environmentKey,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsKey,
      [
        environmentKey,
      ],
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

  /// Gets an environment by its ID.
  ///
  /// Takes an [environmentId] as a required parameter.
  /// Returns a [SwitchKeysEnvironmentServices] instance.
  Future<SwitchKeysEnvironmentServices> getById({
    required int environmentId,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsId,
      [
        environmentId.toString(),
      ],
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

  /// Deletes an environment by its ID.
  ///
  /// Takes an [environmentId] as a required parameter.
  /// Returns `true` if the environment is successfully deleted.
  Future<void> delete({
    required int environmentId,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsId,
      [
        environmentId.toString(),
      ],
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

/// Class for managing environment services.
class SwitchKeysEnvironmentServices {
  final SwitchKeysEnvironmentResponse __environment;
  final SwitchKeysEnvironmentUsers users;

  /// Constructs an instance of [SwitchKeysEnvironmentServices] with the given [__environment].
  const SwitchKeysEnvironmentServices(this.__environment, this.users);

  /// The environment ID.
  int get id => __environment.id;

  /// The environment name.
  String get name => getEnvironmentName();

  /// The environment created at datetime.
  String get created => __environment.created;

  /// The environment modified at datetime.
  String get modified => __environment.modified;

  /// The environment key.
  String get environmentKey => __environment.environmentKey;

  /// The environment project.
  SwitchKeysProjectResponse get project => __environment.project;

  /// The environment organization.
  SwitchKeysOrganizationResponse? get organization =>
      __environment.project.organization;

  /// The environment features.
  List<SwitchKeysFeature> get features => __environment.features;

  /// Returns the environment users.
  List<SwitchKeysEnvironmentUserResponse> getUsers() {
    return __environment.users;
  }

  /// Retrieves the environment name based on the environment key.
  String getEnvironmentName() {
    if (__environment.environmentKey ==
        __environment.project.environments.development.environmentKey) {
      return __environment.project.environments.development.name;
    }

    if (__environment.environmentKey ==
        __environment.project.environments.staging.environmentKey) {
      return __environment.project.environments.staging.name;
    }

    if (__environment.environmentKey ==
        __environment.project.environments.production.environmentKey) {
      return __environment.project.environments.production.name;
    }

    return 'Unknown';
  }

  /// Updates the environment by its ID.
  ///
  /// Takes a [name] and [projectID] as required parameters.
  /// Returns a [SwitchKeysEnvironmentResponse] containing information about the updated environment.
  Future<SwitchKeysEnvironmentResponse> update({
    required String name,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsId,
      [
        __environment.id.toString(),
      ],
    );

    Map<String, dynamic> payload = {
      "name": name,
      "project_id": __environment.project.id,
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
      return parseEnvironment(data);
    } catch (e) {
      rethrow;
    }
  }

  /// Adding a new feature in the environment.
  ///
  /// `Note` The action here will be reflected to all of the environment users.
  ///
  /// Takes a [feature] data as required parameters.
  /// Returns an updated [SwitchKeysFeature] instance.
  Future<SwitchKeysFeature> addFeature({
    required SwitchKeysFeatureData feature,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentAddFeature,
      [
        __environment.environmentKey.toString(),
      ],
    );

    try {
      var response = await SwitchKeysRequest.call(
        apiUrl,
        SwitchKeysRequestMethod.post,
        feature.toJson(),
        false,
      );

      if (response.errorMessage != null) {
        throw response.error;
      }

      var data = response.data;
      var featResponse = parseFeature(data);
      __environment.features.add(featResponse);
      return featResponse;
    } catch (e) {
      rethrow;
    }
  }

  /// Deleting a feature from the environment.
  ///
  /// `Note` The action here will be reflected to all of the environment users.
  ///
  /// Takes a [feature] data as required parameters.
  /// Returns an updated [SwitchKeysFeature] instance.
  Future<Null> deleteFeature({
    required String featureName,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentDeleteFeature,
      [__environment.environmentKey.toString(), featureName],
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
      int idx = __environment.features.indexWhere(
        (element) => element.name == featureName,
      );
      __environment.features.removeAt(idx);
      return null;
    } catch (e) {
      rethrow;
    }
  }

  /// Updates an existing feature in the environment.
  ///
  /// `Note` The action here will be reflected to all of the environment users.
  ///
  /// Takes a [featureName] and [feature] data as required parameters.
  /// Returns an updated [SwitchKeysFeature] instance.
  Future<SwitchKeysFeature> updateFeature({
    required String featureName,
    required SwitchKeysFeatureData feature,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentUpdateFeature,
      [
        __environment.environmentKey.toString(),
        featureName,
      ],
    );

    try {
      var response = await SwitchKeysRequest.call(
        apiUrl,
        SwitchKeysRequestMethod.put,
        feature.toJson(),
        false,
      );

      if (response.errorMessage != null) {
        throw response.error;
      }

      var data = response.data;
      var featResponse = parseFeature(data);

      int idx = __environment.features.indexWhere(
        (element) => element.name == featureName,
      );
      __environment.features[idx] = featResponse;

      return featResponse;
    } catch (e) {
      rethrow;
    }
  }

  /// Adds a user to the environment.
  ///
  /// Takes a [user] as a required parameter.
  /// Returns a [SwitchKeysEnvironmentUserResponse] containing information about the added user.
  Future<SwitchKeysEnvironmentUserResponse> addUser({
    required SwitchKeysEnvironmentsUser user,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsKeyAddUser,
      [
        __environment.environmentKey.toString(),
      ],
    );
    String deviceType =
        (user.device?.deviceType == SwitchKeyUserDeviceType.android)
            ? 'android'
            : 'iphone';

    Map<String, dynamic> payload = {
      "username": user.username,
      "device": {
        "device_type": deviceType,
        "version": user.device?.version,
      },
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
      var userResponse = parseEnvironmentUser(data);
      __environment.users.add(userResponse);
      return userResponse;
    } catch (e) {
      rethrow;
    }
  }

  /// Removes a user from the environment.
  ///
  /// Takes a [user] as a required parameter.
  /// Returns a list of remaining [SwitchKeysEnvironmentUserResponse].
  Future<List<SwitchKeysEnvironmentUserResponse>> removeUser({
    required SwitchKeysEnvironmentsUser user,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentsKeyRemoveUser,
      [
        __environment.environmentKey.toString(),
      ],
    );

    Map<String, dynamic> payload = {"username": user.username};

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

      __environment.users.removeWhere(
        (user_) => user_.username == user.username,
      );

      return __environment.users;
    } catch (e) {
      rethrow;
    }
  }
}
