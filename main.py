
from util import ALL_DIFF
from util import GRID
from mysudoku import SOLVE

grid = GRID()
grid.SetValue(2,0,3)
grid.SetValue(4,0,2)
grid.SetValue(6,0,6)
grid.SetValue(0,1,9)
grid.SetValue(3,1,3)
grid.SetValue(5,1,5)
grid.SetValue(8,1,1)
grid.SetValue(2,2,1)
grid.SetValue(3,2,8)
grid.SetValue(5,2,6)
grid.SetValue(6,2,4)
grid.SetValue(2,3,8)
grid.SetValue(3,3,1)
grid.SetValue(5,3,2)
grid.SetValue(6,3,9)
grid.SetValue(0,4,7)
grid.SetValue(8,4,8)
grid.SetValue(2,5,6)
grid.SetValue(3,5,7)
grid.SetValue(5,5,8)
grid.SetValue(6,5,2)
grid.SetValue(2,6,2)
grid.SetValue(3,6,6)
grid.SetValue(5,6,9)
grid.SetValue(6,6,5)
grid.SetValue(0,7,8)
grid.SetValue(3,7,2)
grid.SetValue(5,7,3)
grid.SetValue(8,7,9)
grid.SetValue(2,8,5)
grid.SetValue(4,8,1)
grid.SetValue(6,8,3)

constraintList = []
for i in range(9):
    constraintList.append(ALL_DIFF(*[(x,i) for x in range(9)]))
    constraintList.append(ALL_DIFF(*[(i,y) for y in range(9)]))
    constraintList.append(ALL_DIFF(*[(x+3*(i%3),y+3*(i//3)) for x in range(3) for y in range(3)]))

print(grid)

SOLVE(grid, constraintList)

print() # Added for print clarity
print(grid)