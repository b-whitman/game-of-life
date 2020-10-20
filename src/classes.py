class Grid():
    # Methods: resolve()

    def __init__(self, rows, columns):

        self.xdim = rows
        self.ydim = columns
        
        self.cells = [[0 for x in range(columns)] for y in range(rows)]
        self.clickable = 1

    def resolve(self):
        new_grid = Grid(self.xdim, self.ydim)
        for x in range(self.xdim):
            for y in range(self.ydim):
                if self.cells[x][y] == 1:
                    if self.neighbors(x, y) < 2:
                        new_grid.cells[x][y] = 0
                    elif self.neighbors(x, y) > 3:
                        new_grid.cells[x][y] = 1
                elif self.cells[x][y] == 0 and self.neighbors(x, y) == 3:
                    new_grid.cells[x][y] == 1
        
        return new_grid

    def neighbors(self, row, column):
        # Count up live cells in adjacent and diagonal
        # Return total
        # TODO: Try modifying this to close wrap-around on borders
        if row == self.ydim-1:
            row = -1
        if column == self.xdim-1:
            column = -1
            
        total = sum([self.cells[row-1][column-1],
                    self.cells[row][column-1],
                    self.cells[row-1][column],
                    self.cells[row+1][column-1],
                    self.cells[row+1][column],
                    self.cells[row+1][column+1],
                    self.cells[row][column+1],
                    self.cells[row-1][column+1]])

        return total

    
if __name__ == "__main__":
    grid = Grid(10,10)
    x = 2
    y = 4
    grid.cells[y-1][x-1] = not grid.cells[y-1][x-1]
    grid.resolve()
