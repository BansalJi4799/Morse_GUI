# YUVRAJ BANSAL 
# TASK 5.3D 
# 2110994799

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
from ast import keyword
import time

myLed = LED(4)

win = Tk()
win.title("Morse Code Blink")
win.geometry("275x175")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def userInput():
    input = Input_Section.get('1.0','end-1c')
    ledBlink(input)

def dot(): 
    myLed.on()
    time.sleep(0.2) 
    myLed.off()
    time.sleep(0.2)
    
def line():
    myLed.on()
    time.sleep(0.6)
    myLed.off()
    time.sleep(0.2)


def ledBlink(input):
    print("Converting....")
    time.sleep(1)

    for alphabet in input:    
        if alphabet.lower() == 'a':
            dot()
            line()

        elif alphabet.lower() == 'b':
            line()
            dot()
            dot()
            dot()

        elif alphabet.lower() == 'c':
            line()
            dot()
            line()
            dot()


        elif alphabet.lower() == 'd':
            line()
            dot()
            dot()
            
        elif alphabet.lower() == 'e':
            dot()
            
        elif alphabet.lower() == 'f':
            dot()
            dot()
            line()
            dot()
            
        elif alphabet.lower() == 'g':
            line()
            line()
            dot()

        elif alphabet.lower() == 'h':
            dot()
            dot()
            dot()
            dot()
            
        elif alphabet.lower() == 'i':
            dot()
            dot()

        elif alphabet.lower() == 'j':
            dot()
            line()
            line()
            line()
            
        elif alphabet.lower() == 'k':
            line()
            dot()
            line()
            
        elif alphabet.lower() == 'l':
            dot()
            line()
            dot()
            dot()
            
        elif alphabet.lower() == 'm':
            line()
            line()

        elif alphabet.lower() == 'n':
            line()
            dot()
            
        elif alphabet.lower() == 'o':
            line()
            line()
            line()
            
        elif alphabet.lower() == 'p':
            dot()
            line()
            line()
            dot()
            
        elif alphabet.lower() == 'q':
            line()
            line()
            dot()
            line()
            
        elif alphabet.lower() == 'r':
            dot()
            line()
            dot()
            
        elif alphabet.lower() == 's':
            dot()
            dot()
            dot()
            
        elif alphabet.lower() == 't':
            line()
            
        elif alphabet.lower() == 'u':
            dot()
            dot()
            line()
            
        elif alphabet.lower() == 'v':
            dot()
            dot()
            dot()
            line()
            
        elif alphabet.lower() == 'w':
            dot()
            line()
            line()
            
        elif alphabet.lower() == 'x':
            line()
            dot()
            dot()
            line()
            
        elif alphabet.lower() == 'y':
            line()
            dot()
            line()
            line()
            
        elif alphabet.lower() == 'z':
            line()
            line()
            dot()
            dot()


def closeWin():
    win.destroy()


Label(win, text = "Enter the Word:", bg = 'red', font = myFont, height = 1, width = 30).grid(row = 0, column = 0)

Input_Section = Text(win, height = 1, width = 30, bg = 'grey')
Input_Section.grid(row = 1, column = 0)
Submit_Button = Button(win, text = "Submit", command = userInput, bg = 'blue', font = myFont, height = 1, width = 5)
Submit_Button.grid(row = 2, column = 0)
Exit_Button = Button(win, text = "Return", command = closeWin, bg = 'green', font = myFont, height = 1, width = 5)
Exit_Button.grid(row = 3, column = 0)

win.protocol("WM_DELETE_WINDOW",closeWin)
win.mainloop()