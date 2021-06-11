import pyautogui
import time
from PIL import Image, ImageGrab
# from numpy import asarray, imag

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(230, 310):
        for j in range(455, 485):
            if data[i, j] < 100:
                return True
    return False

if __name__ == '__main__':
    print("Dino game is about to start in 1 second...")
    time.sleep(1)

    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        if isCollide(data) == True:
            hit('up')
        # print(asarray(image))
        # for i in range(230, 310):
        #     for j in range(455, 485):
        #         data[i, j] = 0

    # image.show()