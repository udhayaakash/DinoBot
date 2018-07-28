from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn=(340,420)
    dinosaur=(165,425)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')


#restartGame()
#time.sleep(1)
#pressSpace()


def imageGrab():
    box = (Cordinates.dinosaur[0]+60,Cordinates.dinosaur[1],Cordinates.dinosaur[0]+80,Cordinates.dinosaur[1]+ 30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restartGame()
    while True:
        if(imageGrab() != 847):
                pressSpace()
                time.sleep(0.1)
            # print("hi")

main()