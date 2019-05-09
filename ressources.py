import pygame
from settings import Settings


# Transparent COLORKEY
transparent = pygame.Color(255, 0, 255)


"""GRAPHICS"""

"""Units"""
#Terran
terran_png = pygame.image.load('images/terran.png')
terran_png.set_colorkey(transparent)

terran_w_png = pygame.image.load('images/terran_w.png')
terran_w_png.set_colorkey(transparent)

terran_d_png = pygame.image.load('images/terran_d.png')
terran_d_png.set_colorkey(transparent)

#Psion
psion_png = pygame.image.load('images/psion.png')
psion_png.set_colorkey(transparent)

psion_w_png = pygame.image.load('images/psion_w2.png')
psion_w_png.set_colorkey(transparent)

psion_d_png = pygame.image.load('images/psion_d.png')
psion_d_png.set_colorkey(transparent)

#Robo
robo_png = pygame.image.load('images/robo.png')
robo_png. set_colorkey(transparent)

robo_w_png = pygame.image.load('images/robo.png')
robo_w_png. set_colorkey(transparent)

#Roti
roti_png = pygame.image.load('images/roti.png')
roti_png. set_colorkey(transparent)

roti_w_png = pygame.image.load('images/roti.png')
roti_w_png. set_colorkey(transparent)


"""Graphics"""
gib_png = pygame.image.load('images/gib.png')
gib_png.set_colorkey(transparent)

pew_png = pygame.image.load('images/pew.png')
pew_png.set_colorkey(transparent)



#background_battle_png = pygame.image.load('images/background2.png')