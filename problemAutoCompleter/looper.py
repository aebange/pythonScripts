#######################################################################
# Filename:  looper.py
# Author:    Alex Bange
#######################################################################
# Purpose:
#   To identify the coordinates of the mouse cursor on screen in realtime
#
# Usage
#   DOS> python looper.py
#
# Assumptions
#   A) The user has the pyautogui module installed.
#######################################################################

import time
import pyautogui
import os

while True:
	mouse_pos = pyautogui.position()
	print(mouse_pos)
	time.sleep(1)
	os.system("cls")
