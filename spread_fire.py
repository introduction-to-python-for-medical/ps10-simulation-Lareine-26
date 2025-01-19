
def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    new_grid = copy.deepcopy(grid)

    for i in range(grid_size):  # Iterate through all rows
        for j in range(grid_size):  # Iterate through all columns
            if grid[i][j] == 1:  # Check for trees
                # Check neighbors for fire, considering the margins
                if (i > 0 and grid[i-1][j] == 2) or (i < grid_size - 1 and grid[i+1][j] == 2) or \
                   (j > 0 and grid[i][j-1] == 2) or (j < grid_size - 1 and grid[i][j+1] == 2):
                    new_grid[i][j] = 2  # Set the tree on fire

    return new_grid
