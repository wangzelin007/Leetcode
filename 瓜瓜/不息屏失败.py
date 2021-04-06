import pyautogui

def myMove():
    pyautogui.moveTo(300,300, duration=0.25)
    pyautogui.moveTo(300,301, duration=0.25)

if __name__ == '__main__':
    while True:
        myMove()