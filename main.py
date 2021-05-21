import pygame
import random
import math
#import variables
from variables import *
pygame.init()

upPressed = False
downPressed = False

g= 9.8 #newton's gravatational constant
rvx = 50 #horizontal veloctiy
rvy = 50 #vertical velocity
tx=0 #time
ty=0
rx = xpos
ry = ypos

#fisherman = pygame.image.load('amogus.png')

while PlayingGame:
  
    clocky.tick(60)
  
    while TextTime > 0:
        TextTime - 1
    

    events = pygame.event.get()
 
    for event in events:
        if event.type == pygame.QUIT:
            PlayingGame = False
      
    keys = pygame.key.get_pressed()
      
    if keys[pygame.K_p] and game_state == START:
        game_state = FISHING
    if keys[pygame.K_p] and game_state == MENU:
        game_state = FISHING

    if keys[pygame.K_m]:
        game_state = MENU

    if keys[pygame.K_i]:
        game_state = INVENTORY
  
    if keys[pygame.K_a] and game_state == MENU:
        game_state = AQUARIUM

    if game_state == FISHING:      
        if keys[pygame.K_LEFT]:
            if cast is False and xpos > 0:
                vx=-2
    if keys[pygame.K_RIGHT]:
       if cast is False and xpos  < 80:
          vx=2


    if xpos > 80:
      xpos = 80
    if keys[pygame.K_1]:
        game_state = POND


    if keys[pygame.K_DOWN]:
        #ry+=3
        #vx = 0
        tx+=.1
        ty+=.1
        LinePower += .1
        downPressed = True

    if not keys[pygame.K_DOWN]:
        downPressed = False

    #else: make rx and ry come back towards player
    if keys[pygame.K_UP] and rx > 100:
         # tx-=.1
        rx -=2
        upPressed = True
   
    if keys[pygame.K_UP] and ry > ypos:
        #ty-=.1
        ry -=2
        upPressed = True
    if not keys[pygame.K_UP]:
        upPressed = False
    
    #if xpos > 80:
     # xpos = 80  
    vx*=.95 #friction

    #fishing rod physics
    if ry <= ypos: #make the arc
        rvy = 50
        rx = (rvx * tx) + xpos
        ry = (-rvy*ty + 1*g*ty*ty) + ypos# 
        
    
    if ry > ypos:
        ry += rvy
    
    if ry > ypos and downPressed:
        rvy = 2
    elif ry > ypos and not downPressed:
        rvy = 0
    if upPressed:
        tx = 0
        ty = 0

    
   
    #so what i'm trying to do is reset the time variable whenever you go to high, cause in the example code the time always resets after you let go of space but here it keeps increasing
    #if ry > 75 and upPressed == False: #sinking
    #    ry+=2

    xpos += vx #update player position
    
    #stop player from leaving screen
    if xpos < 0:
        xpos = 0
    if xpos+20>700:
        xpos = 680
       
    #stop player from moving when line is down

    #else:
    #   cast = True
      
    #check if you're over a hole

     
    #f1.move()
    #f2.move()
     #f3.move()

    #catch the fish
    for i in range(len(schoolAndSandwich)):
        if math.sqrt((rx+10-schoolAndSandwich[i].xpos)*(rx+10-schoolAndSandwich[i].xpos)+(ry-schoolAndSandwich[i].ypos)*(ry-schoolAndSandwich[i].ypos))<10 and schoolAndSandwich[i].caught == False:
            schoolAndSandwich[i].onHook = True
          
    for i in range (len(schoolAndSandwich)):
        if schoolAndSandwich[i].type == "minnow":
          schoolAndSandwich[i].MinnowMove(xpos+10+rx, ypos+18+ry)   
        elif schoolAndSandwich[i].type == "jelly": 
          schoolAndSandwich[i].JellyMove(xpos+10+rx, ypos+18+ry) 
        #else:
         # schoolAndSandwich[i].FrogMove(xpos+10+rx,ypos+18+ry)
          #print ("Moving jellyfish")
          
    #render section-------------------------------------------------------------------------------------
    gamescreen.fill((0,0,250))

    if game_state == START:
        gamescreen.fill((0,0,180))
        gamescreen.blit(text1,(100, 100))
  
    elif game_state == FISHING:
    
        pygame.draw.rect(gamescreen, (200,200,255), (0,0,700, 100))#sky
        pygame.draw.rect(gamescreen, (239,221,111), (0,95,100, 500)) #sand
        gamescreen.blit(text5, (0,0))
    #holes in ice
    #pygame.draw.rect(gamescreen, (0,0,0), (100, 95, 30, 5))
    #pygame.draw.rect(gamescreen, (0,0,0), (250, 95, 30, 5))
    #pygame.draw.rect(gamescreen, (0,0,0), (400, 95, 30, 5))
    #pygame.draw.rect(gamescreen, (0,0,0), (550, 95, 30, 5))
    
        while TextTime > 0:
            gamescreen.blit(text2,(xpos, ypos-10))

    #f1.draw()
    #f2.draw()
    #f3.draw()
        for i in range (len(schoolAndSandwich)):
          if schoolAndSandwich[i].type == "minnow":
            schoolAndSandwich[i].MinnowDraw()
          elif schoolAndSandwich[i].type == "jelly":
            schoolAndSandwich[i].JellyDraw()
        
        #draw player
        
        #gamescreen.blit(fisherman, (xpos,ypos), (0,0,32,64))

        pygame.draw.rect(gamescreen, (200,0,0), (xpos, ypos, 20,20))

  #draw fishing bar
    #pygame.draw.rect(gamescreen, (0,255,0), (xpos+10,ypos+30, 10,LinePower))
  
  #draw line


        pygame.draw.rect(gamescreen, (0,0,0), (rx,ry, 2,1))
        pygame.draw.rect(gamescreen, (180,180, 0), (rx, ry, 10, 2))
        pygame.draw.rect(gamescreen, (180,180, 0), (rx+20, ry+12, 2, 5))

    elif game_state == POND:
        
        pygame.draw.rect(gamescreen, (112,84,62), (0,75,700,500))
        pygame.draw.circle(gamescreen, (10,55,200), (400,150), 300) #300 is radius?  400 is x-pos of the center, 150 is how far down the circle's center is
        pygame.draw.rect(gamescreen, (200,200,255), (0,0,700, 95))#sky

        pygame.draw.rect(gamescreen, (200,0,0), (xpos, ypos, 20,20))
        #for i in range(len(schoolAndSandwich)-30):
         # schoolAndSandwich[i].FrogDraw()
          #schoolAndSandwich[i].FrogMove(xpos+10+rx, ypos+18+ry)

        pygame.draw.rect(gamescreen, (0,0,0), (rx,ry, 2,1))
        pygame.draw.rect(gamescreen, (180,180, 0), (rx, ry, 10, 2))
        pygame.draw.rect(gamescreen, (180,180, 0), (rx+20, ry+12, 2, 5))



    elif game_state == MENU:
        gamescreen.fill((0,25,200))
        gamescreen.blit(text3, (100,100))
        gamescreen.blit(text6,(50,150))
        gamescreen.blit(text7, (50, 200))

    elif game_state == INVENTORY:

        gamescreen.fill((150,150,160))
        gamescreen.blit(text4,(200,200))
        #put a loop so it draws the number of fish in a slot of the bag
        for i in bagArray:
            pygame.draw.ellipse(gamescreen, (50, 200, 40), (20, 20, 25, 15))
            pygame.draw.polygon(gamescreen, (50, 200, 40), ((20, 20), (200+30, 200+15), (200+20, 200+5)))
            pygame.draw.circle(gamescreen, (0,0,0), (200+5, 200+5), 3)

    elif game_state == AQUARIUM:
   
        gamescreen.fill((0,10,240))
        gamescreen.blit(text5, (0,0))
        for i in range (bagArray[0]):
            schoolAndSandwich[i].MinnowDraw()
            schoolAndSandwich[i].MinnowMove(xpos+10+rx, ypos+18+ry)   

        for i in range (bagArray[1]):
            #schoolAndSandwich[i].JellyDraw()
            schoolAndSandwich[i+20].JellyDraw()
            schoolAndSandwich[i+20].JellyMove(xpos+10+rx, ypos+18+ry)   
       # for i in range(bagArray[2]):
        #    schoolAndSandwich[i+30].FrogDraw()
         #   schoolAndSandwich[i+30].FrogMove(xpos+10+rx,ypos+18+ry)
  
    pygame.display.flip()


pygame.quit()
