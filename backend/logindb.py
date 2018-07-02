#logindb.py
import sqlalchemy

class LoginDatabase(object):
	def __init__(self):
		pass

	def connect(self):
		'''Returns a connection and a metadata object'''
		# We connect with the help of the PostgreSQL URL
		self.url = 'postgres://ywwmuoyqpyjugw:521f628886d87f8298cf5a844c03b5da8b2dace51acb87b1f3b99cc9d97e0b87@ec2-184-73-249-56.compute-1.amazonaws.com:5432/dd8qit7ha3emp5'

		# The return value of create_engine() is our connection object
		self.con = sqlalchemy.create_engine(self.url, client_encoding='utf8')

		# We then bind the connection to MetaData()
		self.meta = sqlalchemy.MetaData(bind=self.con, reflect=True)
		#table
		self.db = self.meta.tables['userbase']

	def register(self, fname, lname, email, pword, home):
		insert_statement = self.db.insert().values(fname=fname,lname=lname,email=email,pword=pword,home=home)
		self.con.connect().execute(insert_statement)

	def getpword(self, email):
		result_set = self.con.connect().execute("SELECT pword FROM userbase where email = '{}'".format(email))
		for row in result_set:
			correctpword = (row[0])
		return correctpword

	def insertprices(self, time_stamp, origin, destination, outbounddeparture, outboundarrival, outboundroute, inbounddeparture, inboundarrival, inboundroute, price):
		self.db = self.meta.tables['prices'] #connect with prices table
		insert_statement = self.db.insert().values(time_stamp=time_stamp, origin=origin, destination=destination, outbounddeparture=outbounddeparture, outboundarrival=outboundarrival, outboundroute=outboundroute, inbounddeparture=inbounddeparture, inboundarrival=inboundarrival, inboundroute=inboundroute, price=price)
		self.con.connect().execute(insert_statement)