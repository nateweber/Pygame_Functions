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
inMainRoom = 0
inScottRoom = 0
withGnome = 0
doorKey = "no"
metGuard = "no"
coinpick = 0
counter = 0






'''
BACKGROUND IMAGE
'''

setBackgroundImage( [  ["images/forest.jpg","images/forest.jpg"] ,
                       ["images/stage2.png", "images/forest.jpg"]  ])


'''
SPRITES
'''
#DOOR
door = makeSprite("images/door2.png")
showSprite(door)
doorX = 590
doorY = -1180
moveSprite(door,doorX,doorY,False)

#gnome
gnome = makeSprite("images/gnome.png")
showSprite(gnome)
gnomeX = 650
gnomeY = -1060
moveSprite(gnome,gnomeX,gnomeY,False)

#COIN1
coin = makeSprite("images/coin.png")
showSprite(coin)
coinX = 90
coinY = -500
moveSprite(coin,coinX,coinY,False)

#COIN2
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

#SCOTT
scott = makeSprite("images/travis-scott-head.png")
showSprite(scott)
scottX = 90
scottY = -1200
moveSprite(scott,scottX,scottY,False)

#SCOTT Door
scottdoor = makeSprite("images/door.png")
showSprite(scottdoor)
scottdoorX = 192
scottdoorY = -1030
moveSprite(scottdoor,scottdoorX,scottdoorY,False)

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


#HAWK
hawk = makeSprite("images/hawk.png")
showSprite(hawk)
hawkX = 100
hawkY = 300
moveSprite(hawk,hawkX,hawkY,False)

#HERO
hero  = makeSprite("images/links.gif",32)  # links.gif contains 32 separate frames of animation. Sizes are automatically calculated.
heroX = 300
heroY = 300
moveSprite(hero,heroX,heroY,False)
showSprite(hero)

#AMMO
ammo = makeSprite("images/ammo.png")
ammoX = heroX
ammoY = heroY
ammoX_change = 10
ammoY_change = 10
ammo_state = "ready"

def fire_ammo(x, y):
    global ammo_state
    ammo_state = "fire"
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


#Enemy
enemy = makeSprite("images/enemy.png")
showSprite(enemy)
enemyx = 500
enemyy = 1000
moveSprite(enemy,enemyx,enemyy,False)
enemy_status = "alive"


'''
TEXT
'''
#TEST TEXT


gnomeColor = "white"
gnomeIntro1 = makeLabel("Hi! I'm Lil Tjay the Gnome. I guard the red door. Want to enter it? Y or N?", 25, 100, 200, gnomeColor, background="red")
gnomeIntro2 = makeLabel("You're back? Fine, want to try again? Y or N?", 25, 100, 200, gnomeColor, background="red")
gnomeIntro3 = makeLabel("Hope you enjoyed the main room.", 25, 100, 200, gnomeColor, background="red")
gnomeN = makeLabel("K. Bye.", 24, 100, 200, gnomeColor, background="red")
gnomeYes = makeLabel("You must answer a riddle. What is always in front of you but can’t be seen?", 24, 100, 200, gnomeColor, background="red")
riddleAnswer = "the future"
gnomeCorrect = makeLabel("Correct! Here's the key. You may enter.", 24, 100, 200, gnomeColor, background="red")


#gnomeLabel3 = makeLabel("Correct! You may enter!", 24, 100, 200, gnomeColor, background="red")


ftnColour = "white"
ftnLabel2 = makeLabel("Cool. Not much happening here. Just testing. Leave, press x.", 24, 100, 200, ftnColour, background="pink")


scoreColour = "yellow"
scoreLabel = makeLabel("Score: 0", 28, 100, 100, scoreColour, background="black")
showLabel(scoreLabel)
score = 0

slayedColor = "orange"
slayedLabel = makeLabel("Dragons Slayed: 0", 28, 225, 100, slayedColor, background="black")
showLabel(slayedLabel)
slayed = 0

dthColour = "white"
dthLabel = makeLabel("EATEN BY DRAGON!!!!", 80, 100, 50, dthColour, background="orange")

gameoverColor = "white"
gameoverLabel = makeLabel("Game Over :(", 80, 100, 150, gameoverColor, background="maroon")

killColour = "black"
killLabel = makeLabel("SLAYED DRAGON!!!!", 70, 100, 200, killColour, background="orange")

guardColor = "white"
guardLabel = makeLabel("HALT! You can't enter unless you killed a dragon. Go south to find one.", 25, 100, 200, guardColor, background="navy")

guardLabel2 = makeLabel("Slayed that dragon boy!! Welcome to", 25, 100, 200, guardColor, background="purple")
guardLabel3 = makeLabel("UHHS Bridge Castle game! You may now enter.", 25, 100, 230, guardColor, background="purple")


natejohn = makeLabel("Greetings peasant... err I mean student. Welcome to Bridge. You're", 25, 100, 450, "white", background="maroon")

natejohn2 = makeLabel("going to make a game like this, but way better. Press 'x' to leave room.", 25, 100, 485, "white", background="maroon")

scottexit = makeLabel("Press 'x' to exit", 25, 100, 600, "white", background="red")

hawkLabel = makeLabel("Hi, I'm Hawk. To enter castle, move north.", 25, 100, 500, "black", background="pink")

hawkLabel2 = makeLabel("To shoot dragon, press 'a' to shoot left, 'd' right, 'w' up, & 's' down.", 25, 100, 500, "black", background="pink")

hawkLabel3 = makeLabel("Nice dragon slay bro.", 25, 100, 500, "black", background="pink")



noKeyColor = "red"
noKeyLabel = makeLabel("You can't enter without a key!", 35, 100, 200, noKeyColor, background="black")


wordBox = makeTextBox(450, 300, 300, 0, "Enter answer here", 15, 24)
hideTextBox(wordBox)

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

#ENEMY MOVEMENT
    distance = 500
    speed = 1


    if counter >= 0 and counter <= distance:
      enemyx -= speed
      
      
    elif counter >= distance and counter <= distance*2:
      enemyx += speed


    else:
      counter = 0

    counter+=1
    
    

    moveSprite(enemy,enemyx,enemyy,False)
#HERO MOVEMENT
    if keyPressed("right"):
        changeSpriteImage(hero, 0*8+frame)    # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5,0)                      # The player is moving right, so we scroll the background left
        doorX -= 5
        #exitx -=5
        coinX -= 5
        coin2X -= 5
        enemyx -= 5
        gnomeX -= 5
        scottX -= 5
        scottdoorX -= 5
        guardX -= 5
        hawkX -= 5
        gateX -= 5
        moveSprite(gate,gateX,gateY,False)
        moveSprite(door,doorX,doorY,False)
        #moveSprite(exit,exitx,exity,False)
        moveSprite(coin2,coin2X,coin2Y,False)
        moveSprite(coin,coinX,coinY,False)
        moveSprite(enemy,enemyx,enemyy,False)
        moveSprite(gnome,gnomeX,gnomeY,False)
        moveSprite(scott,scottX,scottY,False)
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        moveSprite(guard,guardX,guardY,False)
        moveSprite(hawk,hawkX,hawkY,False)








    elif keyPressed("down"):
        changeSpriteImage(hero, 1*8+frame)    # down facing animations are the 1st set
        scrollBackground(0, -5)
        doorY -= 5
       # exity -=5
        coinY -=5
        coin2Y -=5
        enemyy -=5
        gnomeY -=5
        scottY -= 5
        scottdoorY -= 5
        guardY -= 5
        hawkY -= 5
        gateY -= 5
        moveSprite(gate,gateX,gateY,False)
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        moveSprite(door,doorX,doorY,False)
        #moveSprite(exit,exitx,exity,False)
        moveSprite(coin2,coin2X,coin2Y,False)
        moveSprite(coin,coinX,coinY,False)
        moveSprite(enemy,enemyx,enemyy,False)
        moveSprite(gnome,gnomeX,gnomeY,False)
        moveSprite(scott,scottX,scottY,False)
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        moveSprite(guard,guardX,guardY,False)
        moveSprite(hawk,hawkX,hawkY,False)



    elif keyPressed("left"):
        changeSpriteImage(hero, 2*8+frame)    # and so on
        scrollBackground(5,0)
        doorX += 5
        #exitx += 5
        coinX += 5
        coin2X += 5
        enemyx += 5
        gnomeX += 5
        scottX += 5
        scottdoorX += 5
        guardX += 5
        hawkX += 5
        gateX += 5
        moveSprite(gate,gateX,gateY,False)

        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        moveSprite(door,doorX,doorY,False)
        #moveSprite(exit,exitx,exity,False)
        moveSprite(coin2,coin2X,coin2Y,False)        
        moveSprite(coin,coinX,coinY,False)
        moveSprite(enemy,enemyx,enemyy,False)
        moveSprite(gnome,gnomeX,gnomeY,False)
        moveSprite(scott,scottX,scottY,False)
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        moveSprite(guard,guardX,guardY,False)
        moveSprite(hawk,hawkX,hawkY,False)



    elif keyPressed("up"):
        changeSpriteImage(hero,3*8+frame)
        scrollBackground(0,5)

        doorY += 5
        #exity += 5
        coinY += 5
        coin2Y += 5
        enemyy += 5
        gnomeY +=5
        scottY += 5
        scottdoorY += 5
        guardY += 5
        hawkY += 5
        gateY += 5
        moveSprite(gate,gateX,gateY,False)
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        moveSprite(door,doorX,doorY,False)
        #moveSprite(exit,doorX,doorY,False)
        moveSprite(coin2,coin2X,coin2Y,False)
        moveSprite(coin,coinX,coinY,False)
        moveSprite(enemy,enemyx,enemyy,False)
        moveSprite(gnome,gnomeX,gnomeY,False)
        moveSprite(scott,scottX,scottY,False)
        moveSprite(scottdoor,scottdoorX,scottdoorY,False)
        moveSprite(guard,guardX,guardY,False)
        moveSprite(hawk,hawkX,hawkY,False)



    else:
        changeSpriteImage(hero, 1 * 8 + 5)  # the static facing front look

    updateDisplay()
    tick(120)
#SHOOT
    if keyPressed("w"):
      if ammo_state is "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo(ammoX, ammoY)
    
    if keyPressed("a"):
      if ammo_state is "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo_left(ammoX, ammoY)

    if keyPressed("s"):
      if ammo_state is "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo_down(ammoX, ammoY)

    if keyPressed("d"):
      if ammo_state is "ready":
                    # Get the current x cordinate of the spaceship
        ammoX = heroX
        ammoY = heroY
        fire_ammo_right(ammoX, ammoY)


    # Bullet Movement
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



    if ammo_state is "fire":
      fire_ammo(ammoX, ammoY)
      ammoY -= ammoY_change

    if ammo_state is "fire left":
      fire_ammo_left(ammoX, ammoY)
      ammoX -= ammoX_change

    if ammo_state is "fire down":
      fire_ammo_down(ammoX, ammoY)
      ammoY += ammoY_change
    
    if ammo_state is "fire right":
      fire_ammo_right(ammoX, ammoY)
      ammoX += ammoX_change
        


    
#COIN PICKUP
    if touching(hero,coin) and coinpick == 0:
      killSprite(coin)
      score += 1
      changeLabel(scoreLabel,"Score: " + str(int(score)), scoreColour)  # Update the label
      coinpick = 1
      showSprite(safe)
      updateDisplay()
      tick(1)
      hideSprite(safe)

    if touching(hero,coin2) and coinpick == 1:
      killSprite(coin2)
      score += 1
      changeLabel(scoreLabel,"Score: " + str(int(score)), scoreColour)  # Update the label
      coinpick = 2
      showSprite(safe)
      updateDisplay()
      tick(1)
      hideSprite(safe)

#KILL DRAGON

    if touching(ammo, enemy) and enemy_status is "alive":
      killSprite(enemy)
      enemy_status = "dead"
      slayed += 1
      changeLabel(slayedLabel,"Slayed Dragons: " + str(int(slayed)), slayedColor)  # Update the label
      showLabel(killLabel)
      updateDisplay()
      tick(2)
      #pause(5000, allowEsc=True)
      hideLabel(killLabel)
      #updateDisplay()
      #tick(60)

#EATEN BY DRAGON

    if touching(hero, enemy) and enemy_status is "alive":
      hideAll()
      setBackgroundImage("images/death.jpg")
      showLabel(dthLabel)
      showLabel(gameoverLabel)

#GATE LOCKED
    if touching(hero, gate) and enemy_status is "alive":
      heroY += 5
      moveSprite(hero, heroX, heroY, False)
#GATE UNLOCKED
    if enemy_status is "dead":
      hideSprite(gate)


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

    if touching(hero, guard) and enemy_status == "dead":
      showLabel(guardLabel2)
      showLabel(guardLabel3)
    else:
      hideLabel(guardLabel2)
      hideLabel(guardLabel3)


    if touching(hero, guard) and enemy_status == "alive":
      showLabel(guardLabel)
      metGuard = "yes"

    else:
      hideLabel(guardLabel)

    if touching(hero, guard) and enemy_status == "dead":
      showLabel(guardLabel2)
    else:
      hideLabel(guardLabel2)
#SPEAK WITH GNOME
    #FIRST INTERACTION
    if touching(hero, gnome) and withGnome < 1 and inScottRoom == 0:
      showLabel(gnomeIntro1)
      if keyPressed("Y"):
        hideLabel(gnomeIntro1)
        showLabel(gnomeYes)
        withGnome = 1
        showTextBox(wordBox)
        entry = textBoxInput(wordBox).lower()
        if entry == riddleAnswer and inMainRoom < 1:
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
    if touching(hero, gnome) and withGnome == 1 and doorKey is "no" and inScottRoom == 0:
      showLabel(gnomeIntro2)
      if keyPressed("Y"):
        hideLabel(gnomeIntro1)
        showLabel(gnomeYes)
        withGnome = 1
        showTextBox(wordBox)
        entry = textBoxInput(wordBox).lower()
        if entry == riddleAnswer and inMainRoom < 1:
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


#ENTER MAIN ROOM
    if touching(hero, door) and inScottRoom == 0 and doorKey == "no":
      showLabel(noKeyLabel)
    else:
      hideLabel(noKeyLabel)

    if touching(hero, door) and inScottRoom == 0 and doorKey == "yes":
      inMainRoom = 1
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
    if keyPressed("x") and inMainRoom == 1:
        inMainRoom = 0
        unhideAll()
        hideSprite(safe)
        setBackgroundImage( [  ["images/stage2.png", "images/forest.jpg"] ,["images/forest.jpg", "images/forest.jpg"]  ])
        hawkX = 100
        hawkY = 1570
        guardX = 305
        #SHOULD BE POSITIVE
        guardY = -1160
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


#SCOTT ROOM
    if touching(hero, scottdoor):
      inScottRoom = 1
      hideSprite(scottdoor)
      hideAll()
      showSprite(hero)
      showLabel(scottexit)
      #moveSprite(hero,200,475,False)
      setBackgroundImage("images/stage.png")

#LEAVE SCOTT ROOM
    if inScottRoom == 1 and keyPressed("x"):
        inScottRoom = 0
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




endWait()
