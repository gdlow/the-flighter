import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender(object):
	def __init__(self):
		pass
	def sendemail(self,toaddr,destination,outbounddeparture,outboundarrival,outboundroute,inbounddeparture,inboundarrival,inboundroute,price,link):
		"""
		Sends an email to recipient alerting him of offers!
		"""
		fromaddr = "theflighterupc@gmail.com"
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "[THEFLIGHTER] CHEAP DEALS ARE AVAILABLE FOR YOU M8"
		 
		part1 = "  Greetings my lad, \
        \n  Here's a good deal we found for you from {} to {}\
		\n      \
		\n - Outbound Departure: \
		\n \t {}\
		\n - Outbound Arrival: \
		\n \t {}\
		\n - Outbound Route: \
		\n \t {}\
		\n - Inbound Departure: \
		\n \t {}\
		\n - Inbound Arrival: \
		\n \t {}\
		\n - Inbound Route: \
		\n \t {}\
		\n      \
		\n - PRICE: £ \
		\n \t {} ".format("London Luton",destination,outbounddeparture,outboundarrival,outboundroute,inbounddeparture,inboundarrival,inboundroute,price)
		part2 = """
		<html>
		<head></head>
		<body>
		<p>Link Here:</p>
		<a href={}>skyscanner</a>
		</body>
		</html>
		""".format(link)
		part3 = "\n \
		\n \
		\n Signing off,\
		\n Your Beloved team at TheFlighter"
		
		msg.attach(MIMEText(part1, 'plain'))
		msg.attach(MIMEText(part2, 'html'))
		msg.attach(MIMEText(part3, 'plain'))
		
		
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "anisishere")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()

#test
#callfunction = EmailSender()
#callfunction.sendemail("upcthefighter@gmail.com","JFK New York","2018-01-01 19:00:00","2018-01-02 00:45:00","Through the midlands","2018-01-07 16:45:00","2018-01-08 00:00:00","Through the nordics","500","www.skyscanner.net")