from models.comment_model import CommentModel

__author__ = 'Ashkan'

from google.appengine.ext import ndb


class LevelModel(ndb.Model):
    level_id = ndb.IntegerProperty(indexed=True)
    name = ndb.StringProperty()
    comments = ndb.StructuredProperty(CommentModel, repeated=True)
    likes = ndb.IntegerProperty(repeated=True)
    comments_count = ndb.ComputedProperty(lambda self: len(self.comments))
    likes_count = ndb.ComputedProperty(lambda self: len(self.likes))

