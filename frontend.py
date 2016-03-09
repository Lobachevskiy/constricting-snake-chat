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
client_input = textinput.Input(screen)
server_input = textinput.Input(screen)
def print_message(message):
    server_input.message = message
    print("received Message")
chat_client.on_received = print_message
chat_client.connect()
client_input.y = 200

def message_server():
    chat_client.send_message(client_input.message)


done = False
clock = pygame.time.Clock()
client_input.on_return = message_server
while not done:
    chat_client.receive()
    screen.fill(WHITE)
    events = pygame.event.get()
    shift = False
    for event in events:
        if (event.type == pygame.QUIT):
            done = True
    client_input.update(events)
    client_input.draw()
    server_input.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
