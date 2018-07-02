# uses skyscannerAPI.py to apply results
import requests
import json
import time

from .skyscannerAPI import places
from .skyscannerAPI import locales
from .skyscannerAPI import countries
from .skyscannerAPI import getquote
from .skyscannerAPI import liveprices
from .skyscannerAPI import getCityId

def getBestPlaceMatch(allplaces):
    #places(...)
    listplaces = allplaces['Places']
    bestmatch = listplaces[0]
    return bestmatch['PlaceId']
    
def getBestLiveQuote(lveprices):
    itin = lveprices['Itineraries']
    #cheapest at index 0
    cheapestitin = itin[0]
    outboundLegId = cheapestitin['OutboundLegId']
    inboundLegId = cheapestitin['InboundLegId']
    outboundLeg = None;
    inboundLeg = None;
    for leg in lveprices['Legs']:
        if leg['Id'] == outboundLegId:
            outboundLeg = leg
        elif leg['Id'] == inboundLegId:
            inboundLeg = leg
    outboundDep = outboundLeg['Departure']
    outboundArr = outboundLeg['Arrival']
    inboundDep = inboundLeg['Departure']
    inboundArr = inboundLeg['Arrival']
    lowestPrice = cheapestitin['PricingOptions'][0]['Price']
    deeplink = cheapestitin['PricingOptions'][0]['DeeplinkUrl']
    segs = lveprices['Segments']
    carriers = lveprices['Carriers']
    placeslist = lveprices['Places']
    outboundSeg = outboundLeg['SegmentIds']
    outboundRoute = ""
    for segments in outboundSeg:
        currseg = segs[segments]
        startStatNo = currseg['OriginStation']
        endStatNo = currseg['DestinationStation']
        carrierId = currseg['Carrier']
        startStat = ""
        endStat = ""
        currcarrier = ""
        for place in placeslist:
            if place['Id'] == startStatNo:
                startStat = place['Name']
            elif place['Id'] == endStatNo:
                endStat = place['Name']
        for carrier in carriers:
            if carrier['Id'] == carrierId:
                currcarrier = carrier['Name']
        outboundRoute = outboundRoute + startStat + " -> " + endStat + " (" + currcarrier  + "), "

    inboundSeg = inboundLeg['SegmentIds']
    inboundRoute = ""
    for segments in inboundSeg:
        currseg = segs[segments]
        startStatNo = currseg['OriginStation']
        endStatNo = currseg['DestinationStation']
        carrierId = currseg['Carrier']
        startStat = ""
        endStat = ""
        currcarrier = ""
        for place in placeslist:
            if place['Id'] == startStatNo:
                startStat = place['Name']
            elif place['Id'] == endStatNo:
                endStat = place['Name']
        for carrier in carriers:
            if carrier['Id'] == carrierId:
                currcarrier = carrier['Name']
        inboundRoute = inboundRoute + startStat + " -> " + endStat + " (" + currcarrier  + "), "
    
    bestquote = {
        'Price': lowestPrice,
        'DeeplinkUrl': deeplink,
        'OutboundDeparture' : outboundDep,
        'OutboundArrival' : outboundArr,
        'OutboundRoute' : outboundRoute,
        'InboundDeparture' : inboundDep,
        'InboundArrival' : inboundArr,
        'InboundRoute' : inboundRoute,
    }
    print (bestquote)
    return bestquote
    

#Test
#doesnt seem to work if LOND-sky is used as city not airport
#ldnjfkprices = liveprices("UK","GBP","LTN-sky","JFK-sky","2018-01-01","2018-01-07")
#getBestLiveQuote(ldnjfkprices)

