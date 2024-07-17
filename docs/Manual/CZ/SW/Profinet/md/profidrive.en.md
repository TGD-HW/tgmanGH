##PROFIdrive parameters

The TGZ servo drive supports parameter access through slots 1 and 2 (slot 2 for the variant with two axes only). Three record data object indexes can be used to access TGZ parameters:

- `47` – legacy record data. The axis is specified directly in the request header.
- `0xB02E` – local base parameters access. The axis is specified by the slot performing the access.
- `0xB02F` – global base parameters access. The axis is specified directly in the request header.

##Supported standard PROFIdrive PNUs

The TGZ servo drive supports the following standard and mandatory PROFIdrive parameters (PNUs):

| Number | Description | Data type |
|--------|-------------|-----------|
| 922    | Telegram selection | Unsigned16 |
| 930    | Operating mode | Unsigned16 |
| 944    | Fault message counter | Unsigned16 |
| 947    | Fault number | Array of Unsigned16 |
| 964    | Drive unit identification | Structure |
| 965    | Profile identification | Structure |
| 975    | Drive object identification | Structure |

##Reference values PNU

| Number | Description | Data type | TGZ register name | TGZ register number |
|--------|-------------|-----------|-------------------|---------------------|
| 2000   | Reference speed | Float32 | M-Nn | 0x2118, 0x2218 |
| 2001   | Reference voltage | Float32 | M-Un | 0x2117, 0x2217 |
| 2002   | Reference current | Float32 | M-In | 0x211B, 0x221B |
| 2003   | Reference torque | Float32 | M-Mn | 0x2119, 0x2219 |
| 2007   | Reference acceleration | Float32 | PG-PD_Acc | 0x395E, 0x3A5E |

##Additional PROFIdrive parameters

| Number | Description | Data type |
|--------|-------------|-----------|
| 2583   | Backlash compensation | Signed32 |

The parameter numbers from 2010 to 8191 are reserved for future firmware extensions. PNU 2583 is used for backlash compensation and is unique for each axis.

##TGZ registers

All TGZ registers are accessible as manufacturer-specific PROFIdrive registers, starting from number 0x2000 (8192 DEC). The list of usable registers can be downloaded from the TG Drives website. Parameters are grouped into categories such as common, motor, drive, profile generator, etc. Groups and parameters within groups are numbered starting from zero. For example, parameter number 0x2119 belongs to group 1 (Motor) with an index of 25 (0x19 = 25 DEC).

##PROFINET related parameters

TGZ parameter names and their corresponding PROFINET names and descriptions:

| TGZ parameter name | PROFINET name | Description | Number for axis 1 | Number for axis 2 |
|--------------------|---------------|-------------|-------------------|-------------------|
| PD_TelegramNumber  | Telegram selection (PNU922) | Selects telegram | 0x2321 | 0x2421 |
| PD_DisplayInfo     | -             | Displays debugging messages on TGZ GUI output | 0x2323 | N/A |
| PD_SetDataCounter  | -             | Counts cyclic PROFINET messages from I/O controller | 0x2324 | 0x2424 |
| PD_StatusWord_ZSW1 | Status word 1 (ZSW1) | Copy of PROFIdrive status word sent to I/O controller | 0x3500 | 0x3600 |
| PD_ControlWord_STW1| Control word 1 (STW1) | - | 0x3501 | 0x3601 |
| PD_SATZANW         | SATZANW       | Selects traversing block | 0x3503 | 0x3603 |
| PD_AKTSATZ         | AKTSATZ       | Actual traversing block | 0x3504 | 0x3604 |
| PD_State           | State diagram mode | State diagram mode | 0x3505 | 0x3605 |

TGZ supports up to 10 traversing blocks for independent use. Each block includes mode, acceleration, deceleration, velocity, and target position.

##PD_Task1

Parameters for PD_Task1:

| Name         | Description              | Number for axis 1 | Number for axis 2 |
|--------------|--------------------------|-------------------|-------------------|
| mod          | Mode (0 – relative, 1 – absolute) | 0x3922 | 0x3A22 |
| acc          | Acceleration             | 0x3923            | 0x3A23            |
| dec          | Deceleration             | 0x3924            | 0x3A24            |
| velocity     | Speed                    | 0x3925            | 0x3A25            |
| tarPosAngle  | Target position – angle  | 0x3926            | 0x3A26            |
| tarPosRevol  | Target position – revolutions | 0x3927         | 0x3A27            |

##PD_Task2 to PD_Task10

Parameters for PD_Task2 to PD_Task10 follow similar numbering patterns for axes 1 and 2.




