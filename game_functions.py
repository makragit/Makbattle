import sys
import pygame
import math

from time import sleep
from random import randint
from random import choice

from graphics import Hit_Decal
from psion import Psion


def update_screen_menu(settings, all_groups):
    """Update images on the screen and flip tot the new screen."""
    # Redraw the MENU screen during each pass through the loop.
    settings.screen.fill(settings.bg_color)
    #settings.screen.blit(settings.background, settings.background_rect)

    pygame.display.flip()

def update_screen_map(settings, worldmap, testplayer, testbutton, all_groups):
    """Update images on the screen and flip tot the new screen."""
    # Redraw the MAP screen during each pass through the loop.
    settings.screen.fill(settings.bg_color_map)
    #settings.screen.blit(settings.background, settings.background_rect)

    worldmap.update()

    testplayer.update()
    testplayer.blitme()

    #worldmap.blitme()
    testbutton.blitme()

    pygame.display.flip()

def update_screen(settings, all_groups):
    """Update images on the screen and flip tot the new screen."""
    # Redraw the screen during each pass through the loop.
    settings.screen.fill(settings.bg_color)
    settings.screen.blit(settings.background, settings.background_rect)

    unit_group_l = all_groups["unit_group_l"]
    unit_group_r = all_groups["unit_group_r"]
    blood = all_groups["blood"]
    hit_decals = all_groups["hit_decals"]

    blood.update()

    #Draw and Update Units
    army_update_order(unit_group_l) #TESTTEST TEST Auto Shoot Order!
    unit_group_l.update()
    army_update_order(unit_group_r) #TESTTEST TEST Auto Shoot Order!
    unit_group_r.update()
    all_groups["unit_group_dead"].update()

    hit_decals.update()

    blood.draw(settings.screen)
    all_groups["unit_group_dead"].draw(settings.screen)
    unit_group_l.draw(settings.screen)
    unit_group_r.draw(settings.screen)

    hit_decals.draw(settings.screen)

    pygame.display.flip()

def check_events_menu(settings, all_groups):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("x: ", mouse_x)
            print("y: ", mouse_y)

            #TEST
            settings.game_state = "battle"

        if event.type == pygame.KEYDOWN:
            # Quit
            if event.key == settings.control_key_quit:
                sys.exit()

            if event.key == settings.control_key_play:
                settings.game_state = "battle"

def check_events_map(settings, testplayer, all_groups):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("x: ", mouse_x)
            print("y: ", mouse_y)

            #TEST
            #settings.game_state = "battle"

        if event.type == pygame.KEYDOWN:
            # Quit
            if event.key == settings.control_key_quit:
                sys.exit()

            if event.key == settings.control_key_play:
                settings.game_state = "battle"

            if event.key == pygame.K_LEFT:
                testplayer.move(dx=-1)
            if event.key == pygame.K_RIGHT:
                testplayer.move(dx=1)
            if event.key == pygame.K_UP:
                testplayer.move(dy=-1)
            if event.key == pygame.K_DOWN:
                testplayer.move(dy=1)




def check_events(settings, all_groups):

    terran = all_groups["unit_group_l"]

    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("x: ", mouse_x)
            print("y: ", mouse_y)

        if event.type == pygame.KEYDOWN:
            # Quit
            if event.key == settings.control_key_quit:
                sys.exit()

            if event.key == settings.control_key_up:
                for unit in terran:
                    unit.move(0, -5)

            if event.key == settings.control_key_down:
                for unit in terran:
                    unit.move(0, 5)

            if event.key == settings.control_key_left:
                for unit in terran:
                    unit.move(-5, 0)

            if event.key == settings.control_key_right:
                for unit in terran:
                    unit.move(5, 0)

def add_unit(settings, group, typ, number_units, all_groups):
    id_number = 0
    for i in range(number_units):
        unit = typ(settings, all_groups)

        #Get ID
        id_number += 1
        unit.id = id_number

        group.add(unit)

"""UPDATE REFRACTOR"""
# (settings, group, all_groups, -1) side = "left" "right Seite wechseln?
def create_army(settings, group, all_groups, side):
    """Create the army."""
    # ...

    army_size = len(group)

    #Define Side Multiplier and flip image
    if side == "left":
        center_multiplier = 3
        side_multiplier = -1

    elif side == "right":
        center_multiplier = 5
        side_multiplier = 1

        for unit in group:
            unit.flip_horizontal()

    #Square = Rows, 3*3 etc. durch Soldatenzahl herausfinden
    army_sqr = int(math.sqrt(army_size))

    #Platzierung Startort
    battle_center_x = ((settings.screen_width / 8) * center_multiplier)
    battle_center_y = (settings.screen_height / 2)


    #unit width und height herausfinden lol
    for i in group:
        unit_width = i.rect.width
        unit_height = i.rect.height
        break

    new_x = []
    new_y = []

    #Change y_step x_step and +1 for formation order (long or wide)
    for x_step in range(army_sqr):
        for y_step in range(army_sqr+1):

            kopfweh_x = battle_center_x
            kopfweh_y = battle_center_y

            kopfweh_x += ((unit_width + 10) * (x_step)) * side_multiplier
            kopfweh_y += (unit_height - 20) * (y_step)

            new_x.append(kopfweh_x)
            new_y.append(kopfweh_y)

    #Apply x and y to units in group



    for unit, range_army in zip(group, range(army_size)):
        unit.rect.x = new_x[range_army]
        unit.rect.y = new_y[range_army]

        """TEST"""
        unit.army_side = side


        """Placement Step by Step
        sleep(0.1)
        update_screen(settings, all_groups)
        """

    #Move army up (to the middle)
    for unit in group:
        unit.rect.y -= unit_height * (army_sqr / 4)

"""BATTLE""""""BATTLE""""""BATTLE""""""BATTLE""""""BATTLE"""

#ALT
def battle(settings, all_groups):

    unit_group_l = all_groups["unit_group_l"]
    unit_group_r = all_groups["unit_group_r"]


    """TEST ROUND COUNTER"""
    i=0

    #Start loop unit_l -> unit_r, unit_r -> unit_l
    for unit_l, unit_r in zip(unit_group_l, unit_group_r):


        # Unit on the LEFT shoots Random Unit on the RIGHT
        random_unit_r = choice(unit_group_r.sprites())
        hit_calc(settings, unit_l, random_unit_r, all_groups)

        """TEST Step through each Round"""
        print("Round Counter", unit_l.name, i, "group len: ", len(unit_group_l))
        i+=1
        #sleep(0.05)
        update_screen(settings, all_groups)
        """"""

        # Unit on the RIGHT shoots Random Unit on the LEFT
        random_unit_l = choice(unit_group_l.sprites())
        hit_calc(settings, unit_r, random_unit_l, all_groups)


        """TEST Step through each Round"""
        print("Round Counter:", unit_r.name , i, " group len: ", len(unit_group_r))
        i+=1
        #sleep(0.05)
        update_screen(settings, all_groups)
        """"""

        # Check if an army is defeated (not checks for FALSE if group is empty)
        ##### RETURN WINNER?
        if not unit_group_l:
            # TEST Kill Counter
            test_kill_counter(all_groups)
            print("ENEMY WON WE LOST ")
            break

        if not unit_group_r:
            #TEST Kill Counter
            test_kill_counter(all_groups)
            print("WE WON LOL")
            break

def hit_calc(settings, unit, target, all_groups):

    # if target != None:
    #     graphics.rect = target.rect
    #
    # if unit != None:
    #     graphics.rect2 = unit.rect

    add_graphic(settings, unit.rect.x, unit.rect.y, 1, all_groups["hit_decals"])


    rand = randint(1, 100)
    if rand <= unit.accuracy:
        add_graphic(settings, target.rect.x, target.rect.y, 2, all_groups["hit_decals"])
        if randint(0, 100) <= 50 and target.type == 1:
            wound_unit(target)

        else:
            #kill_unit(target)
            kill_unit_pop(target, all_groups)
            unit.kill_count += 1

#image gib oder pew, (2 = gib)
def add_graphic(settings, x, y, image, group):
    graphic = Hit_Decal(settings)
    graphic.rect.x = x #+ randint(-5, 5)
    graphic.rect.y = y #+ randint(-5, 5)

    if image == 2:
        graphic.image = graphic.image2

    #rect?
    group.add(graphic)

def kill_unit(unit):
    unit.type = 0
    unit.combat_active = 0
    unit.draw_wound()

def kill_unit_pop(unit, all_groups):
    unit.type = 0
    unit.combat_active = 0
    unit.draw_wound()

    unit.kill()
    all_groups["unit_group_dead"].add(unit)

def wound_unit(unit):
    unit.type = 2
    unit.draw_wound()

def test_kill_counter(all_groups):
    """TEST KILLCOUNTER"""
    print("Kill Counter:")
    for unit in all_groups["unit_group_l"]:
        print(unit.name, unit.type, " killed: ", unit.kill_count)

    for unit in all_groups["unit_group_r"]:
        print(unit.name, unit.type, " killed: ", unit.kill_count)

    for unit in all_groups["unit_group_dead"]:
        print(unit.name, unit.type, " killed: ", unit.kill_count)

#UPDATEN!!!
def army_update_order(group):
    """Update shooting order for auto_shoot_group"""
    if group:

        #Ganze Gruppe last_update now, als hätten geschossen
        now = pygame.time.get_ticks()

        #herausfinden ob eh nur einer in der Gruppe bereit zu shooten ist
        behindert = 0
        for unit in group:
            if unit.ready_to_fire == 1:
                behindert = 1

        #Alle außer ready to fire auf last_update now
        for unit in group:
            if unit.ready_to_fire == 0:
                unit.last_update = now

        #Wenn keiner ready ist -> random auf ready stellen
        if behindert != 1:
            unit = choice(group.sprites())
            unit.ready_to_fire = 1







