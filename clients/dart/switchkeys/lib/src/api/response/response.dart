class SwitchKeysResponse {
  final int statusCode;
  final dynamic data;
  final String? message;
  final String? errorMessage;
  final dynamic error;

  SwitchKeysResponse({
    required this.statusCode,
    this.data,
    this.message,
    this.errorMessage,
    this.error,
  });

  @override
  String toString() {
    return 'SwitchKeysResponse(status_code: $statusCode, data: $data, error_message: $errorMessage, error: $error, message: $message)';
  }
}
