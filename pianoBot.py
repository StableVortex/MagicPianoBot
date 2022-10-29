# First bot - MagicPianoBot
# website - https://www.agame.com/game/magic-piano-tiles
# Environment: MacOS

import pyautogui
from pyautogui import *

import keyboard

# fourth column X:  850 Y:  400 RGB: (NaN, NaN, NaN)
# third  column X:  780 Y:  400 RGB: (NaN, NaN, NaN)
# second column X:  700 Y:  400 RGB: (NaN, NaN, NaN)
# first  column X:  595 Y:  400 RGB: (NaN, NaN, NaN)

sleep(1)
while not keyboard.is_pressed("esc"):
    if pyautogui.pixel(595, 400)[0] == 0:
        pyautogui.moveTo(595, 500)
        pyautogui.dragTo(button='left')
    if pyautogui.pixel(700, 400)[0] == 0:
        pyautogui.moveTo(700, 500)
        pyautogui.dragTo(button='left')
    if pyautogui.pixel(780, 400)[0] == 0:
        pyautogui.moveTo(780, 500)
        pyautogui.dragTo(button='left')
    if pyautogui.pixel(850, 400)[0] == 0:
        pyautogui.moveTo(850, 500)
        pyautogui.dragTo(button='left')
