import { ConfigIniParser } from "config-ini-parser";
import { ISwitchKeysAuthTokensResponse } from "../api/response/types";
import { SwitchKeysValidationError } from "../core/exceptions";
import * as fs from "fs";

/**
 * Manages loading and writing tokens from/to localStorage or a configuration file.
 */
class SwitchKeysConfig {
  private static readonly CONFIG_KEY = "switchKeysConfig";

  /**
   * Checks if the configuration file exists and contains the required values.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   * @returns `true` if the config file exists and contains the required values, `false` otherwise.
   */
  private checkFS(configFile: string = "config.ini"): boolean {
    if (!fs.existsSync(configFile)) {
      throw new SwitchKeysValidationError(`Config file '${configFile}' does not exist.`);
    }

    try {
      const parser = new ConfigIniParser();
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
        throw new SwitchKeysValidationError("Access token or refresh token not found in the config file.");
      }
    } catch (error) {
      throw new SwitchKeysValidationError(`Error reading config file: ${error}`);
    }
  }

  /**
   * Checks if the localStorage contains the required values.
   * @returns `true` if the config exists and contains the required values, `false` otherwise.
   */
  private checkLocalStorage(): boolean {
    const config = localStorage.getItem(SwitchKeysConfig.CONFIG_KEY);

    if (!config) {
      throw new SwitchKeysValidationError("Config does not exist in localStorage. Please try to login before using any of SwitchKeys services.");
    }

    try {
      const parsedConfig = JSON.parse(config);

      if (!parsedConfig.TOKENS) {
        throw new SwitchKeysValidationError("No [TOKENS] section found in the config.");
      }

      const accessToken = parsedConfig.TOKENS.accessToken;
      const refreshToken = parsedConfig.TOKENS.refreshToken;

      if (accessToken && refreshToken) {
        console.info("Config contains access and refresh tokens.");
        return true;
      } else {
        throw new SwitchKeysValidationError("Access token or refresh token not found in the config.");
      }
    } catch (error) {
      throw new SwitchKeysValidationError(`Error reading config: ${error}`);
    }
  }

  /**
   * Checks if the localStorage or configuration file contains the required values.
   * @returns `true` if the config exists and contains the required values, `false` otherwise.
   */
  public check(): boolean {
    if (typeof localStorage !== 'undefined') {
      return this.checkLocalStorage();
    }
    return this.checkFS();
  }

  /**
   * Loads access and refresh tokens from localStorage.
   * @returns A `SwitchKeysTokensResponse` object containing the access and refresh tokens.
   */
  private loadLocalStorage(): ISwitchKeysAuthTokensResponse {
    try {
      const config = localStorage.getItem(SwitchKeysConfig.CONFIG_KEY);

      if (!config) {
        throw new SwitchKeysValidationError("Config does not exist in localStorage. Please try to login before using any of SwitchKeys services.");
      }

      const parsedConfig = JSON.parse(config);

      if (parsedConfig.TOKENS) {
        const accessToken = parsedConfig.TOKENS.accessToken;
        const refreshToken = parsedConfig.TOKENS.refreshToken;

        if (accessToken && refreshToken) {
          return { accessToken, refreshToken };
        } else {
          console.warn("Tokens not found in the config, maybe you have to login first.");
          return {};
        }
      } else {
        console.warn("No [TOKENS] section found in the config, maybe you have to login first.");
        return {};
      }
    } catch (error) {
      throw new SwitchKeysValidationError(`Error reading config: ${error}`);
    }
  }

  /**
   * Loads access and refresh tokens from the configuration file.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   * @returns A `SwitchKeysTokensResponse` object containing the access and refresh tokens.
   */
  private loadFS(configFile: string = "config.ini"): ISwitchKeysAuthTokensResponse {
    try {
      const parser = new ConfigIniParser();
      const content = fs.readFileSync(configFile, "utf-8");
      const config = parser.parse(content);

      if (config.isHaveSection("TOKENS")) {
        const accessToken = config.get("TOKENS", "accessToken");
        const refreshToken = config.get("TOKENS", "refreshToken");

        if (accessToken && refreshToken) {
          return { accessToken, refreshToken };
        } else {
          console.warn("Tokens not found in the config file, maybe you have to login first.");
          return {};
        }
      } else {
        console.warn("No [TOKENS] section found in the config file, maybe you have to login first.");
        return {};
      }
    } catch (error) {
      throw new SwitchKeysValidationError(`Error reading config file: ${error}`);
    }
  }

  /**
   * Loads access and refresh tokens from localStorage or the configuration file.
   * @returns A `SwitchKeysTokensResponse` object containing the access and refresh tokens.
   */
  public load(): ISwitchKeysAuthTokensResponse {
    if (typeof localStorage !== 'undefined') {
      return this.loadLocalStorage();
    }
    return this.loadFS();
  }

  /**
   * Writes access and refresh tokens to localStorage.
   * @param tokens `ISwitchKeysAuthTokensResponse` object containing the access and refresh tokens.
   * @param remove If `true`, removes the tokens from the config.
   */
  private writeLocalStorage(tokens: ISwitchKeysAuthTokensResponse, remove: boolean = false) {
    try {
      const config = localStorage.getItem(SwitchKeysConfig.CONFIG_KEY);
      const parsedConfig = config ? JSON.parse(config) : {};

      if (tokens.accessToken && tokens.refreshToken) {
        parsedConfig.TOKENS = {
          accessToken: tokens.accessToken,
          refreshToken: tokens.refreshToken
        };
      } else if (remove) {
        delete parsedConfig.TOKENS;
      } else {
        throw new SwitchKeysValidationError("The tokens cannot be set to null values. Both the `accessToken` and `refreshToken` fields are currently null.");
      }

      localStorage.setItem(SwitchKeysConfig.CONFIG_KEY, JSON.stringify(parsedConfig));
    } catch (error) {
      throw new SwitchKeysValidationError(`Error writing config: ${error}`);
    }
  }

  /**
   * Writes access and refresh tokens to the configuration file.
   * @param tokens `ISwitchKeysAuthTokensResponse` object containing the access and refresh tokens.
   * @param remove If `true`, removes the tokens from the config.
   * @param configFile Path to the configuration file. Default is `config.ini`.
   */
  private writeFS(tokens: ISwitchKeysAuthTokensResponse, remove: boolean = false, configFile: string = "config.ini") {
    const parser = new ConfigIniParser();

    if (tokens.accessToken && tokens.refreshToken) {
      parser.addSection('TOKENS');
      parser.set('TOKENS', 'accessToken', tokens.accessToken);
      parser.set('TOKENS', 'refreshToken', tokens.refreshToken);

      try {
        const content = parser.stringify();
        fs.writeFileSync(configFile, content);
      } catch (error) {
        throw new SwitchKeysValidationError(`Error writing tokens to: ${configFile} due: ${error}`);
      }
    } else {
      if (!remove) {
        throw new SwitchKeysValidationError("The tokens cannot be set to null values. Both the `accessToken` and `refreshToken` fields are currently null.");
      } else {
        parser.removeSection('TOKENS');
        const content = parser.stringify();
        fs.writeFileSync(configFile, content);
      }
    }
  }

  /**
   * Writes access and refresh tokens to localStorage or the configuration file.
   * @param tokens `ISwitchKeysAuthTokensResponse` object containing the access and refresh tokens.
   * @param remove If `true`, removes the tokens from the config.
   */
  public write(tokens: ISwitchKeysAuthTokensResponse, remove: boolean = false): void {
    if (typeof localStorage !== 'undefined') {
      return this.writeLocalStorage(tokens, remove);
    }
    return this.writeFS(tokens, remove);
  }
}

export default SwitchKeysConfig;
