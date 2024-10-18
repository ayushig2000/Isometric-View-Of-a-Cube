import pyautogui
import math
import time
import pandas as pd
import numpy as np

time.sleep(6) #tgithis is a time it takes to start


a=210 #side length of a cube


x=a*math.cos(math.pi/6)
y=a*math.sin(math.pi/6)

pyautogui.moveTo(600, 440, duration = 1)
pyautogui.dragRel(0, +a, duration = 1)
pyautogui.dragRel(x, +y, duration = 1)
pyautogui.dragRel(x, -y, duration = 1)
pyautogui.dragRel(0, -a, duration = 1)
pyautogui.dragRel(-x, -y, duration = 1)
pyautogui.dragRel(-x, +y, duration = 1)
pyautogui.dragRel(x, +y, duration = 1)
pyautogui.dragRel(x, -y, duration = 1)
pyautogui.dragRel(-x, +y, duration = 1)
pyautogui.dragRel(0, +a, duration = 1)
