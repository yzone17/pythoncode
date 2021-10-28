
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.scroll('Yehudi.Rudge')
    else:
        display.show(Image.SAD)

from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.SILLY)
        sleep(2000)
    if accelerometer.was_gesture('face up'):
        display.show(Image.HAPPY)
    if accelerometer.was_gesture('left'):
        display.show('<')
    if accelerometer.was_gesture('right'):
        display.show('>')

display.clear()

from microbit import *

while True:
    if display.read_light_level() > 100:
        display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
    else:
        display.clear()