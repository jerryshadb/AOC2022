def is_visible(trees: list, row: int, col: int) -> bool:
	tree = trees[row][col]
	# Check all trees above current tree.
	for i in range(row - 1, -1, -1):
		if trees[i][col] >= tree:
			break
	else:
		return True
	
	# Check all trees below current tree.
	for i in range(row + 1, len(trees)):
		if trees[i][col] >= tree:
			break
	else:
		return True
		
	# Check all trees to the left of current tree.
	for neighbour in reversed(trees[row][:col]):
		if neighbour >= tree:
			break
	else:
		return True
	
	# Check all trees to the right of current tree.
	for neighbour in trees[row][col + 1:]:
		if neighbour >= tree:
			break	
	else:
		return True	
	
	return False


def scenic_score(trees: list, row: int, col: int) -> int:
	tree = trees[row][col]
	up, down, left, right = 0, 0, 0, 0
	
	# Check trees above current tree.
	for i in range(row - 1, -1, -1):
		up += 1
		if trees[i][col] >= tree:
			break
	
	# Check trees below current tree.
	for i in range(row + 1, len(trees)):
		down += 1
		if trees[i][col] >= tree:
			break
		
	# Check trees to the left of current tree.
	for neighbour in reversed(trees[row][:col]):
		left += 1
		if neighbour >= tree:
			break
	
	# Check trees to the right of current tree.
	for neighbour in trees[row][col + 1:]:
		right += 1
		if neighbour >= tree:
			break	
	
	return up * down * right * left

def solution():
    with open('input.txt', 'r') as f:
        input = f.read().split('\n')
        # read input to a 2-D matrix containing trees as integers
        trees = list()
        for treeline in input:
            trees.append([int(tree) for tree in treeline])

    total_rows = len(trees)
    total_columns = len(trees[0])
    # all outer trees are visible so add these trees in right away by summing rows and columns and multiplying them by 2 (2 rows which has len(rows) of trees)
    # and subtract 4 since corners overlap. 
    visible_trees = (total_rows + total_columns) * 2 - 4

    # add visible inner trees to visible and calculate scenic scores
    scores = list()
    for row in range(1, total_rows - 1):
        for column in range(1, total_columns - 1):
            if is_visible(trees, row, column):
                scores.append(scenic_score(trees, row, column))
                visible_trees += 1

    print(f"Part 1 solution: {visible_trees}")
    print(f"Part 2 solution: {max(scores)}")

solution()