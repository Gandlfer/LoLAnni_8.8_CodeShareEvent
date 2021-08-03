# Anniversary 8.8 Code Share event
# Made by https://github.com/Gandlfer

import pyautogui as auto
import time
from python_imagesearch.imagesearch import imagesearch as search
import keyboard
import sys

auto.FAILSAFE= False

if __name__=="__main__":
    inputBox_X, inputBox_Y=search("./captures/InputBox.PNG",0.9)
    button_X,button_Y=search("./captures/Button.PNG",0.9)

    inputCodeFile= open("CodeInput","r")
    inputCode=inputCodeFile.read().split(" ")
    inputCodeFile.close()

    usedCodeFile=open("UsedCode","r")
    usedCode=usedCodeFile.read().split(" ")
    usedCodeFile.close()

    for x in inputCode:
        if(x in usedCode):
            inputCode.remove(x)

    print("Input codes: {}".format(len(inputCode)))
    print("Used Codes: {}".format(len(usedCode)))

    for x in inputCode:
        # if keyboard.is_pressed('a'):
        #     sys.exit(0)
        auto.moveTo(inputBox_X,inputBox_Y)
        auto.doubleClick(button="left")
        auto.write(x)

        time.sleep(0.5)

        auto.moveTo(button_X,button_Y)
        auto.click(button="left")
        
        time.sleep(0.5)
        auto.moveTo(search("./captures/Confirm.PNG",0.8))
        auto.click(button="left")
        auto.moveTo(0,0)
        time.sleep(0.5)
        if(auto.locateOnScreen("./captures/Used.PNG") or auto.locateOnScreen("./captures/Balloon.PNG")):
            usedCodeFile=open("UsedCode","a")
            usedCodeFile.write(x+" ")
            usedCodeFile.close()
        
        auto.moveTo(search("./captures/Confirm.PNG",0.1))
        auto.click(button="left")
        time.sleep(1)
    
    inputCodeFile= open("CodeInput","w")
    for x in inputCode:
        inputCodeFile.write(x + " ")

    inputCodeFile.close()
