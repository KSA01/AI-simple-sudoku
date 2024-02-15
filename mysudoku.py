
import random
import math
from util import ALLOWED

# ASSIGNMENT #3
# Write this function to solve the sudoku puzzle
# DO NOT change the function name SOLVE
# DO NOT change the input parameters of SOLVE
# DO NOT change anything in the util module or the main file
# To test, run main.py
# BTW: This is an easy Sudoku puzzle to solve. You won't need to do some of the advance stuff that is needed to solve the harder ones.
# Make use of 'grid' and 'constraintList' and the tools provided in the util module; do not grab a solution from the internet
# Zip this entire project (not just this file) and submit to Moodle
    
def SOLVE(grid, constraintList):
    def is_valid(x, y, val, grid, allowed):
        return val in allowed.AllowedAtLocation(x, y) # Checks for values allow at current location
    
    def backtrack(csp, x, y, next_x, next_y): # Backtracking function
        for val in csp.AllowedAtLocation(x, y):
            if is_valid(x, y, val, grid, csp): # Checks for if the value is not violating rules before moving onto the next one
                grid.SetValue(x, y, val)
                if solve_csp(next_x, next_y):
                    return True

    def solve_csp(x, y):
        allowed = ALLOWED()

        if y == 9: # Checks for the last row
            return True # It reached the end of the puzzle
        
        next_x = (x + 1) % 9
        next_y = y + 1 if next_x == 0 else y # If next x val is starting over again at 0 then increment y
        
        if grid.GetValue(x, y) is not None: # Checks for if the grid value (x and y) are already filled and cannot be changed
            return solve_csp(next_x, next_y)
        
        allowed.Constrain(grid, constraintList) # Works on solving puzzle by determining what value it can set

        #backtracking
        if backtrack(allowed, x, y, next_x, next_y):
            return True
                
        grid.SetValue(x, y, None) # Finally sets the final value for that grid (x, y)
        return False
    
    if solve_csp(0, 0): # Starts solving the puzzle at (0, 0)
        # If it solves it completely it'll return the grid otherwise None
        return grid
    else:
        return None