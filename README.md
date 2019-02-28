# Solving Akari using CSP

Introduction 
---

Akari uses a rectangular grid of black cells and white cells.

The player solves puzzles via placing light bulbs in the white boxes according to following rules:
* Light bulbs are permitted to be placed at any white square. A numbered square
indicates how many light bulbs are next to it, vertically and horizontally.
* Each light bulb illuminates from itself to a black square or the outer frame in its
row and column.
* Every white square must be illuminated and no light bulbs should illuminate
each other.

Program Specifications:
---

* The code is implemented in Python 
* Game is represented as a constraint satisfaction problem
* E cell represents an empty cell
* A numbered cell represents the numbered squared mentioned above
* This code only solves 7x7 Akari Puzzles

How To Use:
---

Any user can simply put their desired input (puzzle) by simply changing the matrix "matrix" inside the code (in any of the python files included in this project). 
3 Files are included in the Akari folder. Three 7x7 puzzles with different difficulties 
