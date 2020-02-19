import sys
import numpy as np
sys.dont_write_bytecode = True

import node
import actions
import utils

def solve8PuzzleProblem(input_data_matrix):
	input_data = node.Node(data_matrix=input_data_matrix, 
						current_idx=0, 
						parent_idx=-1)

	if not input_data.isSolvable():
		print("Sorry mate! No can do!!")
	
	is_visited = []

	Q = []
	Q.append(input_data)
	Q_idx = 0
	curr_idx = 1

	while (Q_idx < len(Q)):
		is_visited.append(input_data)

		if Q[Q_idx].reachedGoalState():
			utils.printSolutionPath(Q, Q_idx)
			utils.writeNodeIdxInformation(node_list=Q, node_info_filename="./NodesInfo.txt")
			utils.writeNodeStates(node_list=Q, node_state_filename="./Nodes.txt")
			return (utils.getSolutionPath(Q, Q_idx))

		new_state = actions.actionMoveLeft(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		new_state = actions.actionMoveRight(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		new_state = actions.actionMoveUp(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		new_state = actions.actionMoveDown(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		Q_idx += 1

	print("I am really sorry but I could not find a solution. This is weird because as per my logic the solution exists.")
	return None


def main():
	# input_data_matrix = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
	input_data_matrix = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
	solution_path = solve8PuzzleProblem(input_data_matrix)
	# print("--------- PRINTING SOLUTION PATH ---------\n", solution_path)
	np.savetxt("./nodePath.txt", np.array(solution_path), fmt="%d")


if __name__ == '__main__':
	main()
