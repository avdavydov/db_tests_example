import re

import sqlalchemy.engine
from sqlalchemy import create_engine


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class EngineFactory(metaclass=MetaSingleton):
    connections, db_urls_local = ({},)*2
    user, passw, stand, db_name = (None,)*4


    def get_engine(self, db_name, schema_name=None) -> sqlalchemy.engine.Engine:
        self.db_name = db_name

        if None in (self.user, self.stand, self.db_name):
            raise ValueError('Не заданы обязательные параметры: stand, user, db_name')

        if self.connections.get((db_name, schema_name)):
            return self.connections.get((db_name, schema_name))
        else:
            url = self.get_postgres_url(db_name)
            if schema_name:
                self.connections[(db_name, schema_name)] = create_engine(url, echo=False, echo_pool=False,
                                                                         connect_args={
                                                                             'options': f'-csearch_path={schema_name}'})
            else:
                self.connections[(db_name, schema_name)] = create_engine(url, echo=False, echo_pool=False)
        return self.connections[(db_name, schema_name)]

    def dispose_engines(self) -> None:
        for engine in self.connections.values():
            engine.dispose()
        self.connections = {}

    def add_local_db(self, base_name, url):
        self.db_urls_local[base_name] = url

    def get_postgres_url(self, base_name) -> str:
        stand = self.stand.lower()
        user = self.user
        passw = self.passw

        if stand == 'localhost':
            if self.db_urls_local.get(base_name):
                url = f'postgresql://{user}:{passw}@{self.db_urls_local.get(base_name)}' if passw else f'postgresql://{user}@{self.db_urls_local.get(base_name)}'
                return url
            else:
                raise ValueError(f'''URL для параметров stand={stand}, db_name='{base_name}' не найден ''')
