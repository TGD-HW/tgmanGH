## Overview {#common_UNIR_HALL_desc}
The TGZ servo amplifier in its ruggedized version (UNIR-RI) provides 3 high-speed inputs for Hall sensors on connector **X7** (pins 7, 9, 11).
These are electrically non-isolated inputs that are active-low. Therefore, the connected position sensor (most common application) with Hall sensors is active at 0V (shorts to GND if activated).

## Usage {#common_UNIR_HALL_usage}
For proper operation, an external power supply must be provided on pin 12 (VHI).
The voltage range for this supply is 5-30 VDC.
Power for the individual Hall sensors appears on pin 10 (VHO).
This voltage level is identical to that on pin 12 (VHI), but includes overcurrent and short-circuit protection.
The 0V (common) connection for the Hall sensors must be connected to pin 8 (HGND).
When the sensor is disconnected or its output is inactive, the supply voltage proportional to the external voltage (connected to VHI) will appear at the particular Hall input.

## Connection Example {#common_UNIR_HALL_schematic}
See the connection example in the "Connection Example" section for each corresponding TGZ device that supports this function.

![HallExample1](../img/UNIR_HALL_example1.webp){: style="width:40%;" }

!!! warning "Firmware"
	Ensure that you are using the correct firmware for the selected feedback type.