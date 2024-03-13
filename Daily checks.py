import pyautogui
import os
import subprocess
import time
import webbrowser
import code
def open_url(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Error: {e}")

# Specify the URL you want to open
url_to_open = "https://docs.google.com/spreadsheets/d/1PKlFJszpv9pvN8ZdVmEZGCWRMbYptrdF/edit?usp=drive_link&ouid=118424839536083389510&rtpof=true&sd=true"  # Replace with the actual URL

# Call the function to open the URL
open_url(url_to_open)

time.sleep(5)

# Delay before starting to allow time to switch to the browser window
time.sleep(5)

# Copy the name 
pyautogui.click(719, 416, clicks=1,button='left' )
pyautogui.hotkey('ctrl', 'c')  # copy the name
time.sleep(5)

def open_application(application_path):
    try:
        # Open the application using subprocess
        subprocess.Popen(application_path, shell=True)

        # Wait for the application to open (you may need to adjust the delay)
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")

# Specify the path to the application you want to open
application_path = r"C:\Program Files (x86)\Splashtop\Splashtop Remote\Client for STB\strwinclt.exe"  # Replace with the actual path

# Call the function to open the application
open_application(application_path)

time.sleep(10)
# Paste the name 
pyautogui.click(969, 110, clicks=1,button='left' )
pyautogui.hotkey('ctrl', 'v')  # copy the name
time.sleep(5)

#Doubleclick the Name
pyautogui.click(1044, 257, clicks=2,button='left' )
time.sleep(5)

#Blank the screen
pyautogui.click(956, 67, clicks=1,button='left' )
time.sleep(5)
pyautogui.click(1039, 84, clicks=1,button='left' )
time.sleep(2)

#Services start
pyautogui.hotkey('win', 'r')
time.sleep(5)

# Type the text using the write function
pyautogui.write("services.msc")
# Press Enter to simulate pressing the Enter key
pyautogui.press("enter")
