import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:switchkeys/src/api/response/response.dart';

class SwitchKeysRequest {
  static Future<SwitchKeysResponse> call(
    String url,
    String method,
    Map<String, dynamic> data,
    String? token,
  ) async {
    try {
      Map<String, String> headers = {};
      if (token != null) {
        headers["Authorization"] = "Bearer $token";
      }

      late http.Response response;

      switch (method) {
        case "GET":
          response = await http.get(Uri.parse(url), headers: headers);
          break;
        case "POST":
          response = await http.post(Uri.parse(url),
              headers: headers, body: jsonEncode(data));
          break;
        case "PUT":
          response = await http.put(Uri.parse(url),
              headers: headers, body: jsonEncode(data));
          break;
        case "DELETE":
          response = await http.delete(Uri.parse(url), headers: headers);
          break;
        default:
          throw ArgumentError("Invalid method provided.");
      }

      final Map<String, dynamic> responseContent =
          jsonDecode(response.body.toString());

      if (response.statusCode >= 200 && response.statusCode < 400) {
        return SwitchKeysResponse(
          statusCode: response.statusCode,
          message: responseContent["message"],
          data: responseContent["results"],
        );
      } else if (response.statusCode >= 400) {
        return SwitchKeysResponse(
          statusCode: response.statusCode,
          errorMessage: responseContent["detail"] ?? responseContent["message"],
          error: responseContent["error"],
        );
      } else {
        return SwitchKeysResponse(
          statusCode: response.statusCode,
          errorMessage: responseContent["detail"],
        );
      }
    } catch (e) {
      return SwitchKeysResponse(
        statusCode: 500,
        errorMessage: e.toString(),
      );
    }
  }
}
