</br>  
# The Take a Break Sensor - Micro:bit Radio Sensor

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [How does the micro:bit radio work?](#how-does-the-micro:bit-radio-work?)
* [Contact](#contact)

## General info
The Take a Break Sensor is the sensor which brings taking a break to a whole nother level.  
  
We created this project with the intent of solving a problem.  
The problem where workers behind their desks could not be able to work at their full potential because of them sitting behind their desks all day.

The way we solved this problem is by using the radio feature within the micro:bit's to unite two micro:bit's together to form an connection.
for a perfect amount of break time and for a more efficient work time.

    -Provide general information about your project here.
    -What problem does it (intend to) solve?
    -What is the purpose of your project?
    -Why did you undertake it?


## Technologies Used
Project is created with:
- Python 3.9.0
- Micro:bit version: V1 (V2 is also compatible)

## Features
List the ready features here:
- Exact amount of work time.
- Exact amount of break time.
- Exact amount of time before having to walk around.

## Setup
To run this project, you are going to need two Micro:bit V1 or Micro:bit V2's (combinations are compatible):

```
1 - Connect both of them to your computer.
2 - Download the Project.
3 - Open the microbit map on your file file explorer (you can find it at devices and drives).
4 - Put the KAANMIRCOBIT.py onto whichever microbit you'd like to become the sender.
5 - Put the SAMMICROBIT.py onto the other microbit to become the receiver.
6 - You are now ready to use the product.

7 - Turn on the microbit's within the reach of max 70 meters (max 230 feet).
8 - You will know that the product is working if the micro:bit's start to show a connecting animation on their screens.
9 - They will connect within 3 seconds of being turned on.
10 - You will know that they are working if they start to show anything besides the connecting animation.
11 - Enjoy.
```


## How does the micro:bit radio work?

### The radio module allows devices to work together via simple wireless networks.

### The radio module is conceptually very simple:

    - Broadcast messages are of a certain configurable length (up to 251 bytes).
    - Messages received are read from a queue of configurable size (the larger the queue the more RAM is used). If the queue is full, new messages are ignored. Reading a message removes it from the queue.
    - Messages are broadcast and received on a preselected channel (numbered 0-83).
    - Broadcasts are at a certain level of power - more power means more range.
    - Messages are filtered by address (like a house number) and group (like a named recipient at the specified address).
    - The rate of throughput can be one of three pre-determined settings.
    - Send and receive bytes to work with arbitrary data.
    - As a convenience for children, it’s easy to send and receive messages as strings.
    - The default configuration is both sensible and compatible with other platforms that target the BBC micro:bit.


## Contact
Created by [@unfinished](https://www.unfinishedd.nl)  
Created by [@KaanSecen](https://www.kaansecen.nl)  

- feel free to contact us!

This project is open source and available under the Take a Break Sensor License.