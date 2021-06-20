import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    time.sleep(0.15)
    return


def collide(data):
    if Time == 'night':
        for k in range(190, 360):
            for l in range(350, 379):
                if data[k, l] > 160:
                    hit('down')
                    pyautogui.keyUp('down', time.sleep(0.15))
                    # print('night_down')
                    return

        for k in range(170, 320):  # x
            for l in range(380, 460):  # y
                if data[k, l] > 160:
                    hit("up")
                    pyautogui.keyDown('down', time.sleep(0.02))
                    pyautogui.keyUp('down')
                    # print('night_jump')
                    return

    elif Time == 'day':
        for k in range(190, 360):
            for l in range(350, 379):
                if data[k, l] < 123:
                    hit('down')
                    pyautogui.keyUp('down', time.sleep(0.15))
                    # print('day_down')
                    return

        for k in range(180, 330):  # x
            for l in range(380, 460):  # y
                if data[k, l] < 123:
                    hit("up")
                    pyautogui.keyDown('down', time.sleep(0.02))
                    pyautogui.keyUp('down')
                    # print('day_jump')
                    return

    return


if __name__ == "__main__":
    print("Hey... Dino game about to START in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()

        for i in range(10, 15):  # x
            for j in range(95, 100):  # y
                if data[i, j] < 123:
                    Time = 'night'
                elif data[i, j] >= 123:
                    Time = 'day'

        collide(data)

# if __name__ == "__main__":
#     time.sleep(2)
#
#     while True:
#         image = ImageGrab.grab().convert('L')
#         data = image.load()
#         # Draw the rectangle for cactus
#         for i in range(170, 320):  # x
#             for j in range(380, 460):  # y
#                 data[i, j] = 200
#
#         # Draw the rectangle for bird
#         for i in range(190, 360):  # x
#             for j in range(350, 379):  # y
#                 data[i, j] = 130
#
#         # Draw the rectangle for time
#         for i in range(10, 15):  # x
#             for j in range(95, 100):  # y
#                 data[i, j] = 170
#
#         image.show()
#         break
