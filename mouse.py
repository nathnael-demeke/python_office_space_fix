import pyautogui as au
import random
import time
list = []

for i in range(500):
    list.append(i)
while True:
    
    au.moveTo(random.choice(list),random.choice(list))
    
