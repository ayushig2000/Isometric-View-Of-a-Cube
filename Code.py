import pyautogui
import math
import time

time.sleep(6)


a=210


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
