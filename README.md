# Conway's Game of Life

The game can be run by cloning this repository and running, from the game-of-life directory in the console:
 
    python3 life.py
    
 To run tests for the grid module:
 
    python3 -m unittest tests/test_grid.py
 
 </br>
 This implementation uses toroidal geometry to simulate an infinite grid.  
 This means the top row is considered adjacent to the bottom row and the left-most column considered adjacent to the right-most column.  

</br>
The usual rules for cell interactions are applied:  
   
 • A live cell with fewer than 2 neighbours dies by underpopulation.  
 • A live cell with more than 3 neighbours dies by overpopulation.  
 • A dead/empty cell with exactly 3 neighbours becomes live by reproduction.  
  
</br>
The following assumptions have been made:</br> 

  Cells are selected randomly for seeding the initial grid.  

  All cell interactions occur simultaneously in an iteration.  

  Cell age is not relevant. This has interesting implications:  
  • All live cells are equal. There is no maturation; new and old cells are just as capable of reproduction.  
  • There is no maximum lifespan for cells: they can live forever!
