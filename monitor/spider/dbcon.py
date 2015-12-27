# encoding: utf-8
import MySQLdb
from base import *
class dbCon:
	def __init__(self,address,user,password,dbName):
		self.address = address
		self.user = user
		self.password = password
		self.dbName = dbName
	def getDb():
		try:
			db = MySQLdb.connect("localhost","cg","123456","online_opinion" )
			return db
		except:
			base = new Base()
			base.write('./','db.log','数据库连接失败')
			print "数据库连接失败";
