like-api
========

API for handling likes and comments


Specs:
- For each level in our game, we want the ability for the player to like it and add a comment.

- The flow in our app is this way: the user plays a level, then at the end he can see the number of people who liked it and the number of comments.
The player has then the option to see the list of comments and add one, or he can also like the level.

Then on the user profile page we want to display which levels he liked.
Please tell us which end-point calling with which parameters.



Interfaces:

Level releated calls:
- Like a Level by a user:
    This method will add a like for a level by a user.</br>
    Sample curl:
        curl -X POST http://localhost:8080/level/2/like/1

- Comment on a level:
    This method will add a user comment for a level.</br>
    
    Path = POST /level/{level id}/comment/<user id> and in post data comment_text
    sample curl:
                curl -X POST http://localhost:8080/level/2/comment/1 --data "comment_text=hello songpop"

- Get level stats:
    This method will return total number of likes and comments for a level</br>
    
    Path = GET level/{level id}
    sample curl:
        curl -X GET http://localhost:8080/level/2/

- Get comments for a level:
    This method will return list of comments for a level</br>

    path = GET /level/{level id}/comment/
      sample curl:
          curl -X GET http://localhost:8080/level/2/comment/


User related calls:
- Get levels liked by a user:
    This method will return a list of levels this user has liked</br>

    Path = GET /user/{user id}/like

    sample curl:
        curl -X GET http://localhost:8080/user/2/like

- Get user comments:
    This method will return a list of comments on the levels this user has made </br>

    Path = GET /user/{user id}/comment

    sample curl:
        curl -X GET http://localhost:8080/user/2/comment
