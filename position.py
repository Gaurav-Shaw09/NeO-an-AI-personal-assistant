import pyautogui
import time

print("Move your mouse around. Press Ctrl+C to stop.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}  Y: {y}")
        time.sleep(0.1)  # updates every 0.1 sec
except KeyboardInterrupt:
    print("\nDone.")
