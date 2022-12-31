import time
import pydirectinput as pyp
import keyboard
import pyautogui as gui
import threading
import mouse

incrementvar = 20


class Rightside(threading.Thread):
    def run(self):
        while True:
            if keyboard.is_pressed('6'):
                pos2 = gui.position()
                pos = pos2
                print(pos)
                xaxis = pos[0] + incrementvar
                yaxis = pos[1]
                print(xaxis, yaxis)
                mouse.move(xaxis, yaxis, absolute=True, duration=0.01)
                #pyp.move(x=xaxis, y=yaxis)


class Downside(threading.Thread):
    def run(self):
        while True:
            if keyboard.is_pressed('5'):
                pos2 = gui.position()
                pos = pos2
                print(pos)
                yaxis = pos[1] + incrementvar
                xaxis = pos[0]
                print(xaxis, yaxis)
                mouse.move(x=xaxis, y=yaxis, absolute=True, duration=0.01)


class Leftside(threading.Thread):
    def run(self):
        while True:
            if keyboard.is_pressed('4'):
                pos2 = gui.position()
                pos = pos2
                print(pos)
                xaxis = pos[0] - incrementvar
                yaxis = pos[1]
                print(xaxis, yaxis)
                mouse.move(x=xaxis, y=yaxis, absolute=True, duration=0.01)


class Upside(threading.Thread):
    def run(self):
        while True:
            if keyboard.is_pressed('8'):
                pos2 = gui.position()
                pos = pos2
                print(pos)
                yaxis = pos[1] - incrementvar
                xaxis = pos[0]
                print(xaxis, yaxis)
                mouse.move(x=xaxis, y=yaxis, absolute=True, duration=0.01)


class click(threading.Thread):
    def run(self):
        while True:
            if keyboard.is_pressed('0'):
                pyp.leftClick()


class rclick(threading.Thread):
    def run(self):
        while True:
            if keyboard.is_pressed('.'):
                pyp.rightClick()


moveright = Rightside()
movedown = Downside()
moveleft = Leftside()
moveup = Upside()
leftclick = click()
rightclick = rclick()

moveright.start()
movedown.start()
moveup.start()
moveleft.start()
leftclick.start()
rightclick.start()
