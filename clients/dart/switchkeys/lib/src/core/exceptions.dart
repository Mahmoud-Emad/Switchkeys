import 'package:switchkeys/src/utils/logger.dart';

/// Base class for all kinds of client-side errors.
class Error implements Exception {
  @override
  String toString() {
    return runtimeType.toString();
  }
}

/// Indicates connection error.
class SwitchKeysConnectionError extends Error {
  final String message;

  SwitchKeysConnectionError(this.message);

  @override
  String toString() {
    return message;
  }
}

/// Indicates connection error.
class SwitchKeysRecordNotFoundError extends Error {
  final String message;

  SwitchKeysRecordNotFoundError(this.message);

  @override
  String toString() {
    return message;
  }
}

/// Indicates a broken response package.
class ResponseError extends Error {
  final String message;

  ResponseError(this.message);

  @override
  String toString() {
    return message;
  }
}

/// Indicates a missing authentication.
class AuthenticationError extends Error {
  AuthenticationError() {
    SwitchKeysLogger().error(
        'There are no tokens found in the config file, and none were specified when initializing an instance of the SwitchKeys client. Please ensure that tokens are provided either in the config file or passed during initialization.');
  }
}

/// Indicates that a feature is not enabled.
class FeatureNotEnabled implements Exception {
  final String message;
  final dynamic errors;

  FeatureNotEnabled(this.message, {this.errors});

  @override
  String toString() {
    return 'FeatureNotEnabled: $message';
  }
}
