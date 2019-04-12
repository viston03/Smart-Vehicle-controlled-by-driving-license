
import lcddriver
import time

def lcd(str, p):

    # Load the driver and set it to "display"
    # If you use something from the driver library use the "display." prefix first
    display = lcddriver.lcd()
    count = 0
    # Main body of code
    try:
        while count<1:
            # Remember that your sentences can only be 16 characters long!
            #print("Writing to display")
            display.lcd_display_string(str, p) # Write line of text to first line of display
            display.lcd_display_string(str, p) # Write line of text to second line of display
            #time.sleep(2)                                     # Give time for the message to be read
            display.lcd_display_string(str, p)
            display.lcd_display_string(str, p)  # Refresh the first line of display with a different message
            time.sleep(3)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            #time.sleep(2)                                     # Give time for the message to be read
            display.backlight(1)
            count += 1
    except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()
    
