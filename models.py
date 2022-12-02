import datetime
from sqlalchemy import Column, Boolean, Integer, String, DateTime
from database import Base


class ZefixSearches(Base):
    __tablename__ = 'zefix_searches'
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    results = Column(Integer)
    time_created = Column(DateTime(timezone=True), default=datetime.datetime.now())

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean)