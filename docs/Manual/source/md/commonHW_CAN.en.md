##Basic Description {#commonCAN}
The TGZ servo amplifier includes full-featured galvanically isolated CAN bus circuitry with internal isolated power supply on the **X10** connector in the standard (UNI) design.
The bus is more resistant due to the isolation.
It is possible to connect the CANGND (pin 3) to other devices on the bus and thus maintain the same potential between them (recommended).
The device does not contain any internal termination resistor.
If it is necessary to terminate the line, an external resistor must be used. 
One possible method is to press a 120R resistor of size 0207 into the common ferrule on the CANH and CANL pins (1 and 2, respectively).

## Cabling
We recommend using a cable with a characteristic impedance of 100 - 120 Ω.
The maximum possible cable length decreases as the required bus baud rate increases.
All standard CAN bus speeds are supported: 10, 20, 50, 100, 125, 250, 500, 800 and 1000 Kbit/s.
The baud rate is selected using the `CAN_BaudRate` register in the service program [TGZ GUI](../../CZ/TGZ/TGZ_SW/GUI/md/parameters.md#GUIbasicParams).