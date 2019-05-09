import pygame
from pygame.sprite import Sprite
import ressources as res
from random import randint

RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(70, 70, 200)



# class Wall(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.walls
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE
#
#
#         RED = pygame.Color(255, 0, 0)
#         pygame.draw.circle(settings.screen, RED, self.center, 5, 0)
#
#         pygame.draw.circle(screen, BLUE, pos, 20, 0)  # Here <<<




        # x = (400, 300)
        # RED = pygame.Color(255, 0, 0)
        # for i in range(8):
        #     x = (400 + randint(-10, 10), 300 + randint(-10, 10))
        #     pygame.draw.circle(settings.screen, RED, x, randint(10, 20), 0)

class Blood_Puddle(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, settings):
        """Initialize the alien and set its starting position"""
        super(Blood_Puddle,self).__init__()
        self.settings = settings
        self.screen = settings.screen
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.radius = 10

        self.name = "Blood"
        self.color = RED


    def update(self):
        """Draw Blood"""
        pygame.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y), self.radius, 0)


class Hit_Decal(Sprite):
    """A class to represent Gun Flash and Hitmarkers"""

    def __init__(self, settings):
        """Initialize ..."""
        super(Hit_Decal,self).__init__()

        self.settings = settings
        self.screen = settings.screen

        self.image = res.pew_png.convert()
        self.rect = self.image.get_rect()

        self.image2 = res.gib_png.convert()
        self.rect2 = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        # Store the alien's exact position.
        self.x = float(self.rect.x)


        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100



    def update(self):
        #self.rect.x = unit.rect.x
        #self.rect.y = unit.rect.y

        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.kill()

        self.screen.blit(self.image, self.rect)


        # now = pygame.time.get_ticks()
        # if now - self.last_update > self.frame_rate:
        #     self.last_update = now
        #     self.frame += 1
        #     if self.frame == len(explosion_anim[self.size]):
        #         self.kill()
        #     else:
        #         center = self.rect.center
        #         self.image = explosion_anim[self.size][self.frame]
        #         self.rect = self.image.get_rect()
        #         self.rect.center = center



    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
        #self.screen.blit(self.image2, self.rect2)


        #unit = typ(settings, all_groups)

        # self.last_update = pygame.time.get_ticks()
        # self.frame_rate = 50
        #
        # def update(self):
        #     now = pygame.time.get_ticks()
        #     if now - self.last_update > self.frame_rate:
        #         self.last_update = now
        #         self.frame += 1
        #         if self.frame == len(explosion_anim[self.size]):
        #             self.kill()
        #         else:
        #             center = self.rect.center
        #             self.image = explosion_anim[self.size][self.frame]
        #             self.rect = self.image.get_rect()
        #             self.rect.center = center