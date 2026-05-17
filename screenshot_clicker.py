#!/usr/bin/env python3
"""
Takes a screenshot, left-clicks the browser frame, and repeats 42 times.
Screenshots are saved to ~/Downloads/screens/
"""

import os
import time
import pyautogui

# --- Configuration ---
SAVE_DIR = os.path.expanduser("~/Downloads/screens")
CLICK_X = None   # Set to a specific X coordinate, or None to click screen center
CLICK_Y = None   # Set to a specific Y coordinate, or None to click screen center
DELAY_BETWEEN_STEPS = 1.5  # Seconds to wait between screenshot and click
DELAY_AFTER_CLICK = 2.0    # Seconds to wait after clicking (for page to advance)
NUM_REPEATS = 42
# Crop to browser window: (left, top, width, height) in pixels, or None for full screen
REGION = (891, 77, 530, 815)
# ---------------------

os.makedirs(SAVE_DIR, exist_ok=True)

screen_width, screen_height = pyautogui.size()
click_x = CLICK_X if CLICK_X is not None else screen_width // 2
click_y = CLICK_Y if CLICK_Y is not None else screen_height // 2

print(f"Saving screenshots to: {SAVE_DIR}")
print(f"Clicking at: ({click_x}, {click_y})")
print(f"Starting in 3 seconds — switch to your browser now!")
time.sleep(3)

for i in range(NUM_REPEATS):
    step = i + 1
    filename = os.path.join(SAVE_DIR, f"slide_{step:02d}.png")

    # Take screenshot
    screenshot = pyautogui.screenshot(region=REGION)
    screenshot.save(filename)
    print(f"[{step}/{NUM_REPEATS}] Saved: {filename}")

    time.sleep(DELAY_BETWEEN_STEPS)

    # Press right arrow to advance
    pyautogui.press('right')
    print(f"[{step}/{NUM_REPEATS}] Pressed right arrow")

    time.sleep(DELAY_AFTER_CLICK)

print(f"\nDone! {NUM_REPEATS} screenshots saved to {SAVE_DIR}")
