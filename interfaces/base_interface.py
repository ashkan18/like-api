import json
import webapp2

__author__ = 'Ashkan'


class BaseInterface(webapp2.RequestHandler):

    def send_response(self, response_object):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(response_object))
