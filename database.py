import sys
import config
import sqlalchemy

module = sys.modules[__name__]
singleton_var = "_database"


def load():
    config_obj = config.get()
    default_db = config_obj.database.default
    db_config = getattr(config_obj.database, default_db)

    switcher = {
        "mysql": load_mysql,
        "sqlite": load_sqlite
    }
    database_load_fn = switcher.get(default_db, "There is no database configuration")
    if isinstance(database_load_fn, str):
        raise database_load_fn

    database_load_fn(db_config)


def get_connection_string(db_config):
    return f'mysql://{db_config.username}:{db_config.password}@{db_config.host}/{db_config.database}'


def load_mysql(db_config):
    conn_str = get_connection_string(db_config)
    try:
        engine = sqlalchemy.create_engine(conn_str)
        setattr(module, singleton_var, engine)
    except Exception as exc:
        raise exc


def load_sqlite(db_config):
    try:
        engine = sqlalchemy.create_engine(db_config.path)
        setattr(module, singleton_var, engine)
    except Exception as exc:
        raise exc


def get():
    var_database = getattr(module, singleton_var, None)
    if var_database:
        return var_database

    load()
    return getattr(module, singleton_var, None)
