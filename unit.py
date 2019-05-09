import pygame
from pygame.sprite import Sprite
import ressources as res

from random import randint
from random import choice

from graphics import Blood_Puddle

import game_functions as gf




class Terran(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, settings, all_groups):
        """Initialize the alien and set its starting position"""
        super(Terran,self).__init__()
        self.settings = settings
        self.screen = settings.screen

        self.all_groups = all_groups
        self.blood_group = all_groups["blood"]


        # Load the alien image and set its rect attribute.
        self.image = res.terran_png.convert()
        self.image_w = res.terran_w_png.convert()
        self.image_d = res.terran_d_png.convert()
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        self.name = "Terran"
        self.type = 1
        self.accuracy = self.settings.accuracy_terran

        self.blood_drawn = False
        self.directon_facing = "right"

        self.kill_count = 0

        self.shoot_delay = self.settings.shoot_delay_terran
        self.last_update = self.settings.last_update_terran
        self.army_side = "left"

        #Test Coma
        self.combat_active = 1

        # Test AutoShoot
        self.shooting_order = 0
        self.ready_to_fire = 0 # 2 = nicht in gruppe shooten
        self.id = 0





    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def flip_horizontal(self):
        """Flip the unit sideways (crate_army)"""
        self.image = pygame.transform.flip(self.image, True, False)

    def draw_blood_splatter(self):
        # Create Blood Splatter and add to group
        # IF Blood is not drawn yet
        if self.blood_drawn == False:
            for i in range(self.settings.blood_splatter_count):
                blood_splatter = Blood_Puddle(self.settings)
                blood_splatter.rect.x = (self.rect.x + (self.rect.width / 2)) + randint(-100, 100)
                blood_splatter.rect.y = (self.rect.y + self.rect.height) + randint(-20, 20)
                blood_splatter.radius = randint(2, 15)
                blood_splatter.color = pygame.Color(255, 0, 0)
                self.blood_group.add(blood_splatter)

            self.blood_drawn = True

    def draw_wound(self):
        # Change Images considering Unit.Type
        if self.type == 2:
            self.image = self.image_w
            self.draw_blood_splatter()

        if self.type == 0:
            self.image = self.image_d
            self.draw_blood_splatter()

    def unit_wiggle(self):
        """Wiggle (if wounded)"""
        if self.type == 2:
            self.rect.x += randint(-1, 1)
            self.rect.y += randint(-1, 1)


    def auto_shoot(self, all_groups):
        """Let a unit shoot individually based on shooting delay"""
        """PROBLEM: Overshooting on a single unit?"""
        # Get Shoot Delay, 1000ms - 1001ms = 1ms, only shoot at over the delay
        now = pygame.time.get_ticks()
        if now - self.last_update > self.shoot_delay and self.combat_active == 1:
            self.last_update = now

            # Check which side you are on, which side is the enemy
            if self.army_side == "left":
                enemys = all_groups["unit_group_r"]
            elif self.army_side == "right":
                enemys = all_groups["unit_group_l"]

            # Check if Group not Empty, Randomly choose Enemy, shoot
            if enemys:
                target = choice(enemys.sprites())
                gf.hit_calc(self.settings, self, target, all_groups)

                """TEST"""
                print("Terran", self.id, " ", self.army_side, "BAM BAM")

            #If unit is not in individual mode (2) reset ready to fire
            if self.ready_to_fire != 2:
                self.ready_to_fire = 0


    def update(self):

        """Auto_shoot"""
        if self.combat_active == 1 and self.ready_to_fire != 0:
            self.auto_shoot(self.all_groups)

        self.unit_wiggle()














