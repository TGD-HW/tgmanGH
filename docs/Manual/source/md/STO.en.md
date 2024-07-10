##Safe Torque Off (STO)
The STO function is a basic safety function integrated in the servo amplifier.
It ensures that no torque-generating energy can continue to act on the engine in the event of an emergency and at the same time prevents unintentional starting.
The input terminals for STO are part of the connector X1, through which the power supply of the control part and the motor brake is also realized.
For correct electrical connection of the servo amplifier, it is necessary to apply +24 V DC to the inputs STO A and STO B.
If the power supply is disconnected from the STO A or STO B input, the power supply to the motor will be interrupted immediately and will no longer be below torque.
If the motor is in motion, the motor will turn to a standstill due to inertial forces.

![STO connection](../../../../source/img/STOpins.png){: style="width:15%;" }

It is possible to connect a user safety system to the STO A and STO B inputs depending on the specific application and customer needs.
After equipping the STO protection, it is necessary to perform a system reset and re-enable SW ENABLE.
STO protection is redundant and is characterized by a high degree of reliability.

![STO schematic](../../../../source/img/STOschematic.png){: style="width:80%;" }

!!! info "STO norm"
	System STO meets the requirements on safety level integrity SIL3 according to the standards ČSN EN 61508-1 ed.2, ČSN EN 61508-2 ed.2, ČSN EN 61508-6 ed.2 and performance level with high demand PLe according to the standard ČSN EN ISO 13849-1.

