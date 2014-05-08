from google.appengine.ext import ndb

__author__ = 'root'


class CommentModel(ndb.Model):
    text = ndb.StringProperty()
    user_id = ndb.IntegerProperty()
    level_id = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now=True)

