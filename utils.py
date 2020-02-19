import numpy as np


##
## Gets the solution path.
## Backtracks from the goal state to the input state to get the solution path
##
## :param      queue:  The queue containing all the visited nodes
## :type       queue:  List
## :param      q_idx:  The index of the current configuration
## :type       q_idx:  Integer
##
## :returns:   The list of configurations along the solution path.
## :rtype:     2D List
##
def getSolutionPath(queue, q_idx):
	solution_path = []
	while q_idx != -1:
		solution_path.append(queue[q_idx].getFlatMatrix())
		q_idx = queue[q_idx].parent_idx

	solution_path.reverse()
	return solution_path


##
## Prints the solution path.
##
## :param      queue:  The queue containing all the visited nodes
## :type       queue:  List
## :param      q_idx:  The index of the current configuration
## :type       q_idx:  Integer
##
def printSolutionPath(queue, q_idx):
	sol_path = getSolutionPath(queue, q_idx)
	for state in sol_path:
		print(state)


##
## Writes every visited node's current index and parent index in a txt file.
##
## :param      node_list:           The list of visited nodes
## :type       node_list:           List
## :param      node_info_filename:  The output node information txt filename
## :type       node_info_filename:  String
##
def writeNodeIdxInformation(node_list, node_info_filename):
	node_idx_information = []
	for node in node_list:
		node_idx_information.append([node.current_idx, node.parent_idx])
	
	np.savetxt(node_info_filename, np.array(node_idx_information), fmt="%d")


##
## Writes every visited node configuration in a txt file.
##
## :param      node_list:            The list of visited nodes
## :type       node_list:            List
## :param      node_state_filename:  The output node state txt filename
## :type       node_state_filename:  String
##
def writeNodeStates(node_list, node_state_filename):
	node_states = []
	for node in node_list:
		node_states.append(node.getFlatMatrix())

	np.savetxt(node_state_filename, np.array(node_states), fmt="%d")


##
## Convert the input commandline grid values to a 2D list.
##
## :param      grid_values:  The grid values
## :type       grid_values:  List
##
## :returns:   The input grid.
## :rtype:     2D List
##
def getInputGrid(grid_values):
	num_rows = 3
	num_cols = 3

	grid = [[0] * num_cols for _ in range(num_rows)]

	for r in range(0, num_rows):
		for c in range(0, num_cols):
			grid[r][c] = int(grid_values[c * num_rows + r])

	return grid
