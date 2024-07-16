##Technical Specification
The TGZ servo amplifier uses PROFIdrive Profile according to the above-mentioned technical specification: 

- Application Class 1 (*Standard Drive* – speed regulator)
- Application Class 3 (Single Axis positioning drive, with local *Motion Control* – position regulator).

Several PROFIdrive telegrams are available for use with the PLC for controlling the TGZ:

- Standard telegram 1 – n-setpoint interface, 16 bits
- Standard telegram 3 – n-setpoint interface, 32 bits, with one sensor
- Standard telegram 7 – positioning interface
- Standard telegram 9 – positioning interface plus MDI submode
- Telegram 111 – SinaPos basic positioner
- Telegram 352 – extended telegram 1 with additional status information

For detailed description of the telegrams see the appropriate documentation.   

According to the PROFINET specification, the TGZ servo drive supports the Conformance Class A.
The PROFIdrive parameters can be read and written over PROFINET network, as well as cyclic data.
Synchronization between devices is done only through PLC within the cycle time of RT data.
For the two axes servo drive variant, exact synchronization (electronic gearing) inside one TGZ is also possible.

##Cycle Time of RT Data
TGZ fastest cycle time for the PROFINET RT data is 1 ms (firmware from August 2022 or newer).
The maximal response jitter is 250 µs.

##TGZ-S-48-xxx Servo Type
This version has special firmware handling: due to similarity of the TGZ-D version, it must be programmed with the firmware designated for TGZ-D variant.
Therefore, it is necessary to use also the `GSDML` file named `GSDML-V2.4-TGDrives-TGZ-D-xxxxxxxx.xml`, i.e., the file for the double axis variant.
During the drive commissioning, only the first axis can be used.
The second axis remains always in an error.

