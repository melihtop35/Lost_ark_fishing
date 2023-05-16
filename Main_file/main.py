import cv2
import numpy as np
from pyautogui import*
import pyautogui
import time
import schedule
import random

def DONGU_BOZ():
    time.sleep(random.uniform(0.10,0.15))
    pyautogui.keyDown('e')
    time.sleep( random.uniform( 0.10, 0.15 ))
    pyautogui.keyUp('e')

def EKRAN_GORUNTUSU():
        screenWidth, screenHeight= pyautogui.size()
        ekranGörüntüsü = pyautogui.screenshot()
        resim = "resim.png"
        ekranGörüntüsü.save(resim)
        
def BOT_DONGU():
    resim = cv2.imread("resim.png")
    resim_gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    
    ara_resim = cv2.imread("ikon.png")
    ara_resim_gri = cv2.cvtColor(ara_resim,cv2.COLOR_BGR2GRAY)
    
    eslesme = cv2.matchTemplate(resim_gri,ara_resim_gri,cv2.TM_CCOEFF_NORMED)
    loc=np.where(eslesme>=0.7)
    if len(loc[0]) > 0:
        time.sleep(random.uniform(0.10,0.15))
        pyautogui.keyDown('e')
        time.sleep( random.uniform( 0.10, 0.15 ))
        pyautogui.keyUp('e')
        time.sleep(random.uniform(5.5, 7.5))
        print("Balik tutuldu")

        if True:
             time.sleep(random.uniform(0.15,0.35))
             pyautogui.keyDown('e')
             time.sleep(random.uniform(0.10,0.30))
             pyautogui.keyUp('e')
             time.sleep(random.uniform(5.0,6.0))

def main():
    print("Basladi")
    schedule.every(0.1).seconds.do(EKRAN_GORUNTUSU)
    schedule.every(0.1).seconds.do(BOT_DONGU)
    #schedule.every(1).minutes.do(DONGU_BOZ)

    while True:
        schedule.run_pending()

main()

