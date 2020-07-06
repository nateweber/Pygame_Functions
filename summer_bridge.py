from pygame_functions import *
import sys     # let  python use your file system
import os      # help python identify your OS
import pygame
import math, random


'''
SETUP
'''

counter = 0
shoot = 0


screenSize(960,720)
setAutoUpdate(False)
atFountain = 0
inMainRoom = 0
'''
BACKGROUND IMAGE
'''

#setBackgroundImage("images/stage2.png")

setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,
                       ["images/forest.jpg", "images/forest.jpg"]  ])


'''
SPRITES
'''
#DOOR
door = makeSprite("images/door.png")
showSprite(door)
#door.rect.x = 600
#door.rect.y = 0
doorx = 600
doory = 0
moveSprite(door,doorx,doory,False)



'''
#PORTAL
portal = makeSprite("images/portal.png")
showSprite(portal)
#door.rect.x = 600
#door.rect.y = 0
portalx = 600
portaly = 400
moveSprite(portal,portalx,portaly,False)
'''
#COIN
coin = makeSprite("images/fountain.png")
showSprite(coin)
coinx = 150
coiny = 500
moveSprite(coin,coinx,coiny,False)

#FOUNTAIN
fountain = makeSprite("images/fountain.png")
showSprite(fountain)
fountainx = 900
fountainy = 150
moveSprite(fountain,fountainx,fountainy,False)
'''
#NATHAN
nathan = makeSprite("images/nathan.png")
nathanx = 100
nathany = 100
moveSprite(nathan,nathanx,nathany,False)

#EXIT
exit = makeSprite("images/nathan.png")
#moveSprite(exit,240,10,False)
#showSprite(exit)
exitx = 300
exity = 0
'''

#HERO
hero  = makeSprite("images/links.gif",32)  # links.gif contains 32 separate frames of animation. Sizes are automatically calculated.
herox = 300
heroy = 300
moveSprite(hero,herox,heroy,False)

showSprite(hero)

#AMMO
#ammo = makeSprite("images/ball.png")
#ammox = herox
#ammoy = heroy
ammo = makeSprite("images/ball.png")
ammoX = herox
ammoY = heroy
ammoX_change = 0
ammoY_change = 10
ammo_state = "ready"

def fire_ammo(x, y):
    global ammo_state
    ammo_state = "fire"
    showSprite(ammo)
    moveSprite(ammo, x+16, y+10)


#Enemy
enemy = makeSprite("images/enemy.png")
showSprite(enemy)
enemyx = 500
enemyy = 200
moveSprite(enemy,enemyx,enemyy,False)
#enemy.xspeed = 1
#enemy.yspeed = 1

#TEST TEXT


ftnColour = "white"
ftnLabel = makeLabel("Welcome to the fountain. Want to know more? Press y. Leave, press x.", 24, 100, 200, ftnColour, background="pink")

ftnColour = "white"
ftnLabel2 = makeLabel("Cool. Not much happening here. Just testing. Leave, press x.", 24, 100, 200, ftnColour, background="pink")


scoreColour = "yellow"
scoreLabel = makeLabel("Score: 0", 28, 100, 100, scoreColour, background="black")
showLabel(scoreLabel)
score = 0

dthColour = "black"
dthLabel = makeLabel("EATEN BY DRAGON!!!!", 70, 100, 200, dthColour, background="green")


'''
OTHER SETUP
'''

nextFrame = clock()
frame=0

'''
GAME LOOP
'''

while True:
    if clock() > nextFrame:                         # We only animate our character every 80ms.
        frame = (frame+1)%8                         # There are 8 frames of animation in each direction
        nextFrame += 80                             # so the modulus 8 allows it to loop

    ammox = herox
    ammoy = heroy
#ENEMY MOVEMENT
    
    distance = 500
    speed = 1


    if counter >= 0 and counter <= distance:
      enemyx -= speed
      #enemyy += speed
      
      
    elif counter >= distance and counter <= distance*2:
      enemyx += speed
      #enemyy -= speed


    else:
      counter = 0

    counter+=1
    
    

    moveSprite(enemy,enemyx,enemyy,False)

    if keyPressed("right"):
        changeSpriteImage(hero, 0*8+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left
        doorx -= 5
        #exitx -=5
        fountainx -=5
        coinx -= 5
        enemyx -= 5

        moveSprite(door,doorx,doory,False)
        #moveSprite(exit,exitx,exity,False)
        moveSprite(fountain,fountainx,fountainy,False)
        moveSprite(coin,coinx,coiny,False)
        moveSprite(enemy,enemyx,enemyy,False)

        print(door.rect.x)
        print(door.rect.y)



    elif keyPressed("down"):
        changeSpriteImage(hero, 1*8+frame)    # down facing animations are the 1st set
        scrollBackground(0, -5)
        doory -= 5
       # exity -=5
        fountainy -=5
        coiny -=5
        enemyy -=5

        moveSprite(door,doorx,doory,False)
        #moveSprite(exit,exitx,exity,False)
        moveSprite(fountain,fountainx,fountainy,False)
        moveSprite(coin,coinx,coiny,False)
        moveSprite(enemy,enemyx,enemyy,False)

        print(door.rect.x)
        print(door.rect.y)

    elif keyPressed("left"):
        changeSpriteImage(hero, 2*8+frame)    # and so on
        scrollBackground(5,0)
        doorx += 5
        #exitx += 5
        fountainx +=5
        coinx += 5
        enemyx += 5

        moveSprite(door,doorx,doory,False)
        #moveSprite(exit,exitx,exity,False)
        moveSprite(fountain,fountainx,fountainy,False)
        moveSprite(coin,coinx,coiny,False)
        moveSprite(enemy,enemyx,enemyy,False)

        print(door.rect.x)
        print(door.rect.y)

    elif keyPressed("up"):
        changeSpriteImage(hero,3*8+frame)
        scrollBackground(0,5)
        doory += 5
        #exity += 5
        fountainy +=5
        coiny += 5
        enemyy += 5

        moveSprite(door,doorx,doory,False)
        #moveSprite(exit,doorx,doory,False)
        moveSprite(fountain,fountainx,fountainy,False)
        moveSprite(coin,coinx,coiny,False)
        moveSprite(enemy,enemyx,enemyy,False)

        print(door.rect.x)
        print(door.rect.y)

    else:
        changeSpriteImage(hero, 1 * 8 + 5)  # the static facing front look

    updateDisplay()
    tick(120)
#SHOOT

    if keyPressed("space"):
      if ammo_state is "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = herox
        ammoY = heroy
        fire_ammo(ammoX, ammoY)

    # Bullet Movement
    if ammoY <= 0:
      ammoY = 480
      ammo_state = "ready"

    if ammo_state is "fire":
      fire_ammo(ammoX, ammoY)
      ammoY -= ammoY_change

    '''
    distance = 500
    speed = 1


    if keyPressed("a") and shoot >= 0 and shoot <= distance:
      ammox -= speed
      moveSprite(ammo, ammox, ammoy)
      showSprite(ammo)
      
      
    elif keyPressed("d") and shoot >= distance and shoot <= distance*2:
      ammox += speed
      moveSprite(ammo, ammox, ammoy)
      showSprite(ammo)

    else:
      shoot = 0

    shoot+=1
    '''


#COIN PICKUP
    if touching(hero,coin):
      print("coin!")
      score += 50
      changeLabel(scoreLabel,"Score: " + str(int(score)), scoreColour)  # Update the label
      #hideSprite(coin)
      coinpick = 1


    '''

#FOUNTAIN TOUCHING
    if touching(hero, fountain):
      print("Fountain!")
      score += 50
      changeLabel(scoreLabel,"Score: " + str(int(score)), scoreColour)  # Update the label
      atFountain = 1
      killSprite(fountain)

    if atFountain == 1:
      setBackgroundImage("images/garden.jpg")
      showLabel(ftnLabel)
      if keyPressed("y"):
        hideLabel(ftnLabel)
        showLabel(ftnLabel2)
      elif keyPressed("x"):
        setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,["images/forest.jpg", "images/forest.jpg"]  ])
        hideLabel(ftnLabel)
        atFountain = 0
    '''
#EATEN BY DRAGON

    if touching(hero, enemy):
      hideAll()
      hideSprite(fountain)
      setBackgroundImage("images/death.jpg")
      showLabel(dthLabel)

      if keyPressed("x"):
        setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,["images/forest.jpg", "images/forest.jpg"]  ])
        unhideAll()
        hideLabel(dthLabel)
        enemyx = 600
        enemyy = 200
        doorx = 600
        doory = 0
        moveSprite(door,doorx,doory,False)
        moveSprite(hero,300,300,False)
        moveSprite(enemy,enemyx,enemyy,False)
        #print(hero.rect.x)
        #print(hero.rect.y)


#ENTER MAIN ROOM
    if touching(hero, door):
      inMainRoom = 1
      #hideSprite(door)
      hideAll()
      #moveSprite(hero,2000,2000,False)
      print(door.rect.x)
      print(door.rect.y)
      hideSprite(door)
      setBackgroundImage("images/mainroom.jpg")
      if keyPressed("x"):
        unhideAll()
        setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,["images/forest.jpg", "images/forest.jpg"]  ])
        #showSprite(door)
        doorx = 600
        doory = 0
        moveSprite(hero,600,200,False)
        moveSprite(door,600,0,False)
        #print(hero.rect.x)
        #print(hero.rect.y)

        


'''
      #hideSprite(fountain)
      #hideSprite(hero)
      if inMainRoom == 1:
        score += 50
        print("Door!")
        changeLabel(scoreLabel,"Score: " + str(int(score)), scoreColour)  # Update the label

    if inMainRoom >= 1:
      setBackgroundImage("images/mainroom.jpg")
      showLabel(ftnLabel)
      #showSprite(nathan)

      if keyPressed("y"):
        #changeLabel(ftnLabel, "ftnLabel2")
        hideLabel(ftnLabel)
        showLabel(ftnLabel2)
      elif keyPressed("x"):
        inMainRoom = 0
        setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,["images/forest.jpg", "images/forest.jpg"]  ])
        hideLabel(ftnLabel)
        showSprite(hero)
        showSprite(door)
        moveSprite(hero,200,200,False)
        moveSprite(door,100,400,False)
'''        




'''
    if touching(hero, door):
      print("touching")
      setBackgroundImage("images/stage.png")
      showSprite(exit)
      moveSprite(exit,0,0,False)
      killSprite(door)
    if keyPressed("space"):
      print("exit!")
      setBackgroundImage("images/stage2.png")
      showSprite(door)
      killSprite(exit)
'''



      #if touching(hero, exit):
        #print("exit!")
        #setBackgroundImage("images/stage2.png")
    #else:
     # setBackgroundImage("images/stage2.png")




endWait()
