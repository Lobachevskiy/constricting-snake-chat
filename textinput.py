import pygame

BLUE = (54,110,159)
WHITE = (255, 255, 255)
GOLD   = (254, 205, 40)
def empty():
    return

class Input:
    def __init__(self, screen):
        self.message = ""
        self.shift = False
        self.x = 0
        self.y = 0
        self.screen = screen
        self.lastKeys = pygame.key.get_pressed()
        self.maxlength = 25
        self.backspace_delay = 0
        self.on_return = empty
    
    def update(self,events):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
            self.shift = True
        else:
            self.shift = False
        if(keys[pygame.K_BACKSPACE]):
            if(self.backspace_delay == 0):
                self.message = self.message[:-1]
                self.backspace_delay = 1
            else:
                self.backspace_delay -= 1
        if(keys[pygame.K_SPACE]  and not self.lastKeys[pygame.K_SPACE] and len(self.message) < self.maxlength):
            self.message += " "
        for i in range(pygame.K_EXCLAIM, pygame.K_DELETE):
            if(keys[i] and not self.lastKeys[i] and len(self.message) < self.maxlength):
                keyname = pygame.key.name(i)
                if(self.shift):
                    keyname = keyname.upper();
                self.message += keyname;
        if(keys[pygame.K_RETURN] and self.message != ""):
            self.on_return()
            self.message = ""
        self.lastKeys = keys
    def draw(self):
        font = pygame.font.Font(None, 40)
        size = font.size(self.message)
        ren = font.render(self.message,0,BLUE,GOLD)
        self.screen.blit(ren,(self.x, self.y) )