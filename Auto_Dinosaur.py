import cv2
import numpy as np
import pyautogui
import time
import webbrowser

webbrowser.open("https://chromedino.com/")

time.sleep(5)

pyautogui.press("space")
print("Game Started...")

x, y, w, h = 690, 330, 120, 60 # intial points x,y and w,h width and height

while True:
    # Screenshot
    img = pyautogui.screenshot(region=(x, y, w, h))

    # Numpy array এ convert
    frame = np.array(img)
    # Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Binary threshold
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    # Count obstacle pixels
    count = cv2.countNonZero(thresh)
    if count > 50:
        pyautogui.press("space")
        print("Jump!")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
