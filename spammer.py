import pyautogui, time

time.sleep(5)

f = open("bee_movie.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
