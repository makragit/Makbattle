import pygame
from pygame.sprite import Sprite

import pygame.font

WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)
font_name = pygame.font.match_font('arial')

class Button():
    """A class to represent a single alien in the fleet"""

    def __init__(self, settings, size, x, y, text):
        """Initialize the alien and set its starting position"""
        self.settings = settings
        self.screen = settings.screen

        self.font = pygame.font.Font(font_name, size)
        self.text_surface = self.font.render(text, True, WHITE)

        self.text_rect = self.text_surface.get_rect()
        self.text_rect.topleft = (x, y)


    def blitme(self):
        """Draw the alien at its current location"""
        #self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text_surface, self.text_rect)

    def update(self):
        pass




"""in check events"""
"""
def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
"""

