import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'package:switchkeys/src/utils/parser.dart';

class SwitchKeyAuth {
  const SwitchKeyAuth();

  Future<SwitchKeysAuthResponse> login(
      {required String email, required String password}) async {
    // API endpoint for login
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.login);
    // Request body
    Map<String, String> body = {
      "email": email,
      "password": password,
    };

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      // Make POST request
      http.Response response = await http.post(Uri.parse(apiUrl),
          headers: headers, body: jsonEncode(body));

      if (response.statusCode == 200) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysAuthResponse authLoginResponse = parseAuth(data["results"]);

        var config = SwitchKeysTokensConfig();
        config.writeTokens(
            accessToken: authLoginResponse.accessToken,
            refreshToken: authLoginResponse.refreshToken);
        return authLoginResponse;
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['detail'];
        throw ResponseError("Login failed: $message ${data0['error'] ?? ''}");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }

  Future<SwitchKeysAuthResponse> register({
    required String firstName,
    required String lastName,
    required String email,
    required String password,
    required UserTypeEnum memberType,
  }) async {
    // API endpoint for registration
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.signUp);

    // Request body
    Map<String, String> body = {
      "first_name": firstName,
      "last_name": lastName,
      "email": email,
      "password": password,
      "user_type": memberType.value,
    };

    // Headers
    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    try {
      // Make POST request
      http.Response response = await http.post(Uri.parse(apiUrl),
          headers: headers, body: jsonEncode(body));

      if (response.statusCode == 201) {
        Map<String, dynamic> data = jsonDecode(response.body);
        SwitchKeysAuthResponse authRegisterResponse =
            parseAuth(data["results"]);

        var config = SwitchKeysTokensConfig();
        config.writeTokens(
            accessToken: authRegisterResponse.accessToken,
            refreshToken: authRegisterResponse.refreshToken);

        return authRegisterResponse;
      } else {
        // Check if response contains an error message
        Map<String, dynamic> data = jsonDecode(response.body);
        String errorMessage = data['message'] ?? 'User creation failed';
        throw ResponseError(
            "Registration failed: $errorMessage ${data['error'] ?? ''}");
      }
    } catch (e) {
      // Exception occurred, handle error
      throw ResponseError(e.toString());
    }
  }
}
