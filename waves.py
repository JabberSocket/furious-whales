"""
_waves_

This module implements the sprite logic for the waves.

"""
import pygame_sdl2
import math


WAVE_IMG = "wave.png"
SPEED = 2

class WaveSprite(pygame_sdl2.sprite.Sprite):
    def __init__(self, image, position, display):
        pygame_sdl2.sprite.Sprite.__init__(self)
        self.image = pygame_sdl2.image.load(image)
        self.position = position  # x, y
        self.speed = SPEED  # pixels per update
        self.display = display

    def update(self):
        """
        _update_
        
        Move the wave's position, resetting after one wavelength.
        """
        x, y = self.position
        x_new = x + self.speed

        if x_new >= self.display.get_rect().right + (self.image.get_size()[0] - self.display.get_size()[0]):
            x_new = self.display.get_rect().right

        self.position = x_new, y

        self.rect = self.image.get_rect()
        self.rect.right = self.position[0]


def get_waves(display):
    """
    Return a sprite of waves
    """
    position = (display.get_rect().right, 150)
    wave = WaveSprite(WAVE_IMG, position, display)
    wave_group = pygame_sdl2.sprite.RenderPlain(wave)
    return wave_group
