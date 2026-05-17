#!/usr/bin/env python3
"""Prompt the user to position their mouse at each corner of the capture region."""

import pyautogui

print("=== Region Finder ===")
print("\nMove your mouse to the UPPER-LEFT corner of the region, then press Enter...")
input()
x1, y1 = pyautogui.position()
print(f"  Upper-left: ({x1}, {y1})")

print("\nMove your mouse to the LOWER-RIGHT corner of the region, then press Enter...")
input()
x2, y2 = pyautogui.position()
print(f"  Lower-right: ({x2}, {y2})")

left = min(x1, x2)
top = min(y1, y2)
width = abs(x2 - x1)
height = abs(y2 - y1)

print(f"\nSet this in screenshot_clicker.py:")
print(f"  REGION = ({left}, {top}, {width}, {height})")
