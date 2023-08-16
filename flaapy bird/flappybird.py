import pygame
import random
import sys
from pygame.locals import*
fps=40
width=400
height=700
screen=pygame.display.set_mode((width,height))
ground=height*0.5
pipe= 'C:\\Users\\user\\Desktop\\flaapy bird\\pipe.png'
background="C:\\Users\\user\\Desktop\\flaapy bird\\bg.jpg"
bird="C:\\Users\\user\\Desktop\\flaapy bird\\bird.png"
start="C:\\Users\\user\\Desktop\\flaapy bird\\start.jpeg"
game_sprits={}

def show_window():
    try:
        playerx=int(width/5)
        playery=int((height-game_sprits['bird'].get_height())/2)
        messagex=int((width-game_sprits['start'].get_width())/2)
        messagey=int(height*1.1)
        basex=0
    except Exception as e:
        print(e)    
    playbutton=pygame.Rect(108,222,68,65)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT: 
                if(event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            elif event.type==KEYDOWN :
                if(event.key==K_SPACE and event.key==K_UP):
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
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\0.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\1.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\no2.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\no3.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\no4.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\no5.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\6.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\7.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\8.png").convert_alpha(),
        pygame.image.load("C:\\Users\\user\Desktop\\flaapy bird\\9.png").convert_alpha()
    }
    game_sprits['background']={pygame.image.load(background).convert_alpha()}
    game_sprits['bird']={pygame.image.load(bird).convert_alpha()}
    game_sprits['pipe']={pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180),
                         pygame.image.load(pipe).convert_alpha()}
    game_sprits['base']={pygame.image.load("C:\\Users\\user\\Desktop\\flaapy bird\\base.png").convert_alpha()}
    game_sprits['start']={pygame.image.load("C:\\Users\\user\\Desktop\\flaapy bird\\start.jpeg").convert_alpha()}
    while True:
        show_window()


