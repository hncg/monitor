# coding=utf-8
from sqlalchemy import Column, String, Integer, DateTime, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from handler import DBSession

Base = declarative_base()


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    fid = Column(Integer, index=True)

    @classmethod
    def mget(cls):
        return DBSession().query(cls).all()

    @classmethod
    def add(cls, **kwds):
        session = DBSession()
        session.add(cls(**kwds))
        try:
            session.flush()
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise(SQLAlchemyError)
        finally:
            session.close()


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, index=True)
    tid = Column(Integer, index=True)
    type = Column(String(32), index=True)
    title = Column(String(128))
    time_at = Column(DateTime)
    content = Column(Text)
    author = Column(String(128))
    reply_number = Column(Integer)
    read_number = Column(Integer)
    url = Column(String(256))

    @classmethod
    def mget_tids_by_city_id(cls, city_id):
        return DBSession().query(cls.tid). \
            filter(cls.city_id == city_id).all()

    @classmethod
    def mget_latest_time_at(cls):
        return DBSession().query(func.max(cls.time_at), cls.city_id). \
            group_by(cls.city_id).all()

    @classmethod
    def add(cls, **kwds):
        session = DBSession()
        session.add(cls(**kwds))
        try:
            session.flush()
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise(SQLAlchemyError)
        finally:
            session.close()

    @classmethod
    def add_all(cls, articles):
        if not articles:
            return
        session = DBSession()
        session.add_all(articles)
        try:
            session.flush()
            session.commit()
        except SQLAlchemyError:
            session.rollback()
            raise(SQLAlchemyError)
        finally:
            session.close()
