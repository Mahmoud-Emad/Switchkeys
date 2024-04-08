import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/api/routes.dart';
import 'package:http/http.dart' as http;
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';
import 'dart:convert';

import 'package:switchkeys/src/utils/parser.dart';

class SwitchKeysUsers {
  final _config = SwitchKeysTokensConfig();

  Future<SwitchKeysUserResponse> getUserById({
    required int userId,
  }) async {
    String apiUrl = SwitchKeysRoutes.getRoute(EndPoints.usersId, [
      userId.toString(),
    ]);

    var tokens = _config.readTokens();

    Map<String, String> headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer ${tokens.accessToken}",
    };

    try {
      http.Response response = await http.get(
        Uri.parse(apiUrl),
        headers: headers,
      );

      if (response.statusCode < 400) {
        Map<String, dynamic> data = jsonDecode(response.body);
        return parseUser(data["results"]);
      } else {
        Map<String, dynamic> data0 = jsonDecode(response.body);
        String message = data0['message'] ?? data0['detail'];
        throw ResponseError("Failed to get user due: $message");
      }
    } catch (e) {
      throw ResponseError(e.toString());
    }
  }
}
