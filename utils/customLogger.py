import logging
import os

class logGen:
    @staticmethod
    def loggen():
        log_dir = "./Logs/"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True
        )
        logger = logging.getLogger()
        return logger
