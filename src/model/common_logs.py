from datetime import datetime

from sqlalchemy import Column, Integer, String, DATETIME, BOOLEAN, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import database

Base = declarative_base()


class CommonLogs(Base):
    __tablename__ = 'common_logs'
    id = Column(Integer, primary_key=True)

    route = Column(String)
    log_message = Column(String)
    log_date = Column(DATETIME, default=datetime.now())


class CommonLogsRepository:
    def __init__(self):
        self.engine = database.get()
        session_fn = sessionmaker(bind=self.engine)
        self.session = session_fn()

    def add_log(self, log):
        log = CommonLogs(id=log["id"], route=log["route"], log_message=log["log_message"])
        self.session.add(log)
        self.session.commit()
