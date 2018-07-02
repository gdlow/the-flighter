import os
from flask import Flask, request
from flask_cors import CORS
from backend import logincred, dataParsing
from time import gmtime, strftime
import sendalertemail
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
	return "Hello, World!"

@app.route("/register/", methods=['GET', 'POST'])
def register():
	"""
	Register a new user to the service

	Parameters:

	- fname : First Name of the person
	- lname : Last Name of the person
	- email : email address
	- pword : password stored
	- home : person's home city
	Data must be JSON encoded.
	"""
	if request.method == 'GET':
		r = {"error": "Unexpected request; Expected POST."}
		r = json.dumps(r)
		return r
	elif request.method == 'POST':
		fname = request.form['fname']
		lname = request.form['lname']
		email = request.form['email']
		pword = request.form['pword']
		home = request.form['home']
		#connect to db
		UserManagement = logincred.UserManagement()
		UserManagement.register(fname=fname,lname=lname,email=email,pword=pword,home=home)
		r = {"Success": "You have been successfully registered."}
		r = json.dumps(r)
		return r

@app.route("/login/", methods=['GET','POST'])
def login():
	"""
	Login Gateway

	Post email and password to this URL endpoint. If the entries match database, authenticated and return 1. Else return 0 and ask for reauthentication.

	Parameters:
	- email: email address
	- pword : password entered
	Data must be JSON encoded.
	"""
	if request.method == 'GET':
		r = {"error": "Unexpected request; Expected POST."}
		r = json.dumps(r)
		return r

	elif request.method == 'POST':
		email = request.form['email']
		pword = request.form['pword']
		#connect to db
		UserManagement = logincred.UserManagement()
		if pword == UserManagement.gateway(email=email,pword=pword):
			r = {"Auth":"Correct"}
			r = json.dumps(r)
			return r
		else:
			r = {"Auth":"Wrong"}
			r = json.dumps(r)
			return r

@app.route("/destinations/", methods=['GET','POST'])
def inputdestinations():
	"""
	Input Destination, Outbound Date, Inbound Date.
	Service creates a new table for each parameter setting.
	Computes moving average and sends alert email to email address when threshold met.
	"""
	if request.method == 'GET':
		r = {"error": "Unexpected request; Expected POST."}
		r = json.dumps(r)
		return r

	elif request.method == 'POST':
		destination1 = request.form['destination1']
		destination1 = dataParsing.getCityId(destination1)
		outbounddate1 = request.form['outbounddate1'] #MM/DD/YYYY
		tokens1 = [word for word in outbounddate1.strip().split('/')]
		outbounddate1 = tokens1[2]+'-'+tokens1[0]+'-'+tokens1[1] #YYYY-MM-DD
		inbounddate1 = request.form['inbounddate1'] #MM/DD/YYYY
		tokens2 = [word for word in inbounddate1.strip().split('/')]
		inbounddate1 = tokens2[2]+'-'+tokens2[0]+'-'+tokens2[1] #YYYY-MM-DD
		destination2 = request.form['destination2']
		destination2 = dataParsing.getCityId(destination2)
		inbounddate2 = request.form['inbounddate2'] #MM/DD/YYYY
		tokens3 = [word for word in inbounddate2.strip().split('/')]
		inbounddate2 = tokens3[2]+'-'+tokens3[0]+'-'+tokens3[1] #YYYY-MM-DD
		outbounddate2 = request.form['outbounddate2'] #MM/DD/YYYY
		tokens4 = [word for word in outbounddate2.strip().split('/')]
		outbounddate2 = tokens4[2]+'-'+tokens4[0]+'-'+tokens4[1] #YYYY-MM-DD
		destination3 = request.form['destination3']
		destination3 = dataParsing.getCityId(destination3)
		outbounddate3 = request.form['outbounddate3'] #MM/DD/YYYY
		tokens5 = [word for word in outbounddate3.strip().split('/')]
		outbounddate3 = tokens5[2]+'-'+tokens5[0]+'-'+tokens5[1] #YYYY-MM-DD
		inbounddate3 = request.form['inbounddate3'] #MM/DD/YYYY
		tokens6 = [word for word in inbounddate3.strip().split('/')]
		inbounddate3 = tokens6[2]+'-'+tokens6[0]+'-'+tokens6[1] #YYYY-MM-DD
		#connect to db
		UserManagement = logincred.UserManagement()
		#get live prices for all 3 destinations (in the future, implement a cron job. for now, just demo with fake data)
		destination1info = dataParsing.liveprices("UK","GBP","LTN-sky",destination1,outbounddate1,inbounddate1)
		destination1parsedinfo = dataParsing.getBestLiveQuote(destination1info)
		#insert destination information into DB
		UserManagement.insertprices(time_stamp=strftime("%Y-%m-%d %H:%M:%S", gmtime()),origin="LTN-sky", destination=destination1, outbounddeparture=destination1parsedinfo['OutboundDeparture'], outboundarrival=destination1parsedinfo['OutboundArrival'], outboundroute=destination1parsedinfo['OutboundRoute'], inbounddeparture=destination1parsedinfo['InboundDeparture'], inboundarrival=destination1parsedinfo['InboundArrival'], inboundroute=destination1parsedinfo['InboundRoute'], price=destination1parsedinfo['Price'])
		#repeat for 2
	 	#get live prices for all 3 destinations (in the future, implement a cron job. for now, just demo with fake data)
		destination2info = dataParsing.liveprices("UK","GBP","LTN-sky",destination2,outbounddate2,inbounddate2)
		destination2parsedinfo = dataParsing.getBestLiveQuote(destination2info)
		#insert destination information into DB
		UserManagement.insertprices(time_stamp=strftime("%Y-%m-%d %H:%M:%S", gmtime()),origin="LTN-sky", destination=destination2, outbounddeparture=destination2parsedinfo['OutboundDeparture'], outboundarrival=destination2parsedinfo['OutboundArrival'], outboundroute=destination2parsedinfo['OutboundRoute'], inbounddeparture=destination2parsedinfo['InboundDeparture'], inboundarrival=destination2parsedinfo['InboundArrival'], inboundroute=destination2parsedinfo['InboundRoute'], price=destination2parsedinfo['Price'])
		#repeat for 3
		#get live prices for all 3 destinations (in the future, implement a cron job. for now, just demo with fake data)
		destination3info = dataParsing.liveprices("UK","GBP","LTN-sky",destination3,outbounddate3,inbounddate3)
		destination3parsedinfo = dataParsing.getBestLiveQuote(destination3info)
		#insert destination information into DB
		UserManagement.insertprices(time_stamp=strftime("%Y-%m-%d %H:%M:%S", gmtime()),origin="LTN-sky", destination=destination3, outbounddeparture=destination3parsedinfo['OutboundDeparture'], outboundarrival=destination3parsedinfo['OutboundArrival'], outboundroute=destination3parsedinfo['OutboundRoute'], inbounddeparture=destination3parsedinfo['InboundDeparture'], inboundarrival=destination3parsedinfo['InboundArrival'], inboundroute=destination3parsedinfo['InboundRoute'], price=destination3parsedinfo['Price'])

		#LOGIC OF CODE HERE
		#For demo purposes: send destination 1 details to email
		email1 = sendalertemail.EmailSender()
		email1.sendemail("upcthefighter@gmail.com", destination1, destination1parsedinfo['OutboundDeparture'],destination1parsedinfo['OutboundArrival'],destination1parsedinfo['OutboundRoute'],destination1parsedinfo['InboundDeparture'],destination1parsedinfo['InboundArrival'],destination1parsedinfo['InboundRoute'],destination1parsedinfo['Price'],destination1parsedinfo['DeeplinkUrl'])

		#IRL - set up cron job, compute moving average and set threshold
		# scheduler = BlockingScheduler()
		# scheduler.add_executor('processpool')
		# scheduler.add_job("separate sql insertion job here", 'cron', hour='0,4,8,12,16,20')
		# print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

		# try:
		# 	scheduler.start()
		# except (KeyboardInterrupt, SystemExit):
		# 	pass
		# UserManagement.readtolist() #using pandas
		# UserManagement.insertMA() #insert into statmements using moving average formula - sum(:)/len(x)
		# if destination1parsedinfo['Price'] <= 0.8* MA:
			# email1 = sendalertemail.EmailSender()
			# email1.sendemail("upcthefighter@gmail.com", destination1, destination1parsedinfo['OutboundDeparture'],destination1parsedinfo['OutboundArrival'],destination1parsedinfo['OutboundRoute'],destination1parsedinfo['InboundDeparture'],destination1parsedinfo['InboundArrival'],destination1parsedinfo['InboundRoute'],destination1parsedinfo['Price'],destination1parsedinfo['DeeplinkUrl'])
			# # email address can be changed to something more flexible



		#Response
		r = {"Success": "Your entries have been recorded."}
		r = json.dumps(r)
		return r

		
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 33507))
	app.run(host='0.0.0.0', port=port, debug=True)
	#app.run()

