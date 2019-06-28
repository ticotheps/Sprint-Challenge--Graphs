#------------------------UNDERSTANDING THE PROBLEM-----------------------

#  Problems: 
#     (1) The list of [traversal] directions provided is NOT complete.
#     (2) There is no current graph that represents all 500 rooms in the
#         game.
#     (3) All the tests in adv.py DO NOT pass when the code is executed.
    
#  Provided Specs:
#     (1) This is an adventure game.
#     (2) The game has a total of 500 rooms that can be visited by a player.
#     (3) The game only has ONE player (you).
#     (4) Through the list of directions in 'traversalPath,' you can
#         perform ONE move at a time, and each move will be made in ONE of 
#         the following directions: 
#            (a) n (North)
#            (b) s (South) 
#            (c) e (East) 
#            (d) w (West) 

#  Player's Objective: 
#     (1) Visit all 500 rooms in the SHORTEST number of moves possible.
#     (2) Construct a dictionary that represents a graph of all 500 
#         rooms, filling the dictionary one entry at a time, AS the player 
#         is traversing through all 500 rooms.
#            (a) i.e. - {
#                         0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#                         5: {'n': 0, 's': '?', 'e': '?'}
#                       }
#     (3) Create a list of directions called 'traversalPath' that 
#         stores [the directions of] each move you make while visiting
#         all 500 rooms.
#            (a) The moves will be stored in sequential order with index 0
#                being the very FIRST move that is made from the 
#                'startingRoom'.
#                   (i) i.e. - traversalPath = ['n', 'e']
#     (4) You will know when you all 500 rooms have been visited if the
#         following TWO conditions have been met:
#            (a) There are a total of 500 entries in your adjacency 
#                dictionary.
#            (b) There are no more "?" values in the adjacency dictionary.