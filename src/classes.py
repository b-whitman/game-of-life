import pygame

class Grid():
    # Methods: resolve()

    def __init__(self, rows, columns):

        self.xdim = rows
        self.ydim = columns
        
        self.cells = [[0 for x in range(columns)] for y in range(rows)]
        self.clickable = 1

    def resolve(self):

        new_grid = [[0 for x in range(self.ydim)] for y in range(self.xdim)]

        for x in range(self.xdim):
            for y in range(self.ydim):
                neighbors = self.neighbors(x, y)
                is_alive = self.cells[x][y]

                if is_alive == 1:
                    if neighbors < 2:
                        new_grid[x][y] = 0
                    elif 2 <= neighbors <= 3:
                        new_grid[x][y] = 1
                    elif neighbors > 3:
                        new_grid[x][y] = 0

                elif (is_alive == 0) and (neighbors == 3):
                    new_grid[x][y] = 1
                    
        return new_grid

    def neighbors(self, row, column):
        # Count up live cells in adjacent and diagonal
        # Return total
        # TODO: Try modifying this to close wrap-around on borders
        if row == self.ydim-1:
            row = -1
        if column == self.xdim-1:
            column = -1
            
        total = sum([
                    self.cells[row-1][column-1],
                    self.cells[row-1][column],
                    self.cells[row-1][column+1],
                    self.cells[row+1][column-1],
                    self.cells[row+1][column],
                    self.cells[row+1][column+1],
                    self.cells[row][column-1],
                    self.cells[row][column+1]
                    ])
                    
        return total

class Button():
    def __init__(self, color, x,y,width,height,text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        pygame.draw.rect(win, 
        self.color, 
        (self.x,self.y,self.width,self.height),
        0)

        if self.text != '':
            font = pygame.font.SysFont('Corbel',35)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, 
                    (self.x + (self.width/2 - text.get_width()/2), 
                    self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y+self.height:
                return True
        
        return False

    
if __name__ == "__main__":
    grid = Grid(10,10)
    x = 2
    y = 4
    grid.cells[y-1][x-1] = not grid.cells[y-1][x-1]
    print(grid.resolve())
