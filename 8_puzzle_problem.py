import copy

class Node(object):
	"""docstring for Node"""
	
	def __init__(self, 
				 data_matrix, 
				 current_idx, 
				 parent_idx):
		self.data_matrix = data_matrix
		self.blank_tile_location = self.getBlankTileLocation()
		self.current_idx = current_idx
		self.parent_idx = parent_idx


	def getBlankTileLocation(self):
		idx = [-1,-1]
		for i, row in enumerate(self.data_matrix):
			if 0 in row:
				idx[0] = i
				idx[1] = row.index(0)

		return idx


	def isSolvable(self):
		inversion = 0

		# l = 1,8,2,4,3,7,6,5
		l = [c for r in self.data_matrix for c in r]

		for i in range(len(l)):
			for j in range(i+1, len(l)):
				if l[j] == 0 or l[i] == 0:
					continue

				if l[i] > l[j]:
					inversion += 1

		if inversion%2 == 0:
			return True
		return False


	def reachedGoalState(self):
		goal_state_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
		return (self.data_matrix == goal_state_matrix)
		

	def printNode(self):
		print("blank_tile_location:\n\t", self.blank_tile_location)
		print("current_idx:\n\t", self.current_idx)
		print("parent_idx:\n\t", self.parent_idx)
		print("data_matrix:")
		for row in self.data_matrix:
			print("\t",row)


	def getFlatMatrix(self):
		ret_list = []
		for c in range(0, len(self.data_matrix[0])):
			for r in range(0, len(self.data_matrix)):
				ret_list.append(self.data_matrix[r][c])
		return ret_list



# returns if the process was successful or not
def actionMoveLeft(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[1] == 0:
		# print("OOPS!!! NOT POSSIBLE TO MOVE LEFT:\t", ret_val.blank_tile_location)
		return None
	else:
		ret_val.blank_tile_location[1] -= 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r][c+1] = ret_val.data_matrix[r][c+1], ret_val.data_matrix[r][c]
		return ret_val


# returns if the process was successful or not
def actionMoveRight(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[1] == 2:
		# print("OOPS!!! NOT POSSIBLE TO MOVE RIGHT:\t", ret_val.blank_tile_location)
		return None
	else:
		ret_val.blank_tile_location[1] += 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r][c-1] = ret_val.data_matrix[r][c-1], ret_val.data_matrix[r][c]
		return ret_val


# returns if the process was successful or not
def actionMoveUp(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[0] == 0:
		# print("OOPS!!! NOT POSSIBLE TO MOVE UP:\t", ret_val.blank_tile_location)
		return None
	else:
		ret_val.blank_tile_location[0] -= 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r+1][c] = ret_val.data_matrix[r+1][c], ret_val.data_matrix[r][c]
		return ret_val


# returns if the process was successful or not
def actionMoveDown(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[0] == 2:
		# print("OOPS!!! NOT POSSIBLE TO MOVE DOWN:\t", ret_val.blank_tile_location)
		return None
	else:
		ret_val.blank_tile_location[0] += 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r-1][c] = ret_val.data_matrix[r-1][c], ret_val.data_matrix[r][c]
		return ret_val


def getSolutionPath(queue, q_idx):
	solution_path = []
	while q_idx != -1:
		solution_path.append(queue[q_idx].getFlatMatrix())
		q_idx = queue[q_idx].parent_idx

	return reversed(solution_path)


def printSolutionPath(queue, q_idx):
	sol_path = getSolutionPath(queue, q_idx)
	for state in sol_path:
		print(state)


def main():
	# input_data_matrix = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
	input_data_matrix = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
	input_data = Node(data_matrix=input_data_matrix, 
						current_idx=0, 
						parent_idx=-1)
	# input_data.printNode()

	if not input_data.isSolvable():
		print("Sorry mate! No can do!!")


	##
	## Ok now I am about to solve the 8 puzzle problem.
	##
	
	is_visited = []

	Q = []
	Q.append(input_data)
	Q_idx = 0
	curr_idx = 1

	while (Q_idx < len(Q)):
		is_visited.append(input_data)

		if Q[Q_idx].reachedGoalState():
			printSolutionPath(Q, Q_idx)
			break

		new_state = actionMoveLeft(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		new_state = actionMoveRight(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		new_state = actionMoveUp(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		new_state = actionMoveDown(Q[Q_idx])
		if (new_state is not None) and (new_state not in is_visited):
			new_state.current_idx = curr_idx
			curr_idx += 1
			new_state.parent_idx = Q_idx
			Q.append(new_state)

		Q_idx += 1


if __name__ == '__main__':
	main()
