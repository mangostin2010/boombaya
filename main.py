import pygame
import datetime
import playsound
from play_sounds import play_file
import os
os.putenv('SDL_FBDEV', '/dev/fb1')
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    
pygame.init()

size = [500, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("By Justin")
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()

session = '김주원' # 기본 세션은 김주원


while done==False:

    for event in pygame.event.get(): # User did something
        now = datetime.datetime.now()
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION


        if event.type == pygame.JOYBUTTONDOWN:
            pressedbutton = str(event.button)
            if pressedbutton == '8': session = '김주원'
            if pressedbutton == '9': session = '붐바야'
            if pressedbutton == '0':
                if session == '김주원': play_file('oni.mp3', block=False)  #playsound.playsound('oni.mp3', False)
                if session == '붐바야': play_file('oni-b.mp3', block=False) #playsound.playsound('oni-b.mp3', False)
            if pressedbutton == '1':
                if session == '김주원': play_file('ona.mp3', block=False) #playsound.playsound('ona.mp3', False)
                if session == '붐바야': play_file('troll-b.mp3', block=False) #playsound.playsound('troll-b.mp3', False)
            if pressedbutton == '2':
                if session == '김주원': play_file('boombaya.mp3', block=False) #playsound.playsound('boombaya.mp3', False)
                if session == '붐바야': play_file('zoowon.mp3', block=False) #playsound.playsound('zoowon.mp3', False)
            if pressedbutton == '3':
                if session == '김주원': play_file('ipum.mp3', block=False) #playsound.playsound('ipum.mp3', False)
                if session == '붐바야': play_file('Zonzal.mp3', block=False) #playsound.playsound('Zonzal.mp3', False)
            if pressedbutton == '5': play_file('legend.mp3', block=False) #playsound.playsound('legend.mp3', False)
            if pressedbutton == '4': play_file('wa.mp3', block=False) #playsound.playsound('wa.mp3', False)
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    textPrint.indent()


    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
            
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        textPrint.unindent()
        
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    #clock.tick(20)

pygame.quit ()
