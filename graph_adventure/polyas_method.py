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
#            (b) There are no more "?" values in the adjacency lists within
#                your adjacency dictionary.

#  Hints:
#     (1) Try traversing the smaller graphs in adv.py first.

#     (2) Use Depth First Traversal (DFT) to write an algorithm that: 
#           (a) picks a RANDOM, unexplored exit from the player's 
#               CURRENT room.
#           (b) moves the player in the chosen direction to get to
#               the NEXT room.
#           (c) adds the player's move (as a direction, such as 'n',
#               's', 'e', or 'w') into the 'traversalPath' list.
#           (d) loops through steps (a) - (c) to continually move the 
#               player through unexplored exits, until the player reaches
#               a DEAD-END room with NO UNEXPLORED exits available (meaning
#               there are no more "?" values in the adjacency list for that
#               room).
#           (e) walks the player back to the NEAREST room that DOES
#               contain an UNEXPLORED exit (meaning there IS at least
#               ONE "?" value in the adjacency list for that room).
#           (f) repeats steps (a) - (e) until all 500 rooms have been
#               visited and each room no longer contains ANY "?" in their
#               adjacency lists.
