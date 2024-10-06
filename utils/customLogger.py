import logging

class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename="./Logs/automation.log",
            format = '%(asctime)s -%(name)s -%(levelname)s - %(message)s',
            datefmt = '%m/%d/%Y %I:%M:%S', level = logging.INFO)
        logger = logging.getLogger()
        return logger