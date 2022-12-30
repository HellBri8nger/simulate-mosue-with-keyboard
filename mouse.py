import pydirectinput as pyp
import keyboard
import pyautogui as gui
import threading

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
                pyp.moveTo(x=xaxis, y=yaxis)


class Downside(threading.Thread):
    def run(self):
        while True:
            if keyboard.is_pressed('2'):
                pos2 = gui.position()
                pos = pos2
                print(pos)
                yaxis = pos[1] + incrementvar
                xaxis = pos[0]
                print(xaxis, yaxis)
                pyp.moveTo(x=xaxis, y=yaxis)


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
                pyp.moveTo(x=xaxis, y=yaxis)


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
                pyp.moveTo(x=xaxis, y=yaxis)


class click(threading.Thread):
    def run(selfs):
        while True:
            if keyboard.is_pressed('5'):
                pyp.leftClick()

class rclick(threading.Thread):
    def run(selfs):
        while True:
            if keyboard.is_pressed('0'):
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