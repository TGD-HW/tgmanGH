##Basic Description {#commonFB12}
The TGZ servo amplifier includes feedback circuits for axis 1 and axis 2 on the **X6** and **X7** connectors in the standard (UNI) version.
It is possible to connect Endat, SSI, BISS, incremental encoder feedback and, after applying the FBSELx jumper, also Hiperface DSL.   

A simplified internal wiring diagram is shown in the figure below.

![Simplified TGZ FB12 schematic](../img/FB12internals.svg){: style="width:80%;" }

These are 2 very fast RS485 bus drivers capable of operating at data rates up to 20 Mbit/s.

!!! note "Cable length"
	The maximum baud rate decreases with the length of the feedback cable.
	To increase the interference immunity of the device, make sure to use the original cable of the appropriate length.
	An unnecessarily long cable (spare loop/cable) may cause a reduction in the device's EMI immunity.

Each RS485 line is internally symmetrically terminated with a 112 Ω resistor.
In addition, there is a common mode choke for greater immunity to the EMI.
The X6 and X7 connector is represented by pins 1-8 in the schematic.   

In case of a Hiperface DSL feedback, pins 1-3 and 2-4 need to be connected together. 
This will connect the RS_485_2 signal to the line power output circuit.
Then just connect a suitable Hiperface DSL position sensor at pins 7-8.

!!! warning "Firmware"
	Make sure that you use the correct firmware for the selected feedback type.
	Contact your supplier for further details.