#------------------------UNDERSTANDING THE PROBLEM-----------------------

#  Problems: 
#     (1) The list of [traversal] directions provided is NOT complete.
#     (2) There is no current graph that represents all 500 rooms in the
#         game.
#     (3) All the tests DO NOT pass when the code is executed.
    
#  Provided Specs:
#     (1) This is an adventure game.
#     (2) The game as a total of 500 rooms that can be visited by a player.
#     (3) The game only has ONE player (you).
#     (4) Through inputs or through a list of directions, you can perform ONE 
#         move at a time, and each move will be made in ONE of the following
#         directions: 
#            (a) north (n)
#            (b) south (s) 
#            (c) east  (e) 
#            (d) west  (w) 
    
#  Player's Objective: 
#     (1) Visit all 500 rooms in the shortest number of moves possible.
#     (2) Construct a dictionary that represents a graph of all 500 
#         rooms, filling the dictionary one entry at a time, while 
#         visiting each room.
#            (a) i.e. - {
#                         0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#                         5: {'n': 0, 's': '?', 'e': '?'}
#                       }
#     (3) Create a list of directions called 'traversalPath' that 
#         stores [the directions of] each move you make while visiting
#         all 500 rooms.
#            (a) The moves will be stored in sequential order.
#                   (i) i.e. - traversalPath = ['n', 'e']
#     (4) You will know when you've visited all 500 rooms if:
#            (a) There are a total of 500 entries in your dictionary.
#            (b) There are no more "?" in the adjacency dictionaries.

#  Hints:
#     (1) Try traversing the smaller graphs in adv.py first.

#     (2) Use Depth First Traversal (DFT) to write an algorithm that: 
#           (a) picks a RANDOM, unexplored exit from the player's 
#               CURRENT room.
#           (b) moves the player in the chosen direction to get to
#               the NEXT room.
#           (c) adds the player's move (as a direction the player 
#               traveled) into the 'traversalPath' list.
#           (d) loops through steps (a) - (c) to continually move the 
#               player through unexplored exits, until the player reaches
#               a DEAD-END room with NO UNEXPLORED exits, meaning there 
#               are no more "?" in the adjacency dictionary for that room.
#           (e) walks the player back to the NEAREST room that DOES
#               contain an UNEXPLORED exit, meaning there IS at least
#               ONE "?" in the adjacency dictionary for that room.
#           (f) repeats steps (a) - (e) until all 500 rooms have been
#               visited and each room no longer contains ANY "?" in their
#               adjacency dictionaries.

#     (3) Use a Breadth First Search (BFS) to find the SHORTEST path 
#         to the NEAREST room with an UNEXPLORED exit.
#            (a) Set your 'destination_vertex' to a value of "?", which
#                will search for the shortest path to a room with a
#                "?" as ONE of its "exit" values.
#            (b) If a room has NO "?" for any "exit" values (because all  
#                exits have been explored) you can put it in your
#                BFS queue like normal.
#            (c) BFS will return the shortest path as a LIST of room IDs.
#                   (i)  Every move that the player makes to get to this
#                        'nearest room with an unexplored exit' must ALSO 
#                        be added to the 'traversalPath' list.
#                   (ii) Each move will need to be converted from a room
#                        ID to a DIRECTION (i.e. - north(n), south(s), 
#                        etc.) before it can be added to the
#                        'traversalPath' list.

#     (4) Do not use a STACK as the data structure for your DFT & BFS.
#            (a) Using a DEQUE as the data structure for your DFT and BFS
#                methods will be superior to using a STACK because:
#                   (i)  DEQUES (double-ended queues) allow for the fast 
#                        addition & removal of elements from BOTH ends 
#                        of the queue, whereas elements in a STACK can 
#                        only be added or removed from the end of a STACK.
#                   (ii) DEQUES also have built-in methods that STACKS do
#                        not, such as:
#                           (a) .append()
#                           (b) .appendLeft()
#                           (c) .pop()
#                           (d) .popLeft()
#                           (e) .reverse() 

#     (5) Once all exits have been explored, the game is over!
    
    
#------------------------------DEVISE A PLAN-----------------------------

#  Objectives: 
#     (1) Create a BFS helpe method (with a DEQUE) that will be called 
#         when the player reaches a room that has NO exits or has NO 
#         unexplored exits available at player's the current room.
#            (a) This method will take two parameters(starting_vertex &
#                destination_vertex).
#     (2) Use a DFT method (with a DEQUE) to move the player through 
#         UNEXPLORED exits.
#            (a) Create a dictionary [of dictionaries] that will store 
#                'room' entries for each room that the player has already 
#                visited. 
#            (b) Each 'room' entry will store 0 to 4 'exit' entries (n, 
#                s, e, w) that have 'room' values, which represent 
#                the room that the player WILL enter if they choose to 
#                travel through that specific exit.
#            (c) Create a DEQUE called 'traversalPath' that will store 
#                a list of each move (in the form of a direction, such as:
#                "n", "s", "e", "w") that the player makes, from the start
#                of the game to the end of the game. 
#            (d) Use a WHILE loop that will continue (so long as the the
#                number of entries in the dictionary is < 500) to move the 
#                player from room to room AS LONG AS the player continues
#                to enter rooms that have UNEXPLORED exits in them.
#                available, which will also include rooms with 0 exits.
#                   (i)   If an unexplored exit exists at the current room,
#                         move the player through a randomly-chosen, 
#                         unexplored exit to the NEXT room, log the player's 
#                         move in a list called 'traversalPath'. Then, exit
#                         this IF statement & re-enter the WHILE loop.
#                   (ii)  If an unexplored exit DOES NOT exist at the 
#                         current room, call the BFS helper method, which 
#                         will utilize the same DICT and the same DEQUE 
#                         ('traversalPath') as this DFT method, but will
#                         also utilize a newly returned DEQUE with the 
#                         shortest BACKWARDS path, to the NEAREST room that
#                         contains an unexplored exit.
#                           (1) Pass in the player's 'current room' as the
#                               'starting_vertex' and pass in a "?" as the 
#                               'destination_vertex' for the BFS method. 
#                           (2) Use the ".reverse()" built-in DEQUE method 
#                               to reverse the order of the DEQUE (from 
#                               [left:right] to [right:left]) to allow for
#                               BACKWARDS traversing.
#                           (3) Perform the BFS method on the newly-
#                               reversed DEQUE to return the shortest path
#                               (as a list of ROOM IDs) to the nearest room
#                               with an unexplored exit.
#                           (4) Use a FOR loop to iterate through the 
#                               'shortest path' list of room IDs to:
#                                  (a) convert each room ID into a 
#                                      direction (i.e. - north(n), 
#                                      south(s), east(e), or west(w)) that
#                                      can be added to the 'traversalPath'
#                                      list.
#                                  (b) move the player according to the
#                                      newly-converted direction.
#                                  (c) add the player's move to the
#                                      BEGINNING of the 'traversalPath' 
#                                      DEQUE.                                       
#                           (5) Once the player arrives at the last room 
#                               in the returned 'shortest path' list, use
#                               the ".reverse()" built-in DEQUE method 
#                               AGAIN to reverse the CURRENT order of the
#                               DEQUE, from [right:left] BACK to 
#                               [left:right], to allow the player to 
#                               traverse the rooms in the OPPOSITE 
#                               (original) direction.
#     (3) Fill the dictionary, one entry at a time, while 
#         visiting each room.
#     (4) Create a list of directions called 'traversalPath' that 
#         stores [the directions of] each move you make while visiting
#         all 500 rooms.
#     (5) All the tests must pass.
#     (6) If possible, try to achieve < 957 moves total, while visiting 
#         all 500 rooms. 

#---------------------------IMPLEMENT THE PLAN---------------------------
#------------------------REFLECT & ITERATE SOLUTION----------------------