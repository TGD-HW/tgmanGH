The EtherCAT network is connected using the X13 (Fieldbus IN) connector and X12 (Fieldbus OUT) connector.
Use the IN connector in the direction to the EtherCAT master and the OUT connector to connect other EtherCAT devices in the chain.
The standard speed is 100Mbit/s, there is also possibility to use 1Gbit/s connection, and in that case all the devices (including the master) must use gigabit speed.
Use the `C-Enable_1G` register for selecting desired communication speed, see. [EtherCAT settings](EtherCAT.md#ECATcommSettings).
See chapter Communication setup below for more detailed description.   

When connecting the EtherCAT network cables, the **supply of the equipment must be switched off**.   

The CAN bus is connected by the X10 connector.
There is no 120Ω terminating resistor.
TGZ servo amplifier supports all the standard CAN bus speeds: 10, 20, 50, 100, 125, 250, 500, 800 and 1000 Kbit/s.
The speed is selected by CAN_BaudRate register using TGZ_GUI service program.   

Only professional staff member with a sufficient knowledge of drive technology is allowed to setup the TGZ servo amplifier.
All the electrical connections must be done in conformance with the [TGZ HW user's manual](../../../../CZ/TGZ/TGZ-D-48-13_26/md/mark.md).