import json
import os
import logging

logging.basicConfig(level=logging.DEBUG)

class database:
    def __init__(self):
        log = logging.getLogger("__init__")
        self._db_file_path = ""
        self._db_content = {}

        log.debug("Database class initalized!")

    def db_set_file_name(self, path):
        log = logging.getLogger(self._db_set_file_name.func_name)

        self.db_file_path = path

        log.debug("db_file_path set to: " + self.db_file_path)

    def db_get_file_name(self):
        return self._db_file_path

    def db_read(self, path):
        log = logging.getLogger(self.db_read.func_name)

        if (len(self.db_file_path) < 1) or (not os.path.exists(self.db_file_path)):
            log.debug("Wrong database path (" + self.db_file_path + ")")
            return False

        try:
            self._db_content = json.loads(open(self.db_file_path, "r").read())
            log.debug("DB loaded!")
        except ValueError:
            log.debug("DB not loaded!")
            return False

        return True
