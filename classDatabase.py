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
        self._db_questionList = []

        log.debug("Database class initalized!")

    def db_set_file_name(self, path):
        log = logging.getLogger(self.db_set_file_name.__name__)

        self._db_file_path = path

        log.debug("db_file_path set to: " + self._db_file_path)

    def db_get_file_name(self):
        return self._db_file_path

    def db_read(self):
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

        self.__db_parse()

        return True

    def db_create(self, name, path):
        log = logging.getLogger(self.db_create.__name__)

        if name:
            log.debug("Create new db with path: " + path)

            self._db_name = name
            self._db_file_path = path

            self.__db_set_timestamp(str(datetime.datetime.now()))
            self.db_set_author("Nobody")

            meta_data = {'name': self._db_name,
                         'author': self.db_get_author(),
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
        log = logging.getLogger(self.db_set_name.__name__)

        self._db_name = name

        log.debug("_db_name set to: " + self._db_name)

    def db_get_name(self):
        return self._db_name

    def db_set_author(self, author):
        log = logging.getLogger(self.db_set_author.__name__)

        self._db_author = author

        log.debug("_db_author set to: " + self._db_author)

    def db_get_author(self):
        return self._db_author

    def __db_set_timestamp(self, stamp):
        log = logging.getLogger(self.__db_set_timestamp.__name__)

        self._db_timestamp = stamp

        log.debug("_db_timestamp set to: " + self._db_timestamp)

    def db_get_timestamp(self):
        return self._db_timestamp

    def db_get_questionsList(self):
        return self._db_questionList

    def __db_parse(self):
        log = logging.getLogger(self.__db_parse.__name__)

        self._db_questionList = []

        if len(self._db_content) < 1:
            log.debug("Fail, database content is empty!")
        else:
            for item in self._db_content:
                if "Question" in item:
                    self._db_questionList.append(item)

        self._db_questionList.sort()

        self.db_set_author(self._db_content['author'])
        self.db_set_name(self._db_content['name'])
        self.__db_set_timestamp(self._db_content['timestamp'])

    def db_del_question(self, node_name):
        log = logging.getLogger(self.db_del_question.__name__)

        log.debug("Node to remove: " + node_name)

        del self._db_content[node_name]
        self._db_questionList.remove(node_name)

    def db_find_free_id(self):
        log = logging.getLogger(self.db_find_free_id.__name__)

        id = 1

        flag = False

        while id < 255:
            pattern = "Question" + str(id) + "@"
            for item in self._db_content:
                if pattern in item != -1:
                    log.debug(item)
                    flag = True
                    break
                else:
                    flag = False

            if flag is True:
                id += 1
            else:
                log.debug("Found free id = " + str(id))

                return id

        log.debug("No free id!!")
        return False

    def db_add_question(self, id):
        log = logging.getLogger(self.db_add_question.__name__)

        node_name = "Question" + str(id) + "@" + self.db_get_name()

        question_pattern = {node_name: {"id": id, "descr": ""}}

        log.debug("Adding question: " + node_name)

        self._db_questionList.append(node_name)
        self._db_content.update(question_pattern)

    def db_dump_to_file(self):
        log = logging.getLogger(self.db_dump_to_file.__name__)

        f = open(self._db_file_path, "w")
        f.write(json.dumps(self._db_content, sort_keys=True, indent=4))
        f.close()

        log.debug("DB dumped to file " + self.db_get_file_name())

    def db_get_questions_cnt(self):
        return len(self._db_questionList)
