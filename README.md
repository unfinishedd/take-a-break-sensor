The Take a Break Sensor


Radio

The radio module allows devices to work together via simple wireless networks.

The radio module is conceptually very simple:

    Broadcast messages are of a certain configurable length (up to 251 bytes).
    Messages received are read from a queue of configurable size (the larger the queue the more RAM is used). If the queue is full, new messages are ignored. Reading a message removes it from the queue.
    Messages are broadcast and received on a preselected channel (numbered 0-83).
    Broadcasts are at a certain level of power - more power means more range.
    Messages are filtered by address (like a house number) and group (like a named recipient at the specified address).
    The rate of throughput can be one of three pre-determined settings.
    Send and receive bytes to work with arbitrary data.
    Use receive_full to obtain full details about an incoming message: the data, receiving signal strength, and a microsecond timestamp when the message arrived.
    As a convenience for children, it’s easy to send and receive messages as strings.
    The default configuration is both sensible and compatible with other platforms that target the BBC micro:bit.