##General
The PROFINET network is connected using the X13 (Fieldbus IN) connector and X12 (Fieldbus OUT) connector.
Use the IN connector in the direction to the PLC and the OUT connector to connect other PROFINET devices in the chain.
The TGZ servo amplifier has built-in PROFINET bridge functionality, so for a small number of devices and simple configuration a dedicated PROFINET managed switch is not needed.
**When connecting the PROFINET network cables, the supply of the equipment must be switched off.**   

!!! warning "Warning"
    Only professional staff member with sufficient knowledge of drive technology is allowed to set up the TGZ servo amplifier.
    All the electrical connections must be done in conformance with the [TGZ user’s manual](../../../../CZ/TGZ/TGZ-D-48-13_26/md/mark.md).

##Fast Guide to Setup
- Check the installation and assembly. Consult all the safety instructions in the user’s manual.
- Connect PC to X11 Ethernet service connector and start TGZ GUI service program.
- Setup the MAC address of the device:

![Profinet img 1](../../../../source/img/profinet1.webp){: style="width:90%;" }

- The MAC address shall start with `00` (two zeros) and `0A`.
  The last four numbers could be arbitrary, but unique in the PROFINET network.
  In addition, the last number must vary by 8, so the valid values for the last number are `00, 08, 10, 18, 20, 28, ..., 90, 98, A0, A8, B0, B8, ..., F0, F8`.
- The MAC address base value is used for the service port X11.
  The PROFINET interface MAC address is calculated by adding `4` to the base value, X13 (IN) has address `base + 5` and X12 (OUT) `base + 6`.
  Usually only the PROFINET interface MAC address is used during PROFINET device commissioning.
  The first two hexadecimal numbers are always `00` and `0A` for all the PROFINET interface and connectors X13 and X12 regardless of the value entered in the TGZ GUI.
- Select the right telegram number according to the PROFINET project and type of the mechanism controlled by the TGZ servo.

![Profinet img 2](../../../../source/img/profinet2.webp){: style="width:90%;" }

- Set the telegram type for both axes in the case of the two axes servo amplifier variant.
- Save the parameters to the drive.

![Profinet img 3](../../../../source/img/profinet3.webp){: style="width:40%;" }

- Restart the drive.

![Profinet img 4](../../../../source/img/profinet4.webp){: style="width:40%;" }

!!! note "Note"
    It is important to always save parameters and restart the drive when the MAC address and/or the telegram number is changed.

	
## IP address and device name {#ProfinetIPsettings}
The factory setting of the IP address is `0.0.0.0` and the device name is empty. There is a need to assign a unique device name and IP address in the PROFINET network. Any commissioning PROFINET software can be used for that, for example **TIA Portal**.

- Select the PC network adapter which is connected to the PROFINET network and double click on line **Update accessible devices**.

![Profinet img 5](../../../../source/img/profinet5.webp){: style="width:40%;" }

- Connected devices will appear after a while:

![Profinet img 6](../../../../source/img/profinet6.webp){: style="width:40%;" }

- There should be a list of all connected PROFINET devices on the network. Expand the device with a given MAC address and double click on **Online & diagnostics**.

![Profinet img 7](../../../../source/img/profinet7.webp){: style="width:40%;" }

- Enter a unique IP address and appropriate subnet mask (usually `255.255.255.0`) and click the **Assign IP address** button.

![Profinet img 8](../../../../source/img/profinet8.webp){: style="width:70%;" }

- Set the device name, which must be also one and only in the PROFINET network and assign it by button **Assign name**.

![Profinet img 9](../../../../source/img/profinet9.webp){: style="width:70%;" }

- Optionally, the check box LED flashes can be used to locate the device in the field. TGZ blinks with letters "Pd" on its segment LED display (Pd stands for PROFIdrive).

##Homing modes
The drive must be in operational state with positioning mode set (telegrams `7`, `9` or `111`). No task must be active and the drive must be in standstill. The mode is selected by the `Homing_Mode` parameter in the TGZ_GUI application. To initiate a homing procedure, set the control word `STW1` bit `11` to one. As the homing procedure is running, the status word `ZSW1` bits `10, 11 and 13` are set to zero. After successful homing, these bits `10, 11 and 13` go to one. In the case of any error during homing, only the bit `13` is set. The homing procedure can be aborted by setting the `STW1 bit 11` to zero. It is also necessary to finish the successful homing procedure by setting the `STW1 bit 11` to zero. Only after this the drive goes back to the basic operational state.

The following homing modes are available:

| Mode no. | Mode description |
|-----|-------|
| 0   | Set zero to the actual position. Uses the actual position as the home point reference. |
| 1   | Find limit input. Movement starts in positive or negative direction until the limit switch is detected. Then the reverse movement is used until the limit switch is no longer active. The actual position is used as the home point. `Homing_NegLimSwitchMask` and `Homing_PosLimitSwitchMask` parameters are used to select the digital input bit of the limit switch. The sign of `Homing_Velocity_Direction` parameter determines the homing direction. |
| 2   | Find limit input, then zero angle. Similar to mode 1, but after the home position is set, the motor moves to the zero angle of the feedback. |
| 4   | Find home input. This mode is similar to mode 1, but uses the homing switch as the input (parameter `Homing_ReferenceSwitchMask`). The initial direction is determined by the sign of `Homing_Velocity_Direction` parameter. The positive and negative switches are also taken into account in the algorithm. |
| 5   | Find home input, then zero angle. Similar to mode 4, after the home position is set, the drive goes to the zero angle of the feedback. |
| 8   | Move to mechanical stop. The drive moves until it encounters a hard stop, causing the position error to be exceeded. The move stops afterwards and the home position is set. |
| 9   | Move to mechanical stop, then zero angle. Similar to mode 8, after the home position is set, the motor moves to the zero angle of the feedback. |

##Tasks
The TGZ amplifier allows up to ten tasks to be used in positioning mode. The task numbers are set by the `SATZANW` signal in telegrams `7, 9` or `111`. The task parameters can be set by TGZ_GUI. The target position is always 64 bits (in TGZ units) to allow full value precision. The mode of the task is either 0 - relative positioning, or 1 - absolute target value. No action is performed for invalid task numbers. Valid values are 0 - 9 `(PD_Task1 - PD_Task10`). For a detailed description of the task and direct **Manual data input (MDI)** mode, see the **PROFIdrive Profile** documentation.

##Jog
The jogging function is supported in both position (telegrams `7, 9, 111`) and speed mode (telegrams `1, 3, 352`). All the jog parameters can be set by the TGZ_GUI application. Two jog setpoints are available by using the control word `STW1` bits `8 and 9`. If both bits are set the drive either stops in speed mode or does nothing in positioning mode.

The drive works in speed mode when the jog is active, i.e., it moves the axis with the desired jog speed endlessly until stopped.

The functionality is implemented according to the standard described in the PROFIdrive Profile documentation.

##Error codes
The error code is copied to the fault buffer in the case of any drive error. The standard PROFIdrive fault buffer mechanism is used. Because the standard PROFIdrive error code has a width of 16 bits only and TGZ uses 32-bit errors, there are always two fault messages containing the full 32-bit error word. Therefore, the parameter `947` is organized with 8 fault situations with 2 fault messages. The message with index `0` contains the low 16 bits of the error code and the message with index `1` the high 16 bits.

The fault buffer can be completely cleared by writing zero to the parameter `952`.

Telegram `111` contains space for the last active error code, where the `WARN code` field (PZD11) contains the low 16 bits and the `FAULT code` field (PZD10) contains the high 16 bits of the TGZ error code. Similarly, the telegram `352` has fields for `WARN (PZD5)` and `FAULT (PZD6)`. They are coded in the same manner. The TGZ error codes are bit-oriented, i.e., there are up to 32 errors possible, and they are cumulative, i.e., several bits can be set at the same time.

| Bit | Description |
|-----|-------|
| 0   | Mains phase (1-phase supply) |
| 1   | Mains supply fault |
| 2   | reserved (internal error) |
| 3   | Over voltage DC-Link |
| 4   | Under voltage DC-link |
| 5   | reserved |
| 6   | Holding brake error |
| 7   | Holding brake switch damaged |
| 8   | reserved |
| 9   | Motor thermostat |
| 10  | Ambient temperature |
| 11  | Heat sink temperature |
| 12  | Feedback Error |
| 13  | Commutation error |
| 14  | Over speed |
| 15  | Contouring Error |
| 16  | Trajectory Error (Position Setpoint) |
| 17  | Host Communication Error |
| 18  | Drive Error Ramp E2 |
| 19  | Drive Error No Ramp E1 |
| 20  | External Enable/Locked/Brake Enable Error |
| 21  | IGBT Driver Voltage Error |
| 22  | Maximal Regen Power Error |
| 23  | 24V Brake Supply Error |
| 24  | reserved |
| 25  | I2T Error |
| 26  | Motor Temperature Warning |
| 27  | Motor Parameter Error |
| 28  | Multi-turn Revolution Error |
| 29  | Max. Sum Power Limitation |
| 30  | reserved |
| 31  | reserved |


## Relationship between TGZ coordinates and PROFIdrive values
The TGZ drive uses 64-bit values for position. This value consists of number of revolutions in upper 32 bits, and number of increments within one turn.
On the other hand, PROFIdrive standard uses only 32-bit values for position. For this reason, some kind of up and downscaling is necessary.
The wanted position value from PROFIdrive telegram is expanded to 64 bits and then shifted left by 32 minus the number of bits specified in the TGZ settings – Profile generator (PG) value `BitsPerRevol`.
If `BitsPerRevol=20`, then the value from PROFIdrive is shifted left by 12 bits. The shifting has the same effect as multiplying the value by 2^12 (i.e., 4096).
The similar downscaling is performed when sending actual position value from TGZ to the PROFIdrive controller: the 64-bit TGZ position is shifted right by `32 - BitsPerRevol` (which is the same operation as dividing by 2<sup>32-BitsPerRevol</sup>) and the resulting lower 32 bits are sent in the PROFIdrive telegram.

The values of velocity are not scaled at all because both TGZ and PROFIdrive telegrams use 32-bit values. Therefore, the meaning of velocity is the same as velocity for the Profile generator.
Acceleration and deceleration must be set directly in the TGZ by service program TGZ_GUI in the PROFIdrive section and can be changed by PROFIdrive telegrams only by means of override (percentage) values contained in the respective telegrams.

## Backlash compensation
The firmware from August 2023 or newer implements the backlash compensation. The standard parameter `PNU 2583` is used for the backlash value.
It is stored as signed 32-bit integer value and has the same physical meaning as desired or actual position in telegrams `9` or `111`.
To use the backlash compensation, a successful homing procedure must be performed first.

The positive movement direction is performed when the actual position is incremented. Likewise, the negative movement is defined when the position is decremented.
The compensation itself is dependent on the sign of the backlash:

- Positive backlash value: when the wanted position is in the positive direction, the backlash value is added to the value. On the other hand, for the negative movement, no value is added to the desired position.
- Negative backlash value: during the negative movement the backlash is subtracted from the wanted position, making the result more negative. For the positive direction, no value is added to the final desired position.

Use of the positive or negative backlash depends on the chosen homing procedure and its final movement. If the homing finishes with the negative movement, use the positive backlash, because the looseness is already adjusted to the left side. Likewise choose the negative backlash value when the last homing movement goes in the positive direction.

The backlash value can be set only by the parameter `PNU 2583` by PLC, there is no equivalent in the TGZ register area.
The program block called `SinParaS` can be used in the TIA portal for setting the `PNU 2583`.

![Profinet img](../../../../source/img/profinet10.webp){: style="width:50%;" }

The `hardwareId` input is set to the same value as `HWIDSTW` input of `SinaPos` block, i.e., the telegram identifier of the TGZ. `AxisNo` can be `0` for the first axis or `1` for the second one.
As the backlash is of type `DINT` (signed 32-bit integer), the wanted backlash value must be written to the `ValueWrite2` input.
The write is performed by toggling `Start` from `False` to `True`.

## Speed control mode and normalized values
Telegrams `1`, `3` and `352` are used for speed control mode. These telegrams use normalized speed values in the `N2` or `N4` format.
Setpoint and actual speed are expressed as a percentage of the reference value. TGZ amplifier uses the nominal speed register named `M-Nn` for this purpose – it must be non-zero, otherwise the speed control mode would not work.
Normalized `N2` or `N4` values in the telegram are in the range from `-200 %` to `200 %` of the reference `M-Nn` value.

The `M-Nn` register can be read by the standard `PNU` parameter `60 000` **Velocity reference value**.
Complete access (read/write) is possible by direct TGZ parameters access, register numbers are `0x211B` for axis `1` and `0x221B` for axis `2`.
See also chapter TGZ registers.

!!! note "Note"
    Note that `PNU 60 000` is read as floating point value, while direct access to TGZ registers is always 32-bit integer.

The internal speed profile generator uses register `PD_Dec` (`0x355F / 0x365F`) as the acceleration value when changing the speed.
