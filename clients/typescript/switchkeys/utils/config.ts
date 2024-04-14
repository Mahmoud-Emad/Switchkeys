import * as fs from "fs";
import { SwitchKeysTokensResponse } from "../api/response/types";
import { SwitchKeysLogger } from "./logger";

class SwitchKeysConfig {
  private logger: SwitchKeysLogger = new SwitchKeysLogger();


  public check(configFile: string = "config.ini"): boolean {
    if (!fs.existsSync(configFile)) {
      this.logger.error(`Config file '${configFile}' does not exist.`);
      return false;
    }

    try {
      const data = fs.readFileSync(configFile, "utf-8");
      const config = JSON.parse(data);

      if (!config.TOKENS) {
        this.logger.error("No [TOKENS] section found in the config file.");
        return false;
      }

      const { access_token, refresh_token } = config.TOKENS;
      if (access_token && refresh_token) {
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

  public load(configFile: string = "config.ini"): SwitchKeysTokensResponse {
    try {
      const data = fs.readFileSync(configFile, "utf-8");
      const config = JSON.parse(data);

      if (config.TOKENS) {
        const { access_token, refresh_token } = config.TOKENS;
        if (access_token && refresh_token) {
          return new SwitchKeysTokensResponse(access_token, refresh_token);
        } else {
          this.logger.warning(
            "Tokens not found in the config file, maybe you have to login first."
          );
          return new SwitchKeysTokensResponse();
        }
      } else {
        this.logger.warning(
          "No [TOKENS] section found in the config file, maybe you have to login first."
        );
        return new SwitchKeysTokensResponse();
      }
    } catch (error) {
      this.logger.error(`Error reading config file: ${error}`);
      return new SwitchKeysTokensResponse();
    }
  }

  public write(
    access_token: string,
    refresh_token: string,
    configFile: string = "config.ini"
  ): void {
    const configData = JSON.stringify({
      TOKENS: { access_token, refresh_token },
    });

    try {
      fs.writeFileSync(configFile, configData);
      this.logger.info(`Tokens written to: ${configFile}.`);
    } catch (error) {
      this.logger.error(`Error writing tokens to: ${configFile} due: ${error}`);
    }
  }
}

export default SwitchKeysConfig;
