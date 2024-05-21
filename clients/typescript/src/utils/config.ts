import * as fs from "fs";
import { ConfigIniParser } from "config-ini-parser";
import { ISwitchKeysAuthTokensResponse } from "../api/response/types";
import { SwitchKeysValidationError } from "../core/exceptions";

/**
 * Manages loading and writing tokens from/to a configuration file.
 */
class SwitchKeysConfig {
  /**
   * Checks if the configuration file exists and contains the required values.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   * @returns `true` if the config file exists and contains the required values, `false` otherwise.
   */
  public check(configFile: string = "config.ini"): boolean {
    if (!fs.existsSync(configFile)) {
      throw new SwitchKeysValidationError(`Config file '${configFile}' does not exist.`);
    }

    try {
      const parser = new ConfigIniParser(); // Create a new instance of ConfigIniParser
      const content = fs.readFileSync(configFile, "utf-8");
      const config = parser.parse(content);

      if (!config.isHaveSection('TOKENS')) {
        throw new SwitchKeysValidationError("No [TOKENS] section found in the config file.");
      }

      const accessToken = config.get("TOKENS", "accessToken");
      const refreshToken = config.get("TOKENS", "refreshToken");

      if (accessToken && refreshToken) {
        console.info("Config file contains access and refresh tokens.");
        return true;
      } else {
        throw new SwitchKeysValidationError(
          "Access token or refresh token not found in the config file."
        );
      }
    } catch (error) {
      throw new SwitchKeysValidationError(`Error reading config file: ${error}`);
    }
  }

  /**
   * Loads access and refresh tokens from the specified configuration file.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   * @returns A `SwitchKeysTokensResponse` object containing the access and refresh tokens.
   */
  public load(configFile: string = "config.ini"): ISwitchKeysAuthTokensResponse {
    try {
      const parser = new ConfigIniParser(); // Create a new instance of ConfigIniParser
      const content = fs.readFileSync(configFile, "utf-8");
      const config = parser.parse(content);

      if (config.isHaveSection("TOKENS")) {
        const accessToken = config.get("TOKENS", "accessToken");
        const refreshToken = config.get("TOKENS", "refreshToken");

        if (accessToken && refreshToken) {
          return { accessToken, refreshToken }
        } else {
          console.warn(
            "Tokens not found in the config file, maybe you have to login first."
          );
          return {}
        }
      } else {
        console.warn(
          "No [TOKENS] section found in the config file, maybe you have to login first."
        );
        return {}
      }
    } catch (error) {
      throw new SwitchKeysValidationError(`Error reading config file: ${error}`);
    }
  }

  /**
   * Writes access and refresh tokens to the specified configuration file.
   * @param tokens `ISwitchKeysAuthTokensResponse` object containing the access and refresh tokens.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   * @param remove a boolean parameter to remove the tokens from the config file.
   */
  public write(
    tokens: ISwitchKeysAuthTokensResponse,
    configFile: string = "config.ini",
    remove: boolean =false
  ): void {
    const parser = new ConfigIniParser();

    if (tokens.accessToken && tokens.refreshToken) {
      parser.addSection('TOKENS')
      parser.set('TOKENS', 'accessToken', tokens.accessToken)
      parser.set('TOKENS', 'refreshToken', tokens.refreshToken)

      try {
        const content = parser.stringify()
        fs.writeFileSync(configFile, content);
      } catch (error) {
        throw new SwitchKeysValidationError(`Error writing tokens to: ${configFile} due: ${error}`);
      }
    } else {
      if(!remove){
        throw new SwitchKeysValidationError("The tokens cannot be set to null values. Both the `accessToken` and `refreshToken` fields are currently null.");
      } else {
        parser.removeSection('TOKENS');
        const content = parser.stringify()
        fs.writeFileSync(configFile, content);
      }
    }
  }
}

export default SwitchKeysConfig;
