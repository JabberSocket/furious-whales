"""
_whale_

This module implements a whale sprite. It can move in the x, y plane
and carries some momentum. If it reaches a screen boundary the whale
will stop moving in the colliding axis.
"""
import pygame_sdl2
import math


ACCELERATION = 1
MAX_SPEED = 5
WHALE_IMG = "whale.png"
WHALE_SIZE = (150, 82) 


class WhaleSprite(pygame_sdl2.sprite.Sprite):
    def __init__(self, image, position, display):
        pygame_sdl2.sprite.Sprite.__init__(self)
        # We do rotations so we need to track the original image as well as
        # the image used for rendering.
        self.original_image = pygame_sdl2.transform.scale(pygame_sdl2.image.load(image), WHALE_SIZE)
        self.image = pygame_sdl2.transform.scale(pygame_sdl2.image.load(image), WHALE_SIZE)
        self.position = position  # x, y
        self.x_speed = 0  # pixels per update
        self.y_speed = 0
        self.display = display
        
    def update(self):
        """
        _update_
        
        Move the ship's position, turning around if we reach the screen edge.
        """
        for event in pygame_sdl2.event.get():
            if event.type == pygame_sdl2.KEYDOWN:
                if event.key == pygame_sdl2.K_DOWN:
                    self.y_speed += ACCELERATION
                    if self.y_speed > MAX_SPEED: self.y_speed = MAX_SPEED
                if event.key == pygame_sdl2.K_UP:
                    self.y_speed -= ACCELERATION
                    if self.y_speed < -MAX_SPEED: self.y_speed = -MAX_SPEED
                if event.key == pygame_sdl2.K_RIGHT:
                    self.x_speed += ACCELERATION
                    if self.x_speed > MAX_SPEED: self.x_speed = MAX_SPEED
                if event.key == pygame_sdl2.K_LEFT:
                    self.x_speed -= ACCELERATION
                    if self.x_speed < -MAX_SPEED: self.x_speed = -MAX_SPEED

        rotation = - self.y_speed * math.pi / 2
        self.image = pygame_sdl2.transform.rotate(self.original_image, rotation)
        x, y = self.position
        x_new = x + self.x_speed
        y_new = y + self.y_speed

        x_boundary, y_boundary = self.at_boundary(x_new, y_new)

        if x_boundary:
            x_new = x
            self.x_speed = 0

        if y_boundary:
            y_new = y
            self.y_speed = 0

        self.position = x_new, y_new
        
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def at_boundary(self, x, y):
        """
        Check if the whale is at a screen boundary. Returns a tuple of
        (x_boundary, y_boundary) where each element is True or False if a
        boundary is met.
        """
        x_boundary = False
        y_boundary = False

        if x >= self.display.get_rect().right - WHALE_SIZE[0] / 2:
            x_boundary =  True

        if x <= self.display.get_rect().left + WHALE_SIZE[0] / 2:
            x_boundary = True

        if y <= self.display.get_rect().top + WHALE_SIZE[1] / 2:
            y_boundary = True

        if y >= self.display.get_rect().bottom - WHALE_SIZE[1] / 2:
            y_boundary = True
        
        return (x_boundary, y_boundary)


def get_whale(display):
    """
    Return a group of just one whale sprite, initialized in the center.
    """
    position = display.get_rect().center
    whale = WhaleSprite(WHALE_IMG, position, display)
    whale_group = pygame_sdl2.sprite.RenderPlain(whale)
    return whale_group
