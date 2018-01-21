from pygame import display, draw, time, event, KEYDOWN
from random import randint


MAX_SIZE = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Circle:
    def __init__(self):
        self.colour = [randint(0, 255) for _ in range(3)]
        self.center = [randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)]
        self.radius = 1

    def grow(self):
        self.radius += 1


screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = time.Clock()
circles = []
while True:
    screen.fill([255, 255, 255])  # reset screen
    # limit number and size of circles
    if len(circles) == MAX_SIZE:
        circles = circles[1:]
    circles.append(Circle())

    for c in circles:
        draw.circle(screen, c.colour, c.center, c.radius, 1)
        c.grow()

    # wait for next frame
    clock.tick(60)
    display.flip()

    # detect key pressed
    ev = event.poll()
    if ev.type == KEYDOWN:
        break
