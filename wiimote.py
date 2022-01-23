# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# The following lines of code demonstrate many of the features realted to wiimotes, such as capturing button presses and rumbling the controller.
# I have managed to map the home button to the accelerometer - simply hold it and values will appear!

# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!

import cwiid, time

button_delay = 0.1

print('Please press buttons 1 + 2 on your Wiimote now ...')
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
    wii=cwiid.Wiimote()
except RuntimeError:
    print("Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!")
    quit()

print('Wiimote connection established!\n')


wii.rpt_mode = cwiid.RPT_BTN


def kitt():
    for i in range(4):
        wii.led = 2**i
        print(2**i)
        time.sleep(0.2)


    for i in range(3, -1, -1):
        wii.led = 2**i
        print(2**i)
        time.sleep(0.2)

    wii.led = 0


kitt()

print('Go ahead and press some buttons\n')
print('Press PLUS and MINUS together to disconnect and quit.\n')
time.sleep(3)


while True:

    buttons = wii.state['buttons']

    # Detects whether + and - are held down and if they are it quits the program
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        print('\nClosing connection ...')
        # NOTE: This is how you RUMBLE the Wiimote
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        exit(wii)

    # Detects whether A and B are held down and if they are, run kitt
    if (buttons - cwiid.BTN_A - cwiid.BTN_B == 0):
        kitt()

    # Detects whether A and Down are held down and if they are, run rumble
    if (buttons - cwiid.BTN_A - cwiid.BTN_DOWN == 0):
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0

    # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
    if (buttons & cwiid.BTN_LEFT):
        print('Left pressed')
        time.sleep(button_delay)

    if(buttons & cwiid.BTN_RIGHT):
        print('Right pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_UP):
        print('Up pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_DOWN):
        print('Down pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_1):
        print('Button 1 pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_2):
        print('Button 2 pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_A):
        print('Button A pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_B):
        print('Button B pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_HOME):
        wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        check = 0
        while check == 0:
            print(wii.state['acc'])
            time.sleep(0.01)
            check = (buttons & cwiid.BTN_HOME)
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_MINUS):
        print('Minus Button pressed')
        time.sleep(button_delay)

    if (buttons & cwiid.BTN_PLUS):
        print('Plus Button pressed')
        time.sleep(button_delay)
