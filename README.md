# Akari
Solving Akari using CSP


Akari uses a rectangular grid of black cells and white cells.

The player solves
puzzles via placing light bulbs in the white boxes according to following rules:
 Light bulbs are permitted to be placed at any white square. A numbered square
indicates how many light bulbs are next to it, vertically and horizontally.
 Each light bulb illuminates from itself to a black square or the outer frame in its
row and column.
 Every white square must be illuminated and no light bulbs should illuminate
each other.

The code is implemented in Python and the game itself is represented as a constraint satisfaction problem
E cell represents an empty cell
A numbered cell represents the numbered squared mentioned above

Any user can simply put their desired input (puzzle) by simply changing the matrix "matrix" inside the code. 
This code only solves 7x7 Akari Puzzles
3 Files are included in the Akari folder. Three 7x7 puzzles with different difficulties 
