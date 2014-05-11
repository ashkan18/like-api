from models.user_model import UserModel

__author__ = 'Ashkan'


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
