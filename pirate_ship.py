"""
_pirate_ship_

This module implements the sprite logic for a pirate ship.

It will bounce left and right across the top of the display.
"""
import pygame_sdl2
import math


SHIP_IMG = "pirate_ship.png"
SHIP_SIZE = (150, 150)
SPEED = 3


class PirateShipSprite(pygame_sdl2.sprite.Sprite):
    def __init__(self, image, position, display):
        pygame_sdl2.sprite.Sprite.__init__(self)
        self.image = pygame_sdl2.image.load(image)
        self.image = pygame_sdl2.transform.scale(self.image, SHIP_SIZE)
        self.position = position  # x, y
        self.speed = SPEED  # pixels per update
        self.direction = 1  # 1 == positive x, -1 == negative x
        self.display = display
        
    def update(self):
        """
        _update_
        
        Move the ship's position, turning around if we reach the screen edge.
        """
        x, y = self.position
        x_new = x + self.direction * self.speed
        if self.should_turn(x_new):
            self.direction = -self.direction
            x_new = x + self.direction * self.speed

        self.position = x_new, y
        
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def should_turn(self, x_new):
        """
        _should_turn_

        If x_new is a half-ship away from a boundary, return True.
        """
        if x_new >= self.display.get_rect().right - SHIP_SIZE[0] / 2:
            return True

        if x_new <= self.display.get_rect().left + SHIP_SIZE[0] / 2:
            return True
        
        return False

def get_pirate_ship(display):
    """
    Return a group of just one ship sprite, initialized just off the top left position.
    """
    position = (10 + SHIP_SIZE[0] / 2, (display.get_rect().top + 10 + SHIP_SIZE[1] / 2))  
    ship = PirateShipSprite(SHIP_IMG, position, display)
    ship_group = pygame_sdl2.sprite.RenderPlain(ship)
    return ship_group
