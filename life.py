"""
Basic implementation of The Game of Life.

An infinite grid is simulated using toroidal geometry:
    The top and bottom rows are adjacent, as are the left- and right-most columns.

The grid is seeded randomly with a proportion of cells specified by the user, or with a default of 25%.

The next generation of the game is calculated and displayed every 0.5 seconds until game end.
Game ends when all cells are dead or user presses Ctrl+C.

To run from game-of-life directory:

    python3 life.py

    Dependent on get_input.py and grid.py in ./modules
"""

import datetime
import time

from modules import get_input
from modules import grid

empty, alive = 0, 1  # Values to represent cell states
cell_states = {empty: " ", alive: "#"}  # Arg for grid.display() directing cell value replacement

num_rows, num_cols = 40, 60  # Grid dimensions
min_seed, max_seed, default_seed = 0, 100, 25  # Args for grid.seed()
separator = "\n" + "-" * num_cols * 2 + "\n"  # Arg for grid.display()

print(f"""
Welcome to The Game of Life!

In this version of the game:
    If a live cell has fewer than 2 neighbours, it will die by underpopulation.
    If a live cell has more than 3 neighbours, it will die by overpopulation.
    If an empty cell has exactly 3 neighbours, it will become live by reproduction.

Note that the top and bottom rows are considered adjacent, as are the left- and right-most columns.

To begin, you can choose a proportion of cells to begin alive, or press enter to use the default ({default_seed}%).
Press Ctrl+C at any time to stop the game.
""")
seed_percentage = get_input.integer(
    "Enter the percentage of live cells for the initial state: ", min_seed, max_seed, default_seed
    )

life_grid = grid.create(num_rows, num_cols, empty)
grid.seed(life_grid, alive, seed_percentage)  # Converts a percentage of randomly selected cells to alive (1).
print(separator)
print(grid.display(life_grid, cell_states), separator)  # Converts grid list to a string and prints it.
                                                        # cell_states dictates cell value representation.

tstep = datetime.timedelta(seconds=0.5)  # Specifies 0.5 second intervals.
tnext = datetime.datetime.now() + tstep  # Calculates end time of delay from time.sleep() (below) on first iteration.
try:
    while True:
        if grid.value_check(life_grid, alive) is True:  # If any cells alive...

            grid.update(life_grid, empty, alive)  # Next generation calculated and grid updated.
            print(grid.display(life_grid, cell_states), separator)

            tdiff = tnext - datetime.datetime.now()  # Calculates wait time for time.sleep()
            time.sleep(tdiff.total_seconds())  # Wait
            tnext = tnext + tstep

        else:  # If no live cells...
            print("All the cells have died.\n\nGame Over!\n")
            break
except KeyboardInterrupt:  # Game ends if user presses Ctrl+C
    print("\n\nGame ended by user.\n")
    exit