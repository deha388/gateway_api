import hashlib

from sqlalchemy import Column, Integer, String, DATETIME, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import database

Base = declarative_base()


class RouteAlias(Base):
    __tablename__ = 'route_aliases'
    id = Column(Integer, primary_key=True)

    route = Column(String)
    alias_name = Column(String)


class RouteAliasRepository:
    def __init__(self):
        self.engine = database.get()
        session_fn = sessionmaker(bind=self.engine)
        self.session = session_fn()

    def get_by_route(self, route_name):
        query = self.session.query(RouteAlias).filter(RouteAlias.route == route_name).all()
        return query
