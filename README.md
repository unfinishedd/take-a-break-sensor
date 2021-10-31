# The Take a Break Sensor

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Extra info](#radio)

## General info
The Take a Break Sensor is the sensor which brings taking a break to a whole nother level. 
The way 

## Technologies
Project is created with:
* Python
* Micro:bit version: V1 (V2 is also compatible)

## Setup
To run this project, you are going to need two Micro:bit V1 or Micro:bit V2's:

```
* Connect both of them to the computer.
* Download the Project.
* Open the microbit map on your file file explorer (you can find it at devices and drives).
* Put the KAANMIRCOBIT.py onto whichever microbit you'd like to become the sender.
* Put the SAMMICROBIT.py onto the other microbit to become the receiver.
* You are now ready to use the product.
* Enjoy.
```


## Radio

### The radio module allows devices to work together via simple wireless networks.

### The radio module is conceptually very simple:

    * Broadcast messages are of a certain configurable length (up to 251 bytes).
    * Messages received are read from a queue of configurable size (the larger the queue the more RAM is used). If the queue is full, new messages are ignored. Reading a message removes it from the queue.
    * Messages are broadcast and received on a preselected channel (numbered 0-83).
    * Broadcasts are at a certain level of power - more power means more range.
    * Messages are filtered by address (like a house number) and group (like a named recipient at the specified address).
    * The rate of throughput can be one of three pre-determined settings.
    * Send and receive bytes to work with arbitrary data.
    * Use receive_full to obtain full details about an incoming message: the data, receiving signal strength, and a microsecond timestamp when the message arrived.
    * As a convenience for children, it’s easy to send and receive messages as strings.
    * The default configuration is both sensible and compatible with other platforms that target the BBC micro:bit.
