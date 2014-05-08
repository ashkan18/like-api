import webapp2

__author__ = 'root'


class UserInterface(webapp2.RequestHandler):

    def get_user_liked_levels(self, user_id):
        """
        This method will return a list of levels this user has liked
        @param user_id: int id of the user we are looking for list of levels liked

        sample curl:
            curl -X GET http://localhost:8080/user/2/like/
        """
        pass

    def get_user_comments(self, user_id):
        """
        This method will return a list of comments on the levels this user has made
        @param user_id: int id of the user we want to get list of comments for

        sample curl:
            curl -X GET http://localhost:8080/user/2/comment/
        """
        pass

