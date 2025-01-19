def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)  # Copy the grid to store updates

    for i in range(grid_size):  # Iterate over all rows
        for j in range(grid_size):  # Iterate over all columns
            if grid[i][j] == 1:  # Check if the cell is a tree
                # Collect valid neighbors within bounds
                neighbors = []
                if i > 0:  # Top neighbor
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # Bottom neighbor
                    neighbors.append(grid[i+1][j])
                if j > 0:  # Left neighbor
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # Right neighbor
                    neighbors.append(grid[i][j+1])

                # If any neighbor is on fire, the current tree catches fire
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
# Set up the grid
grid_size = 30
p_tree = 0.6
grid = initialize_forest(grid_size, p_tree)

# Run the simulation and visualize
fig, ax = plt.subplots()
for step in range(100):  # Limit to 100 steps
    new_grid = spread_fire(grid)
    
    # Stop if no changes are observed
    if new_grid == grid:
        break

    grid = new_grid
    ax.imshow(grid, cmap='YlOrRd', vmin=0, vmax=2)
    ax.set_title(f'Step {step}')
    display(fig)
    clear_output(wait=True)
    plt.pause(0.1)  # Pause for visualization

plt.show()
