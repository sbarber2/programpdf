#!/usr/bin/env python3
"""Prompt the user to position their mouse at each corner of the capture region."""

import time
import pyautogui

SETTLE_SECONDS = 3  # time after Enter to move mouse to target corner

print("=== Region Finder ===")
print(f"\nPress Enter, then move your mouse to the UPPER-LEFT corner ({SETTLE_SECONDS}s to position)...")
input()
time.sleep(SETTLE_SECONDS)
x1, y1 = pyautogui.position()
print(f"  Upper-left: ({x1}, {y1})")

print(f"\nPress Enter, then move your mouse to the LOWER-RIGHT corner ({SETTLE_SECONDS}s to position)...")
input()
time.sleep(SETTLE_SECONDS)
x2, y2 = pyautogui.position()
print(f"  Lower-right: ({x2}, {y2})")

left = min(x1, x2)
top = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)

print(f"\nRun this to set your capture region:")
print(f"  export SCREEN_REGION=\"{left},{top},{width},{height}\"")
