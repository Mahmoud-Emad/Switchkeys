import 'dart:io';
import 'package:ini/ini.dart';

/// Manages writing and reading access and refresh tokens to/from a configuration file.
class SwitchKeysTokensConfig {
  late TokensType tokens = TokensType(accessToken: '', refreshToken: '');
  final Config config = Config();
  final File file = File("config.ini");
  final String sectionName = "TOKENS";

  SwitchKeysTokensConfig();

  /// Writes the access and refresh tokens to the config file.
  ///
  /// - This method creates or updates the 'config.ini' file in the current directory.
  /// - It adds a section named 'TOKENS' to the config file and sets the access
  /// and refresh tokens under this section.
  /// - Returns a string representation of the config after writing.
  TokensType writeTokens({
    required String accessToken,
    required String refreshToken,
  }) {
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

  removeTokens() {
    // var duration = const Duration(seconds: 5);
    // sleep(duration);

    config.removeSection(sectionName);
    file.writeAsStringSync(config.toString());

    if (!file.existsSync()) {
      file.createSync();
    }
  }
}

/// Holds access and refresh tokens.
class TokensType {
  late String accessToken;
  late String refreshToken;
  TokensType({required this.accessToken, required this.refreshToken});
}
