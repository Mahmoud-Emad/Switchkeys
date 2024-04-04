import 'dart:io';
import 'package:ini/ini.dart';

/// Manages writing and reading access and refresh tokens to/from a configuration file.
class SwitchKeysTokensConfig {
  late TokensType tokens =
      TokensType(accessToken: '', refreshToken: ''); // Initialize tokens
  final Config config =
      Config(); // The configuration object to manage the config file.
  final File file = File("config.ini"); // Reference to the config file.
  final String sectionName =
      "TOKENS"; // Name of the section in the config file.

  /// Constructs a new SwitchKeysTokensConfig instance.
  SwitchKeysTokensConfig();

  /// Writes the access and refresh tokens to the config file.
  ///
  /// This method creates or updates the 'config.ini' file in the current directory.
  /// It adds a section named 'TOKENS' to the config file and sets the access
  /// and refresh tokens under this section.
  /// Returns a string representation of the config after writing.
  TokensType writeTokens(
      {required String accessToken, required String refreshToken}) {
    config.addSection(sectionName);
    config.set(sectionName, "accessToken", accessToken);
    config.set(sectionName, "refreshToken", refreshToken);
    file.writeAsStringSync(config.toString());

    if (!file.existsSync()) {
      file.createSync();
    }

    tokens.accessToken = accessToken;
    tokens.refreshToken = refreshToken;

    return tokens;
  }

  /// Reads access and refresh tokens from the config file.
  ///
  /// Returns a string representation of the tokens after reading.
  TokensType readTokens() {
    final lines = file.readAsLinesSync();
    final config = Config.fromStrings(lines);
    var accessToken = config.get(sectionName, 'accessToken');
    var refreshToken = config.get(sectionName, 'refreshToken');

    if (accessToken != null && refreshToken != null) {
      tokens.accessToken = accessToken;
      tokens.refreshToken = refreshToken;
    }

    return tokens;
  }
}

/// Holds access and refresh tokens.
class TokensType {
  late String accessToken;
  late String refreshToken;
  TokensType({required this.accessToken, required this.refreshToken});
}
