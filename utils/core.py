import json
import logging
import logging.config
from constants.files import FilePath

class Logger():
    with open(FilePath.LOG_FILE.value, "rt") as file:
        config = json.load(file)

    logging.config.dictConfig(config)

    def get_log():
        return logging.getLogger()