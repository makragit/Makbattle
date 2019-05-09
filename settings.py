import pygame
from pygame.sprite import Sprite

from random import randint

class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (0, 50, 0)

        self.title = "Mak Battle Simulator v2"

        # Background WOANDERS?
        self.background = pygame.image.load('images/background2.png')
        self.background_rect = self.background.get_rect()

        # Maxerl
        self.army_size_l = 100
        self.army_size_r = 100

        self.blood_splatter_count = 5

        self.accuracy_terran = 30
        self.accuracy_psion = 30

        self.shoot_delay_terran = 1
        self.shoot_delay_psion = 1

        #self.last_update_terran = randint(0, 500)
        #self.last_update_psion = randint(0, 500)

        self.last_update_terran = 1
        self.last_update_psion = 1

        # World Map
        self.bg_color_map = (0, 0, 0)
        self.tilesize = 32
        self.menu_offset = self.tilesize * 10




        # Controls
        self.control_key_quit = pygame.K_q
        self.control_key_up = pygame.K_UP
        self.control_key_down = pygame.K_DOWN
        self.control_key_left = pygame. K_LEFT
        self.control_key_right = pygame. K_RIGHT

        # Controls Menu
        self.control_key_play = pygame.K_p


        #GAME STATE WO?
        self.game_state = "map"






