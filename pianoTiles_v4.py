import pyautogui as pg
import mss

bbox = (810,729,1111,730)
yatay = (0,140,160,300)

with mss.mss() as sct:
    while True:
        img = sct.grab(bbox)
        for cord in yatay:
            if img.pixel(cord,0)[0] < 70:
                pg.click(cord+810,729)
                break