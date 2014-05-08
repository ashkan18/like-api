import json
import webapp2
from interfaces.base_interface import BaseInterface
from services import level_service

__author__ = 'root'


class LevelInterface(BaseInterface):

    def like_level(self, level_id, user_id):
        """
        This method will add a like for a level by a user
        @param level_id: integer id of the level we want to like
        @param user_id: integer id of the user who liked the level
        @return: json with success showing if like was successful

        sample curl:
            curl -X GET http://localhost:8080/level/2/like/1
        """
        level_service.like_level(level_id=int(level_id), user_id=int(user_id))
        self.send_response({"success": True})

    def comment_on_level(self, level_id, user_id):
        """
        This method will add a user comment for a level
        @param level_id:
        @param user_id:
        @return:
        """
        comment_text = self.request.params['comment_text']
        level_service.comment_on_level(level_id=level_id, user_id=user_id, comment_text=comment_text)
        self.send_response({"success": True})

    def get_total_number_likes(self, level_id):
        """
        This method will return total number of likes for a level
        @param level_id: int id of the level we are looking to get its likes

        sample curl:
            curl -X GET http://localhost:8080/level/2/like/
        """

        likes_count = level_service.get_total_likes_for_level(int(level_id))
        total_like_results = {'count': likes_count, 'date': 'today'}
        self.send_response(total_like_results)

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

