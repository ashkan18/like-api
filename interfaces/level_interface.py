import json
import webapp2

__author__ = 'root'


class LevelInterface(webapp2.RequestHandler):

    def get_total_number_likes(self, level_id):
        """
        This method will return total number of likes for a level
        @param level_id: int id of the level we are looking to get its likes

        sample curl:
            curl -X GET http://localhost:8080/level/2/like/
        """
        self.response.headers['Content-Type'] = 'application/json'
        total_like_results = {'count': 23, 'date': 'today'}
        self.response.write(json.dumps(total_like_results))

    def get_total_number_comments(self, level_id):
        """
        This method will return total number of comments for a level
        @param level_id: int id of the level we are looking to get its comments

        sample curl:
            curl -X GET http://localhost:8080/level/2/comment/total
        """
        pass

    def get_comments(self, level_id):
        """
        This method will return list of comments for a level
        @param level_id: int id of the level we are looking to get its comments

        sample curl:
            curl -X GET http://localhost:8080/level/2/comment/
        """
        pass

