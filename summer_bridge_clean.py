from pygame_functions import *
import sys     # let  python use your file system
import os      # help python identify your OS
import pygame
import math, random


'''
SETUP
'''
screenSize(960,720)
setAutoUpdate(False)

#SETUP VARIABLES
counter = 0 #For enemy motion
slayed = 0 #To count number of dragons slayed
enemy_status = "alive" #shows status of dragon
metGuard = "no" #has the hero met the guard yet






'''
BACKGROUND IMAGE
'''

setBackgroundImage( [  ["images/forest.jpg","images/forest.jpg"] ,["images/stage2.png", "images/forest.jpg"]  ])

'''
SPRITES
'''
#HERO
hero  = makeSprite("images/links.gif",32)  # links.gif contains 32 separate frames of animation. Sizes are automatically calculated.
heroX = 300
heroY = 300
moveSprite(hero,heroX,heroY,False)
showSprite(hero)

#HAWK
hawk = makeSprite("images/hawk.png")
showSprite(hawk)
hawkX = 100
hawkY = 300
moveSprite(hawk,hawkX,hawkY,False)

#CASTLE GUARD
guard = makeSprite("images/castle-guard.png")
showSprite(guard)
guardX = 305
guardY = -110
moveSprite(guard,guardX,guardY,False)

#DRAGON
enemy = makeSprite("images/enemy.png")
showSprite(enemy)
enemyX = 500
enemyY = 1000
moveSprite(enemy,enemyX,enemyY,False)

#AMMO
ammo = makeSprite("images/ammo.png")
ammoX = heroX
ammoY = heroY
ammoX_change = 10
ammoY_change = 10
ammo_state = "ready"

#AMMO - FUNCTIONS
def fire_ammo_up(x, y):
    global ammo_state
    ammo_state = "fire up"
    showSprite(ammo)
    moveSprite(ammo, x+16, y+10)

def fire_ammo_left(x, y):
    global ammo_state
    ammo_state = "fire left"
    showSprite(ammo)
    moveSprite(ammo, x+16, y+10)

def fire_ammo_right(x, y):
    global ammo_state
    ammo_state = "fire right"
    showSprite(ammo)
    moveSprite(ammo, x+16, y+10)

def fire_ammo_down(x, y):
    global ammo_state
    ammo_state = "fire down"
    showSprite(ammo)
    moveSprite(ammo, x+16, y+10)

'''
TEXT
'''
#HAWK CONVERSATION
hawkLabel = makeLabel("Hi, I'm Hawk. To enter castle, move north.", 25, 100, 500, "black", background="pink")

hawkLabel2 = makeLabel("To shoot dragon, press 'a' to shoot left, 'd' right, 'w' up, & 's' down.", 25, 100, 500, "black", background="pink")

hawkLabel3 = makeLabel("Nice dragon slay bro.", 25, 100, 500, "black", background="pink")


#GUARD CONVERSATION
guardColor = "white"
guardLabel = makeLabel("HALT! You can't enter unless you killed a dragon. Go south to find one.", 25, 100, 200, guardColor, background="navy")

guardLabel2 = makeLabel("Slayed that dragon boy!! Welcome to", 25, 100, 200, guardColor, background="purple")

guardLabel3 = makeLabel("UHHS Bridge Castle game! You may now enter.", 25, 100, 230, guardColor, background="purple")

#GAME OVER
dthColour = "white"
dthLabel = makeLabel("EATEN BY DRAGON!!!!", 80, 100, 50, dthColour, background="orange")

gameoverColor = "white"
gameoverLabel = makeLabel("Game Over :(", 80, 100, 150, gameoverColor, background="maroon")

#SLAYED DRAGON
killColour = "black"
killLabel = makeLabel("SLAYED DRAGON!!!!", 70, 100, 200, killColour, background="orange")

#SLAYED DRAGON SCORE
slayedColor = "orange"
slayedLabel = makeLabel("Dragons Slayed: 0", 28, 225, 100, slayedColor, background="black")
showLabel(slayedLabel)
slayed = 0

'''
OTHER SETUP
'''

nextFrame = clock()
frame=0

'''
GAME LOOP
'''

while True:
    if clock() > nextFrame:   # We only animate our character every 80ms.
        frame = (frame+1)%8                         # There are 8 frames of animation in each direction
        nextFrame += 80                             # so the modulus 8 allows it to loop


#HERO MOVEMENT
    if keyPressed("right"):
        changeSpriteImage(hero, 0*8+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left

        #keep sprites stationary
        hawkX -= 5
        moveSprite(hawk,hawkX,hawkY,False)
        guardX -= 5
        moveSprite(guard,guardX,guardY,False)
        enemyX -= 5
        moveSprite(enemy,enemyX,enemyY,False)


    elif keyPressed("down"):
        changeSpriteImage(hero, 1*8+frame)    # down facing animations are the 1st set
        scrollBackground(0, -5)
        
        #keep sprites stationary
        hawkY -= 5
        moveSprite(hawk,hawkX,hawkY,False)
        guardY -= 5
        moveSprite(guard,guardX,guardY,False)
        enemyY -= 5
        moveSprite(enemy,enemyX,enemyY,False)

    elif keyPressed("left"):
        changeSpriteImage(hero, 2*8+frame)    # and so on
        scrollBackground(5,0)
        
        #keep sprites stationary
        hawkX += 5
        moveSprite(hawk,hawkX,hawkY,False)
        guardX += 5
        moveSprite(guard,guardX,guardY,False)
        enemyX += 5
        moveSprite(enemy,enemyX,enemyY,False)

    elif keyPressed("up"):
        changeSpriteImage(hero,3*8+frame)
        scrollBackground(0,5)

        #keep sprites stationary
        hawkY += 5
        moveSprite(hawk,hawkX,hawkY,False)
        guardY += 5
        moveSprite(guard,guardX,guardY,False)
        enemyY += 5
        moveSprite(enemy,enemyX,enemyY,False)

    else:
        changeSpriteImage(hero, 1 * 8 + 5)  # the static facing front look

#ENEMY MOVEMENT
    distance = 500
    speed = 1

    if counter >= 0 and counter <= distance:
      enemyX -= speed
      #enemyY -= speed
      
    elif counter >= distance and counter <= distance*2:
      enemyX += speed
      #enemyY += speed
    else:
      counter = 0

    counter+=1
    moveSprite(enemy,enemyX,enemyY,False)


#CONVERSATIONS

    #SPEAK WITH HAWK
    if touching(hero, hawk) and metGuard == "no" and enemy_status == "alive":
      showLabel(hawkLabel)
    else:
      hideLabel(hawkLabel)

    if touching(hero, hawk) and metGuard == "yes" and enemy_status == "alive":
      showLabel(hawkLabel2)
    else:
      hideLabel(hawkLabel2)

    if touching(hero, hawk) and enemy_status == "dead":
      showLabel(hawkLabel3)
    else:
      hideLabel(hawkLabel3)

    #SPEAK WITH GUARD
    if touching(hero, guard) and enemy_status == "alive":
      showLabel(guardLabel)
      metGuard = "yes"
    else:
      hideLabel(guardLabel)

    if touching(hero, guard) and enemy_status == "dead":
      showLabel(guardLabel2)
      showLabel(guardLabel3)
    else:
      hideLabel(guardLabel2)
      hideLabel(guardLabel3)



#EATEN BY DRAGON

    if touching(hero, enemy):
      hideAll()
      setBackgroundImage("images/death.jpg")
      showLabel(dthLabel)
      showLabel(gameoverLabel)

#SHOOT AMMO
    if keyPressed("w"):
      if ammo_state == "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo_up(ammoX, ammoY)
    
    if keyPressed("a"):
      if ammo_state == "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo_left(ammoX, ammoY)

    if keyPressed("s"):
      if ammo_state == "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo_down(ammoX, ammoY)

    if keyPressed("d"):
      if ammo_state == "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo_right(ammoX, ammoY)


    # Ammo Movement
    if ammoY <= 0:
      ammoY = heroY
      ammo_state = "ready"

    if ammoY >= 950:
      ammoY = heroY
      ammo_state = "ready"

    if ammoX <= 0:
      ammoX = heroX
      ammo_state = "ready"
    
    if ammoX >= 950:
      ammoX = heroX
      ammo_state = "ready"

    if ammo_state == "fire up":
      fire_ammo_up(ammoX, ammoY)
      ammoY -= ammoY_change

    if ammo_state == "fire left":
      fire_ammo_left(ammoX, ammoY)
      ammoX -= ammoX_change

    if ammo_state == "fire down":
      fire_ammo_down(ammoX, ammoY)
      ammoY += ammoY_change
    
    if ammo_state == "fire right":
      fire_ammo_right(ammoX, ammoY)
      ammoX += ammoX_change
  

#KILL DRAGON

    if touching(ammo, enemy) and enemy_status is "alive":
      enemy_status = "dead"
      killSprite(enemy)
      killSprite(ammo)
      slayed += 1
      changeLabel(slayedLabel,"Slayed Dragons: " + str(int(slayed)), slayedColor)  # Update the label
      showLabel(killLabel)
      updateDisplay()
      tick(2)
      hideLabel(killLabel)

      


    '''
    CLOSING CODE
    '''
    updateDisplay()
    tick(120)
endWait()
