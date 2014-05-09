from google.appengine.ext import ndb
from models.comment_model import CommentModel

__author__ = 'Ashkan'


class UserModel(ndb.Model):
    """
    This class defines a user model which has
    id of the user
    likes which is an array of level id
    an array of comment models this user has made
    """
    user_id = ndb.IntegerProperty(indexed=True)
    likes = ndb.IntegerProperty(repeated=True)
    comments = ndb.StructuredProperty(CommentModel, repeated=True)
