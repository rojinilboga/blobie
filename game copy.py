#importing the libraries
import pgzrun
from random import randint

TITLE = "BLOBFISH SHOT GAME!!!"
WIDTH = 600
HEIGHT = 600
R = randint(1,255)
G = randint(1,255)
B = randint(1,255)
#creating the capybara
blobfish =Actor("blobfish")

msg = ""

def draw():
    screen.clear()
    screen.fill(color =(R,G,B))

    blobfish.draw()

pgzrun.go()