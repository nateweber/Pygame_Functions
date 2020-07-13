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
score = 0 #set initial score to 0 since we've haven't got coins yet
coin1_status = "not collected" # Coin 1 collection status
coin2_status = "not collected" # Coin 2 collection status
inScottRoom = "no"  # is the hero currently in Scott Room?
doorKey = "no" #key to the main room
inMainRoom = "no" #is the hero currently in main room?
riddleAnswer = "the future" #answer to gnome's riddle
withGnome = 0 #counter to count how many times hero has spoken with gnome





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

#GATE
gate = makeSprite("images/gate.png")
showSprite(gate)
gateX = 200
gateY = -110
moveSprite(gate,gateX,gateY,False)

#DRAGON
enemy = makeSprite("images/enemy.png")
showSprite(enemy)
enemyX = 500
enemyY = 1000
moveSprite(enemy,enemyX,enemyY,False)

#COIN 1
coin = makeSprite("images/coin.png")
showSprite(coin)
coinX = 90
coinY = -500
moveSprite(coin,coinX,coinY,False)

#COIN 2
coin2 = makeSprite("images/coin.png")
showSprite(coin2)
coin2X = 500
coin2Y = -550
moveSprite(coin2,coin2X,coin2Y,False)

#BANDS IN SAFE
safe = makeSprite("images/safe.png")
hideSprite(safe)
safeX = 250
safeY = 200
moveSprite(safe,safeX,safeY,False)

#TRAVIS SCOTT HEAD
scott = makeSprite("images/travis-scott-head.png")
showSprite(scott)
scottX = 90
scottY = -1200
moveSprite(scott,scottX,scottY,False)

#TRAVIS SCOTT Door
scottdoor = makeSprite("images/door.png")
showSprite(scottdoor)
scottdoorX = 192
scottdoorY = -1030
moveSprite(scottdoor,scottdoorX,scottdoorY,False)

#MAIN ROOM DOOR
door = makeSprite("images/door2.png")
showSprite(door)
doorX = 590
doorY = -1180
moveSprite(door,doorX,doorY,False)

#GNOME
gnome = makeSprite("images/gnome.png")
showSprite(gnome)
gnomeX = 650
gnomeY = -1060
moveSprite(gnome,gnomeX,gnomeY,False)

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

#ROOM EXITS
scottexit = makeLabel("Press 'x' to exit", 25, 100, 600, "white", background="red")

#DOOR LOCKED
noKeyColor = "red"
noKeyLabel = makeLabel("You can't enter without a key!", 35, 100, 200, noKeyColor, background="black")


#GNOME CONVERSATIONS
gnomeColor = "white"

  #first greeting
gnomeIntro1 = makeLabel("Hi! I'm Lil Tjay the Gnome. I guard the red door. Want to enter it? Y or N?", 25, 100, 200, gnomeColor, background="red")
  
  #if hero responds "N" for no
gnomeN = makeLabel("K. Bye.", 24, 100, 200, gnomeColor, background="red")

  #if hero responds "N" first time and then comes back later
gnomeIntro2 = makeLabel("You're back? Fine, want to try again? Y or N?", 25, 100, 200, gnomeColor, background="red")

  #if hero responds "Y"
gnomeYes = makeLabel("You must answer a riddle. What is always in front of you but can’t be seen?", 24, 100, 200, gnomeColor, background="red")

  #if hero answers riddle correctly
gnomeCorrect = makeLabel("Correct! Here's the key. You may enter.", 24, 100, 200, gnomeColor, background="red")

  #after hero has entered main room
gnomeIntro3 = makeLabel("Hope you enjoyed the main room.", 25, 100, 200, gnomeColor, background="red")

  #user input for answer to riddle 
wordBox = makeTextBox(450, 300, 300, 0, "Enter answer here", 15, 24)
hideTextBox(wordBox)

#MAIN ROOM CONVERSATIONS
natejohn = makeLabel("Greetings peasant... err I mean student. Welcome to Bridge. You're", 25, 100, 450, "white", background="maroon")

natejohn2 = makeLabel("going to make a game like this, but way better. Press 'x' to leave room.", 25, 100, 485, "white", background="maroon")

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

#SCORE FROM COLLECTING COINS
scoreColor = "yellow"
scoreLabel = makeLabel("Score: 0", 28, 100, 100, scoreColor, background="black")
showLabel(scoreLabel)

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
        gateX -= 5
        moveSprite(gate,gateX,gateY,False)
        coinX -= 5
        moveSprite(coin,coinX,coinY,False)
        coin2X -= 5
        moveSprite(coin2,coin2X,coin2Y,False)
        scottX -= 5
        moveSprite(scott,scottX,scottY,False)
        scottdoorX -= 5
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        doorX -= 5
        moveSprite(door,doorX,doorY,False)
        gnomeX -= 5
        moveSprite(gnome,gnomeX,gnomeY,False)






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
        gateY -= 5
        moveSprite(gate,gateX,gateY,False)
        coinY -= 5
        moveSprite(coin,coinX,coinY,False)
        coin2Y -= 5
        moveSprite(coin2,coin2X,coin2Y,False)
        scottY -= 5
        moveSprite(scott,scottX,scottY,False)
        scottdoorY -= 5
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        doorY -= 5
        moveSprite(door,doorX,doorY,False)
        gnomeY -= 5
        moveSprite(gnome,gnomeX,gnomeY,False)        

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
        gateX += 5
        moveSprite(gate,gateX,gateY,False)
        coinX += 5
        moveSprite(coin,coinX,coinY,False)
        coin2X += 5
        moveSprite(coin2,coin2X,coin2Y,False)
        scottX += 5
        moveSprite(scott,scottX,scottY,False)
        scottdoorX += 5
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        doorX += 5
        moveSprite(door,doorX,doorY,False)
        gnomeX += 5
        moveSprite(gnome,gnomeX,gnomeY,False)

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
        gateY += 5
        moveSprite(gate,gateX,gateY,False)
        coinY += 5
        moveSprite(coin,coinX,coinY,False)
        coin2Y += 5
        moveSprite(coin2,coin2X,coin2Y,False)
        scottY += 5
        moveSprite(scott,scottX,scottY,False)
        scottdoorY += 5
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        doorY += 5
        moveSprite(door,doorX,doorY,False)
        gnomeY += 5
        moveSprite(gnome,gnomeX,gnomeY,False)

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

#COINS
    #COIN PICKUP
    if touching(hero,coin) and coin1_status == "not collected":
      killSprite(coin)
      score += 1
      changeLabel(scoreLabel,"Score: " + str(int(score)), scoreColor)  # Update the label
      coin1_status = "collected"
      showSprite(safe)
      updateDisplay()
      tick(1)
      hideSprite(safe)

    if touching(hero,coin2) and coin2_status == "not collected":
      killSprite(coin2)
      score += 1
      changeLabel(scoreLabel,"Score: " + str(int(score)), scoreColor)  # Update the label
      coin2_status = "collected"
      showSprite(safe)
      updateDisplay()
      tick(1)
      hideSprite(safe)
      
#DOORS & ROOMS
  
  #CASTLE GATE

  #GATE LOCKED
    if touching(hero, gate) and enemy_status is "alive":
      heroY += 5
      moveSprite(hero, heroX, heroY, False)
  #GATE UNLOCKED
    if enemy_status is "dead":
      hideSprite(gate)

  #SCOTT ROOM
    #ENTER ROOM
    if touching(hero, scottdoor):
      inScottRoom = "yes"
      hideSprite(scottdoor)
      hideAll()
      showSprite(hero)
      setBackgroundImage("images/stage.png")
      showLabel(scottexit)

    #LEAVE ROOM
    if inScottRoom == "yes" and keyPressed("x"):
      inScottRoom = "no"
      unhideAll()
      hideSprite(safe)
      hideLabel(scottexit)
      setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,["images/forest.jpg", "images/forest.jpg"]  ])
      guardX = 305
      guardY = 1160        
      hawkX = 100
      hawkY = 1570
      coinX = 90
      coinY = 500
      coin2X = 500
      coin2Y = 550
      doorX = 590
      doorY = 90
      gnomeX = 650
      gnomeY = 170
      scottdoorX = 192
      scottdoorY = 225
      scottX = 90
      scottY = 70
      moveSprite(hero,200,300,False)
      moveSprite(door,doorX,doorY,False)
      moveSprite(gnome, gnomeX, 170, False)
      moveSprite(scottdoor,192, 225, False)
      moveSprite(scott,90, 70, False)
      moveSprite(coin2,coin2X,coin2Y,False)
      moveSprite(coin,coinX,coinY,False)
      moveSprite(guard,guardX,guardY,False)
      moveSprite(hawk,hawkX,hawkY,False)
    
  #MAIN ROOM
    #ENTER MAIN ROOM
    if touching(hero, door) and inScottRoom == "no" and doorKey == "no":
      showLabel(noKeyLabel)
    else:
      hideLabel(noKeyLabel)

    if touching(hero, door) and inScottRoom == "no" and doorKey == "yes":
      inMainRoom = "yes"
      withGnome = 2
      hideLabel(gnomeCorrect)
      hideAll()
      hideSprite(door)
      showLabel(natejohn)
      showLabel(natejohn2)
      setBackgroundImage("images/mainroom.jpg")
    else:
      hideLabel(natejohn)
      hideLabel(natejohn2)

    #LEAVE MAIN ROOM
    if keyPressed("x") and inMainRoom == "yes":
        inMainRoom = "no"
        unhideAll()
        hideSprite(safe)
        setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,["images/forest.jpg", "images/forest.jpg"]  ])
        hawkX = 100
        hawkY = 1570
        guardX = 305
        guardY = 1160
        coinX = 90
        coinY = 770
        coin2X = 500
        coin2Y = 720
        doorX = 590
        doorY = 90
        gnomeX = 650
        gnomeY = 170
        scottdoorX = 192
        scottdoorY = 225
        scottX = 90
        scottY = 70
        moveSprite(hero,600,200,False)
        moveSprite(door,600,0,False)
        moveSprite(gnome, gnomeX, 170, False)
        moveSprite(scottdoor,192, 225, False)
        moveSprite(scott,90, 70, False)
        moveSprite(coin2,coin2X,coin2Y,False)
        moveSprite(coin,coinX,coinY,False)
        moveSprite(guard,guardX,guardY,False)
        moveSprite(hawk,hawkX,hawkY,False)
    

#SPEAK WITH GNOME
    #FIRST INTERACTION
    if touching(hero, gnome) and withGnome < 1 and inScottRoom == "no":
      showLabel(gnomeIntro1)
      if keyPressed("Y"):
        hideLabel(gnomeIntro1)
        showLabel(gnomeYes)
        withGnome = 1
        showTextBox(wordBox)
        entry = textBoxInput(wordBox).lower()
        if entry == riddleAnswer and inMainRoom == "no":
          showLabel(gnomeCorrect)
          doorKey = "yes"
          hideTextBox(wordBox)
          hideLabel(gnomeYes)
        else:
          hideLabel(gnomeCorrect)
      if keyPressed("N"):
        withGnome = 1
        hideLabel(gnomeIntro1)
        showLabel(gnomeN)
        updateDisplay()
        tick(2)
        hideLabel(gnomeN)
    else:
      hideLabel(gnomeIntro1)
   
    #SECOND INTERACTION
    if touching(hero, gnome) and withGnome == 1 and doorKey is "no" and inScottRoom == "no":
      showLabel(gnomeIntro2)
      if keyPressed("Y"):
        hideLabel(gnomeIntro1)
        showLabel(gnomeYes)
        withGnome = 1
        showTextBox(wordBox)
        entry = textBoxInput(wordBox).lower()
        if entry == riddleAnswer and inMainRoom == "no":
          showLabel(gnomeCorrect)
          doorKey = "yes"
          hideTextBox(wordBox)
          hideLabel(gnomeYes)
        else:
          hideLabel(gnomeCorrect)
      if keyPressed("N"):
        withGnome = 1
        hideLabel(gnomeIntro2)
        showLabel(gnomeN)
        updateDisplay()
        tick(2)
        hideLabel(gnomeN)
    else:
      hideLabel(gnomeIntro2)
    
    #POST-ROOM INTERACTION
    if touching(hero, gnome) and withGnome == 2:
      showLabel(gnomeIntro3)
    else:
      hideLabel(gnomeIntro3)


#DRAGON & AMMO
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
