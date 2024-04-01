import logging

class SwitchKeysLogger:
    __logger = None

    @staticmethod
    def get_logger():
        if SwitchKeysLogger.__logger is None:
            SwitchKeysLogger.__logger = logging.getLogger(__name__)
            SwitchKeysLogger.__logger.setLevel(logging.INFO)
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            SwitchKeysLogger.__logger.addHandler(console_handler)
        return SwitchKeysLogger.__logger