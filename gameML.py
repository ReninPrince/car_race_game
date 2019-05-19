import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 136

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race game')
clock = pygame.time.Clock()


carImg = pygame.image.load('Car1.png')
racetrack = pygame.image.load('resizedcropped_racetrackpicture.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " +str(count), True, red)
    gameDisplay.blit(text, (30,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay,color, [thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,color,posx,posy):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = ((display_width/posx),(display_height/posy))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    
##    game_loop()

def crash():
    message_display('You Crashed',red,2,2)
def score(dodged):  
    message_display('Your score:' + str(dodged),red,2,3)
    game_loop()
    

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.6)
    x_change = 0 
    
    thing_startx = random.randrange(30, display_width-130)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100
    
    dodged = 0
    

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
##            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            side_speed = int(dodged / 10) 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 + (-(side_speed))

                        
                elif event.key == pygame.K_RIGHT:
                    x_change = 5 + (side_speed)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
 
        
        x += x_change 

        gameDisplay.blit(racetrack,(0,0))
##        gameDisplay.fill(racetrack)
        for i in range(2):
            things(thing_startx,thing_starty,thing_width,thing_height, black)
        thing_starty += thing_speed
        
        car(x,y)
        
        #score
        things_dodged(dodged)
        
        #boundry hit
        if x > (display_width - car_width) or x < 0:
            crash()
            score(dodged)

        #object loop
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(30, display_width-130)
            
            #difficulty
            dodged += 1
            thing_speed += 0.3
            
        #collision
        if y+12 < thing_starty+thing_height:
            if x > thing_startx and x+15 < thing_startx + thing_width or x+car_width < thing_startx + thing_width and (x-10) + car_width > thing_startx:
                crash()
                score(dodged)

            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()





















