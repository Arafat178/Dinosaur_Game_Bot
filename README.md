# Dinosaur Game Auto Player (Python + OpenCV)

This is a Python script that plays the Google Chrome Dino Game automatically. It uses screenshots, OpenCV image processing, and PyAutoGUI to detect obstacles in the game and jump over them without any manual input.

## Features

- Automatically opens the Chrome Dino game in the browser  
- Starts the game automatically by pressing the spacebar  
- Detects obstacles in a specific screen region using image processing  
- Jumps over obstacles by simulating spacebar key presses  
- Simple, lightweight, and easy to customize  

## Requirements

Make sure you have Python installed (preferably 3.8+), and install these required libraries with pip:

```bash
pip install opencv-python numpy pyautogui
```

## How to Run

1. Run the main script:

```bash
python Auto_Dinosaur.py
```

2. The script will:  
- Open the Dino game at https://chromedino.com/ automatically in your default browser  
- Wait for a few seconds to load  
- Start the game by pressing the spacebar(automatically)  
- Continuously monitor a specific region on the screen for obstacles  
- Press spacebar(automatically) to jump whenever an obstacle is detected  

## Customization

### Region of Interest (ROI)

Change the bounding box coordinates to fit your screen resolution and Dino's position. The variables represent `(x, y, width, height)`:

```python
x, y, w, h = 690, 330, 120, 60
```

### Threshold for Obstacle Detection

The script converts the screenshot region to grayscale and applies binary inverse thresholding with a value of 128:

```python
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
```

You might need to adjust this threshold value if obstacle detection is not accurate on your screen.

### Jump Condition

The script counts the number of white pixels in the thresholded image. If this count exceeds 50, it will simulate a jump by pressing the spacebar:

```python
if count > 50:
    pyautogui.press("space")
```

Adjust the count threshold according to obstacle size and your system's sensitivity.

## 📸 Demo

(demo video)(media/demo.gif)

## Notes

- This script depends heavily on screen resolution, browser zoom level, and Dino's exact position. You may need to tweak the ROI coordinates based on your setup.
- For best results, run the Dino game in Google Chrome with 100% zoom.
- The script does not include auto-adaptive features yet; it relies on fixed detection parameters.
