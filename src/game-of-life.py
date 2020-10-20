import pygame
import sys
from classes import Grid

pygame.init()

width = 15
height = 15
margin = 3

rows = 20
columns = 20
clock = pygame.time.Clock()
screen = pygame.display.set_mode(((width + margin) * rows, 
                                (height + margin) * columns))

red = (255,0,0)
blue = (0,0,255)
black = 0, 0, 0
white = 255, 255, 255

grid = Grid(rows, columns)

def to_grid(n):
    # Convert pixels to grid coordinates
    return (n - margin) // (width + margin) + 1

while (True):
    for event in pygame.event.get():
        # TODO: Keyboard controls
        # Define controls from buttons on screen? Will those show up as events?
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # TODO: Smooth selection while holding down mouse button
            # Use a while loop and keep track of which cells have been toggled
            # Make it smart like picross
            x, y = pygame.mouse.get_pos()
            x = to_grid(x)
            y = to_grid(y)
            print(f"Click: {x}, {y}")
            grid.cells[y-1][x-1] = not grid.cells[y-1][x-1]
        elif event.type == pygame.KEYDOWN:
            grid.cells = grid.resolve()
        

    for row in range(rows):
        for column in range(columns): 
            color = white
            if grid.cells[row][column] == 1:
                color = blue   
            pygame.draw.rect(screen, 
                            color, 
                            [(margin + width) * column + margin,
                            (margin + height) * row + margin,
                            width,
                            height])

    pygame.display.update()

pygame.quit()
