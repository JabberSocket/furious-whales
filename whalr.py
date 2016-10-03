import pygame_sdl2
import math

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

quit = False
while not quit:
    clock.tick(30)

    # INPUT
    for event in pygame_sdl2.event.get():
        if event.type == pygame_sdl2.KEYDOWN:
            if event.key == pygame_sdl2.K_DOWN:
                speed += ACCELERATION
                if speed > MAX_SPEED: speed = MAX_SPEED
                if speed < -MAX_SPEED: speed = -MAX_SPEED
            if event.key == pygame_sdl2.K_UP:
                speed -= ACCELERATION
                if speed > MAX_SPEED: speed = MAX_SPEED
                if speed < -MAX_SPEED: speed = -MAX_SPEED
        if event.type == pygame_sdl2.QUIT:
            quit = True

    # SIMULATION
    x, y = position
    y = y + speed
    position = x, y
    rotation = - speed * math.pi / 2

    # RENDERING
    rotated = pygame_sdl2.transform.rotate(whale_img, rotation)
    rect = rotated.get_rect()
    rect.center = position
    display.fill(BLUE)
    display.blit(rotated, rect)
    pygame_sdl2.display.flip()

pygame_sdl2.quit()