All the elements in the object dictionary can be accessed by either EtherCAT or by CAN.

## CANopen Communication Objects

The following standard objects are supported. Some of the objects are common for CAN and EtherCAT communication, others are used only in CAN or EtherCAT (CoE) communication.

| Index  | Name                                | Access | Used in | CAN PDO Mapping |
|--------|-------------------------------------|--------|---------|-----------------|
| 0x1000 | device type                         | ro     | CoE/CAN | No              |
| 0x1001 | error register                      | ro     | CoE/CAN | TPDO            |
| 0x1003 | pre-defined error field             | ro     | CoE/CAN | No              |
| 0x1010 | store parameters                    | rw     | CoE/CAN | No              |
| 0x1011 | restore default parameters          | rw     | CoE/CAN | No              |
| 0x1018 | identity object                     | ro     | CoE/CAN | No              |
| 0x1400 | 1st RPDO communication parameter    | rw     | CAN     | No              |
| 0x1401 | 2nd RPDO communication parameter    | rw     | CAN     | No              |
| 0x1402 | 3rd RPDO communication parameter    | rw     | CAN     | No              |
| 0x1403 | 4th RPDO communication parameter    | rw     | CAN     | No              |
| 0x1600 | 1st RPDO mapping parameter          | rw     | CAN     | No              |
| 0x1601 | 2nd RPDO mapping parameter          | rw     | CAN     | No              |
| 0x1602 | 3rd RPDO mapping parameter          | rw     | CAN     | No              |
| 0x1603 | 4th RPDO mapping parameter          | rw     | CAN     | No              |
| 0x1800 | 1st TPDO communication parameter    | rw     | CAN     | No              |
| 0x1801 | 2nd TPDO communication parameter    | rw     | CAN     | No              |
| 0x1802 | 3rd TPDO communication parameter    | rw     | CAN     | No              |
| 0x1803 | 4th TPDO communication parameter    | rw     | CAN     | No              |
| 0x1A00 | 1st TPDO mapping parameter          | rw     | CAN     | No              |
| 0x1A01 | 2nd TPDO mapping parameter          | rw     | CAN     | No              |
| 0x1A02 | 3rd TPDO mapping parameter          | rw     | CAN     | No              |
| 0x1A03 | 4th TPDO mapping parameter          | rw     | CAN     | No              |
| 0x1C12 | Sync manager 2 assignment           | rw     | CoE     | No              |
| 0x1C13 | Sync manager 3 assignment           | rw     | CoE     | No              |
| 0x1C32 | Sync manager 2 synchronization       | rw     | CoE     | No              |
| 0x1C33 | Sync manager 3 synchronization       | rw     | CoE     | No              |

## TGZ Specific Objects

In addition to TGZ registers (indexes 0x2000 – 0x3FF), there are special objects defined for easy access to native TGZ registers.

### Digital Inputs (0x4000)
This object is defined as an `UNSIGNED8` value and contains all the digital inputs of the TGZ servo drive. It is used for easy TPDO mapping in the CAN network. The object can be mapped for CAN TPDO only.

### Digital Outputs (0x4001)
Similarly, the digital outputs are defined as `UNSIGNED8` (only the first 6 bits are used) and are directly mapped to this object for easy RPDO mapping. The object can be mapped for CAN RPDO.

### Analog Inputs (0x4002)
Sub-index 0 is constant and equals 2 – two analog inputs are available.
Sub-indexes 1 and 2 contain read-only analog input values of type `UNSIGNED16`. These objects are a copy of TGZ native registers `0x3328` and `0x3428`, scaled down to `UNSIGNED16`. They can be easily mapped to CAN TPDO, saving PDO length.

### Drive Status (0x4003)
Sub-index 0 is constant and equals 2 – it indicates the status of two axes.
Sub-indexes 1 and 2 contain read-only drive status – the lower 16 bits of the native TGZ registers `0x3325` and `0x3425`. They can be easily mapped to CAN TPDO, saving PDO length.

## Device Profile (DSP402) Objects

The following standard DSP402 objects are supported. The first axis uses objects in the range `0x6000` – `0x67FF`, and the second axis adds an offset of `0x800` to the object indexes, i.e., the range is `0x6800` – `0x6FFF`. For example, the control word for the first axis is located at index `0x6040`, while the second axis uses the control word at index `0x6840`. The description of the objects can be found in the DSP402 documentation. Some of the objects are described below the table. All DSP402 objects can be accessed both from CAN and EtherCAT (CoE). The TGZ-S servo variant allows access to objects `0x6800` – `0x6FFF`, but the values are ignored.

| 1st Axis | 2nd Axis | Name                          | CAN PDO Mapping     |
|----------|----------|-------------------------------|---------------------|
| 0x6040   | 0x6840   | control word                   | RPDO                |
| 0x6041   | 0x6841   | status word                    | TPDO                |
| 0x6060   | 0x6860   | modes of operation             | RPDO                |
| 0x6061   | 0x6861   | modes of operation display     | TPDO                |
| 0x6064   | 0x6864   | position actual value          | TPDO                |
| 0x6065   | 0x6865   | following error window         | RPDO                |
| 0x6066   | 0x6866   | following error time out       | RPDO                |
| 0x606B   | 0x686B   | velocity demand value          | TPDO                |
| 0x606C   | 0x686C   | velocity actual value          | TPDO                |
| 0x6071   | 0x6871   | target torque                  | RPDO                |
| 0x6077   | 0x6877   | torque actual value            | TPDO                |
| 0x607A   | 0x687A   | target position                | RPDO                |
| 0x607C   | 0x687C   | home offset                    | RPDO                |
| 0x607D   | 0x687D   | software position limits       | RPDO (sub1, sub2)   |
| 0x6081   | 0x6881   | profile velocity               | RPDO                |
| 0x6083   | 0x6883   | profile acceleration          | RPDO                |
| 0x6084   | 0x6884   | profile deceleration          | RPDO                |
| 0x6085   | 0x6885   | quick stop deceleration       | RPDO                |
| 0x6086   | 0x6886   | motion profile type            | RPDO                |
| 0x608F   | 0x688F   | position encoder resolution    | RPDO (sub1, sub2)   |
| 0x6094   | 0x6894   | velocity encoder resolution    | RPDO (sub1, sub2)   |
| 0x6098   | 0x6898   | homing method                  | RPDO                |
| 0x6099   | 0x6899   | homing speed                   | RPDO (sub1, sub2)   |
| 0x609A   | 0x689A   | homing acceleration            | RPDO                |
| 0x60B2   | 0x68B2   | torque offset                  | RPDO                |
| 0x60C1   | 0x68C1   | interpolation wanted position  | RPDO (sub1)         |
| 0x60C2   | 0x68C2   | interpolation time period      | RPDO (sub1, sub2)   |
| 0x60D9   | 0x68D9   | supported synchronization functions | No            |
| 0x60E3   | 0x68E3   | supported homing methods       | No                  |
| 0x60F4   | 0x68F4   | following error actual value   | TPDO                |
| 0x60FD   | 0x68FD   | digital inputs                 | TPDO                |
| 0x60FE   | 0x68FE   | digital outputs                | RPDO                |
| 0x60FF   | 0x68FF   | target velocity                | RPDO                |
| 0x6502   | 0x6D02   | supported drive modes          | No                  |

### Modes of Operation `0x6060` {#0x6060}

The TGZ servo drive supports the following modes of operation:

| Value | Description                                       | Required TGZ Mode (D-Mode) |
|-------|---------------------------------------------------|-----------------------------|
| 1     | Profile Position Mode (PP)                       | 7: Position PG Mode         |
| 3     | Profile Velocity Mode (PV)                       | 6: Speed PG Mode            |
| 4     | Torque Profile Mode (PT)                         | 1: Current Mode             |
| 6     | Homing Mode                                       | 7: Position PG Mode         |
| 7     | Interpolated Position Mode (IP)                   | 3: Position Mode            |
| 8     | Cyclic Synchronous Position Mode (CSP)            | 3: Position Mode            |
| 9     | Cyclic Synchronous Velocity Mode (CSV)            | 2: Velocity Mode            |
| 10    | Cyclic Synchronous Torque Mode (CST)              | 1: Current Mode             |

!!! warning "Important Note"
    The object `0x6060` (`0x6860`) does NOT change the TGZ drive mode.
    The D-Mode register must be set to the correct value either by the TGZ_GUI service program and saved to the servo amplifier, or it must be set separately by the SDO object `0x2303` (first axis) or `0x2403` (second axis) by the master during startup.
    If the DSP402 mode of operation does not match the corresponding value of the D-Mode (according to the table above), the TGZ servo amplifier will ignore the EtherCAT/CANopen master commands.
    This feature allows for a virtual "disconnection" of the servo from the master, enabling testing or jogging directly from the TGZ_GUI program by simply setting the D-Mode value to a different (service-required) value.
    Note that the Torque Profile Mode (PT) and Cyclic Synchronous Torque Mode (CST) are functionally identical in the TGZ implementation. Also, the Interpolated Position Mode (IP) and Cyclic Synchronous Position Mode (CSP) behave identically.
    The IP mode uses object `0x60C1sub1` which is internally mapped to the Target Position `0x607A`.
    The mode of operation (together with the D-Mode) can be changed at any time but it is highly recommended that the drive is at standstill. Otherwise, a position error may occur.

### Target Torque `0x6071`

The target torque object is used mainly in torque modes PT or CST as the desired value.
Its range is `-32767 – 32767` and is expressed as a normalized value of the motor's M-Ipeak, where `-32767` is -100%, `0` is 0%, and `32767` is 100% of the M-Ipeak current.
It can also be used in cyclic positioning modes IP and CSP as the feedforward torque value.
In this case, the value is added to the desired value of the current regulator.
### Target Position `0x607A`

This is the position the drive should move to in PP, IP, or CSP mode.
The value is multiplied by the ratio given by the Position Encoder Resolution object (`0x608F`).
It is then used as an input value for TGZ's profile generator (PP mode) or directly as a desired 64-bit position in increments (IP or CSP).

$$
DesiredTGZposition = TargetPosition607A \times \frac{PositionEncoderNumerator608F_1}{PositionEncoderDivisor608F_2}
$$

The default value for the numerator is 4096 and for the divisor is 1.
### Profile Velocity `0x6081`

The final desired TGZ velocity for PP, PV, or CSV mode is calculated from the Profile Velocity object by the equation:

$$
DesiredTGZvelocity = ProfileVelocity6081 \times \frac{VelocityEncoderNumerator6094_1}{VelocityEncoderDivisor6094_2}
$$

Default values for both the Velocity Encoder Numerator and Divisor are 1.

### Motion Profile Type `0x6086`

Supported profile types for PP mode are as follows:

| Value | Mode                                             |
|-------|--------------------------------------------------|
| -3    | Sinusoidal (TGZ PG Mode 2)                       |
| -2    | Fast acceleration, fast deceleration (TGZ PG Mode 1) |
| -1    | Fast acceleration, slow deceleration (TGZ PG Mode 0) |
| 0     | Trapezoidal (TGZ Mode 3)                         |
| 1     | sin² (TGZ Mode 4)                                |

### Homing Method `0x6098`

Homing mode is activated by setting the value of object `0x6060` to 6.
The homing procedure itself is controlled by Control Word `0x6040`.
See the DSP402 documentation for additional information.
Object `0x60E3` is implemented and returns the number of supported homing modes (sub-index 0) along with their values (sub-indexes 1 – 10).

The following standard DSP402 homing modes are available:

| Mode | Description                                                                                                                                                                                             |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | Homing on negative limit switch and index pulse. Initial movement is leftward until the negative limit switch is active. Movement continues to the right at the first index pulse where the negative limit switch becomes inactive. The register `Homing_NegLimSwitchMask` determines the negative limit switch. |
| 2    | Homing on positive limit switch and index pulse. Similar to mode 1, but the movements are in opposite directions and the parameter `Homing_PosLimSwitchMask` is used to specify the positive limit switch. |
| 3    | Homing on positive home switch and index pulse. Same as mode 2, but the home switch is defined by `Homing_ReferenceSwitchMask`. The initial movement direction depends on the state of the home switch. |
| 5    | Homing on negative home switch and index pulse. Similar to mode 3, but the movements are reversed.                                                                                                                                   |
| 17   | Homing on negative limit switch. Similar to mode 1, but the home position is not dependent on the index pulse, only on the limit switch transition.                                        |
| 18   | Homing on positive limit switch. Similar to mode 2, without the index pulse search.                                                                                                        |
| 19   | Homing on positive home switch. Like mode 3 without the index pulse.                                                                                                                |
| 21   | Homing on negative limit switch. Equals mode 5 without the index pulse search.                                                                                                           |
| 35   | Set zero to the actual position. Uses the actual position as the home point reference. This method is obsolete for CoE.                                                                 |
| 37   | Set zero to the actual position. Uses the actual position as the home point reference. This mode should be used for CoE.                                                           |

### Digital Inputs `0x60FD`
According to the DSP402 standard, all digital inputs are mapped to the high 16 bits of the UNSIGNED32 value (TGZ servo drive has 8 digital inputs, so only bits 16 – 23 correspond to digital inputs).
The lower 16 bits are set to zero.
This object also exists for the second axis as `0x68FD`, but it is mapped to the same inputs, so both objects return the same value.
For easier access to digital inputs, the object `0x4000` can also be used.

### Digital Outputs 0x60FE~1~ and Mask 0x60FE~2~
The higher 16 bits of the UNSIGNED32 value are used as digital outputs (TGZ servo drive has 6 digital outputs, so only bits 16 – 21 are connected to the output pins).
The lower 16 bits are ignored.
This also applies to the digital output mask.
These objects also exist for the second axis as 0x68FE~1~ and 0x68FE~2~, but they are mapped to the same digital outputs.
Changing the object of one axis changes the object of the other axis as well.
For easier access to digital outputs, the object `0x4001` can be used.

## Error Codes

Two standard objects are used to provide the possible errors:
- Error Register `0x1001`
- Predefined Error Field `0x1003`

### Error Register `0x1001`

| Bit | Meaning            | TGZ Error Bit            | TGZ Error Bit Value          |
|-----|--------------------|--------------------------|-------------------------------|
| 0   | General Error.     | Any active bit           |                               |
| 1   | Current            | 8 or 19 or 21           | 0x100 or 0x80000 or 0x200000 |
| 2   | Voltage            | 3 or 4                   | 0x8 or 0x10                  |
| 3   | Temperature        | 9 or 11                  | 0x200 or 0x800               |
| 4   | Communication       | 12 or 17                 | 0x1000 or 0x20000            |
| 5   | Not Used           |                          |                               |
| 6   | Reserved           |                          |                               |
| 7   | Axis               | Set for the second axis |                               |



### Predefined Error Field `0x1003`
Sub-index 0 contains the number of actual errors in the array.
The maximum number is 64.
Errors are stored in a first-in last-out order, i.e., a new error is stored at sub-index 1 and other errors are moved down.
Writing zero to sub-index 0 clears the entire error history.
Each error bit from the TGZ error register generates one entry in the error history.
Error numbers are 32-bit unsigned values composed of a 16-bit standard DSP402 error code (see table below), an axis identifier in bit 16 (0: first axis, 1: second axis), and the original TGZ error bit number value in bits 24–29 (containing values 0–31).

| 31   | 30      | 29-24               | 23-17 | 16  | 15-0                  |
|------|---------|----------------------|-------|-----|-----------------------|
| 0    | TGZ error bit number value | 0    | axis | DSP402 error code     |

| DSP402 Error Code | Symbolic Name         | TGZ Error Bit |
|-------------------|------------------------|---------------|
| 0x3130            | MAINS_PHASE            | 0             |
| 0x3100            | MAINS_SUPPLY           | 1             |
| 0x8A00            | INTERNAL_ERROR         | 2             |
| 0x3110            | OVER_VOLTAGE           | 3             |
| 0x3120            | UNDER_VOLTAGE          | 4             |
| 0x5430            | STO                    | 5             |
| 0x7110            | HOLDING_BRAKE          | 6             |
| 0x7111            | HOLDING_BRAKE_SWITCH   | 7             |
| 0x2300            | CURRENT_MEASUREMENT    | 8             |
| 0x4310            | MOTOR_THERMOSTAT       | 9             |
| 0x4110            | AMBIENT_TEMPERATURE    | 10            |
| 0x4210            | HEAT_SINK_TEMPERATURE  | 11            |
| 0x7303            | FEEDBACK               | 12            |
| 0x7122            | COMMUTATION            | 13            |
| 0x8400            | OVER_SPEED             | 14            |
| 0x8612            | CONTOURING             | 15            |
| 0x8611            | TRAJECTORY             | 16            |
| 0x8100            | HOST_COMMUNICATION     | 17            |
| 0x8600            | DRIVE_RAMP_E2          | 18            |
| 0x2200            | CURRENT_REGULATION     | 19            |
| 0xF001            | EMERGENCY_STOP         | 20            |
| 0x5110            | IGBT_DRIVER_VOLTAGE    | 21            |
| 0x7113            | BRAKE_RESISTANCE       | 22            |
| 0x5112            | 24V_BRAKE_SUPPLY       | 23            |
| 0x1000            | Reserved               | 24            |
| 0x8310            | I2T                    | 25            |
| 0x4311            | MOTOR_TEMPERATURE      | 26            |
| 0x6320            | MOTOR_PARAMETER        | 27            |
| 0x1000            | Reserved               | 28            |
| 0x1000            | Reserved               | 29            |
| 0x1000            | Reserved               | 30            |
| 0x1000            | Reserved               | 31            |

## PDO Mapping and TGZ Drive Variants {#PDO_TGZ}
There are two variants of the TGZ servo amplifiers: TGZ-D is designed for controlling two axes, while TGZ-S is a single-axis variant.
Both versions use the same XML (EtherCAT) or EDS (CANopen) description files and have the same PDO structure and object dictionary objects.
For the TGZ-S version, the second axis objects do exist but have no meaning; changing or setting them has no effect on the behavior.
The second axis in the TGZ-S variant always responds with an error in the status word, which should be ignored.

## Default CAN PDO Mapping
Free PDO mapping can be used for CAN networks only.
The default mapping is selected to include the most important and usable objects.

###Default CAN RPDO Mapping
The default receive PDO mapping (direction controller → TGZ):

<table>
    <tr>
        <td bgcolor="#70AD47"><b>Index</b></td>
        <td bgcolor="#70AD47"><b>Sub-index</b></td>
        <td bgcolor="#70AD47"><b>Value</b></td>
        <td bgcolor="#70AD47"><b>Description</b></td>
    </tr>
    <tr>
        <td colspan="4" bgcolor="#E2EFD9"><b>RPDO1 uses 8 bytes (first axis)</b></td>
    </tr>
    <tr>
        <td rowspan="5"><b>0x1600</b></td>
        <td>0</td>
        <td>4</td>
        <td>Number of entries</td>
    </tr>
    <tr>
        <td bgcolor="#E2EFD9">1</td>
        <td bgcolor="#E2EFD9">0x60400010</td>
        <td bgcolor="#E2EFD9">Control word 0x6040</td>
    </tr>
    <tr>
        <td>2</td>
        <td>0x607A0020</td>
        <td>Target position 0x607A</td>
    </tr>
    <tr>
        <td bgcolor="#E2EFD9">3</td>
        <td bgcolor="#E2EFD9">0x60600008</td>
        <td bgcolor="#E2EFD9">Modes of operation 0x6060</td>
    </tr>
    <tr>
        <td>4</td>
        <td>0x40010008</td>
        <td>Digital outputs 0x4001</td>
    </tr>
    <tr>
        <td colspan="4" bgcolor="#E2EFD9"><b>RPDO2 uses 7 bytes (second axis)</b></td>
    </tr>
    <tr>
        <td rowspan="4"><b>0x1601</b></td>
        <td>0</td>
        <td>3</td>
        <td>Number of entries</td>
    </tr>
    <tr>
        <td bgcolor="#E2EFD9">1</td>
        <td bgcolor="#E2EFD9">0x68400010</td>
        <td bgcolor="#E2EFD9">Control word 0x6840</td>
    </tr>
    <tr>
        <td>2</td>
        <td>0x687A0020</td>
        <td>Target position 0x687A</td>
    </tr>
    <tr>
        <td bgcolor="#E2EFD9">3</td>
        <td bgcolor="#E2EFD9">0x68600008</td>
        <td bgcolor="#E2EFD9">Modes of operation 0x6860</td>
    </tr>
    <tr>
        <td colspan="4" bgcolor="#E2EFD9"><b>RPDO3 uses 4 bytes (first axis)</b></td>
    </tr>
    <tr>
        <td rowspan="2"><b>0x1602</b></td>
        <td>0</td>
        <td>1</td>
        <td>Number of entries</td>
    </tr>
    <tr>
        <td bgcolor="#E2EFD9">1</td>
        <td bgcolor="#E2EFD9">0x60810020</td>
        <td bgcolor="#E2EFD9">Profile velocity</td>
    </tr>
    <tr>
        <td colspan="4" bgcolor="#E2EFD9"><b>RPDO4 uses 4 bytes (second axis)</b></td>
    </tr>
    <tr>
        <td rowspan="2"><b>0x1603</b></td>
        <td>0</td>
        <td>1</td>
        <td>Number of entries</td>
    </tr>
    <tr>
        <td bgcolor="#E2EFD9">1</td>
        <td bgcolor="#E2EFD9">0x68810020</td>
        <td bgcolor="#E2EFD9">Profile velocity</td>
    </tr>
</table>

###Default CAN TPDO mapping
The default transmit PDO mapping (direction TGZ → controller)

<table>
	<tr>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Index&quot;}"><b>Index</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Sub-index&quot;}"><b>Sub-index</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Value&quot;}"><b>Value</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Description&quot;}"><b>Description</b></td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO1 (first axis, 8 bytes)&quot;}"><b>TPDO1 (first axis, 8 bytes)</b></td>
	</tr>
	<tr>
		<td rowspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A00&quot;}"><b>0x1A00</b></td>
		<td>0</td>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of entries&quot;}">Number of entries</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60410010&quot;}">0x60410010</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status word 0x6041&quot;}">Status word 0x6041</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60640020&quot;}">0x60640020</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Position actual value 0x6064&quot;}">Position actual value 0x6064</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">3</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60610008&quot;}">0x60610008</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Modes of operation display 0x6061&quot;}">Modes of operation display 0x6061</td>
	</tr>
	<tr>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x10010008&quot;}">0x10010008</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Error register 0x1001&quot;}">Error register 0x1001</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO2 (second axis, 8 bytes)&quot;}"><b>TPDO2 (second axis, 8 bytes)</b></td>
	</tr>
	<tr>
		<td rowspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A01&quot;}"><b>0x1A01</b></td>
		<td>0</td>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of entries&quot;}">Number of entries</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68410010&quot;}">0x68410010</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status word 0x6841&quot;}">Status word 0x6841</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68640020&quot;}">0x68640020</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Position actual value 0x6864&quot;}">Position actual value 0x6864</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">3</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68610008&quot;}">0x68610008</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Modes of operation display 0x6861&quot;}">Modes of operation display 0x6861</td>
	</tr>
	<tr>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40000008&quot;}">0x40000008</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digital inputs 0x4000&quot;}">Digital inputs 0x4000</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO3 (first axis, 6 bytes)&quot;}"><b>TPDO3 (first axis, 6 bytes)</b></td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A02&quot;}"><b>0x1A02</b></td>
		<td>0</td>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of entries&quot;}">Number of entries</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x606C0020&quot;}">0x606C0020</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual velocity 0x606C&quot;}">Actual velocity 0x606C</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40020110&quot;}">0x40020110</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analog input 1 0x4002sub1&quot;}">Analog input 1 0x4002sub1</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO4 (second axis, 6 bytes)&quot;}"><b>TPDO4 (second axis, 6 bytes)</b></td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td>0</td>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of entries&quot;}">Number of entries</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x686C0020&quot;}">0x686C0020</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual velocity 0x686C&quot;}">Actual velocity 0x686C</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40020210&quot;}">0x40020210</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analog input 2 0x4002sub2&quot;}">Analog input 2 0x4002sub2</td>
	</tr>
</table>



## PDO Mapping for CANopen over EtherCAT (CoE)

When using EtherCAT communication, two fixed PDO mappings are available:

- Native TGZ Mapping
- CoE Compatible Mapping

### Native TGZ PDO Mapping

This PDO mapping uses full 64-bit position values, allowing the EtherCAT master to control the servo drive with full precision.
The drive operates only in Cyclic Synchronous Position mode.
The drive mode (D-Mode) must be set to 3 (position mode) by the TGZ_GUI service program.
To select native PDO mapping, the EtherCAT master must make the following sequence in the PRE-OPERATIONAL state using SDO access:

- Set object 0x1C12~0~ to `0` (data size UNSIGNED8)
- Set object 0x1C12~1~ to `0x1721` (data size UNSIGNED16)
- Set object 0x1C12~0~ to `1` (data size UNSIGNED8)
- Set object 0x1C13~0~ to `0` (data size UNSIGNED8)
- Set object 0x1C13~1~ to `0x1B21` (data size UNSIGNED16)
- Set object 0x1C13~0~ to `1` (data size UNSIGNED8)

Alternatively, the mapping numbers `0x1721` and `0x1B21` can be set using the TGZ_GUI program with `PDO_Out_Mapping_1C12_1` and `PDO_In_Mapping_1C13_1` registers.

The native RPDO has the following structure (44 bytes):


``` cpp
int64_t positionSetPoint_1;
uint32_t control_1;
int16_t currentSetPoint_1;
uint16_t currentLimit_1;
int64_t positionSetPoint_2;
uint32_t control_2;
int16_t currentSetPoint_2;
uint16_t currentLimit_2;
uint32_t Reserved_1;
uint32_t Reserved_2;
uint32_t Reserved_3;
```

The native TPDO has the following structure (44 bytes):

``` cpp
int64_t positionActValue_1;
int64_t positionActValue_2;
uint32_t positionActValueExt;
uint32_t status_1;
uint32_t status_2;
uint16_t analogInput_1;
uint16_t analogInput_2;
int16_t currentqActValue_1;
int16_t currentqActValue_2;
uint32_t mappedParameter_1;
uint32_t mappedParameter_2;
```

PDOs are described [here](packet.md#ECAT_PDO).

###CoE TGZ PDO mapping
This mapping uses the standard CANopen objects.
Some of the items are used only in certain modes of operation.
The appropriate TGZ drive mode is **NOT** selected automatically when writing object 0x6060 (0x6860) via SDO; it must be set up by the TGZ_GUI program or by SDO.
See also the chapter [Modes of Operation 0x6060](objects.md#0x6060).
Position values are recalculated by a ratio given by the object *Position Encoder Resolution* 0x608F or 0x688F.
The full DSP402 state machine is implemented using control word 0x6040 (0x6840) and status word 0x6041 (0x6841).
The following fixed receive PDO (direction controller -> TGZ) mappings are available:


| Mode                            | Value     |
|----------------------------------|---------|
| Cyclic synchronous position  (CSP) | 0x1701  |
| Cyclic synchronous velocity  (CSV) | 0x1702  |
| Cyclic synchronous torque (CST) | 0x1703  |

There is only one CoE transmit PDO `0x1B01`, which contains all the necessary actual values.

To select CoE mapping, the master must use the following sequence by SDO write in the PRE-OPERATIONAL state:

- Set object 0x1C12~0~ to `0` (zero) (data size UNSIGNED8)
- Set object 0x1C12~1~ to `0x1701` (data size UNSIGNED16)
- Set object 0x1C12~0~ to `1` (one) (data size UNSIGNED8)
- Set object 0x1C13~0~ to `0` (zero) (data size UNSIGNED8)
- Set object 0x1C13~1~ to `0x1B01` (data size UNSIGNED16)
- Set object 0x1C13~0~ to `1` (one) (data size UNSIGNED8)

Alternatively, the mapping numbers `0x1701` (`0x1702`, `0x1703`) and `0x1B01` can be set by using the TGZ_GUI program with the `PDO_Out_Mapping_1C12_1` and `PDO_In_Mapping_1C13_1` registers.

The CoE RPDO for CSP, IP, or PP mode (`0x1701`) has the following structure (40 bytes):


``` cpp
// First axis
int32_t position_setpoint_1; // SDO object 0x607A (modes PP, IP, CSP)
uint32_t velocity_setpoint_1; // SDO object 0x60FF (modes PP a PV)
uint32_t digital_outputs; // SDO object 0x60FE sub 1 
uint16_t control_word_1; // SDO object 0x6040
int16_t current_setpoint_1; // SDO object 0x6071 (PP, CSP, PT, CST)
uint16_t current_limit_1; // see equation below
int16_t padding_1; // not used
// Second axis
int32_t position_setpoint_2; // SDO object 0x687A (modes PP, IP, CSP)
uint32_t velocity_setpoint_2; // SDO object 0x68FF (modes PP a PV)
uint32_t reserved_2; // not used
uint16_t control_word_2; // SDO object 0x6840
int16_t current_setpoint_2; // SDO object 0x6871 (PP, CSP, PT, CST)
uint16_t current_limit_2; // see equation below
int16_t padding_2; // not used
```

The CoE RPDO for CSV or PV mode (`0x1702`) has the following structure (40 bytes):

``` cpp
// First axis
int32_t reserved_1; // not used
uint32_t velocity_setpoint_1; // SDO object 0x60FF (modes PP a PV)
uint32_t digital_outputs; // SDO object 0x60FE sub 1 
uint16_t control_word_1; // SDO object 0x6040
int16_t current_setpoint_1; // SDO object 0x6071 (PP, CSP, PT, CST)
uint16_t current_limit_1; // see equation below
int16_t padding_1; // not used
// Second axis
int32_t reserved_2; // not used
uint32_t velocity_setpoint_2; // SDO object 0x68FF (modes PP a PV)
uint32_t reserved_3; // not used
uint16_t control_word_2; // SDO object 0x6840
int16_t current_setpoint_2; // SDO object 0x6871 (PP, CSP, PT, CST)
uint16_t current_limit_2; // see equation below
int16_t padding_2; // not used
```

The CoE RPDO for CST or PT mode (`0x1703`) has the following structure (40 bytes):

``` cpp
// First axis
int32_t reserved_1; // SDO object 0x607A (modes PP, IP, CSP)
uint32_t reserved_2; // SDO object 0x60FF (modes PP a PV)
uint32_t digital_outputs; // SDO object 0x60FE sub 1 
uint16_t control_word_1; // SDO object 0x6040
int16_t current_setpoint_1; // SDO object 0x6071 (PP, CSP, PT, CST)
uint16_t current_limit_1; // see equation below
int16_t padding_1; // not used
// Second axis
int32_t reserved_3; // not used
uint32_t reserved_4; // not used
uint32_t reserved_5; // not used
uint16_t control_word_2; // SDO object 0x6840
int16_t current_setpoint_2; // SDO object 0x6871 (PP, CSP, PT, CST)
uint16_t current_limit_2; // see equation below
int16_t padding_2; // not used
```

Set-point values are active according to the selected mode of operation. Current limits are calculated as

$$
Iq_{lim}=(32767-CurrentLimit) \times \frac{M I_{peak}}{32767}
$$

For full limitation, set `current_setpoint_x` to `32767`.
For no limitation, where maximal current = `M-Ipeak`, set the limit to `0`.
The CoE TPDO (`0x1B01`) has the following structure (40 bytes):

``` cpp
// First axis
int32_t position_actual_value_1; // SDO object 0x6064
int32_t velocity_actual_value_1; // SDO object 0x606C
uint32_t digital_inputs; // SDO object 0x60FD 
uint16_t status_word_1; // SDO object 0x6041
int16_t torque_actual_value_1; // SDO object 0x6077
uint16_t analog_input_1; // SDO object 0x4002sub1
uint16_t drive_status_1; // SDO object 0x4003sub1
// Second axis
int32_t position_actual_value_2; // SDO object 0x6864
int32_t velocity_actual_value_2; // SDO object 0x686C
int32_t external_encoder; // SDO object 0x333E
uint16_t status_word_2; // SDO object 0x6841
int16_t torque_actual_value_2; // SDO object 0x6877
uint16_t analog_input_2; // SDO object 0x4002sub2
uint16_t drive_status_2; // SDO object 0x4003sub2
```

All the actual values are updated regardless of the active mode of operation.