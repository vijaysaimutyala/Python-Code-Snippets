import pyautogui 
pyautogui.FAILSAFE = False
while True:
    pyautogui.moveTo(100, 100, duration = 1) 
    pyautogui.moveTo(100, 200, duration = 1) 
    pyautogui.moveTo(200, 100, duration = 1) 