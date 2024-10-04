import subprocess, sys, time, pyautogui

def click_on_popup(reference_image: str, reference_image2:str, retry_delay:int) -> None:
    '''
        Receives 2 reference images to locate in the screen based on a taken screenshot on the execution of the script

        reference_image and 2: image archive name -> 'example.png'
        retry_delay: time in seconds to start locating button -> 7 (Default)
    '''
    # Wait until you ope the pop up window
    time.sleep(retry_delay)

    # Take a screenshot to locate the button
    pyautogui.screenshot('screen.png')

    # try to locate the two reference image (buttons) 
    try:
        button_location = pyautogui.locateOnScreen(reference_image, minSearchTime=2)
    except:
        button_location = pyautogui.locateOnScreen(reference_image2, minSearchTime=2)

    # click the button and take the mouse to a safe position for the screenshot
    pyautogui.click(button_location, clicks=1,)
    pyautogui.moveTo(y=0)

def restart_script() -> None:
    '''
        Restart the script creating a new subprocess and killing the previous
    '''
    print("Restarting script...")
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()  # kill the current process

# fundamental variables
reference_image = 'reference_button.png'
reference_image2 = 'reference_button2.png'
retry_delay = 7

# run the script, if no button were found, then restart until find a new popup
while True:
    try:
        click_on_popup(reference_image, reference_image2, retry_delay)
    except:
        restart_script()
