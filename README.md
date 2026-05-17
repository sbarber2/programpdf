# programpdf

Automates capturing a series of screenshots of a browser-based slideshow and combines them into a PDF.

## Requirements

- Python 3.x
- macOS (uses `screencapture` under the hood)
- Screen Recording permission granted to your terminal app (System Settings → Privacy & Security → Screen Recording)
- Accessibility permission granted to your terminal app (System Settings → Privacy & Security → Accessibility)

## Setup

```bash
make init
```

Creates a `.venv` and installs dependencies.

## Usage

### 1. Find your capture region

```bash
make region
```

Press Enter, then move your mouse to the **upper-left** corner of the browser frame and wait. Repeat for the **lower-right** corner. Copy the printed `REGION = (...)` line into `screenshot_clicker.py`.

### 2. Configure the capture

Edit `screenshot_clicker.py` and set:

| Variable | Description |
|---|---|
| `REGION` | Screen region to capture (from `make region`) |
| `NUM_REPEATS` | Number of slides to capture |
| `DELAY_BETWEEN_STEPS` | Seconds to wait between screenshot and keypress |
| `DELAY_AFTER_CLICK` | Seconds to wait after keypress for slide to advance |

### 3. Capture screenshots

```bash
make capture
```

Switch to your browser within 3 seconds. The script will take a screenshot and press the right-arrow key to advance the slide, repeating `NUM_REPEATS` times. Screenshots are saved to `~/Downloads/screens/`.

### 4. Build the PDF

```bash
make pdf
```

Combines all `slide_*.png` files from `~/Downloads/screens/` into `~/Downloads/EncoreSpring2026Program.pdf`, in order.
