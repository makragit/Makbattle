def battle(settings, all_groups):

    unit_group_l = all_groups["unit_group_l"]
    unit_group_r = all_groups["unit_group_r"]

    #round counter
    i=0

    #for x, y in zip_longest(army1, army2):
    for unit_l, unit_r in zip(unit_group_l, unit_group_r):


        """!!! WANN SIND ALLE TOT?"""
        """Wenn tot überspringt Runde"""


        #Random Werte verteilen/initialisieren
        random_unit_l = choice(unit_group_l.sprites())
        random_unit_r = choice(unit_group_r.sprites())

        #While chekct ob angreifer eh lebt, lol = aufhören wenn alle tot
        lol=0
        while random_unit_l.type == 0 and lol < len(unit_group_l):
            random_unit_l = choice(unit_group_l.sprites())

            lol+=1

        lol=0
        while random_unit_r.type  == 0 and lol < len(unit_group_r):
            random_unit_r = choice(unit_group_r.sprites())

            lol+=1


        # Unit on the_Left shoots Random Unit on the Right
        if unit_l.type != 0 and random_unit_r.type != 0:

            #random_unit_r.type = 2

            #hit_calc(ai_settings, screen, x, random_army2, graphics)
            hit_calc(settings, unit_l, random_unit_r, all_groups)

            """Test Runde"""
            print("Round Counter", unit_l.name, i)
            i+=1
            """"""
            #sleep(0.05)
            update_screen(settings, all_groups)
            """"""

        # Unit on the Right shoots Random Unit on the Left
        if unit_r.type != 0 and random_unit_l.type != 0:


            #random_unit_l.type = 2

            #hit_calc (ai_settings, screen, y, random_army1, graphics)
            hit_calc(settings, unit_r, random_unit_l, all_groups)

            """Test Runde"""
            print("Round Counter:", unit_r.name , i)
            i+=1
            """"""
            #sleep(0.05)
            update_screen(settings, all_groups)
            """"""



"""AUTO SHOOT ORDER VOR ÄNDERUNG""""
"""AUTO SHOOT ORDER VOR ÄNDERUNG""""
"""AUTO SHOOT ORDER VOR ÄNDERUNG""""
"""AUTO SHOOT ORDER VOR ÄNDERUNG""""


def auto_shoot_order(self, all_groups):
    """Let a group of units shoot depending on their shooting_order (and delay)"""
    """PROBLEM: Where to initialize shooting order? Create Army?"""
    """PROBLEM:Wenn Shooting_order 1 stirbt wird runde ausgesetzt, neu berechnen?"""
    # Get Shoot Delay, 1000ms - 1001ms = 1ms, only shoot at over the delay
    now = pygame.time.get_ticks()
    if now - self.last_update > self.shoot_delay:
        self.last_update = now

        if self.shooting_order == 1 and self.combat_active == 1:

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
            print("Terran: ", self.id, self.army_side, "BAM BAM")

        # Count through Shooting order after every shooting cycle (for all units)
        """PROBLEM: unit_group_l hard coded"""
        self.shooting_order -= 1
        if self.shooting_order == 0:
            self.shooting_order = len(self.all_groups["unit_group_l"])


def auto_shoot_order(self, all_groups):
    """Let a group of units shoot depending on their shooting_order (and delay)"""
    """PROBLEM: Where to initialize shooting order? Create Army?"""
    # Get Shoot Delay, 1000ms - 1001ms = 1ms, only shoot at over the delay
    now = pygame.time.get_ticks()
    if now - self.last_update > self.shoot_delay:
        self.last_update = now


        if self.shooting_order == 1 and self.combat_active == 1:

            # Check which side you are on, which side is the enemy
            if self.army_side == "left":
                enemys = all_groups["unit_group_r"]
            elif self.army_side == "right":
                enemys = all_groups["unit_group_l"]

            # Check if Group not Empty, Randomly choose Enemy, shoot
            # if enemys != None:
            if enemys:
                target = choice(enemys.sprites())
                gf.hit_calc(self.settings, self, target, all_groups)

            """TEST"""
            print("Psion: ", self.id, self.army_side, "BAM BAM")

        #Count through Shooting order after every shooting cycle (for all units)
        """PROBLEM: unit_group_r hard coded"""
        self.shooting_order -= 1
        if self.shooting_order == 0:
            self.shooting_order = len(self.all_groups["unit_group_r"])



            aasdfasdf