from google.appengine.ext import ndb
from models.comment_model import CommentModel

__author__ = 'Ashkan'


class UserModel(ndb.Model):
    user_id = ndb.IntegerProperty(indexed=True)
    likes = ndb.IntegerProperty(repeated=True)
    comments = ndb.StructuredProperty(CommentModel, repeated=True)
