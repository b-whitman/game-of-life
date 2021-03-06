import pygame
import pygame_textinput
import sys
from classes import Grid, Button

pygame.init()

width = 15
height = 15
margin = 3
rows = 50
columns = 50
menu_x = 150

clock = pygame.time.Clock()
screen = pygame.display.set_mode(((width + margin) * rows + menu_x, 
                                (height + margin) * columns))
textinput = pygame_textinput.TextInput(initial_string="Jump to generation... (INT)",text_color = (0,200,0))

font = pygame.font.SysFont('Corbel',20)

green = (0,255,0)
blue = (0,0,255)
black = 0, 0, 0
white = 255, 255, 255

grid = Grid(50, 50, 15, 15, 3)
play_button = Button(green, 900, 25, 150, 50, 'Play/Pause')
glider_button = Button(white, 900, 850, 50, 50, 'Glider')
clear_button = Button(green, 900, 100, 150, 50, 'Clear')
rand_button = Button(green, 900, 175, 150, 50, 'Random Grid')
speed_button = Button(green, 900, 250, 150, 50, 'Toggle Speed')



def to_grid(n):
    # Convert pixels to grid coordinates
    return (n - margin) // (width + margin) + 1

def draw(grid):
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
                            
    play_button.draw(screen)
    clear_button.draw(screen)
    glider_button.draw(screen)
    rand_button.draw(screen)
    speed_button.draw(screen)

    gen_num = font.render(str(grid.gen_num), True, black, white)
    screen.blit(gen_num, (950, 850))

    clock.tick(30)
    pygame.display.flip()
    pygame.display.update()

def menu(x, y):
    # TODO: This should probably be a class instead of a function
    if play_button.y < y < play_button.y+play_button.height:
        if grid.paused == True:
            print("Pause")
            grid.paused = False
        else:
            print("Play")
            grid.paused = True
    if clear_button.y < y < clear_button.y+clear_button.height:
        grid.reset_cells()
        screen.fill(black)
    if rand_button.y < y < rand_button.y+rand_button.height:
        grid.fill_random()
    if speed_button.y < y < speed_button.y+speed_button.height:
        grid.toggle_speed()
    if glider_button.y < y < glider_button.y+glider_button.height and glider_button.x < x < glider_button.x + glider_button.width:
        print("Glider")

run = True
while run:
    events = pygame.event.get()
    for event in events:
        # TODO: Keyboard controls
        # Define controls from buttons on screen? Will those show up as events?
        if event.type == pygame.QUIT:
            run = False
            pygame.quit(); sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # TODO: Smooth selection while holding down mouse button
            # Use a while loop and keep track of which cells have been toggled
            # Make it smart like picross
            x, y = pygame.mouse.get_pos()
            if x > 900:
                menu(x, y)
            else:    
                x = to_grid(x)
                y = to_grid(y)
                print(f"Click: {x}, {y}")
                if grid.paused == True:
                    grid.cells[y-1][x-1] = not grid.cells[y-1][x-1]
                else:
                    continue
        elif event.type == pygame.KEYDOWN:
            grid.cells = grid.resolve()

    if grid.paused == False:
        grid.cells = grid.resolve()
        draw(grid)
        continue
        
    draw(grid)


pygame.quit()
