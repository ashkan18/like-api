"""
Starting point file for likeapi application
"""

import webapp2
from interfaces import level_interface
from interfaces import user_interface


application = webapp2.WSGIApplication([
                                      # ---------------- Level Interface Routing ----------------
                                      webapp2.Route('/level/<level_id>/like/<user_id>',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="like_level",
                                                    methods=['POST']),

                                      webapp2.Route('/level/<level_id>/comment/<user_id>',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="comment_on_level",
                                                    methods=['POST']),

                                      webapp2.Route('/level/<level_id>/',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="get_level_stats",
                                                    methods=['GET']),

                                      webapp2.Route('/level/<level_id>/comment/total',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="get_total_number_comments"),

                                      webapp2.Route('/level/<level_id>/comment/',
                                                    handler=level_interface.LevelInterface,
                                                    handler_method="get_comments"),

                                      # ---------------- User Interface Routing ----------------
                                      webapp2.Route('/user/<user_id>/like/level',
                                                    handler=user_interface.UserInterface,
                                                    handler_method="get_user_liked_levels"),

                                      webapp2.Route('/user/<user_id>/comment',
                                                    handler=user_interface.UserInterface,
                                                    handler_method="get_user_comments")], debug=True)
