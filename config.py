import json
import sys

module = sys.modules[__name__]
config_var = "_config"


class Config(object):
    def __init__(self, data):
        self.__dict__ = data
        self._data = data

    @property
    def database(self):
        if isinstance(self.__dict__['database'], Database):
            return self.__dict__['database']
        return Database(self._data['database'])

    @property
    def app(self):
        if isinstance(self.__dict__['app'], App):
            return self.__dict__['app']
        return App(self._data['app'])

    @property
    def services(self):
        return self.__dict__['services']


class Database:
    def __init__(self, data):
        self.__dict__ = data
        self._data = data

    @property
    def mysql(self):
        if isinstance(self.__dict__['mysql'], Mysql):
            return self.__dict__['mysql']
        return Mysql(self._data['mysql'])

    @property
    def sqlite(self):
        if isinstance(self.__dict__['sqlite'], Sqlite):
            return self.__dict__['sqlite']
        return Mysql(self._data['sqlite'])

    @property
    def default(self):
        return self.__dict__['default']


class Sqlite:
    def __init__(self, data):
        self.__dict__ = data

    @property
    def path(self):
        return self.__dict__['path']


class Mysql:
    def __init__(self, data):
        self.__dict__ = data

    @property
    def host(self):
        return self.__dict__['host']

    @property
    def port(self):
        return self.__dict__['port']

    @property
    def username(self):
        return self.__dict__['username']

    @property
    def password(self):
        return self.__dict__['password']

    @property
    def database(self):
        return self.__dict__['database']


class App:
    def __init__(self, data):
        self.__dict__ = data

    @property
    def host(self):
        return self.__dict__['host']

    @property
    def port(self):
        return self.__dict__['port']

    @property
    def encrypt_key(self):
        return self.__dict__['encrypt_key']


def load(config_file="config.json"):
    with open(config_file) as cf:
        cf_content = json.load(cf)
        config_obj = Config(cf_content)
        setattr(module, config_var, config_obj)


def get(config_file="config.json"):
    var_config = getattr(module, config_var, None)
    if var_config:
        return var_config

    load(config_file=config_file)
    return getattr(module, config_var, None)
