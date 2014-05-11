"""
Starting point file for likeapi application
"""

import webapp2
from interfaces import level_interface
from interfaces import user_interface


application = webapp2.WSGIApplication([
                                      # ---------------- Level Interface Routing ----------------
                                      # like a level by a user
                                      webapp2.Route('/level/<level_id>/like/<user_id>',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="like_level",
                                                    methods=['POST']),

                                      # comment on a level by a user
                                      webapp2.Route('/level/<level_id>/comment/<user_id>',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="comment_on_level",
                                                    methods=['POST']),

                                      # get level stats (number of likes and number of comments)
                                      webapp2.Route('/level/<level_id>/',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="get_level_stats",
                                                    methods=['GET']),

                                      # get comments for a level
                                      webapp2.Route('/level/<level_id>/comment/',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="get_comments",
                                                    methods=['GET']),

                                      # ---------------- User Interface Routing ----------------
                                      # get levels this user has liked
                                      webapp2.Route('/user/<user_id>/like/level',
                                                    handler=user_interface.UserInterface,
                                                    handler_method="get_user_liked_levels",
                                                    methods=['GET']),

                                      # get comments this user has posted
                                      webapp2.Route('/user/<user_id>/comment',
                                                    handler=user_interface.UserInterface,
                                                    handler_method="get_user_comments",
                                                    methods=['GET'])], debug=True)
