import pygame
import random
import os
import textinput
from pygame.locals import *
#Defining some colors
BLUE = (54,110,159)
WHITE = (255, 255, 255)
GOLD   = (254, 205, 40)

def quit():
	pygame.quit()
pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


done = False
clock = pygame.time.Clock()
input = textinput.Input(screen)
input.on_return = quit
while not done:
	screen.fill(WHITE)
	events = pygame.event.get()
	shift = False
	for event in events:
		if (event.type == pygame.QUIT):
			done = True
	input.update(events)
	input.draw()
	pygame.display.flip()
	clock.tick(30)
pygame.quit()