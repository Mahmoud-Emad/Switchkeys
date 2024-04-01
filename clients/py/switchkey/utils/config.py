import configparser
import os
from switchkey.api.response.types import SwitchKeyTokensResponse
from switchkey.utils.logger import SwitchKeyLogger


class SwitchKeyConfig:
    """
    SwitchKeyConfig class handles loading and writing tokens from/to a configuration file.

    Attributes:
        None

    Methods:
        check(config_file='config.ini'): Check if the config file is exist and contains the tokens.
        load(config_file='config.ini'): Loads access and refresh tokens from the specified configuration file.
        write(access_token, refresh_token, config_file='config.ini'): Writes access and refresh tokens to the specified configuration file.
    """

    def __init__(self):
        self.logger = SwitchKeyLogger.get_logger()

    def check(self, config_file="config.ini"):
        """
        Check if the configuration file exists and contains the required values.

        Args:
            config_file (str): Path to the configuration file. Default is 'config.ini'.

        Returns:
            bool: True if the config file exists and contains the required values, False otherwise.
        """

        if not os.path.exists(config_file):
            self.logger.error(f"Config file '{config_file}' does not exist.")
            return False

        config = configparser.ConfigParser()
        config.read(config_file)
        if "TOKENS" not in config:
            self.logger.error("No [TOKENS] section found in the config file.")
            return False

        access_token = config["TOKENS"].get("access_token")
        refresh_token = config["TOKENS"].get("refresh_token")
        if access_token and refresh_token:
            self.logger.info("Config file contains access and refresh tokens.")
            return True
        else:
            self.logger.error(
                "Access token or refresh token not found in the config file."
            )
            return False

    def load(self, config_file="config.ini") -> SwitchKeyTokensResponse:
        """
        Load access and refresh tokens from the specified configuration file.

        Args:
            config_file (str): Path to the configuration file. Default is 'config.ini'.

        Returns:
            Tuple[str, str]: A tuple containing access token and refresh token.
        """

        config = configparser.ConfigParser()
        config.read(config_file)

        if "TOKENS" in config:
            access_token = config["TOKENS"].get("access_token")
            refresh_token = config["TOKENS"].get("refresh_token")
            if access_token and refresh_token:
                return SwitchKeyTokensResponse(
                    access_token=access_token, refresh_token=refresh_token
                )
            else:
                self.logger.warning(
                    "Tokens not found in the config file, maybe you have to login first."
                )
                return SwitchKeyTokensResponse(access_token=None, refresh_token=None)
        else:
            self.logger.warning(
                "No [TOKENS] section found in the config file, maybe you have to login first"
            )
            return SwitchKeyTokensResponse(access_token=None, refresh_token=None)

    def write(self, access_token, refresh_token, config_file="config.ini"):
        """
        Write access and refresh tokens to the specified configuration file.

        Args:
            access_token (str): Access token to be written.
            refresh_token (str): Refresh token to be written.
            config_file (str): Path to the configuration file. Default is 'config.ini'.

        Returns:
            configparser.ConfigParser: ConfigParser object containing the updated configuration.
        """
        config = configparser.ConfigParser()
        config["TOKENS"] = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        try:
            with open(config_file, "w") as configfile:
                config.write(configfile)
            self.logger.info("Tokens written to %s:", config_file)
        except Exception as e:
            self.logger.error("Error writing tokens to %s: %s", config_file, str(e))
        return config
