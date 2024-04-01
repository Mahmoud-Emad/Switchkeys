import logging

class SwitchKeyLogger:
    __logger = None

    @staticmethod
    def get_logger():
        if SwitchKeyLogger.__logger is None:
            SwitchKeyLogger.__logger = logging.getLogger(__name__)
            SwitchKeyLogger.__logger.setLevel(logging.INFO)
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            SwitchKeyLogger.__logger.addHandler(console_handler)
        return SwitchKeyLogger.__logger