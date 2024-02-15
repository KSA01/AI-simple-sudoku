
import numpy as np

class GRID:
    def __init__(self, init=[[None for i in range(9)] for j in range(9)]):
        self.grid = init

    def SetValue(self, x, y, value):
        self.grid[y][x] = value

    def GetValue(self, x, y):
        return self.grid[y][x]
    
    def GetCopy(self):
        return GRID([[self.grid[y][x] for x in range(9)] for y in range(9)])
    
    def __str__(self):
        return str(np.array(self.grid))
    
class CONSTRAINT:
    def __init__(self):
        pass

    def CanSetValue(self, grid, x, y, value):
        return True

class ALL_DIFF(CONSTRAINT):
    def __init__(self, *locations): # locations are tuples of coordinates
        super().__init__()
        self.locations = locations

    def CanSetValue(self, grid, x, y, value):
        locFound = False
        valueFound = False
        for loc in self.locations:
            if loc[0] == x and loc[1] == y:
                locFound = True
            elif grid.GetValue(*loc) == value:
                valueFound = True
        return not (locFound and valueFound)

class ALLOWED:
    def __init__(self):
        self.allowed = [[[k for k in range(1,10)] for i in range(9)] for j in range(9)]

    def Constrain(self, grid, constraintList):
        for y in range(9):
            for x in range(9):
                if grid.GetValue(x, y) != None:
                    self.allowed[y][x] = None
                    continue
                for i in range(len(self.allowed[y][x])-1, -1, -1):
                    v = self.allowed[y][x][i]
                    for c in constraintList:
                        if not c.CanSetValue(grid, x, y, v):
                            del self.allowed[y][x][i]
                            if len(self.allowed[y][x]) == 0:
                                return False
                            break
        return True

    def AllowedAtLocation(self, x, y):
        return self.allowed[y][x]

    # Returns list of tuples: (# allowed, x, y, [values allowed])
    def GetSortedAllowedList(self):
        lst = []
        for y in range(9):
            for x in range(9):
                if self.allowed[y][x] is not None:
                    lst.append((len(self.allowed[y][x]), x, y, self.allowed[y][x]))
        lst.sort()
        return lst
