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

Press Enter, then move your mouse to the **upper-left** corner of the browser frame and wait. Repeat for the **lower-right** corner. The script will print an `export SCREEN_REGION=...` command — run it to set your capture region.

### 2. Configure the capture

Set the `SCREEN_REGION` environment variable to the four values from the previous step:

```bash
export SCREEN_REGION="left,top,width,height"
```

Or pass it inline when capturing (see step 3). You can also edit `screenshot_clicker.py` directly to adjust:

| Variable | Description |
|---|---|
| `NUM_REPEATS` | Number of slides to capture |
| `DELAY_BETWEEN_STEPS` | Seconds to wait between screenshot and keypress |
| `DELAY_AFTER_CLICK` | Seconds to wait after keypress for slide to advance |

### 3. Capture screenshots

```bash
SCREEN_REGION="891,77,530,815" make capture
```

Or if you already exported `SCREEN_REGION`:

```bash
make capture
```

Switch to your browser within 3 seconds. The script will take a screenshot and press the right-arrow key to advance the slide, repeating `NUM_REPEATS` times. Screenshots are saved to `~/Downloads/screens/`.

### 4. Build the PDF

```bash
make pdf
```

Combines all `slide_*.png` files from `~/Downloads/screens/` into `~/Downloads/ProgramOutput.pdf`, in order.
