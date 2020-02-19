import copy

##
## Moves the blank tile towards the left
##
## :param      data:  The complete state of a configuration
## :type       data:  Node
##
## :returns:   The complete state of the modified configuration or None if the action is not possible
## :rtype:     Node
##
def actionMoveLeft(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[1] == 0:
		return None
	else:
		ret_val.blank_tile_location[1] -= 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r][c+1] = ret_val.data_matrix[r][c+1], ret_val.data_matrix[r][c]
		return ret_val


##
## Moves the blank tile towards the right
##
## :param      data:  The complete state of a configuration
## :type       data:  Node
##
## :returns:   The complete state of the modified configuration or None if the action is not possible
## :rtype:     Node
##
def actionMoveRight(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[1] == 2:
		return None
	else:
		ret_val.blank_tile_location[1] += 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r][c-1] = ret_val.data_matrix[r][c-1], ret_val.data_matrix[r][c]
		return ret_val


##
## Moves the blank tile upward
##
## :param      data:  The complete state of a configuration
## :type       data:  Node
##
## :returns:   The complete state of the modified configuration or None if the action is not possible
## :rtype:     Node
##
def actionMoveUp(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[0] == 0:
		return None
	else:
		ret_val.blank_tile_location[0] -= 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r+1][c] = ret_val.data_matrix[r+1][c], ret_val.data_matrix[r][c]
		return ret_val


##
## Moves the blank tile downward
##
## :param      data:  The complete state of a configuration
## :type       data:  Node
##
## :returns:   The complete state of the modified configuration or None if the action is not possible
## :rtype:     Node
##
def actionMoveDown(data):
	ret_val = copy.deepcopy(data)

	if ret_val.blank_tile_location[0] == 2:
		return None
	else:
		ret_val.blank_tile_location[0] += 1
		r,c = ret_val.blank_tile_location
		ret_val.data_matrix[r][c], ret_val.data_matrix[r-1][c] = ret_val.data_matrix[r-1][c], ret_val.data_matrix[r][c]
		return ret_val