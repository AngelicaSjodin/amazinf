import pygame
import random
pygame.init()

#titeln
pygame.display.set_caption("mega bra spel")
#icon=pygame.image.load('icons8-cool-30.png')
#pygame.display.set_icon(icon)


width=1000
height=800
black = [0, 0, 0]
white = [255, 255, 255]
#skärm
screen=pygame.display.set_mode((width,height)) 
#bak bild
background=pygame.image.load('7411725.png')


#player
playerImg=pygame.image.load('icons8-cat-64.png')
playerX=400
playerY=400
playerX_change=0

 
def player(x,y):
    screen.blit(playerImg,(x,y))

#fiendennnn
enemyImg=pygame.image.load('icons8-cucumber-64.png')
enemyX=random.randint(0,800)
enemyY=random.randint(0,0)
enemyX_change=2
enemyY_change=40

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#bullet
#ready= syns inte än
#fire= den syns och rör sig
bulletImg=pygame.image.load('icons8-farming-48.png')
bulletX=0
bulletY= 400#samma playerY
bulletX_change=0
bulletY_change=6
bullet_state="ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletImg,(x+16,y+10))

#da loop
running=True
while running:

    #bak skärm
    screen.blit(background,(-90,0))

#stänga av knappen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#key bindingsss
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerX_change=-4.5
            if event.key ==pygame.K_RIGHT:
                playerX_change=4.5
            if event.key ==pygame.K_UP:
                playerY_change=-4.5
            if event.key ==pygame.K_DOWN:
                playerY_change=4.5
            if event.key ==pygame.K_SPACE:
                fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change=0

        #if player.colliderect(enemy):
            #running = False
    
# border screeeeen för player
    if playerX <=0:
        playerX=0
    elif playerX >=936:
        playerX=936
    if playerY <=0:
        playerY=0
    elif playerY >=736:
        playerY=736
#border för enemy
    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >936:
        enemyX_change=-2
        enemyY += enemyY_change

    #bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletX_change

    playerY += playerY_change
    playerX += playerX_change
    player(playerX,playerY)

    enemy(enemyX,enemyY)
    pygame.display.update()

pygame.quit()