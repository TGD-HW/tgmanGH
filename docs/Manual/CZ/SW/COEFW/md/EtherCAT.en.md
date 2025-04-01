## Communication Setup {#ECATcommSettings}
The TGZ servo amplifier is capable of communicating with other fieldbus devices at speeds of 100 Mbit/s or 1 Gbit/s. While the 100 Mbit/s standard is supported by all EtherCAT devices and is mandatory, gigabit speed is designed for the future, and only a few devices currently support it. All EtherCAT slaves in the chain must use the same speed. The TGZ servo amplifier uses its register named `C-Enable_1G` to select the correct communication mode. Once the correct mode is selected, it is recommended to save the settings and restart the drive.

| Value | Description | Use |
|-------|-------------|-----|
| 0     | 100Mbit/s force full duplex | Default value for embedded EtherCAT masters |
| 1     | 1Gbit/s auto negotiation | For gigabit fieldbus, all devices (including the master) must use gigabit speed. |
| 2     | 100Mbit/s force half duplex (no MDI-X) | For testing or debugging |
| 3     | 100Mbit/s force full duplex (no MDI-X) | For testing or debugging |
| 4     | 100Mbit/s auto negotiation (no wires swap) | For testing or debugging |
| 5     | 100Mbit/s auto negotiation | Default value for PC-based EtherCAT masters |
| 6     | 100Mbit/s force half duplex (no wires swap) | For testing or debugging |
| 7     | 100Mbit/s force full duplex (no wires swap) | For testing or debugging |

### 100 Mbit/s Speed
The recommended value is 0 for embedded EtherCAT masters, or if the TGZ servo is not the first device in the fieldbus chain. It is necessary to use mode 5 for a PC master equipped with a gigabit-capable Ethernet card, at least for the first TGZ drive connected to the master. Other described modes are mainly used for testing or debugging, and the same mode must be set for all TGZ servo amplifiers in the fieldbus chain.

### 1 Gbit/s Speed
The only possible value is 1. Auto negotiation is mandatory for gigabit speed.

## EtherCAT Profile
The following table lists the most used EtherCAT registers. A detailed description of all registers can be found in the [EtherCAT documentation](https://www.ethercat.org/default.htm).

| Address | Byte Length | Description | Master Access | TGZ Access |
|---------|-------------|-------------|---------------|------------|
| 0x120   | 2           | AL Control   | rw            | ro         |
| 0x130   | 2           | AL Status    | ro            | rw         |
| 0x134   | 2           | AL Status Code | ro          | rw         |
| 0x220   | 2           | IRQ Event    | ro            | rw         |
| 0x600   | 16          | FMMU 0 (outputs) | rw         | ro         |
| 0x610   | 16          | FMMU 1 (inputs) | rw          | ro         |
| 0x800   | 8           | Sync Manager 0 (mailbox out) | rw | ro |
| 0x808   | 8           | Sync Manager 1 (mailbox in) | rw | ro |
| 0x810   | 8           | Sync Manager 2 (PDO out) | rw | ro |
| 0x818   | 8           | Sync Manager 3 (PDO in) | rw | ro |
| 0x1000  | 40 or 44    | PDO Out (set-points) | rw      | ro         |
| 0x1400  | 40 or 44    | PDO In (actual values) | ro      | rw         |
| 0x1800  | 16 or 32    | SDO Out (requests) | rw       | ro         |
| 0x1C00  | 16 or 32    | SDO In (responses from TGZ) | ro  | rw         |

## Node-ID
Both EtherCAT and CAN networks require a unique node identification number assigned to each device. TGZ uses the `C-ID` register for this purpose. The node identification can be read by the EtherCAT master:
- Configured station alias (address `0x12`) (only 8-bit Node-Id supported, i.e., values 1 – 255)
- By setting bit 5 (`0x20`) in the AL control, the Node-Id is copied to AL status code `0x134`.
- EEPROM area at word offset 4 also contains the Configured Station Alias value (full 16-bit value, i.e., values 1 – 65535).

!!! Note "Note"
    Node-Id cannot be zero.

## AL Control `0x120`
Supported AL control states are INIT (`0x01`), PRE-OPERATIONAL (`0x02`), SAFE-OPERATIONAL (`0x04`), OPERATIONAL (`0x08`). Additionally, bit 4 (acknowledgment) and bit 5 (device Node-Id request) are supported. The BOOTSTRAP (`0x03`) request is not supported.

## AL Status `0x130`

| Bit   | Description                                      |
|-------|--------------------------------------------------|
| 3:0   | Actual state of the device (0x01, 0x02, 0x04, 0x08) |
| 4     | Error indication                                |
| 5     | Device identification                           |

## AL Status Code `0x134`
Supported status codes:

| Value  | Description                                    |
|--------|------------------------------------------------|
| 0x0000 | No error                                       |
| 0x0011 | Invalid requested state change                 |
| 0x0012 | Unknown requested state                         |
| 0x0013 | Bootstrap not supported                         |
| 0x0016 | Invalid mailbox configuration (PRE-OP state)    |
| 0x001B | Sync manager watchdog                           |
| 0x001D | Invalid output configuration                    |
| 0x001E | Invalid input configuration                     |
