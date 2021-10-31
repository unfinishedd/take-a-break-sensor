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
        radio.send('working')
        if pairing == 'tyfus':
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
    sendnumber()

def sendnumber():
    display.clear()
    random_number = random.randint(1, 2)
    display.show(Image(
        "09990:"
        "90909:"
        "99909:"
        "90009:"
        "09990"))
    sleep(5000)
    display.scroll(str(random_number) + "M")
    sleep(10000)
    radio.send(str(random_number))
    timerrunout()
    

def timerrunout():
    radio.off()
    radio.on()
    while True:
        walking_time = radio.receive();
        if walking_time == "walk":
            walkingtime()
            break
        
def walkingtime():
    radio.off()
    radio.on()
    walking_time_steps = 2
    display.scroll("walk")
    sleep(5000)
    while True:
        walkingoff_time = radio.receive();
        if walkingoff_time == "walkoff":
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