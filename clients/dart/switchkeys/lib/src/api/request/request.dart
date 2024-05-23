import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:switchkeys/src/api/response/response.dart';
import 'package:switchkeys/src/core/exceptions.dart';
import 'package:switchkeys/src/utils/config.dart';

enum SwitchKeysRequestMethod { get, put, post, delete }

class SwitchKeysRequest {
  static Future<SwitchKeysResponse> call(
    String url,
    SwitchKeysRequestMethod method,
    Map<String, dynamic> data,
    bool? noToken,
  ) async {
    try {
      var response = await SwitchKeysRequest.__request(
        url,
        method,
        data,
        noToken,
      );
      return SwitchKeysRequest.__readResponse(response);
    } catch (error) {
      return SwitchKeysRequest.__readError(error);
    }
  }

  static Future<http.Response> __request(
    String url,
    SwitchKeysRequestMethod method,
    Map<String, dynamic> data,
    bool? noToken,
  ) async {
    Map<String, String> headers = {
      "Content-Type": "application/json",
    };

    if (method != SwitchKeysRequestMethod.get && !(noToken ?? false)) {
      var config = SwitchKeysTokensConfig();
      var accessToken = config.readTokens().accessToken;
      headers["Authorization"] = "Bearer $accessToken";
    }

    late http.Response response;

    switch (method) {
      case SwitchKeysRequestMethod.get:
        response = await http.get(Uri.parse(url), headers: headers);
        break;
      case SwitchKeysRequestMethod.post:
        response = await http.post(Uri.parse(url),
            headers: headers, body: jsonEncode(data));
        break;
      case SwitchKeysRequestMethod.put:
        response = await http.put(Uri.parse(url),
            headers: headers, body: jsonEncode(data));
        break;
      case SwitchKeysRequestMethod.delete:
        response = await http.delete(Uri.parse(url), headers: headers);
        break;
    }

    return response;
  }

  static SwitchKeysResponse __readResponse(http.Response response) {
    try {
      if (response.statusCode == 204) {
        return SwitchKeysResponse(
          statusCode: response.statusCode,
          message: "Deleted!",
          data: {},
        );
      }

      final Map<String, dynamic> responseContent = jsonDecode(response.body);
      if (response.statusCode >= 400) {
        return SwitchKeysRequest.__readError(response);
      } else {
        return SwitchKeysResponse(
          statusCode: response.statusCode,
          message: responseContent["message"],
          data: responseContent["results"],
        );
      }
    } catch (e) {
      return SwitchKeysRequest.__readError(response);
    }
  }

  static SwitchKeysResponse __readError(error) {
    // Check if the error is of type SocketException
    if (error is SocketException) {
      return SwitchKeysResponse(
        statusCode: 500,
        errorMessage: error.message,
        error: SwitchKeysConnectionError(error.message),
      );
    }

    if (error is http.Response) {
      var body = jsonDecode(error.body);
      String message = body['message'] ?? body['detail'];

      if (body['error'] != null) {
        message += "\nError details: \n\t${body['error']}\n";
      }

      return SwitchKeysResponse(
        statusCode: error.statusCode,
        error: ResponseError(message),
        errorMessage: message,
      );
    }

    String message = "An error occurred";
    return SwitchKeysResponse(
      statusCode: 500,
      error: Exception(message),
      errorMessage: message,
    );
  }
}
