# ENPM661: Project 1

## Solving the 8-Puzzle-Problem
The puzzle is to reach to the goal state from the given initial state.

The puzzle is solved by find all the possible states starting from the given initial state. Note that, the states are unique.

From the initial state of the puzzle, different actions are performed to generate new states.

The steps to solving the 8-puzzle are found by back-tracking from the goal node to the initial node.


## To run the code
`python3 8_puzzle_problem.py 1 0 7 8 4 6 2 3 5`

The numbers entered in the commandline, form the input grid. The grid is flattened column-wise during input. Hence the given sample configuration represents the following grid:

`1 8 2`  
`0 4 3`  
`7 6 5`  

This code prints the solution on the terminal as well as stores the solution in a text file which can be better visualized using the code in `plot_path.py`.

## To see the steps to solve the 8-Puzzle-Problem
`python3 plot_path.py`
