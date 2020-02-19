import numpy as np


def getSolutionPath(queue, q_idx):
	solution_path = []
	while q_idx != -1:
		solution_path.append(queue[q_idx].getFlatMatrix())
		q_idx = queue[q_idx].parent_idx

	solution_path.reverse()
	
	# return reversed(solution_path)
	return solution_path


def printSolutionPath(queue, q_idx):
	sol_path = getSolutionPath(queue, q_idx)
	for state in sol_path:
		print(state)


def writeNodeIdxInformation(node_list, node_info_filename):
	node_idx_information = []
	for node in node_list:
		node_idx_information.append([node.current_idx, node.parent_idx])
	
	np.savetxt(node_info_filename, np.array(node_idx_information), fmt="%d")


def writeNodeStates(node_list, node_state_filename):
	node_states = []
	for node in node_list:
		node_states.append(node.getFlatMatrix())

	np.savetxt(node_state_filename, np.array(node_states), fmt="%d")
