import 'package:switchkeys/src/api/request/request.dart';
import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/parser.dart';

class SwitchKeysEnvironmentUsers {
  final SwitchKeysEnvironmentResponse __environment;
  const SwitchKeysEnvironmentUsers(this.__environment);

  SwitchKeysEnvironmentUserServices getUser({required String username}) {
    SwitchKeysEnvironmentUserResponse user = __environment.users
        .where(
          (user) => user.username == username,
        )
        .first;

    return SwitchKeysEnvironmentUserServices(__environment, user);
  }
}

class SwitchKeysEnvironmentUserServices {
  final SwitchKeysEnvironmentResponse __environment;
  final SwitchKeysEnvironmentUserResponse __user;

  const SwitchKeysEnvironmentUserServices(this.__environment, this.__user);

  /// User username.
  String get username => __user.username;

  /// User device.
  SwitchKeyUserDevice get device => __user.device;

  /// User ID.
  int get id => __user.id;

  /// User features.
  List<SwitchKeysFeature> get features => __user.features;

  SwitchKeysFeature getFeature({required String featureName}) {
    try {
      return __user.features
          .where(
            (feature) => feature.name == featureName,
          )
          .first;
    } catch (e) {
      throw SwitchKeysRecordNotFoundError("Feature not found.");
    }
  }

  bool hasFeature({required String featureName}) {
    try {
      var feat = getFeature(featureName: featureName);
      if (feat.id != 0) {
        return true;
      }
    } catch (e) {
      return false;
    }
    return false;
  }

  Future<SwitchKeysFeature> setFeature({
    required SwitchKeysFeatureData feature,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(
      EndPoints.environmentUserAddFeature,
      [
        __environment.environmentKey,
        __user.username,
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
      SwitchKeysFeature featResponse = parseFeature(data);

      if (featResponse.id == 0) {
        throw ResponseError("Response Error.");
      }

      return featResponse;
    } catch (e) {
      rethrow;
    }
  }
}
