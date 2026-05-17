#!/usr/bin/env python3
"""Combine slide_*.png files from ~/Downloads/screens into a single PDF."""

import glob
import os
import img2pdf

files = sorted(glob.glob(os.path.expanduser("~/Downloads/screens/slide_*.png")))
output = os.path.expanduser("~/Downloads/EncoreSpring2026Program.pdf")

with open(output, "wb") as f:
    f.write(img2pdf.convert(files))

print(f"Done: {output} ({len(files)} pages)")
