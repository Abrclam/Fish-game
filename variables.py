import pygame
import random
import math


#game states
START = 0
FISHING = 1
AQUARIUM = 2
SETTINGS = 3
MENU = 4
INVENTORY = 5
POND = 6






TextTime = 0
LinePower = 0
game_state = START

pygame.init()
font = pygame.font.SysFont("comicsansms", 16)

text1 = font.render("start screen. press p to play.", True, (0, 228, 0))

text2 = font.render("Fish caught!", True, (255, 0, 0))

text3 = font.render("Main Menu", True, (255,255,255))

text4 = font.render("Inventory placeholder", True, (0,0,0))

text5 = font.render("Press M to open the menu.", True, (0,0,0))

text6 = font.render("Press A to check your aquarium, P to go back to fishing, and S to open the settings menu.", True, (0,0,0))

text7 = font.render("Press 1 to enter the pond. This is a temporary way to get there and will be changed.", True, (0,0,0))

gamescreen = pygame.display.set_mode((700,500))

pygame.display.set_caption("Fishing Frenzy")

clocky = pygame.time.Clock()





PlayingGame = True

bagArray = [0,0,0,0,0,0,0,0,0]
bagCount = 9
#slot 0 is minnow, 1 is jellyfish, etc

class fish:
    def __init__(self, FishType):
        self.xpos = random.randrange(0, 700)
        self.ypos = random.randrange(100, 450)
        self.Vx = random.randrange(-3, 3)
        self.Vy = random.randrange(-3, 3)
        self.ticker = random.randrange(0,100)
        self.red = random.randrange(0,100)
        self.green = random.randrange(100,250)
        self.blue = random.randrange(50, 200)
        self.onHook = False
        self.caught = False
        self.fishPic = pygame.image.load('fish.png')
        self.type = FishType

   
        #follow end of wire if on hook         

    
       
    def MinnowMove(self,x,y):
        #fish in water algorithm
        if self.caught == False:
            self.ticker+=1

            if self.xpos>680:
                self.xpos = 680
                self.Vx*=-1

            if self.xpos<100:
                self.xpos = 100
                self.Vx*=-1

            if self.ypos<100:
                self.ypos = 100
                self.Vy*=-1

            if self.ypos>500:
                self.ypos = 500
                self.Vy*=-1

            if self.ticker > 200:
                self.Vx = random.randrange(-2, 3)
                self.Vy = random.randrange(-2, 3)
                self.ticker = 0

            self.xpos+=self.Vx
            self.ypos+=self.Vy

        if self.onHook == True:
            self.xpos = x-60
            self.ypos = y-100
            #print(self.ypos)

            if self.ypos <= 100 and self.onHook == True:#if fish gets to top
                self.caught = True
                self.onHook = False

        if self.caught == True and self.xpos !=-50:
            print("FISH GOT")
            TextTime = 100

            self.ypos = -50
            self.xpos = -50
            bagArray[0] +=1     
                
    def MinnowDraw(self):
        counter = 0
        #pygame.draw.ellipse(gamescreen, (self.red, self.green, self.blue), (self.xpos, self.ypos, 25, 15))
        if self.Vx > 0:
            
            counter += 1
            if counter >3:
              counter = 0

            gamescreen.blit(self.fishPic, (self.xpos,self.ypos), (0+counter*32,0,32,32))
            #pygame.draw.polygon(gamescreen, (self.red, self.green, self.blue), ((self.xpos+30, self.ypos-5), (self.xpos+30, self.ypos+15), (self.xpos+20, self.ypos+5)))
            #pygame.draw.circle(gamescreen, (0,0,0), (self.xpos+5, self.ypos+5), 3)
        else:

            counter += 1
            if counter >3:
              counter = 0

            gamescreen.blit(self.fishPic, (self.xpos,self.ypos), (0+counter*32,32,32,64))
            #pygame.draw.polygon(gamescreen, (self.red, self.green, self.blue), ((self.xpos-5, self.ypos-5), (self.xpos-5, self.ypos+15), (self.xpos+5, self.ypos+5)))
            #pygame.draw.circle(gamescreen, (0,0,0), (self.xpos+20, self.ypos+5), 3)
    


    def JellyMove(self,x,y):
         #fish in water algorithm
        if self.caught == False:
            self.ticker+=1
            if self.xpos>680:
                self.xpos = 680
                self.Vx*=-1
            if self.xpos<100:
                self.xpos = 100
                self.Vx*=-1
            if self.ypos<100:
                self.ypos = 100
                self.Vy*=-1
            if self.ypos>500:
                self.ypos = 500
                self.Vy*=-1
            if self.ticker > 200:
                self.Vx = random.randrange(-2, 2)
                self.Vy = random.randrange(-2, 4)
                self.ticker = 0
            self.xpos+=self.Vx
            self.ypos+=self.Vy
        if self.onHook == True:
            self.xpos = x-60
            self.ypos = y-100
            #print(self.ypos)
            if self.ypos <= 100 and self.onHook == True:#if fish gets to top
                self.caught = True
                self.onHook = False
        if self.caught == True and self.xpos !=-50:
            print("JELLY GOT")
            TextTime = 100
            self.ypos = -50
            self.xpos = -50
            bagArray[1] +=1    

    def JellyDraw(self):
        pygame.draw.ellipse(gamescreen, (self.red+100, self.green-50, self.blue+50), (self.xpos, self.ypos, 25, 25))

        pygame.draw.rect(gamescreen, (self.red+100,self.green-50,self.blue+50),(self.xpos,self.ypos+17,3,10))

        pygame.draw.rect(gamescreen, (self.red+100,self.green-50,self.blue+50),(self.xpos+5,self.ypos+20,3,10))

        pygame.draw.rect(gamescreen, (self.red+100,self.green-50,self.blue+50),(self.xpos+10,self.ypos+23,3,10))
        
        pygame.draw.rect(gamescreen, (self.red+100,self.green-50,self.blue+50),(self.xpos+15,self.ypos+23,3,10))

        pygame.draw.rect(gamescreen, (self.red+100,self.green-50,self.blue+50),(self.xpos+20,self.ypos+20,3,10))
   
    #def FrogMove(self,x,y):
     #   if self.caught == False:
      #        self.ticker+=1
       #       self.Vx -=.1
        #      self.Vy -=.1
        
        #if math.sqrt((400-self.xpos)*(400-self.xpos) +(150-self.ypos)*(150-self.ypos)) > 400:

         #     self.Vx *=-1
          #    self.Vy *=-1
       # if self.ypos < 95:

        #      self.Vy *=-1

        #if self.ticker > 5000:

         #   self.Vx = random.randrange(-10, 10)
          #  self.Vy = random.randrange(-10, 10)
           # self.ticker = 0

        #self.xpos+=self.Vx
        #self.ypos+=self.Vy

        #if self.onHook == True:
         #   self.xpos = x-60
          #  self.ypos = y-100
            #print(self.ypos)

           # if self.ypos <= 100 and self.onHook == True:#if fish gets to top
            #    self.caught = True
             #   self.onHook = False

        #if self.caught == True and self.xpos !=-50:

         #   print("FROG GOT")

          #  TextTime = 100

           # self.ypos = -50
           # self.xpos = -50
           # bagArray[2] +=1     
   
    #def FrogDraw(self):

       # pygame.draw.rect(gamescreen, (self.red*0, self.green, self.blue-50), (self.xpos+20, self.ypos+20, 10,10))    

#f1 = fish()
#f2 = fish()
#f3 = fish()
schoolAndSandwich = list()

for i in range(20):
    schoolAndSandwich.append(fish("minnow"))

for i in range(10):
    schoolAndSandwich.append(fish("jelly"))

#for i in range(5):
 #   schoolAndSandwich.append(fish("frog"))

xpos = 50
ypos = 75
vx=0
rx=0
ry = 0
cast = False


