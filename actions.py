import copy

# returns if the process was successful or not
def actionMoveLeft(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[1] == 0:
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
		return None
	else:
		ret_val.blank_tile_location[0] += 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r-1][c] = ret_val.data_matrix[r-1][c], ret_val.data_matrix[r][c]
		return ret_val