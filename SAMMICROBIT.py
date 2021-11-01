from microbit import *
import radio
import random


def pairing():
    radio.off()
    radio.on()
    while True:
        display.show(Image(
            "00000:"
            "00000:"
            "00000:"
            "00000:"
            "90000"))
        sleep(500)
        display.show(Image(
            "00000:"
            "00000:"
            "99000:"
            "00900:"
            "90900"))
        sleep(500)
        display.show(Image(
            "99900:"
            "00090:"
            "99009:"
            "00909:"
            "90909"))
        sleep(500)
        pairing = radio.receive()
        if pairing == 'working':
            radio.send('break')
            paired()
            break

            

def paired():
    display.clear()
    display.show(Image(
        "00000:"
        "00000:"
        "00000:"
        "90000:"
        "00000"))
    sleep(500)
    display.show(Image(
        "00000:"
        "00000:"
        "00000:"
        "90000:"
        "09000"))
    sleep(500)
    display.show(Image(
        "00000:"
        "00000:"
        "00000:"
        "90900:"
        "09000"))
    sleep(500)
    display.show(Image(
        "00000:"
        "00000:"
        "00090:"
        "90900:"
        "09000"))
    sleep(500)
    display.show(Image(
        "00000:"
        "00009:"
        "00090:"
        "90900:"
        "09000"))
    sleep(10000)
    recievernumber()

def recievernumber():
    radio.off()
    radio.on()
    display.clear()
    sleep(20000)
    number_receive = radio.receive();
    display.scroll(str(number_receive))
    sleep(10000)
    time_in_seconds = 60 * int(number_receive)
    display.scroll(time_in_seconds)
    sleep(2000)
    time_in_miliseconds = 1000 * int(time_in_seconds)
    display.scroll(time_in_miliseconds)
    sleep(2000)
    while True:
        if time_in_seconds == 0:
            radio.send('walk')
            walkingtime()
            break
        display.scroll(time_in_seconds)
        sleep(1000)
        time_in_seconds -= 1
    
    
    
def walkingtime():
    walking_time_steps = 2
    display.scroll("walk")
    sleep(5000)
    while True:
        if accelerometer.was_gesture('shake'):
            walking_time_steps -= 1
            display.scroll(str(walking_time_steps))
            sleep(2000)
        if walking_time_steps == 0:
            radio.send('walkoff')
            display.clear()
            display.show(Image(
                "00000:"
                "00000:"
                "00000:"
                "90000:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00000:"
                "00000:"
                "90000:"
                "09000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00000:"
                "00000:"
                "90900:"
                "09000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00000:"
                "00090:"
                "90900:"
                "09000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00009:"
                "00090:"
                "90900:"
                "09000"))
            sleep(5000)
            display.show(Image(
                "00000:"
                "00900:"
                "09990:"
                "00900:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "09990:"
                "09990:"
                "09990:"
                "00000"))
            sleep(500)
            display.show(Image(
                "90909:"
                "09990:"
                "99999:"
                "09990:"
                "90909"))
            sleep(5000)
            display.clear()
            break


def startup_screen():
    display.show(Image(
        "00000:"
        "00900:"
        "09990:"
        "00900:"
        "00000"))
    sleep(500)
    display.show(Image(
        "00000:"
        "09990:"
        "09990:"
        "09990:"
        "00000"))
    sleep(500)
    display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
    sleep(1000)
    pairing()
    display.clear()


startup_screen()