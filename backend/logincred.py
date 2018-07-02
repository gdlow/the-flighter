#logincred

from .logindb import LoginDatabase

class UserManagement(object):
	def __init__(self):
		#connect; read and write to db
		self.LoginDatabase = LoginDatabase()
		self.LoginDatabase.connect()

	def register(self,fname,lname,email,pword,home):
		self.LoginDatabase.register(fname=fname,lname=lname,email=email,pword=pword,home=home)

	def gateway(self,email,pword):
		correctpword = self.LoginDatabase.getpword(email=email)
		return correctpword

	def insertprices(self, time_stamp, origin, destination, outbounddeparture, outboundarrival, outboundroute, inbounddeparture, inboundarrival, inboundroute, price):
		self.LoginDatabase.insertprices(time_stamp=time_stamp, origin=origin, destination=destination, outbounddeparture=outbounddeparture, outboundarrival=outboundarrival, outboundroute=outboundroute, inbounddeparture=inbounddeparture, inboundarrival=inboundarrival, inboundroute=inboundroute, price=price)


