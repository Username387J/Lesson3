import pgzrun
from random import randint

WIDTH=400
HEIGHT=400

TITLE="Shooting game"
message="Game starts..."

alien=Actor('alien')
alien.pos=50,50

def draw():
    screen.clear()
    screen.fill('black')
    alien.draw()
    screen.draw.text(message, center=(200,20), fontsize=30, color="white")


def moveAlien():
    alien.x=randint(50,350)
    alien.y=randint(50,350)

#in built function which gets triggered,when you click on the game screen

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good shot!"
        moveAlien()
    else:
        message="Try again"


moveAlien()
pgzrun.go()