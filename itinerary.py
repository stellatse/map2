import pymongo
from pymongo import MongoClient

print("connecting db and get itinerary db")
client = MongoClient('localhost', 27017)
db = client.itinerary_db


# get simple place object
def _getPlace(pno):
	place = db.places.find_one({"pno": pno})
	return place


# get simple itinerary object
def _getItinerary(ino):
	iti = db.itinerarys.find_one({"ino": ino})
	return iti

# get stops for the itinerary, grouped by day number and stops number
def _getStops(ino):
	ret = []
	names = []
	day = 1
	ret.append([])
	for stop in db.stops.find({"itinerary": ino}).sort([("day_number", pymongo.ASCENDING), ("stop_number", pymongo.ASCENDING)]):
		place = _getPlace(stop["place_no"])
		if place == None: continue
		
		name = place["name"]
		duration = 0
		
		nameExist = False
		# if multiple same places, only use one place
		try:
			if names.index(name) > -1:
				nameExist = True
		except:
			nameExist = False
		
		if nameExist:
			continue
			
		names.append(name)
		
		# if multiple same places, use itinerary name as place
		if stop["sub_itinerary"] != None:
			iti = _getItinerary(stop["sub_itinerary"])
			if iti != None:
				#name = iti["name"]
				duration = iti["duration"]
		
		
		#duration = _calculateDuration(place["pno"])
		if stop["day_number"] != day:
			day = day+1
			ret.append([]);
	
		obj = {"stop": stop, "place": place, "name": name, "duration": duration}
		ret[day-1].append(obj)

	return ret

def _calculateDuration(pno):
	days = 0
	for stop in db.stops.find({"place_no": pno}):
		if stop["sub_itinerary"] != None:
			iti = _getItinerary(stop["sub_itinerary"])
			days = days + iti["duration"]
	
	return days
	
# get itinerary list for the place
def getItinerarysByPlace(name):
	# get place no
	place = db.places.find_one({"name": name})
	
	itineraryList = []
	if (place != None):
		return getPlaceItinerarys(place)

	return []

# get itinerary list for the place
def getItinerarysByIno(ino):
	# get 
	parentStop = db.stops.find_one({"sub_itinerary": ino})
	if parentStop != None:
		# get place no
		place = db.places.find_one({"pno": parentStop["place_no"]})
		# get itinerary list for the place
		itineraryList = []
		if (place != None):
			return getPlaceItinerarys(place)

	return []
	
# get itinerary list for the place by place
def getPlaceItinerarys(place):
	itineraryList = []
	# get subitinerary list
	for stop in db.stops.find({"place_no": place["pno"]}):
		if stop["sub_itinerary"] != None:
			#itiObj = {"place": place, "name": place["name"], "stop": stop}
			itiObj = {"parent_ino": stop["itinerary"]}
			itinerary = _getItinerary(stop["sub_itinerary"])
			#itiObj["itinerary"] = itinerary
			itiObj["ino"] = itinerary["ino"]
			itineraryList.append(itiObj)
	return itineraryList
	
# get itinerary structure including stops and places
def getItineraryStructure(ino):
	iti = db.itinerarys.find_one({"ino": ino})
	
	if iti != None:
		obj = {}
		stops = _getStops(iti["ino"])
		obj["itinerary"] = iti
		obj["stops"] = stops
		return obj
		
	return None
	
#structure = getItineraryStructure("I2")
#print(json.dumps(structure, default=json_util.default))
#json.loads(..., object_hook=json_util.object_hook)