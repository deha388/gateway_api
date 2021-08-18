from datetime import datetime

from sqlalchemy import Column, Integer, String, DATETIME, BOOLEAN, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import database

Base = declarative_base()


class UserRequestLogs(Base):
    __tablename__ = 'user_request_logs'
    id = Column(Integer, primary_key=True)

    username = Column(String)
    alias_name = Column(String)
    request_date = Column(DATETIME, default=datetime.now())
    status = Column(String)


class UserRequestLogsRepository:
    def __init__(self):
        self.engine = database.get()
        session_fn = sessionmaker(bind=self.engine)
        self.session = session_fn()

    def add_log(self, log):
        log = UserRequestLogs(id=log["id"], username=log["username"], alias_name=log["alias_name"], status="0")
        self.session.add(log)
        self.session.commit()

    def update_status(self, log, status_code):
        print(status_code)
        query = self.session.query(UserRequestLogs).filter(UserRequestLogs.id == log["id"])
        query.update({"status": str(status_code)})
        self.session.commit()
