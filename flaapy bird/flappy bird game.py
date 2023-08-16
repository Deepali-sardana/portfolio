import pygame
import random
import sys
from pygame.locals import*
fps=32
width=400
height=700
screen=pygame.display.set_mode((width,height))
ground=height*0.5
pipe= 'flaapy bird/pipe.png'
background="flaapy bird/bg.jpg"
bird="flaapy bird/bird.png"
start="flaapy bird/start.jpeg"
game_sprits={}

def show_window():
    playerx=int(width/5)
    playery=int((height-game_sprits['bird'])/2)
    messagex=int((width-game_sprits['start'])/2)
    messagey=int(height*1.1)
    basex=0
    playbutton=pygame.Rect(108,222,68,65)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or(event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN or(event.key==K_SPACE and event.key==K_UP):
                return
            else:
                screen.blit(game_sprits['background'],(0,0))
                screen.blit(game_sprits['bird'],(playerx,playery))
                screen.blit(game_sprits['start'],(messagex,messagey))
                screen.blit(game_sprits['base'],(basex,ground))
                pygame.display.update()
                fpsclock.tick(fps)
if  __name__=="__main__":
    pygame.init()
    fpsclock=pygame.time.Clock()
    pygame.display.set_caption("flappy bird game")
    game_sprits['numbers']={
        """pygame.image.load('flaapy bird/0.png').convert_alpha(),
        pygame.image.load('flaapy bird/1.pn').convert_alpha(),
        pygame.image.load('flaapy bird/no2.png').convert_alpha(),
        pygame.image.load('flaapy bird/no3.png').convert_alpha(),
        pygame.image.load('flaapy bird/no4.png').convert_alpha(),
        pygame.image.load('flaapy bird/no5.png').convert_alpha(),
        pygame.image.load('flaapy bird/6.png').convert_alpha(),
        pygame.image.load('flaapy bird/7.png').convert_alpha(),
        pygame.image.load('flaapy bird/8.png').convert_alpha(),
        pygame.image.load('flaapy bird/9.png').convert_alpha()"""
    }
    game_sprits['background']={pygame.image.load(background).convert_alpha()}
    game_sprits['bird']={pygame.image.load(bird).convert_alpha()}
    game_sprits['pipe']={pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180),
                         pygame.image.load(pipe).convert_alpha()}
    game_sprits['base']={pygame.image.load('flaapy bird/base.png').convert_alpha()}
    game_sprits['start']={pygame.image.load('flaapy bird/start.jpeg').convert_alpha()}
    while True:
        show_window()
