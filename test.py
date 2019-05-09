
# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d"]

# for x, y in zip(a, b):
#     print(x)
#     print(y)
#
# print("XXXXXXXXXXXXXXXXXXXX")
#
# for i in range(len(a)):
#    print(a[i], b[i])
#
# print("XXXXXXXXXXXXXXXXXXXX")
#

# for i, ele in enumerate(a):
#     print(ele, b[i])


#
# img_center = (img_pos_x + img_size_x/2, img_pos_y + img_size_y/2)
#
# x = (400, 300)
# RED = pygame.Color(255, 0, 0)
# for i in range(8):
#     x = (400 + randint(-10, 10), 300 + randint(-10, 10))
#     pygame.draw.circle(settings.screen, RED, x, randint(10, 20), 0)


self.shoot_delay = 250
self.last_shot = pygame.time.get_ticks()

def update(self):
    self.speedx = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        self.speedx = -8
    if keystate[pygame.K_RIGHT]:
        self.speedx = 8
    if keystate[pygame.K_SPACE]:
        self.shoot()


def shoot(self):
    now = pygame.time.get_ticks()
    if now - self.last_shot > self.shoot_delay:
        self.last_shot = now
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


self.shoot_delay = 250
self.last_update = pygame.time.get_ticks()

self.army_side = "left"

self.

def auto_shoot(self):


    #Get Shoot Delay, 1000ms - 1001ms = 1ms, only shoot at over the delay
    now = pygame.time.get_ticks()
    if now - self.last_update > self.shoot_delay:
        self.last_shot = now

        # Check which side you are on, which side is the enemy
        if self.army_side == "left":
            enemys = all_groups["unit_group_r"]
        else:
            enemys = all_groups["unit_group_l"]

        # Randomly choose Enemy
        target = choice(enemys.sprites())

        gf.hit_calc(self.settings, self, target, all_groups)





    self.last_update = pygame.time.get_ticks()
    self.frame_rate = 50

def update(self):
    now = pygame.time.get_ticks()
    if now - self.last_update > self.frame_rate:
        self.last_update = now
        self.frame += 1
        if self.frame == len(explosion_anim[self.size]):
            self.kill()
        else:
            center = self.rect.center
            self.image = explosion_anim[self.size][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center


"""TILE MAP"""

class TestPlayer(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        #self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        #self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y +dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Tile:
    # a tile of the map and its properties
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # by default, if a tile is blocked, it also blocks sight
        """"""
        if block_sight is None: block_sight = blocked
        """"""
        self.block_sight = block_sight



"""
condition = True
x = 1 if condition else 0
-------

for index, name in enumerate(names, start=1):
 print(index, name)
---------

print(f'{name} is actually {hero}')
---------

setattr()
first = getattr(person, first_key)

person_info = {'first': 'Corey, 'last': 'Schafer'}

for key, value in person_info.items():
 setattr(person, key, value)
 print(getattr(person, key))


#hack in battle?
------------

from getpass import getpass
password = getpass()

---
in konsole
help(smtpd)
---

__str__ is the built-in function in python, used for string representation of object.__repr__ is another built-in which is similar to __str__. ... That method returns a printable string representing that object, i.e. what you'll get when you print that object.

----

"""





