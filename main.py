import keyboard
import os
import webbrowser
from PIL import ImageGrab

# Configuration
HOTKEY = 'ctrl+shift+l'  # Set the hotkey to Ctrl+Shift+L
TEMP_IMAGE_PATH = "screenshot.png"

def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(TEMP_IMAGE_PATH)
        print(f"Screenshot saved to: {TEMP_IMAGE_PATH}")
        return True
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return False

def open_image_in_chrome():
    try:
        file_url = "file://" + os.path.abspath(TEMP_IMAGE_PATH)
        webbrowser.get('chrome').open_new_tab(file_url)
        print(f"Opened image in Chrome: {file_url}")
    except webbrowser.Error as e:
        print(f"Webbrowser Error: {e}")
        print("Make sure Chrome is installed and registered correctly.")
    except Exception as e:
        print(f"Other Error opening in Chrome: {e}")

def register_chrome_path():
    try:
        CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(CHROME_PATH))
        print(f"Chrome path registered manually: {CHROME_PATH}")
    except Exception as e:
        print(f"Error registering Chrome path: {e}")

def on_hotkey_pressed():
    print("Hotkey pressed!")
    if take_screenshot():
        open_image_in_chrome()

if __name__ == "__main__":
    register_chrome_path()

    keyboard.add_hotkey(HOTKEY, on_hotkey_pressed)  # Register the keyboard hotkey

    print(f"Script started. Press {HOTKEY} to take a screenshot and open it in Chrome.")
    keyboard.wait()  # Keep the script running