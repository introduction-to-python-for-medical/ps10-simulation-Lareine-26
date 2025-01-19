import random
import copy
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

def initialize_forest(grid_size=30, p_tree=0.6):
    """Initialize a grid for the forest fire simulation."""
    grid = [[0] * grid_size for _ in range(grid_size)]  # Initialize with 0s

    for i in range(grid_size):
        for j in range(grid_size):
            if random.random() < p_tree:
                grid[i][j] = 1  # 1 represents a tree

    # Start fire in the center
    grid[grid_size // 2][grid_size // 2] = 2  # 2 represents fire

    return grid

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

# Set up the simulation
grid_size = 30
p_tree = 0.6
grid = initialize_forest(grid_size, p_tree)

# Run the simulation and visualize
fig, ax = plt.subplots()
for step in range(100):  # Limit the simulation steps
    new_grid = spread_fire(grid)
    
    # Check for convergence (no more changes)
    if new_grid == grid:
        break

    grid = new_grid
    ax.imshow(grid, cmap='YlOrRd', vmin=0, vmax=2)
    ax.set_title(f'Step {step}')
    display(fig)
    clear_output(wait=True)
    plt.pause(0.1)  # Pause for visualization

plt.show()
