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