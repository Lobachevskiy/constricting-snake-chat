import pygame
import random
import os
import textinput
import client
from pygame.locals import *
#Defining some colors
BLUE = (54,110,159)
WHITE = (255, 255, 255)
GOLD   = (254, 205, 40)

pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

chat_client = client.ChatClient()
chat_client.connect()
text_input = textinput.Input(screen)

def message_server():
    chat_client.send_message(text_input.message)

def print_message():
    print("Printing messages is not yet implemented") #TODO

done = False
clock = pygame.time.Clock()
text_input.on_return = message_server
chat_client.on_received = print_message
while not done:
    chat_client.receive()
    screen.fill(WHITE)
    events = pygame.event.get()
    shift = False
    for event in events:
        if (event.type == pygame.QUIT):
            done = True
    text_input.update(events)
    text_input.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
