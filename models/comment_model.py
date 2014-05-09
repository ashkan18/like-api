from google.appengine.ext import ndb

__author__ = 'root'


class CommentModel(ndb.Model):
    """
    This class defines a Comment model, a comment has actual text,
    id of the user who wrote the comment
    id of the level that we are writing review for it
    date the comment was received
    """
    text = ndb.StringProperty()
    user_id = ndb.IntegerProperty()
    level_id = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now=True)

