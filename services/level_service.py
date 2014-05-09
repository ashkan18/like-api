from models.comment_model import CommentModel
from models.level_model import LevelModel
from models.user_model import UserModel

__author__ = 'root'


def get_level_stats(level_id):
    """
    This method will get the total number of likes for specific level
    @param level_id: integer id of the level we are looking for
    @return: count of number of likes and comments each level has had
    """
    level = LevelModel.query(LevelModel.level_id == level_id).get()
    if level is None:
        return 0
    else:
        return level.likes_count, level.comments_count


def comment_on_level(level_id, user_id, comment_text):
    """
    This method will add a comment to a level and also list of users comments
    @param level_id: integer id of the level we are adding this comment
    @param user_id: ineteger id of the user who is adding this comment
    @param comment_text: the text of the comment
    """
    level = get_level_by_id(level_id)
    user = get_user_by_id(user_id)
    comment = CommentModel(user_id=user_id, level_id=level_id, text=comment_text)
    level.comments.append(comment)
    user.comments.append(comment)
    level.put()
    user.put()


def like_level(level_id, user_id):
    """
    This method will add a like to a level by a user
    @param level_id: integer id of the level we are adding the like
    @param user_id: integer id of the user who liked the level
    """
    level = get_level_by_id(level_id)
    user = get_user_by_id()
    user.likes.append(level_id)
    level.likes.append(user_id)
    level.put()
    user._put()


def get_level_by_id(level_id):
    """
    This method will get a level model by level id, if we don't have this level, it will create one
    @param level_id: id of the level we are looking for
    @return: levelModel of the model we are looking for
    """
    level = LevelModel.query(LevelModel.level_id == level_id).get()
    # if we haven't had this level before, add it
    if level is None:
        level = LevelModel(level_id=level_id)
    return level


def get_user_by_id(user_id):
    """
    This method will get a user model by level id, if we don't have this user, it will create one
    @param user_id: id of the user we are looking for
    @return: userModel of the model we are looking for
    """
    user = UserModel.query(UserModel.user_id == user_id).get()
    # if we haven't had this  user before, add it
    if user is None:
        user = UserModel(user_id=user_id)
    return user