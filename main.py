import time
import pyautogui as pg

time.sleep (3)

txt = open("Rick.txt","r+")

for i in txt:
    pg.write(i)
    pg.press("Enter")
    time.sleep (1.1)
