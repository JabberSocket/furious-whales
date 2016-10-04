import pygame_sdl2
import math

import pirate_ship
import waves
import whale

pygame_sdl2.init()

display_width = 800
display_height = 600

display = pygame_sdl2.display.set_mode((display_width, display_height))

pygame_sdl2.display.set_caption('There Will be Whales')

clock = pygame_sdl2.time.Clock()

whale_img = pygame_sdl2.image.load("whale.png")

WHITE = (255, 255, 255)
BLUE = (0, 0, 192)

x = (display_width * 0.25)
y = (display_height * 0.4)
position = (x, y)

ACCELERATION = 1
MAX_SPEED = 10
speed = 0
rotation = 0.0

ship_group = pirate_ship.get_pirate_ship(display)
wave_group = waves.get_waves(display)
whale_group = whale.get_whale(display)

quit = False
while not quit:
    clock.tick(30)

    # INPUT
    for event in pygame_sdl2.event.get(pygame_sdl2.QUIT):
        quit = True

    display.fill(BLUE)

    # WHALE RENDERING
    whale_group.update()
    whale_group.draw(display)

    # WAVE RENDERING
    wave_group.update()
    wave_group.draw(display)

    # SHIP RENDERING
    ship_group.update()
    ship_group.draw(display)

    pygame_sdl2.display.flip()

pygame_sdl2.quit()
