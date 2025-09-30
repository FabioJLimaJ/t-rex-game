import pyautogui as py
import keyboard

x, y, w, h = 757, 215, 60, 40

py.keyDown('alt')
py.press('tab')
py.keyUp('alt')

py.sleep(2)
py.press("space")
while True:
    img = py.screenshot(region=(x,y,w,h))

    pixels = img.getdata()
    if any(p[0] > 50 for p in pixels):
        py.press("space")
    if keyboard.is_pressed('Esc'):
        break
