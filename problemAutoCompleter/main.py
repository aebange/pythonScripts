#######################################################################
# Filename:  main.py
# Author:    Alex Bange
#######################################################################
# Purpose:
#   To automatically complete online course assignments
#
# Usage
#   DOS> python main.py
#
# Assumptions
#   A) The application has a "check work" button allowing for the user to see if their answer is correct
#   B) The check work button has unlimited uses
#   C) The check work button allows for the user to change back into work mode
#   D) The questions are always multiple choice
#   E) The questions are always at the bottom of the page
#   F) The questions are always displayed in a definable range of coordinates
#   G) There is a button to move on to the next question
#   H) The user has taken screenshots of all scannable buttons and has placed them into the images folder
#   I) The user has adjusted the test coordinates to match the range of multiple choice questions on their screen
#   J) The check work button provides a clear method of identifying whether an answer is false or correct
#   K) The user has the pyautogui and opencv2 modules installed.
#######################################################################
import os
import sys
import time
import pyautogui
import cv2

# The X/Y Coordinates of where the mouse will move to before attempting to scroll
scrollTargetX = 1483
scrollTargetY = 457

# The locations that the program will click on the screen while looking for menu options
Test1 = (1307, 256, 10, 10)
Test2 = (1307, 325, 10, 10)
Test3 = (1307, 394, 10, 10)
Test4 = (1307, 463, 10, 10)
Test5 = (1307, 532, 10, 10)
Test6 = (1307, 601, 10, 10)
Test7 = (1307, 670, 10, 10)
Test8 = (1307, 739, 10, 10)
Test9 = (1307, 808, 10, 10)
Test10 = (1307, 887, 10, 10)
Test11 = (1307, 947, 10, 10)

# The name of the folder being used to contain any referenced image files
image_folder = os.getcwd() + "\\images"

# The names of image files that will be called to identify symbols and buttons
RedX = image_folder + "RedX.png"
GreenC = image_folder + "GreenCheck.png"
CheckMW = image_folder + "CheckMW.png"
ReturnTQ = image_folder + "ReturnTQ.png"
NextB = (1156,998,1,1)

rangeX = 1307
rangeYMin = 256
rangeYMax = 947
rangeFiller = 10
testAmt = 16

def buildTests():
    i = 0
    x = 0
    range_y_current = rangeYMax
    test_dict = {}
    range_difference = rangeYMin - rangeYMax
    range_distribution = range_difference / testAmt
    while i < testAmt:
        current_test = (rangeX,range_y_current,rangeFiller,rangeFiller)
        test_dict[i] = current_test
        range_y_current += range_distribution
        i += 1
    print("Created %s" % test_dict)
    return test_dict


def scroll():
    pyautogui.moveTo(scrollTargetX,scrollTargetY)
    pyautogui.vscroll(-1000000000)
    pyautogui.vscroll(-1000000000)
    pyautogui.vscroll(-1000000000)
    pyautogui.vscroll(-1000000000)
    pyautogui.vscroll(-1000000000)
    pyautogui.vscroll(-1000000000)
    print("Successfully scrolled -6000000000 clicks.")


def testAnswers():
    while True:
        option_list_count = -1
        time.sleep(.4)
        check_work_location = pyautogui.locateOnScreen(CheckMW, confidence = .99)
        if check_work_location == None:
            check_rtq_location = pyautogui.locateOnScreen(ReturnTQ, confidence=.99)
            if check_rtq_location == None:
                print("Step 1. Check work location not found, operation impossible.")
                return False
            else:
                check_rtq_location_x, check_rtq_location_y = pyautogui.center(check_rtq_location)
                time.sleep(.3)
                pyautogui.click(check_rtq_location_x, check_rtq_location_y)
                pyautogui.moveTo(1483,457)
                print("Step 1. Check work location blocked by current check, corrected.")
                time.sleep(2)
        else:
            print("Step 1. Check work location found, operation possible.")
            while True:
                option_list_count += 1
                print("Step 2. Clicking on logged location of image %s" % option_list_count)
                temp_location = optionList[option_list_count]
                temp_button_x, temp_button_y = pyautogui.center(temp_location)
                time.sleep(.3)
                pyautogui.click(temp_button_x, temp_button_y)
                print("Step 3. Enabling check work mode.")
                time.sleep(.2)
                check_mw_location = pyautogui.locateOnScreen(CheckMW, confidence=.99999)
                if check_mw_location == None:
                    print("Test did not hit any buttons, skipping to next test.")
                else:
                    check_mw_location_x, check_mw_location_y = pyautogui.center(check_mw_location)
                    pyautogui.center(check_work_location)
                    pyautogui.click(check_mw_location_x, check_mw_location_y)
                    print("Step 4. Testing correctness of option image %s" % option_list_count)
                    time.sleep(.2)
                    temp_location2 = pyautogui.locateOnScreen(GreenC, confidence=.8)
                    if temp_location2 == None:
                        print("Step 4. Option image is false! Checking next option.")
                        print("Step 5. Returning to question view mode.")
                        time.sleep(.3)
                        check_rtq_location = pyautogui.locateOnScreen(ReturnTQ, confidence=.99)
                        check_rtq_location_x, check_rtq_location_y = pyautogui.center(check_rtq_location)
                        time.sleep(.3)
                        pyautogui.click(check_rtq_location_x, check_rtq_location_y)
                    else:
                        print("Step 4. Option image is correct!")
                        correct_answer = option_list_count
                        print("Step 5. Returning to question view mode.")
                        time.sleep(.3)
                        check_rtq_location = pyautogui.locateOnScreen(ReturnTQ, confidence=.99)
                        check_rtq_location_x, check_rtq_location_y = pyautogui.center(check_rtq_location)
                        time.sleep(.3)
                        pyautogui.click(check_rtq_location_x, check_rtq_location_y)
                        return correct_answer


def submitAnswer():
    # Locate and click on the next button to go to the next problem and restart the cycle.
    check_next_location = NextB
    check_next_location_x, check_next_location_y = pyautogui.center(check_next_location)
    time.sleep(.3)
    pyautogui.click((check_next_location_x, check_next_location_y))


# Depending on your program, pyautogui can "go rogue".
# To force stop programs, move the mouse to the top left corner of the screen to halt.
pyautogui.FAILSAFE = True

# The location of the mouse cursor is provided as an x,y pair
# This value of x and y is determined by the resolution of the monitor
gsScriptName = os.path.basename(__file__)

# Print the date/time when this script started
print("%s has started as of %s." % (gsScriptName, time.strftime("%c")))

print("Press enter to start.")
z = input()

while True:
    print("Generating test coords.")
    optionList = buildTests()
    print("Scrolling")
    scroll()
    print("Starting answer test")
    correctAnswer = testAnswers()
    print("Correct answer colected.")
    print("Submitting answer and clearing screen...")
    time.sleep(1)
    submitAnswer()
    os.system("cls")

# Print the date/time when this script finished
print("%s has finished as of %s." % (gsScriptName, time.strftime("%c")))

# Python script ends here
sys.exit(0)

