# Video link: https://youtu.be/3UxnelT9aCo
import pygame as pg
from pygame.sprite import Sprite
import sys




WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class WorldMap(Sprite):
    """A class to represent the World Map"""

    def __init__(self, settings, all_groups):
        """Initialize the MAP ..."""
        super(WorldMap,self).__init__()
        self.settings = settings
        self.screen = settings.screen
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        self.tilesize = settings.tilesize

        self.all_groups = all_groups



    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def draw_grid(self):
        for x in range(self.settings.menu_offset, self.screen_width, self.tilesize):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, self.tilesize):
            pg.draw.line(self.screen, LIGHTGREY, (self.settings.menu_offset, y), (self.screen_width, y))

    def draw(self):
        self.draw_grid()

    def update(self):
        self.draw_grid()




class TestPlayer(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, settings, all_groups, x, y):
        """Initialize the alien and set its starting position"""
        super(TestPlayer,self).__init__()
        self.settings = settings
        self.screen = settings.screen

        self.screen = settings.screen
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height
        self.tilesize = settings.tilesize

        self.image = pg.Surface((self.tilesize, self.tilesize))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.all_groups = all_groups
        self.blood_group = all_groups["blood"]




    def move(self, dx=0, dy=0):
        if not self.out_of_bounds(dx, dy):
            self.x += dx
            self.y += dy

            """TEST"""
            print("x ", self.x)
            print("y ", self.y)
            print((self.settings.menu_offset / self.tilesize))
            print(dx)

    def update(self):
        self.rect.x = self.x * self.tilesize
        self.rect.y = self.y * self.tilesize

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)


    def out_of_bounds(self, dx=0, dy=0):
        if self.x + dx < (self.settings.menu_offset / self.tilesize)\
                or self.x + dx > (self.screen_width / self.tilesize)\
                or self.y + dy > (self.screen_height / self.tilesize)\
                or self.y + dy < 0:
            return True
        return False








