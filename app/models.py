from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

MainBase = declarative_base()
CacheBase = declarative_base()

class User(MainBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)


class Item(MainBase):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer)


class Cache(CacheBase):
    __tablename__ = "cache"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String)


class TestCache(CacheBase):
    __tablename__ = "test_cache"
    id = Column(Integer, primary_key=True, index=True)
    otherData = Column(String)


main_metadata = MainBase.metadata
cache_metadata = CacheBase.metadata