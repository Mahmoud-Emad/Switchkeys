import 'package:logging/logging.dart';

class SwitchKeysLogger {
  final Logger _logger;

  SwitchKeysLogger._(String name) : _logger = Logger(name);

  static final SwitchKeysLogger _instance = SwitchKeysLogger._('SwitchKeys');

  factory SwitchKeysLogger() {
    return _instance;
  }

  void info(String message) {
    _logger.info(message);
  }

  void warning(String message) {
    _logger.warning(message);
  }

  void error(String message) {
    _logger.severe(message);
  }
}
