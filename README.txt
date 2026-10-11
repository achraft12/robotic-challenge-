AUI Robotics Club - Software Track

This submission follows the challenge requirements with a simple Python program.

What it does
------------
- Uses a 5x5 grid.
- Robot starts at (0, 0).
- Payload is at (2, 2).
- Point B is at (4, 4).
- Uses at least 3 obstacle cells.
- Uses Breadth-First Search (BFS) to find a route.
- First finds a path to the payload.
- Then finds a path from the payload to Point B.
- Includes a blocked layout where Point B cannot be reached.

How to run
----------
1. Open a terminal in this folder.
2. Run:

   python robotics_challenge.py

Symbols
-------
S = Start
P = Payload
B = Point B
# = Obstacle
* = Path
. = Free cell
