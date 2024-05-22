import 'package:switchkeys/src/api/request/request.dart';
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'package:switchkeys/src/utils/parser.dart';

/// A class that handles authentication for the SwitchKeys API.
///
/// This class provides methods for logging in and registering users,
/// and manages the storage of authentication tokens.
class SwitchKeyAuth {
  const SwitchKeyAuth();

  /// Authenticates a user by logging them in with their email and password.
  ///
  /// Sends a login request to the API and retrieves the access and refresh tokens.
  ///
  /// Throws an error if the authentication fails.
  ///
  /// Parameters:
  /// - [email]: The email address of the user.
  /// - [password]: The password of the user.
  ///
  /// Returns a [SwitchKeysAuthResponse] containing the authentication tokens.
  Future<SwitchKeysAuthResponse> login({
    required String email,
    required String password,
  }) async {
    return await _authenticate(
      apiUrl: SwitchKeysRoutes.getRoute(EndPoints.login),
      payload: {
        "email": email,
        "password": password,
      },
      method: SwitchKeysRequestMethod.post,
    );
  }

  /// Registers a new user with the provided details.
  ///
  /// Sends a registration request to the API and retrieves the access and refresh tokens.
  ///
  /// Throws an error if the registration fails.
  ///
  /// Parameters:
  /// - [firstName]: The first name of the user.
  /// - [lastName]: The last name of the user.
  /// - [email]: The email address of the user.
  /// - [password]: The password for the user account.
  /// - [memberType]: The type of user (e.g., admin, regular user).
  ///
  /// Returns a [SwitchKeysAuthResponse] containing the authentication tokens.
  Future<SwitchKeysAuthResponse> register({
    required String firstName,
    required String lastName,
    required String email,
    required String password,
    required UserTypeEnum memberType,
  }) async {
    return await _authenticate(
      apiUrl: SwitchKeysRoutes.getRoute(EndPoints.signUp),
      payload: {
        "first_name": firstName,
        "last_name": lastName,
        "email": email,
        "password": password,
        "user_type": memberType.value,
      },
      method: SwitchKeysRequestMethod.post,
    );
  }

  /// Private method to handle the common authentication logic.
  ///
  /// Sends an authentication request to the specified API endpoint with the provided payload.
  ///
  /// Throws an error if the authentication fails.
  ///
  /// Parameters:
  /// - [apiUrl]: The URL of the API endpoint.
  /// - [payload]: The request payload containing authentication details.
  ///
  /// Returns a [SwitchKeysAuthResponse] containing the authentication tokens.
  Future<SwitchKeysAuthResponse> _authenticate({
    required String apiUrl,
    required Map<String, String> payload,
    required SwitchKeysRequestMethod method,
  }) async {
    var response = await SwitchKeysRequest.call(
      apiUrl,
      method,
      payload,
      true,
    );

    if (response.errorMessage != null) {
      throw response.error;
    }

    var data = response.data;
    SwitchKeysAuthResponse authResponse = parseAuth(data);
    var config = SwitchKeysTokensConfig();
    config.writeTokens(
      accessToken: authResponse.accessToken,
      refreshToken: authResponse.refreshToken,
    );
    return authResponse;
  }
}
