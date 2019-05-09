import sys
import pygame
from pygame.sprite import Group
from settings import Settings

from unit import Terran
from psion import Psion

from map import WorldMap
from map import TestPlayer
from buttons import Button

from graphics import Blood_Puddle
import game_functions as gf

from time import sleep


FPS = 60
clock = pygame.time.Clock()

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    pygame.display.set_caption(settings.title)


    unit_group_l = Group()
    unit_group_r = Group()
    blood = Group()
    unit_group_dead = Group()
    hit_decals = Group()

    buttons = Group()


    all_groups = {
        "unit_group_l": unit_group_l,
        "unit_group_r": unit_group_r,
        "blood": blood,
        "unit_group_dead": unit_group_dead,
        "hit_decals": hit_decals,
        "buttons": buttons
    }

    #Initialize World Map Classes
    """in all_groups/ andere Gruppe?"""
    worldmap = WorldMap(settings, all_groups)
    testplayer = TestPlayer(settings, all_groups, 15, 10)
    testbutton = Button(settings, 32, 30, 30, "test")

    #Add Units to group
    gf.add_unit(settings, unit_group_l, Terran, settings.army_size_l, all_groups)
    gf.add_unit(settings, unit_group_r, Psion, settings.army_size_r, all_groups)


    gf.create_army(settings, unit_group_l, all_groups, "left")
    gf.create_army(settings, unit_group_r, all_groups, "right")


    #Start the main loop for the game.
    while True:

        """MENU"""
        #Menu Screen
        while settings.game_state == "menu":
            gf.check_events_menu(settings, all_groups)
            gf.update_screen_menu(settings, all_groups)

        """MAP"""
        #Map Screen
        while settings.game_state == "map":
            gf.check_events_map(settings, testplayer, all_groups)
            gf.update_screen_map(settings, worldmap, testplayer, testbutton,  all_groups)

            pass

        """Battle"""
        #Battle Screen
        while settings.game_state == "battle":

            # Get Time
            clock.tick(FPS) / 1000
            ticks = pygame.time.get_ticks()
            """TEST TICKS"""
            #print(ticks)


            # Watch for keyboard and mouse events.
            gf.check_events(settings, all_groups)

            gf.update_screen(settings, all_groups)


run_game()

