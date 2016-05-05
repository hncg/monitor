# coding=utf-8
import sys
sys.path.append('../')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import env
print env.socket
engine = create_engine('mysql://cg:123456@localhost:3306/rednet?charset=utf8&unix_socket=' + env.socket, echo=False) # noqa
DBSession = sessionmaker(bind=engine)
