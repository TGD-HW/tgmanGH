## Technical Specification

The TGZ servo amplifier uses PROFIdrive Profile according to the above-mentioned technical specification: 

- Application Class 1 (*Standard Drive* – speed regulator)
- Application Class 3 (Single Axis positioning drive, with local *Motion Control* – position regulator).

Several PROFIdrive telegrams are available for use with the PLC for controlling the TGZ:

- Standard telegram 1 – n-setpoint interface, 16 bits
- Standard telegram 3 – n-setpoint interface, 32 bits, with one sensor (standard firmware only)
- Standard telegram 7 – positioning interface
- Standard telegram 9 – positioning interface plus MDI submode
- Telegram 102 – extended telegram 1 with additional status information (PROFIsafe firmware only)
- Telegram 111 – SinaPos basic positioner
- Telegram 352 – extended telegram 1 with additional status information

PROFIsafe firmware version also supports the following telegrams for both axes:

- Standard PROFIsafe telegram 36 - reading safe position from safety encoder
- Standard PROFIsafe telegram 31 - control safety functions, supported by TIA portal library

For detailed description of the telegrams see the appropriate documentation.

!!! warning "Warning"
    **The PROFIdrive telegrams must be selected using TGZ_GUI application. When changed, the TGZ must be restarted. It is important that the PLC has already the right telegrams selected in the project and it is running before the TGZ is restarted, otherwise the drive will not be able to establish communication with the PLC and will not work. This behaviour is important only when the telegrams are changed, otherwise the power up order of PLC and TGZ does not matter.**

According to the PROFINET specification, the TGZ servo drive supports the Conformance Class A.
The PROFIdrive parameters can be read and written over PROFINET network, as well as cyclic data.
Synchronization between devices is done only through PLC within the cycle time of RT data.
For the two axes servo drive variant, exact synchronization (electronic gearing) inside one TGZ is also possible.

## Cycle Time of RT Data

TGZ fastest cycle time for the PROFINET RT data is 1 ms (firmware from August 2022 or newer).
The maximal response jitter is 250 µs.

## New PROFIsafe firmware

The newest PROFsafe firmware uses just one GSDML file (`GSDML-V2.44-TGDrives-TGZ-F-xxxxxxxx.xml`) for both TGZ variants (TGZ-D and TGZ-S).


