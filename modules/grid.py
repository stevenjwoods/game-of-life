"""
Methods pertaining to the creation, manipulation and display of a 2D grid.
"""

import copy
import math
import random

def create(num_rows, num_cols, value):
    """ 
    Creates a 2D grid (a list of lists).

    Args:

        num_rows: 
            The desired number of rows in the grid.
                
        num_cols:
            The desired number of columns in the grid.

        value:
            The value to initialise all cells of the grid with.

    Returns:

        A list of grid rows. Each row is a list of cells in the row.
    """
    return [[value] * num_cols for row in range(num_rows)]


def display(grid, cell_states):
    """ 
    Converts a grid list to a multiline string.

    Args:

        grid: 
            A list of lists defining a 2D grid.

        cell_states:
            A dictionary: key = cell state, value = replacement string.
    
    Returns:
        
        output:
            The grid in string form.
    """
    output = ""
    for row in grid:
        display_row = []
        for cell in row:
            display_row.append(cell_states[cell])
        output += (" ".join(display_row) + "\n")
    return output


def count_neighbourhood(grid, row, col):
    """ 
    Sums the values of a 3x3 subset of cells.
    Assumes toroidal geometry for central cells located on grid borders.
    Cell values must be integers.

    Args:

        grid:
            A list of lists defining a 2D grid.

        row:
            The grid row of the central cell.

        col:
            The grid column of the central cell.

    Returns:

        count:
            The sum of integer values in a 3x3 grid.
    """
    num_rows, num_cols = len(grid), len(grid[0])
    count = 0
    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            neighbour_row = (row + row_offset + num_rows) % num_rows  # Toroidal geometry: grid[len(grid)] becomes grid[0]
            neighbour_col = (col + col_offset + num_cols) % num_cols
            count += grid[neighbour_row][neighbour_col]
    return count


def value_check(grid, val):
    """ 
    Checks if any cells in the grid have a specified value.

    Args:

        grid:
            A list of lists defining a 2D grid.

        val:
            The value to check for.

    Returns:

        True, upon finding val at any location in the grid.
    """
    for row in grid:
        for cell in row:
            if cell == val:
                return True
                

def seed(grid, seed_val, seed_percentage):
    """ 
    Converts a proportion of cells to seed_val.
    Cells are randomly selected for seeding from a list of all cell locations.

    Args:

        grid:
            A list of lists defining a 2D grid.

        seed_val:
            The value to convert selected cells to.

        seed_percentage:
            The percentage of cells to be converted to seed val.
    """
    cell_locations = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell_locations.append([row, col])  # Lists all cell positions

    total_cells = len(grid) * len(grid[0])
    seed_num = math.ceil(total_cells * seed_percentage / 100)  # Rounded up if not integer

    seed_count = 0
    while seed_count < seed_num:
        cell_loc = random.choice(cell_locations)
        cell_locations.remove(cell_loc)  # Location cannot be chosen again
        row, col = cell_loc
        grid[row][col] = seed_val
        seed_count += 1

        
def update(grid, val1, val2):
    """ 
    Copies grid and determines cell value changes according to conditionals statements.

    Args:

        grid:
            A list of lists defining a 2D grid. Contains a cell object at each position.
        
        val1, val2:
            Values to assign according to conditionals.
    """
    old_grid = copy.deepcopy(grid)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            neighbourhood_count = count_neighbourhood(old_grid, row, col)

            if neighbourhood_count is 3:
                grid[row][col] = val2
            elif neighbourhood_count is 4:
                pass
            else:
                grid[row][col] = val1