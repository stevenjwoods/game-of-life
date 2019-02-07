"""    
Tests for the grid module.

To run:
    python3 -m unittest <path/to/test_grid.py>
"""

import unittest

from modules import grid

class TestGrid(unittest.TestCase):

    def setUp(self):
        self.cell_states = {0: ".", 1: "#"}
        self.test_grid = grid.create(3, 4, 0)
        self.pentomino = [[0, 0, 0, 1],
                          [0, 1, 1, 1],
                          [0, 0, 1, 0]]


    def test_create(self):
        """
        Test that:
            test_grid is intiialised as expected
        """
        self.assertEqual(self.test_grid, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])


    def test_display(self):
        """
        Test that: 
            a grid (list of lists) is converted to a string with cell values correctly replaced
        """

        self.assertEqual(grid.display(self.test_grid, self.cell_states), ". . . .\n. . . .\n. . . .\n")
        self.assertEqual(grid.display(self.pentomino, self.cell_states), ". . . #\n. # # #\n. . # .\n")


    def test_count_neighbourhood(self):
        """
        Test that:
            the neighbourhood value is correctly determined for specific central cell in the pentomino grid
        """
        self.assertEqual(grid.count_neighbourhood(self.pentomino, 0, 2), 5)


    def test_seed(self):
        """
        Test that:
            the correct percentage of grid cells have changed from 0 to 1 after seeding
        """
        def count_values(grid):
            count = dict()
            for row in grid:
                for value in row:
                    try:
                        count[value] += 1
                    except KeyError:
                        count[value] = 1
            return count

        grid.seed(self.test_grid, 1, 25)  # Change 25% of cell values to 1
        count = count_values(self.test_grid)
        self.assertEqual(count[0], 9)
        self.assertEqual(count[1], 3)


    def test_update(self):
        """
        Test that:
            the value of each cell in the pentomino grid is correctly updated
        """
        grid.update(self.pentomino, 0, 1)
        self.assertEqual(self.pentomino, [[1, 1, 0, 1],
                                          [1, 1, 0, 1],
                                          [1, 1, 0, 0]])


        def tearDown(self):
            self.cell_states.dispose()
            self.test_grid.dispose()
            self.pentomino.dispose()