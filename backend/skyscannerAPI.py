# Python implementation. Written by Gerald The Shark - 2017.
import requests
import json
import time

URL = "http://partners.api.skyscanner.net/apiservices"
API_KEY = "ha696723343441434034465280137182"
print ("Your API Key: {}".format(str(API_KEY)))

#define locales - the language you want the response in
def locales(apikey=API_KEY):
	r = requests.get(URL + "/reference/v1.0/locales" + "?apiKey=" + apikey)
	rep = r.json()
	return rep

#define countries
def countries(apikey=API_KEY):
	r = requests.get(URL + "/reference/v1.0/countries/" + "en-GB" + "?apiKey=" + apikey)
	rep = r.json()
	return rep

#define places
def places(country,currency,query,apikey=API_KEY):
	r = requests.get(URL + "/autosuggest/v1.0/" + country + "/" + currency + "/" + "en-GB?query=" + query + "&apiKey=" + apikey)
	rep = r.json()
	print (rep)
	return rep

def getquote(country,currency,locale,originPlace,destinationPlace,outboundPartialDate,inboundPartialDate,apikey=API_KEY):
	r = requests.get(URL + "/browsequotes/v1.0/" + country + "/" + currency + "/" + locale + "/" + originPlace + "/" + destinationPlace + "/" + outboundPartialDate + "/" + inboundPartialDate + "?apiKey=" + apikey, headers={'Accept':'application/json'})
	rep = r.json()
	print (rep)
	return rep

def liveprices(country,currency,originPlace,destinationPlace,outbounddate,inbounddate,locale="en-GB",locationSchema="iata",adults=1,apikey=API_KEY):
	payload = {'country':country,'currency':currency,'locale':locale,'originPlace':originPlace,'destinationPlace':destinationPlace,'outboundDate':outbounddate,'inboundDate':inbounddate,'adults':adults,'apiKey':apikey}
	r1 = requests.post(URL + "/pricing/v1.0", headers={'Content-Type':'application/x-www-form-urlencoded','Accept':'application/json'},data=payload)
	rep1 = r1.headers['Location']
#	print (rep1)
	time.sleep(5)
	r2 = requests.get(rep1 + "?apiKey=" + apikey,headers={'Accept':'application/json'})
	rep2 = r2.json()
#	print (rep2)
	return rep2

def getCityId(city):
	queryresults = places("UK","GBP",query=city)
	return queryresults['Places'][0]['CityId']

#Test
#places("UK","GBP","new york")
print (getCityId("orlando"))
#getquote("UK","GBP","en-GB","LOND-sky","JFK-sky","2018-01","2018-01")
#getquote("UK","GBP","en-GB","LTN-sky","JFK-sky","2018-01","2018-01")
#liveprices("UK","GBP","LTN-sky","JFK-sky","2018-01-01","2018-01-07")

