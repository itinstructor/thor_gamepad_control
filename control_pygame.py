from my_serial import read_thread
from thor import Thor
from threading import Thread
import pygame
from time import sleep

pygame.init()
pygame.joystick.init()
if not pygame.joystick.get_count():
    print("No Gamepad!")
    exit(1)
pygame.joystick.Joystick(0)

thor = Thor()

read_thread.start()  # run the serial listener in a separate thread
while read_thread.is_alive():
    try:
        sleep(0.01)
        _ = pygame.joystick.Joystick(0)
        event = pygame.event.get()
    except KeyboardInterrupt:
        break
    if not event:
        continue
    ev = event[0]
    t = ev.type
    if t == 1540 or (t == 1538 and ev.value == (0, 0)):
        thor.event = ""
        continue
    btn = None
    if t == 1539:
        btn = ev.button
    if t == 1538:
        btn = ev.value
    if btn is None:
        continue
    else:
        thor.event = str(btn)
    match btn:
        # the moving functions run in separate threads to be able to stop on unpressed key
        case 6:
            Thread(target=thor.open_claw).start()
        case 4:
            Thread(target=thor.close_claw).start()
        case (1, 0):
            Thread(target=thor.rotate_claw).start()
        case (-1, 0):
            Thread(target=thor.rotate_claw_cw).start()
        case (0, -1):
            Thread(target=thor.move_claw_b).start()
        case (0, 1):
            Thread(target=thor.move_claw).start()
        case 1:
            Thread(target=thor.art_4).start()
        case 3:
            Thread(target=thor.art_4_cw).start()
        case 2:
            Thread(target=thor.art_3_b).start()
        case 0:
            Thread(target=thor.art_3).start()
        case 5:
            Thread(target=thor.art_2_b).start()
        case 7:
            Thread(target=thor.art_2).start()
        case 10:
            Thread(target=thor.art_1).start()
        case 11:
            Thread(target=thor.art_1_cw).start()
        case 9:
            Thread(target=thor.home).start()
