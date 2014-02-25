#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient

print("connecting db and get itinerary db")
client = MongoClient('localhost', 27017)
db = client.itinerary_db

print("remove all data")
db.places.remove()
db.stops.remove()
db.itinerarys.remove()

print("init places")
db.places.insert([
	{"pno": "CN", "name": "中国", "name_en": "China", "ptype": 1, "coord_type": "wgs-84", "longitude": 1111, "latitude": 222, "description": "Country", "pics": "/static/img/china.png", "opentime": None, "address": "China", "telephone": None, "expense": None},
	{"pno": "SH", "name": "上海", "name_en": "Shanghai", "ptype": 3, "coord_type": "wgs-84", "longitude": 121.473701, "latitude": 31.230416, "description": "Shanghai", "pics": "/static/img/shanghai.png", "opentime": None, "address": "Shanghai, China", "telephone": None, "expense": None},
	{"pno": "HZ", "name": "杭州", "name_en": "Hangzhou", "ptype": 3, "coord_type": "wgs-84", "longitude": 120.15507000000002, "latitude": 30.274085, "description": "Shanghai", "pics": "/static/img/hangzhou.png", "opentime": None, "address": "Hangzhou, China", "telephone": None, "expense": None},
	{"pno": "SZ", "name": "苏州", "name_en": "Suzhou", "ptype": 3, "coord_type": "wgs-84", "longitude": 120.58531600000003, "latitude": 31.298886, "description": "Shanghai", "pics": "/static/img/suzhou.png", "opentime": None, "address": "Suzhou, China", "telephone": None, "expense": None},
	{"pno": "XTD", "name": "新天地", "name_en": "Xintiandi", "ptype": 4, "coord_type": "wgs-84", "longitude": 121.4778867, "latitude": 31.2120803, "description": "Xintiandi", "pics": "/static/img/xintiandi.jpg", "opentime": "8:00", "address": "380 Huangpi South Road, Huangpu, Shanghai, China", "telephone": "021 5383 8833", "expense": "expense info"},
	{"pno": "CHM", "name": "城隍庙", "name_en": "Shanghai Town God s Temple", "ptype": 4, "coord_type": "wgs-84", "longitude": 121.49504389999993, "latitude": 31.2257772, "description": "Shanghai Town God s Temple", "pics": "/static/img/chenghuangmiao.jpg", "opentime": "8:00", "address": "249 Fangbang Middle Road, Huangpu, Shanghai, China", "telephone": "021 6328 4494", "expense": "expense info"},
	{"pno": "YY", "name": "豫园", "name_en": "Yu Garden", "ptype": 4, "coord_type": "wgs-84", "longitude": 121.49251920000006, "latitude": 31.2291828, "description": "Yu Garden", "pics": "/static/img/yugarden.jpg", "opentime": "8:00", "address": "218 Anren Street, Huangpu, Shanghai, China", "telephone": "021 6326 0830", "expense": "expense info"},
	{"pno": "MM", "name": "上海博物馆", "name_en": "Shanghai Museum", "ptype": 4, "coord_type": "wgs-84", "longitude": 121.47552780000001, "latitude": 31.22833069999999, "description": "Shanghai Museum", "pics": "/static/img/shmuseum.jpg", "opentime": "8:00", "address": "01 Renmin Avenue, Huangpu, Shanghai, China", "telephone": "021 6372 3500", "expense": "expense info"},
	{"pno": "BUND", "name": "外滩", "name_en": "The Bund", "ptype": 4, "coord_type": "wgs-84", "longitude": 121.49017559999993, "latitude": 31.2379312, "description": "The Bund", "pics": "/static/img/bund.jpg", "opentime": "24:00", "address": "Zhongshan East 1st Road, Huangpu, Shanghai, China", "telephone": None, "expense": "expense info"},
	{"pno": "OP", "name": "东方明珠塔", "name_en": "Oriental Pearl TV Tower", "ptype": 4, "coord_type": "wgs-84", "longitude": 121.52136599999994, "latitude": 31.2320903, "description": "Oriental Pearl TV Tower", "pics": "/static/img/orientalpear.jpg", "opentime": "8:00", "address": "1 Centural Avenue, Pudong, Shanghai, China", "telephone": "021 5879 1888", "expense": "expense info"}
])

db.places.update({"pno": "XTD"}, {"$set": {"description": "<div>this is html <i>description</i>.</div>"}})
db.places.update({"pno": "CHM"}, {"$set": {"description": "<div>this is html <i>description</i>.</div>"}})
db.places.update({"pno": "YY"}, {"$set": {"description": "<div>this is html <i>description</i>.</div>"}})
db.places.update({"pno": "MM"}, {"$set": {"description": "<div>this is html <i>description</i>.</div>"}})
db.places.update({"pno": "BUND"}, {"$set": {"description": "<div>this is html <i>description</i>.</div>"}})
db.places.update({"pno": "OP"}, {"$set": {"description": "<div>this is html <i>description</i>.</div>"}})

print("init stops")
db.stops.insert([
	{"sno": "S1", "place_no": "CN", "itinerary": "I0", "day_number": 1, "stop_number": 1, "sub_itinerary": "I1", "note": "my memo"},
	{"sno": "S111", "place_no": "SH", "itinerary": "I1", "day_number": 1, "stop_number": 1, "sub_itinerary": "I2", "note": "my memo"},
	{"sno": "S112", "place_no": "SH", "itinerary": "I1", "day_number": 1, "stop_number": 1, "sub_itinerary": "I3", "note": "my memo"},
	{"sno": "S12", "place_no": "HZ", "itinerary": "I1", "day_number": 2, "stop_number": 1, "sub_itinerary": "I4", "note": "my memo"},
	{"sno": "S13", "place_no": "SZ", "itinerary": "I1", "day_number": 3, "stop_number": 1, "sub_itinerary": "I5", "note": "my memo"},
	{"sno": "S3", "place_no": "XTD", "itinerary": "I2", "day_number": 1, "stop_number": 1, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S4", "place_no": "CHM", "itinerary": "I2", "day_number": 1, "stop_number": 2, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S6", "place_no": "MM", "itinerary": "I2", "day_number": 2, "stop_number": 1, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S7", "place_no": "BUND", "itinerary": "I2", "day_number": 2, "stop_number": 2, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S8", "place_no": "OP", "itinerary": "I2", "day_number": 2, "stop_number": 3, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S9", "place_no": "OP", "itinerary": "I3", "day_number": 1, "stop_number": 1, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S10", "place_no": "BUND", "itinerary": "I3", "day_number": 1, "stop_number": 2, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S11", "place_no": "MM", "itinerary": "I3", "day_number": 1, "stop_number": 3, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S12", "place_no": "YY", "itinerary": "I3", "day_number": 2, "stop_number": 1, "sub_itinerary": None, "note": "my memo"},
	{"sno": "S14", "place_no": "XTD", "itinerary": "I3", "day_number": 2, "stop_number": 2, "sub_itinerary": None, "note": "my memo"}
])

print("init itinerarys")
db.itinerarys.insert([
	{"ino": "I0", "name": "亚洲", "description": "itinerary China", "duration": 15},
	{"ino": "I1", "name": "中国", "description": "itinerary China", "duration": 15},
	{"ino": "I2", "name": "上海游1", "description": "itinerary Shanghai 1", "duration": 5},
	{"ino": "I3", "name": "上海游2", "description": "itinerary Shanghai 2", "duration": 5},
	{"ino": "I4", "name": "杭州", "description": "itinerary Shanghai 1", "duration": 3},
	{"ino": "I5", "name": "苏州", "description": "itinerary Shanghai 2", "duration": 2}
])

print("init db successful")