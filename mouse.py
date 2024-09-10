import pyautogui
import time
import math

try:
    center_x = 960
    center_y = 540
    radius = 100
    angle = 0
    while True:
        # Calculate new coordinates
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        # Move mouse to the new coordinates
        pyautogui.moveTo(x, y)
        # Increment the angle
        angle = (angle + 10) % 360
        time.sleep(0.01)
except KeyboardInterrupt:
    print('\nDone')