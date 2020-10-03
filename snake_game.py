import pygame
import math,random
from pygame import mixer
import sys
############################
pygame.init()
#mixer.init()
mixer.pre_init(frequency=4410,size=16,channels=1,buffer=512)
width=300
height=400
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption('Snake Game')

font1=pygame.font.SysFont('arial',35)
font2=pygame.font.SysFont('arial',50)
############  SOUNDS  ############
#provide appropriate path
score_sound=mixer.Sound('D:\Python program\games\FLAPPY_BIRD\sound\sfx_point.wav')
death_sound=mixer.Sound('D:\Python program\games\FLAPPY_BIRD\sound\sfx_hit.wav')

##############  FUNCTIONS  ###############

def myText(text):
    
    screenText=font1.render(text,True,white)
    screen.blit(screenText,(90,5))
    
def gameoverText():
    myText('Score : '+str(score))
    #text1="GAME OVER"
    text2='High Score : '+str(high_score)
    #screenText1=font1.render(text1,True,white)
    #screen.blit(screenText1,(50,20))
    screenText2=font2.render('Press Any Key',True,red)
    screen.blit(screenText2,(20,200))
    screenText2=font1.render(text2,True,white)
    screen.blit(screenText2,(50,320))
    
    
def plotsnake(snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen,green,(x,y,snake_size,snake_size))    

##############  VARIABLES  ###############

#colors
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)

#variables
fps=30
game_over=False
game_exit=False
score=0
high_score=0
#width for score
height_of_score=40

#snake
snake_x=50
snake_y=50
snake_size=10
vel_x=0
vel_y=0

#food
food_size=10
food_x=random.randint(0+food_size,width-food_size)
food_y=random.randint(0+food_size+height_of_score,height-food_size)

#score
score=0
high_score=0

snake_list=[]
snake_len=1

###############  GAME LOOP  ##################
while True:
    #screen.fill(red)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_over:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP or event.key==ord('w'):
                    vel_y=-5
                    vel_x=0
                if event.key==pygame.K_DOWN or event.key==ord('s'):
                    vel_y=5
                    vel_x=0
                if event.key==pygame.K_LEFT or event.key==ord('a'):
                    vel_y=0
                    vel_x=-5
                if event.key==pygame.K_RIGHT or event.key==ord('d'):
                    vel_y=0
                    vel_x=5
        if game_over:
            if event.type==pygame.KEYDOWN:
                game_over=0
                snake_list=[]
                snake_len=1
                plotsnake(snake_list,snake_size)
                pygame.draw.rect(screen,red,(food_x,food_y,food_size,food_size))
                score=0
        
    snake_x=snake_x+vel_x
    snake_y=snake_y+vel_y
    if snake_x<0:
        snake_x=width
    if snake_x>width:
        snake_x=5
    if snake_y<0:
        snake_y=height
    if snake_y>height:
        snake_y=0
    screen.fill(black)
    #pygame.draw.rect(screen,green,(snake_x,snake_y,snake_size,snake_size))
    plotsnake(snake_list,snake_size)
    pygame.draw.rect(screen,red,(food_x,food_y,food_size,food_size))
    myText('Score : '+str(score))
    if abs(snake_x-food_x)<=7 and abs(snake_y-food_y)<=7:
        score+=1
        score_sound.play()
        if score>high_score:
            high_score=score
        food_x=random.randint(0+food_size,width-food_size)
        food_y=random.randint(0+food_size+height_of_score,height-food_size)
        snake_len+=5
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if len(snake_list)>snake_len:
        del snake_list[0]
    if head in snake_list[:-1]:
        death_sound.play()
        game_over=True
        
    if game_over:
        screen.fill(black)
        gameoverText()
    clock.tick(fps)
    pygame.display.update()
    
