import pygame
import sys

pygame.init()

size = width, height = 1024, 768
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

red = (255,0,0)
blue = (0,0,255)
black = 0, 0, 0
speed = [2, 2]

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

def updatePoints(points):
    new_points = []
    for point in points:
        new_points.append((point[0]+2, point[1]))
    return new_points

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()    

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    clock.tick(60)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

# pygame.quit()
