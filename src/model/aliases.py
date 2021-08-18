from sqlalchemy import Column, Integer, String, DATETIME, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import database

Base = declarative_base()


class Alias(Base):
    __tablename__ = 'aliases'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    service_name = Column(String)
    credentials = Column(String)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    is_active = Column(BOOLEAN, default=1)


class AliasRepository:
    def __init__(self):
        self.engine = database.get()
        session_fn = sessionmaker(bind=self.engine)
        self.session = session_fn()

    def get_by_name(self, name):
        query = self.session.query(Alias).filter(Alias.name == name).all()
        return query
