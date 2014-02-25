#-*- coding:utf-8 -*-
import web
from bson import BSON
from bson import json_util
import json
import itinerary

web.config.debug = False

urls = (
    "/signin", "signin",
	"/", "index",
	"/getItinerarysByPlace", "getItinerarysByPlace",
	"/getItinerarysByIno", "getItinerarysByIno",
	"/getItineraryStructure", "getItineraryStructure"
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'login': 0, 'username': 0})
    web.config._session = session
else:
    session = web.config._session
	
render = web.template.render('templates/', globals={'context': session})

def logged():
	if 'login' not in session or session.login == 0:
		session.login = 0
		return False
	else:
		return True

class signin:
	def GET(self):
		if logged():
			return web.seeother('/')
		else:
			return render.signin()
	def POST(self):
		name, passwd = web.input().username, web.input().password
		if (name, passwd) == ("admin", "admin"):
			session.login = 1
			session.username = name
		
			return web.seeother('/')
		else:
			return render.signin()
	
class index:
    def GET(self):
		if logged():
			return render.index()
		else:
			return web.seeother('/signin')
		
class getItinerarysByPlace:
	def POST(self):
		place = web.input().place
		itis = itinerary.getItinerarysByPlace(place)
		return json.dumps(itis, default=json_util.default)

class getItinerarysByIno:
	def POST(self):
		ino = web.input().ino
		itis = itinerary.getItinerarysByIno(ino)
		return json.dumps(itis, default=json_util.default)
		
class getItineraryStructure:
	def POST(self):
		ino = web.input().ino
		iti_structure = itinerary.getItineraryStructure(ino)
		return json.dumps(iti_structure, default=json_util.default)
		
		
def myloadhook():
	global session
	session = web.config._session
		
if __name__ == "__main__":
	app.run()