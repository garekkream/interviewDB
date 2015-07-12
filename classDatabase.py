import json
import os
import logging
import datetime

logging.basicConfig(level=logging.DEBUG)


class database:
    def __init__(self):
        log = logging.getLogger("__init__")
        self._db_file_path = ""
        self._db_name = ""
        self._db_author = ""
        self._db_timestamp = ""
        self._db_content = {}

        log.debug("Database class initalized!")

    def db_set_file_name(self, path):
        log = logging.getLogger(self.db_set_file_name.__name__)

        self._db_file_path = path

        log.debug("db_file_path set to: " + self._db_file_path)

    def db_get_file_name(self):
        return self._db_file_path

    def db_read(self, path):
        log = logging.getLogger(self.db_read.__name__)

        if (len(self._db_file_path) < 1) or (not os.path.exists(self._db_file_path)):
            log.debug("Wrong database path (" + self._db_file_path + ")")
            return False

        try:
            self._db_content = json.loads(open(self._db_file_path, "r").read())
            log.debug("DB loaded!")
        except ValueError:
            log.debug("DB not loaded!")
            return False

        return True

    def db_create(self, name, path):
        log = logging.getLogger(self.db_create.__name__)

        if name:
            log.debug("Create new db with path: " + path)

            self._db_name = name
            self._db_file_path = path + name

            self.db_set_timestamp(str(datetime.datetime.now()))

            meta_data = {'name': self._db_name,
                         'author': "Nobody",
                         'timestamp': self.db_get_timestamp()}

            log.debug("meta_data: " + json.dumps(meta_data))

            f = open(self._db_file_path, "w")
            f.write(json.dumps(meta_data, sort_keys=True, indent=4))
            f.close()

            return True

        else:
            log.debug("Fail to create db! (" + name + ")")
            return False

    def db_set_name(self, name):
        log = logging.debug(self.db_set_name.__name__)

        self._db_name = name

        log.debug("_db_name set to: " + self._db_name)

    def db_get_name(self):
        return self._db_name

    def db_set_author(self, author):
        log = logging.debug(self.db_set_author.__name__)

        self._db_author = author

        log.debug("_db_author set to: " + self._db_author)

    def db_get_author(self):
        return self._db_author

    def __db_set_timestamp(self, stamp):
        log = logging.debug(self.db_set_timestamp.__name__)

        self._db_timestamp = stamp

        log.debug("_db_timestamp set to: " + self._db_timestamp)

    def db_get_timestamp(self):
        return self._db_timestamp
