import * as fs from "fs";
import { SwitchKeysLogger } from "./logger";
import { ISwitchKeysAuthTokens } from "./types";
import { ConfigIniParser } from "config-ini-parser";

/**
 * Manages loading and writing tokens from/to a configuration file.
 */
class SwitchKeysConfig {
  private logger: SwitchKeysLogger = new SwitchKeysLogger();
  private parser = new ConfigIniParser();

  /**
   * Checks if the configuration file exists and contains the required values.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   * @returns `true` if the config file exists and contains the required values, `false` otherwise.
   */
  public check(configFile: string = "config.ini"): boolean {
    if (!fs.existsSync(configFile)) {
      this.logger.error(`Config file '${configFile}' does not exist.`);
      return false;
    }
    
    try {
      const content = fs.readFileSync(configFile, "utf-8");
      const config = this.parser.parse(content)

      if (!config.isHaveSection('TOKENS')) {
        this.logger.error("No [TOKENS] section found in the config file.");
        return false;
      }

      const accessToken = config.get("TOKENS", "accessToken");
      const refreshToken = config.get("TOKENS", "refreshToken");

      if (accessToken && refreshToken) {
        this.logger.info("Config file contains access and refresh tokens.");
        return true;
      } else {
        this.logger.error(
          "Access token or refresh token not found in the config file."
        );
        return false;
      }
    } catch (error) {
      this.logger.error(`Error reading config file: ${error}`);
      return false;
    }
  }

  /**
   * Loads access and refresh tokens from the specified configuration file.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   * @returns A `SwitchKeysTokensResponse` object containing the access and refresh tokens.
   */
  public load(configFile: string = "config.ini"): ISwitchKeysAuthTokens {
    try {
      const content = fs.readFileSync(configFile, "utf-8");
      const config = this.parser.parse(content)

      if (config.isHaveSection("TOKENS")) {
        const accessToken = config.get("TOKENS", "accessToken");
        const refreshToken = config.get("TOKENS", "refreshToken");

        if (accessToken && refreshToken) {
          return { accessToken, refreshToken}
        } else {
          this.logger.warning(
            "Tokens not found in the config file, maybe you have to login first."
          );
          return {}
        }
      } else {
        this.logger.warning(
          "No [TOKENS] section found in the config file, maybe you have to login first."
        );
        return {}
      }
    } catch (error) {
      this.logger.error(`Error reading config file: ${error}`);
      return {}
    }
  }

  /**
   * Writes access and refresh tokens to the specified configuration file.
   * @param tokens `ISwitchKeysAuthTokens` object containing the access and refresh tokens.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   */
  public write(
    tokens: ISwitchKeysAuthTokens,
    configFile: string = "config.ini"
  ): void {
    if(tokens.accessToken && tokens.refreshToken){
      this.parser.addSection('TOKENS')
      this.parser.set('TOKENS', 'accessToken', tokens.accessToken)
      this.parser.set('TOKENS', 'refreshToken', tokens.refreshToken)

      try {
        const content = this.parser.stringify()
        fs.writeFileSync(configFile, content);
      } catch (error) {
        this.logger.error(`Error writing tokens to: ${configFile} due: ${error}`);
      }
    } else {
      this.logger.error("The tokens cannot be set to null values. Both the `accessToken` and `refreshToken` fields are currently null.")
    }
  }
}

export default SwitchKeysConfig;
