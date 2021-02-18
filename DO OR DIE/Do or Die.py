import sys
import random
import time
import pygame
pygame.init()

def new_word():
    global word_x, word_y, text, choosen_word, press_word,speed
    word_x = random.randint(100,620)
    word_y = 0
    choosen_word = random.choice(words)
    press_word = ''
    speed += 0.5
    text = font.render(choosen_word, True, red)    
#########################color
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
########################parameters
x = 1015
y = 620
speed = 0.5                     
score = 0
words = ['apple', 'mango', 'cherry','horror','ghost','scary','fear','witch','wolf','haunt','creepy','danger','skeleton','demon','monster','crow','blood','spirit','shadow','bat','boggart','dead','curse']
font = pygame.font.SysFont('ComicSansMs', 30)
font3 = pygame.font.SysFont('ComicSansMs', 40)
font1 = pygame.font.SysFont('Georgia', 60)
font2 = pygame.font.SysFont('Arial Font', 65)
text1 = font2.render('Hit Space To Restart The Game...', True, red)
text2 = font1.render('START', True, red)
######################screen
win = pygame.display.set_mode((x,y))
pygame.display.set_caption('DO OR DIE')
#######################images
logo = pygame.image.load('flogo.png')
backgroung1 = pygame.image.load('back.png')
backgroung2 = pygame.image.load('finall.jpg')
ghost = pygame.image.load('final.png')
bhoot = pygame.image.load('final.png')
pygame.display.set_icon(logo)
match = pygame.image.load('explosion1.gif')
################sound
pygame.mixer.music.load('bgsound.mp3')
channel0 = pygame.mixer.Channel(0)
channel0.set_volume(0.2)
channel1 = pygame.mixer.Channel(1)
channel1.set_volume(8)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
blastmusic = pygame.mixer.Sound('blast.wav')    
lostmusic = pygame.mixer.Sound('laugh.wav')
#############################
new_word()
###################infinite loop game
while True:
    if(score >= 20):
        win.blit(backgroung2,(0,0))
    else:
        win.blit(backgroung1,(0,0))
    if(score <= 0):
        win.blit(text2,(400, 240))
        pygame.display.update()
    word_caption = font3.render(choosen_word, True, red)    
    win.blit(ghost,(word_x-75,word_y-95))           
    win.blit(text,(word_x, word_y))                 
    word_y += speed                                 # words speed
    word_caption = font3.render(choosen_word, True, red)
    win.blit(word_caption,(10,50))                      # words diplayed below points
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif(event.type == pygame.KEYDOWN):
            press_word += pygame.key.name(event.key)   
            if choosen_word.startswith(press_word):       
                text = font.render(press_word,True, blue)
                if(choosen_word == press_word):
                    score += len(choosen_word)
                    channel0.play(blastmusic,maxtime = 600)
                    win.blit(match,(word_x,word_y))
                    pygame.display.update()
                    time.sleep(0.2)
                    new_word()
            else:
                text = font.render(press_word, True, red)
                press_word = ''
    point_caption = font3.render(str(score), True, blue)      #score 
    win.blit(point_caption,(10,5))
    if(word_y < y-2):               
        pass
    else:
        channel1.play(lostmusic, maxtime = 6000)
        win.blit(text1,(150, 270))
        pygame.display.update()
        event = pygame.event.wait()
        if(event.type == pygame.QUIT):       ###to cancel the screen
            pygame.quit()
            sys.exit()
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            score = 0
            speed = 1   
            new_word()

    pygame.display.update()