import lxml.html, lxml.etree, urllib2, cherrypy, json, time, os

# config
PATH = os.path.abspath(os.path.dirname(__file__))
url = 'http://vanswarpedtour.com/dates'
cachedJSON = 'cities.json'

class Root(object):
    @cherrypy.expose
    def cities(self):
        try:
            mtime = os.path.getctime(cachedJSON)
        except OSError:
            mtime = 0
        if (time.time() - mtime > 3600):
            tree = lxml.html.fromstring(urllib2.urlopen(url).read())
            elements = tree.find_class("location")
            e = []
            for element in elements:
                e.append(element.xpath('text()')[1].strip())
            e.reverse()
            fp = open(cachedJSON, 'w')
            fp.write(json.dumps(e[:5]))
            fp.close()
            return json.dumps(e[:5])
        else:
            return open(cachedJSON).read()

cherrypy.tree.mount(Root(), '/', config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
            },
    })

cherrypy.engine.start()
cherrypy.engine.block()
