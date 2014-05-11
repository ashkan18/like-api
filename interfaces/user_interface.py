from interfaces.base_interface import BaseInterface
from services import user_service

__author__ = 'Ashkan'


class UserInterface(BaseInterface):

    def get_user_liked_levels(self, user_id):
        """
        This method will return a list of levels this user has liked
        @param user_id: int id of the user we are looking for list of levels liked

        sample curl:
            curl -X GET http://localhost:8080/user/2/like
        """
        user = user_service.get_user_by_id(int(user_id))
        self.send_response({"liked_levels": user.likes})

    def get_user_comments(self, user_id):
        """
        This method will return a list of comments on the levels this user has made
        @param user_id: int id of the user we want to get list of comments for

        sample curl:
            curl -X GET http://localhost:8080/user/2/comment
        """
        user = user_service.get_user_by_id(int(user_id))
        comments = [{'text': comment.text, 'level_id': comment.level_id, 'date': comment.date}
                    for comment in user.comments]
        self.send_response({"comments": comments})
