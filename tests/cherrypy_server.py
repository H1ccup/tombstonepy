import cherrypy
from tombstone import Tomb

class HelloWorld(object):
    def index(self):
        return Tomb.get_data()

    index.exposed = True

cherrypy.quickstart(HelloWorld())