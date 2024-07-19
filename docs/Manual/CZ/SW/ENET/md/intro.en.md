The servo amplifier can be monitored and controlled via Ethernet UDP.
The Ethernet cable must be connected to the RJ45 connector "ETH3".
Supported speeds are 100 Mbps and 1,000 Mbps.   

The MAC address can be set by the user.   

All checksums (IP, UDP) must be valid, otherwise the packet will be ignored.   

The UDP port is fixed and set to `0x1F6`.
The IP address of the TGZ servo amplifier is static, the default is `192.168.1.200`   

The servo amplifier functions in communication as a *slave* (i.e. it responds only to requests).
Sends a response packet for each received packet in the correct format.
The master (PC) must always wait for a response from the servo amplifier before sending another query.
If the PC does not receive a response within the specified time, it may try to send another request.