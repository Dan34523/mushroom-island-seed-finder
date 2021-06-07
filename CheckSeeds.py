import pyautogui
from pynput import keyboard
from tkinter import Tk
import time

check = True


def on_release(key):
    global check
    if key == keyboard.Key.esc:
        check = False
        return False


# 5 scrolls down
# Random at 1060, 220
# Seed box at 850 220

def new_seed():
    pyautogui.moveTo(1060, 220)
    pyautogui.click()
    time.sleep(0.1)


def save_seed():
    pyautogui.moveTo(850, 220)

    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')

    pyautogui.hotkey('ctrl', 'c')
    with open("seeds.txt", "a") as seeds:
        seeds.write(f"{Tk().clipboard_get()}\n")


def check_seed():
    im = pyautogui.screenshot(region=(810, 491, 255, 255))
    for x in range(255):
        for y in range(255):
            if im.getpixel((x, y)) == (255, 0, 255):
                save_seed()
                return


listener = keyboard.Listener(
    on_release=on_release
)

listener.start()

pyautogui.moveTo(200, 540)
pyautogui.click()

for _ in range(5000):
    if check:
        check_seed()
        new_seed()
