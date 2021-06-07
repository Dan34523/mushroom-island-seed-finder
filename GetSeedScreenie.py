import pyautogui
from pynput import keyboard
import os

check = True
cwd = os.getcwd()


def on_release(key):
    global check
    if key == keyboard.Key.esc:
        check = False
        return False


def seed_to_chunkbase(seed_to_enter):
    pyautogui.moveTo(850, 220)

    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(seed_to_enter, interval=0.01)
    pyautogui.moveRel(0, 5, duration=0.4)


def save_screenie(file_name):
    im = pyautogui.screenshot(region=(500, 340, 800, 521))
    im.save(cwd + f"\\Screenshots\\{file_name}.png")


listener = keyboard.Listener(
    on_release=on_release
)

listener.start()

pyautogui.moveTo(200, 540)
pyautogui.click()

with open("seeds.txt", "r") as f:
    seeds = [x[:-1] for x in f.readlines()]

for seed in seeds:
    if check:
        seed_to_chunkbase(seed)
        save_screenie(seed)
