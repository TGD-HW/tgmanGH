##Basic principle {#Ramptype}
It allows easy positioning from point to point and speed control of the actuator.
The output of the generator is a 64-bit position variable, which consists of two 32-bit variables `APosAngle` and `APosRevol`, as well as a variable `ASpeed` determining the current speed setpoint.
The parameters of the generator are `Acc` and `Dec`, which determine the acceleration resp. deceleration of the drive, the `Type` parameter determines the course of speed during acceleration and deceleration (see diagram below).
Another parameter is `PosSpeed`, which determines the maximum speed during positioning, the `DPosAngle` and `DposRevol` parameters determine the target position and the `Speed` parameter determines the speed setpoint.
The variables `Mode` and `Rdy` are used to control the generator itself.
The `Mode` variable specifies the PG mode (value 0 indicates the speed mode, value 1 indicates the position mode).
If the positioning is successfully completed and the output position is the same as the setpoint, then this state is signaled by the value of the variable `Rdy = 1`.
The generator works by calculating the current `APosAngle` and `APosRevol` position setpoint and the current `ASpeed` speed setpoint in each period based on the parameters (`Acc, Dec, Type, PosSpeed, DPosAngle, and DPosRevol`) and the status of the `Mode` and `Speed` variables.
The calculation of the generator is performed with the internal resolution given by the `BitsPerRevol` parameter. This parameter then specifies the internal number of increments per revolution.

![TGZ servo ramp type](../../../../source/img/TGZrampType1.webp){: style="width:70%;" } 

- (a) position mode
- (b) speed mode
- (c) type of ascending and descending ramps

The following parameters work with this resolution:

| Parameter               | Unit        |
|-------------------------|-------------|
| Acc, Dec                | [Inc/s²]    |
| ASpeed, DSpeed, Speed   | [Inc/s]     |

The position parameters are 64-bit and consist of two 32-bit registers:

- The Angle register indicates the position within one revolution with a resolution of 32 bits
- The Revol register is an extension of 32 bits (number of whole revolutions):
	- DPosRevol, DPosAngle
	- APosRevol, APosAngle

These built-in functions can be used in the user program to simplify work with the profile generator:

- Relative positioning - this is a position transition:
  int PosRel(int axis, int Acc, int Dec, int Speed, long long Pos, int AddGear);
- Absolute positioning - this is the approach to the absolute position:
  int PosAbs(int axis, int Acc, int Dec, int Speed, long long Pos, int AddGear);
- Speed crossing - the drive spins at a given speed.
  int RunSpeed(int axis, int Acc, int Speed, int AddGear);

Description of parameters:
axis - 0 - axis 1, 1 - axis 2
Acc,Dec - in the same sense as the PG parameters described above
Speed - Maximum position crossing speed or speed crossing speed
AddGear - not implemented yet (will determine cooperation with the Gear module)

##Examples of motor control via Profile Generator
The following tables provide examples of using a generator profile that is set to different motor control modes.
The **Basic Groups** column lists the page name.
Switching between individual pages is allowed in the upper left corner of the TGZ graphical user interface.

!!! Note "Note"
	In the first step, it is important to set / load the correct drive parameters.
	Uploading parameters is possible using the blue envelope in the upper right corner (*LOAD PARAMETERS FROM FILE*), see [TGZ GUI Manual](../../../TGZ/TGZ_SW/GUI/md/intro.md#GUIstart)
	
###Motor position control via TGZ GUI

| Step | Basicgroups | Parametr    | Value [^1]   | Desription                                                                                                         |
|------|-------------|-------------|--------------|--------------------------------------------------------------------------------------------------------------------|
| 1    | -           | -           | -            | Loaddrive parameters.                                                                                              |
| 2    | Drive       | D-mode      | 7            | Profilegenerator - position mode.                                                                                   |
| 3    | Command     | K-Command   | 1            | SW enable. It can also be turned on using the enable button for the respective axis on the bottom bar. The motor generates torque. |
| 4    | PG          | Acc         | 5 000 000[^1]| [inc/s²] Required acceleration.                                                                                   |
| 5    | PG          | Dec         | 5 000 000[^1]| [inc/s²] Desired deceleration.                                                                                    |
| 6    | PG          | PosSpeed    | 1 000 000[^1]| [inc/s] Desired speed of movement in position mode.                                                               |
| 7    | PG          | Mode        | 1            | Position mode.                                                                                                     |
| 8    | PG          | Type        | 1            | Required ramp type.                                                                                                 |
| 9    | PG          | DPosAngle   | 0            | [inc] Desired position within one revolution. After entering the value and pressing the Enter key, the motor rotates to the desired position. |
| 10   | PG          | DPosRevol   | 20[^1]       | [inc] Desired position within the multi-turn range. After entering the value and pressing the Enter key, the motor rotates to the desired position. |

[^1]: Values are for guidance only. They can be changed as desired.

###Motor position control via UDP

**D-mode**   
Description: Servo amplifier mode setting: Profile Generator - position mode.

<table>
    <tr>
        <td colspan="7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram: Request&quot;}"><b>Telegram: Request</b></td>
        <td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
    </tr>
    <tr>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
    </tr>
    <tr>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
        <td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
        <td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
    </tr>
    <tr>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
    </tr>
    <tr>
        <td colspan="7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram: Response&quot;}"><b>Telegram: Response</b></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
    </tr>
    <tr>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
        <td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : no error)&quot;}">(Byte 6, 10 = 0 : no error)</td>
    </tr>
    <tr>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
        <td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
        <td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
    </tr>
</table>

**PG – Acc, Dec, PosSpeed, Type, Mode, DPosAngle, DPosRevol**   
Description: Setting of required acceleration, deceleration, ramp type (see fig.), Generator Profile mode and zero position setpoint (initial state).

<table>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 25&quot;}" style="color:white;"><b>Byte 25</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 26&quot;}" style="color:white;"><b>Byte 26</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x42&quot;}">0x42</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0F&quot;}">0x0F</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="3" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 27&quot;}" style="color:white;"><b>Byte 27</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 28&quot;}" style="color:white;"><b>Byte 28</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 29&quot;}" style="color:white;"><b>Byte 29</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 30&quot;}" style="color:white;"><b>Byte 30</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 31&quot;}" style="color:white;"><b>Byte 31</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 32&quot;}" style="color:white;"><b>Byte 32</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 33&quot;}" style="color:white;"><b>Byte 33</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 34&quot;}" style="color:white;"><b>Byte 34</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 35&quot;}" style="color:white;"><b>Byte 35</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="2" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 36&quot;}" style="color:white;"><b>Byte 36</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 37&quot;}" style="color:white;"><b>Byte 37</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 38&quot;}" style="color:white;"><b>Byte 38</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 39&quot;}" style="color:white;"><b>Byte 39</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 40&quot;}" style="color:white;"><b>Byte 40</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 41&quot;}" style="color:white;"><b>Byte 41</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 42&quot;}" style="color:white;"><b>Byte 42</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 43&quot;}" style="color:white;"><b>Byte 43</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 44&quot;}" style="color:white;"><b>Byte 44</b></td>
	</tr>
	<tr>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="2" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 45&quot;}" style="color:white;"><b>Byte 45</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 46&quot;}" style="color:white;"><b>Byte 46</b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="10" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : no Error)&quot;}">(Byte 6, 10 = 0 : no Error)</td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td colspan="2" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**K – Command**   
Description: SW enable.
After entering this command, the motor is under torque and rotates to the desired position from the previous request.

<table>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="3" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td colspan="2" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : no Error)&quot;}">(Byte 6, 10 = 0 : no Error)</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="3" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td colspan="2" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

###Motor speed control via TGZ GUI

| Step | Basic groups | Parameter  | Value       | Description                                                                                             |
|------|--------------|------------|-------------|---------------------------------------------------------------------------------------------------------|
| 1    | -            | -          | -           | Load drive parameters.                                                                                  |
| 2    | Drive        | D-mode     | 7           | Profile generator - position mode.                                                                      |
| 3    | Command      | K-Command  | 1           | SW permission. It can also be turned on using the activation button on the bottom bar. The motor generates torque. |
| 4    | PG           | Acc        | 5 000 000[^1]| [inc / s²] Required acceleration.                                                                      |
| 5    | PG           | Dec        | 5 000 000[^1]| [inc / s²] Desired acceleration required.                                                              |
| 6    | PG           | Mode       | 0           | Speed mode.                                                                                             |
| 7    | PG           | Type       | 1           | Required ramp type.                                                                                     |
| 8    | PG           | PosSpeed   | ±1 000 000[^1]| [inc / s] Desired speed of movement in position mode. After entering the value and pressing the Enter key, the motor will rotate at the desired speed. |

[^1]: Values are for guidance only. They can be changed as desired.

###Motor speed control via UDP
**D-Mode**   
Description: Servo amplifier mode setting: Profile Generator - position mode.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : no error)&quot;}">(Byte 6, 10 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – Acc, Dec, PosSpeed, Type, Mode**   
Description: Setting of the required acceleration, deceleration, speed, ramp type (see fig.) and Generator Profile mode.
The sign at speed PosSpeed determines the direction of rotation of the motor.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x08&quot;}">0x08</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 25&quot;}" style="color:white;"><b>Byte 25</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 26&quot;}" style="color:white;"><b>Byte 26</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x42&quot;}">0x42</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0F&quot;}">0x0F</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 27&quot;}" style="color:white;"><b>Byte 27</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 28&quot;}" style="color:white;"><b>Byte 28</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 29&quot;}" style="color:white;"><b>Byte 29</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 30&quot;}" style="color:white;"><b>Byte 30</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 31&quot;}" style="color:white;"><b>Byte 31</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 32&quot;}" style="color:white;"><b>Byte 32</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 33&quot;}" style="color:white;"><b>Byte 33</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 34&quot;}" style="color:white;"><b>Byte 34</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5= 0 : no error)&quot;}">(Byte 5= 0 : no error)</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x08&quot;}">0x08</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**K – Command**   
Description: SW enable.
After entering this command, the motor is under torque and starts turning in the desired direction at the desired speed.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : no error)&quot;}">(Byte 5 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

###Software limits for motor speed control in TGZ GUI
| Step | Basic groups | Parameter           | Value           | Description                                                                                                      |
|------|--------------|---------------------|-----------------|------------------------------------------------------------------------------------------------------------------|
| 1    | -            | -                   | -               | Load drive parameters.                                                                                           |
| 2    | Drive        | D-mode              | 7               | Profile generator - position mode.                                                                               |
| 3    | Command      | K-Command           | 1               | SW permission. It can also be turned on using the activation button on the bottom bar. The motor generates torque. |
| 4    | PG           | Acc                 | 5000000 [^1]    | [inc /s²] Required acceleration.                                                                                |
| 5    | PG           | Dec                 | 5000000 [^1]    | [inc /s²] Desired deceleration.                                                                                 |
| 6    | PG           | PosSpeed            | 1000 000 [^1]   | [inc /s] Desired speed of movement in position mode.                                                            |
| 7    | PG           | Mode                | 1               | Position mode.                                                                                                   |
| 8    | PG           | Type                | 1               | [Required ramp type](#Ramptype).                                                                                 |
| 9    | PG           | DPosAngle           | 0               | [inc] Desired position within one revolution. After entering the value and pressing the Enter key, **the motor rotates to the desired angle**. |
| 10   | PG           | DPosRevol           | 0               | [inc] Desired position within the range of multi-turn motion. After entering the value and pressing the Enter key, **the motor rotates to position 0**. Wait for the motor to rotate. |
| 11   | PG           | PosSpeed            | 0               | [inc /s] Desired speed of movement in position mode.                                                             |
| 12   | PG           | Mode                | 0               | Speed mode.                                                                                                      |
| 13   | PG           | PosLimitAnglePosit  | 0 [^1]          | Positive position limit within one revolution in the range from -2<sup>16</sup> to 2<sup>16</sup>.               |
| 14   | PG           | PosLimitRevolPosit  | 20 [^1]         | [± speed] Upper limit of the position within the speed in the range from -2<sup>16</sup> to 2<sup>16</sup>.    |
| 15   | PG           | PosLimitAngleNegat  | 0 [^1]          | Negative position limit within one revolution in the range from -2<sup>16</sup> to 2<sup>16</sup>.               |
| 16   | PG           | PosLimitRevolNegat  | -20 [^1]        | [± number of revolutions] Lower limit of the position within the speed in the range from -2<sup>16</sup> to 2<sup>16</sup>. |
| 17   | PG           | PosSpeed            | ± 5000 000 [^1] | [inc /s] After entering the value, **the motor will rotate** at `PosSpeed` to `PosLimitRevolPosit` or `PosLimitRevolNegat`. The direction of rotation is given by the sign of the `PosSpeed` parameter. |

###Software limits for motor speed control (UDP)
**D-Mode**   
Description: Servo amplifier mode setting: Profile Generator - position mode.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : no error)&quot;}">(Byte 6, 10 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – Acc, Dec, PosSpeed, Type, Mode, DPosAngle, DPosRevol**   
Description: Setting of the required acceleration, deceleration, speed and type of ramps of the Generator Profile.
In the last step, the zero desired position is entered (default state).

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A&quot;}">0x1A</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 25&quot;}" style="color:white;"><b>Byte 25</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 26&quot;}" style="color:white;"><b>Byte 26</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D0A2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F0B08F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 27&quot;}" style="color:white;"><b>Byte 27</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 28&quot;}" style="color:white;"><b>Byte 28</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 29&quot;}" style="color:white;"><b>Byte 29</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 30&quot;}" style="color:white;"><b>Byte 30</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 31&quot;}" style="color:white;"><b>Byte 31</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 32&quot;}" style="color:white;"><b>Byte 32</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 33&quot;}" style="color:white;"><b>Byte 33</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 34&quot;}" style="color:white;"><b>Byte 34</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 35&quot;}" style="color:white;"><b>Byte 35</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 36&quot;}" style="color:white;"><b>Byte 36</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 37&quot;}" style="color:white;"><b>Byte 37</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 38&quot;}" style="color:white;"><b>Byte 38</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 39&quot;}" style="color:white;"><b>Byte 39</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 40&quot;}" style="color:white;"><b>Byte 40</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 41&quot;}" style="color:white;"><b>Byte 41</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 42&quot;}" style="color:white;"><b>Byte 42</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 43&quot;}" style="color:white;"><b>Byte 43</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 44&quot;}" style="color:white;"><b>Byte 44</b></td>
	</tr>
	<tr>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 45&quot;}" style="color:white;"><b>Byte 45</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 46&quot;}" style="color:white;"><b>Byte 46</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10, 14, 18, 22 = 0 : no Error)&quot;}">(Byte 6, 10, 14, 18, 22 = 0 : no Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**K – Command**   
Description: SW enable.
After entering this command, the motor is under torque and rotates to the desired position (i.e., to position 0).
It is necessary to wait until the motor turns.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram&quot;}"><b>Telegram</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram&quot;}"><b>Telegram</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : no error)&quot;}">(Byte 5 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – PosSpeed**   
Description: Set the desired speed to zero.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegramm&quot;}"><b>Telegramm</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : no error)&quot;}">(Byte 5 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – Mode**   
Description: Setting the Generator Profile to speed mode.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : no error)&quot;}">(Byte 5 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – PosLimitAnglePosit, PosLimitRevolPosit, PosLimitAngleNegat, PosLimitRevolNegat**   
Description: Setting of position limits within one revolution and within multiple revolutions.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A&quot;}">0x1A</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x42&quot;}">0x42</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0F&quot;}">0x0F</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5,10 = 0 : no error)&quot;}">(Byte 5,10 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A&quot;}">0x1A</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – PosSpeed**   
Description: SW enable.
After entering this command, the motor is under torque and rotates to the desired position from the previous request.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Request&quot;}"><b>Request</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Response&quot;}"><b>Response</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : no error)&quot;}">(Byte 5 = 0 : no error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

##Extended description of Profile Generator parameters

| Parametername           | Description                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------|
| Acc                     | Required drive acceleration                                                                   |
| Dec                     | Required drive deceleration                                                                   |
| APosAngle               | Current drive position within one revolution                                                   |
| APosRevol               | Current drive position within the speed                                                         |
| DPosAngle               | Required drive position within one revolution                                                   |
| DPosRevol               | Required drive position within the speed                                                         |
| ASpeed                  | Current drive speed                                                                            |
| PosSpeed                | Required speed of movement in position mode                                                     |
| Speed                   | Required speed of movement in speed mode                                                        |
| Mode                    | Generator profile mode. 0 = speed, 1 = position, 2 (only read) = deceleration ramp signaling in position mode |
| Rdy                     | Signaling the completion of the drive movement. 1 = Position reached                            |
| Type                    | Velocity profile type 0 = harmonic unbalanced, 1 = harmonic symmetrical, 2 = fully harmonic, 3 = trapezoidal |
| BitsPerRevol            | Number of bits per revolution for the generator profile                                         |
| RotaryMode              | Special positioning mode within one revolution with a shorter path - use for direct motors. 1 = Rotary mode, 0 = Standard mode |
| PosOffsetAngle          | Position offset within one revolution                                                           |
| PosOffsetRevol          | Position offset within the speed                                                                |
| PosLimitAnglePosit      | Positive position limit within one revolution in the range from -2<sup>16</sup> to 2<sup>16</sup> |
| PosLimitRevolPosit      | Positive position limit within the number of revolutions in the range from -2<sup>16</sup> to 2<sup>16</sup> |
| PosLimitAngleNegat      | Negative position limit within one revolution in the range from -2<sup>16</sup> to 2<sup>16</sup> |
| PosLimitRevolNegat      | Negative position limit within the speed in the range from -2<sup>16</sup> to 2<sup>16</sup>   |
| DPosAngleRotary         | In "RotaryMode = 1", this parameter determines the desired position within one revolution      |
| AccMaxCurrentFeedForward| Current pre-correction                                                                        |
