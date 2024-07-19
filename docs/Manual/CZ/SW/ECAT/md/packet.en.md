EtherCAT Industrial Bus Communication Description

##Distributed Clock (DC)
The distributed clock feature is supported. Sync 1 signal period must be set to the same period as the PDO communication period.

##Process Data Objects (PDO)
The EtherCAT master can use the following PDO communication periods: 250 µs, 500 µs, 1000 µs, 2000 µs (50 µs for specific configuration). The servo drive uses a fixed PDO mapping described in the table below. PDO length is 44 bytes.

**Output PDO for Servo Drive**

<table style="text-align: left;">
    <tr>
        <td><b>Name</b></td>
        <td><b>Type</b></td>
        <td><b>Description</b></td>
    </tr>
    <tr>
        <td rowspan="5">PositionSetPoint_1 or<br>SpeedSetPoint_1</td>
        <td rowspan="5">Signed 64bit integer</td>
        <td><b>Position Mode (3):</b></td>
    </tr>
    <tr>
        <td>Desired position for servo drive 1. Resolution 32 bits/rev.<br>Example:<br>1.5 revolutions:<br>6442450944 = 0x0000000180000000<br>-1.5 revolutions:<br>-6442450944 = 0xFFFFFFFE80000000</td>
    </tr>
    <tr>
        <td><b>Speed Mode (10):</b></td>
    </tr>
    <tr>
        <td>Desired speed for servo drive 1.<br>Resolution 1 rev/min ~ 2^32<br>Example 500 rev/min:<br>2147483648000 = 0x1F4 0000 0000</td>
    </tr>
    <tr>
        <td>-500 rev/min:<br>-2147483648000 = 0xFFFF FE0C 0000 0000</td>
    </tr>
    <tr>
        <td>control_1</td>
        <td>Unsigned 32bit integer</td>
        <td>Control commands for servo drive 1.<br>Bit0 .. Clear errors.<br>Bit1 .. Enable power stage.<br>Bit28 .. Digital output 1<br>Bit29 .. Digital output 3<br>Bit30 .. Digital output 5</td>
    </tr>
    <tr>
        <td>currentSetPoint_1</td>
        <td>Signed 16bit integer</td>
        <td>Desired current for servo drive 1.<br>IqSetPoint = currentSetPoint_1 * M-Ipeak / 32767</td>
    </tr>
    <tr>
        <td>currentLimit_1</td>
        <td>Unsigned 16bit integer</td>
        <td>Current limit for servo drive 1.<br>IqLim = (32767 - currentLimit_1)* M-Ipeak / 32767<br>32767 .. full limit<br>0 .. no limit (maximum current = M- Ipeak)</td>
    </tr>
    <tr>
        <td rowspan="13">positionSetPoint_2<br>or<br>speedSetPoint_2</td>
        <td rowspan="13">Signed 64bit integer</td>
        <td><b>Position Mode</b> (3):<br>Desired position for servo drive 2.</td>
    </tr>
    <tr>
        <td>Resolution 32 bits/rev.</td>
    </tr>
    <tr>
        <td>Example of position mode (0x3):</td>
    </tr>
    <tr>
        <td>1.5 revolutions :</td>
    </tr>
    <tr>
        <td>6442450944 = 0x0000000180000000</td>
    </tr>
    <tr>
        <td>-1.5 revolutions :</td>
    </tr>
    <tr>
        <td>-6442450944 = 0xFFFFFFFE80000000</td>
    </tr>
    <tr>
        <td><b>Speed Mode (10):</b></td>
    </tr>
    <tr>
        <td>Desired speed for servo drive 2.</td>
    </tr>
    <tr>
        <td>Resolution 1 rev/min ~ 2^32</td>
    </tr>
    <tr>
        <td rowspan="3">Example:<br>500 rev/min:<br>2147483648000 = 0x1F4 0000 0000<br>-500 rev/min:<br>-2147483648000 = 0xFFFF FE0C 0000 0000</td>
    </tr>
    <tr></tr>
    <tr></tr>
    <tr>
        <td>control_2</td>
        <td>Unsigned 32bit integer</td>
        <td>Control commands for servo drive 2.<br>Bit0 .. Clear errors.<br>Bit1 .. Enable power stage.<br>Bit28 .. Digital output 2<br>Bit29 .. Digital output 4<br>Bit30 .. Digital output 6</td>
    </tr>
    <tr>
        <td>currentSetPoint_2</td>
        <td>Signed 16bit integer</td>
        <td>Desired current for servo drive 2.<br>IqSetPoint = currentSetPoint_2 * M-Ipeak / 32767</td>
    </tr>
    <tr>
        <td>currentLimit_2</td>
        <td>Unsigned 16bit integer</td>
        <td>Current limit for servo drive 2.<br>IqLim = (32767 - currentLimit_2)* M-Ipeak / 32767<br>32767 .. full limit<br>0 .. no limit (maximum current = M- Ipeak)</td>
    </tr>
    <tr>
        <td>Reserved_1</td>
        <td>Unsigned 32bit integer</td>
        <td></td>
    </tr>
    <tr>
        <td>Reserved_2</td>
        <td>Unsigned 32bit integer</td>
        <td></td>
    </tr>
    <tr>
        <td>Reserved_3</td>
        <td>Unsigned 32bit integer</td>
        <td></td>
    </tr>
</table>

**Input PDO from servo-drive**

<table style="text-align: left;">
    <tr>
        <td colspan="2"><b>Name</b></td>
        <td colspan="2"><b>Type</b></td>
        <td colspan="3"><b>Description</b></td>
    </tr>
    <tr>
        <td colspan="2">positionActValue_1</td>
        <td colspan="2">Signed 64bit integer</td>
        <td colspan="3">Actual position of servo drive 1.<br>Resolution 32 bits/rev.<br>Example:<br>1.5 revolutions:<br>6442450944 = 0x0000000180000000<br>-1.5 revolutions:<br>-6442450944 = 0xFFFFFFFE80000000</td>
    </tr>
    <tr>
        <td colspan="2">positionActValue_2</td>
        <td colspan="2">Signed 64bit integer</td>
        <td colspan="3">Actual position of servo drive 2.<br>Resolution 32 bits/rev.<br>Example:<br>1.5 revolutions:<br>6442450944 = 0x0000000180000000<br>-1.5 revolutions:<br>-6442450944 = 0xFFFFFFFE80000000</td>
    </tr>
    <tr>
        <td colspan="2">positionActValueExt</td>
        <td colspan="2">Signed 32bit integer</td>
        <td colspan="3">External feedback position E.</td>
    </tr>
    <tr>
        <td colspan="2">status_1</td>
        <td colspan="2">Unsigned 32bit integer</td>
        <td colspan="3">Status of servo drive 1.<br>Bit0 .. Power stage enabled – under<br>voltage.<br>Bit1 .. active HW enable.<br>Bit2 .. active Software enable.<br>Bit3 .. motor brake released.<br>Bit4 .. No error.<br>Bit5 .. Initialization.<br>Bit6 .. Fieldbus mode.<br>Bit28 .. Digital input 1<br>Bit29 .. Digital input 3<br>Bit30 .. Digital input 5<br>Bit31 .. Digital input 7</td>
    </tr>
    <tr>
        <td colspan="2">status_2</td>
        <td colspan="2">Unsigned 32bit integer</td>
        <td colspan="3">Status of servo drive 2.<br>Bit0 .. Power stage enabled – under<br>voltage.<br>Bit1 .. active HW enable.<br>Bit2 .. active Software enable.<br>Bit3 .. motor brake released.<br>Bit4 .. No error.<br>Bit5 .. Initialization.<br>Bit6 .. Fieldbus mode.<br>Bit28 .. Digital input 2<br>Bit29 .. Digital input 4<br>Bit30 .. Digital input 6<br>Bit31 .. Digital input 8</td>
    </tr>
    <tr>
        <td colspan="2">analogInput_1</td>
        <td colspan="2">Unsigned 16bit integer</td>
        <td colspan="3">Actual value of analog input 1.<br>0 .. 0V , 32767 .. 10V</td>
    </tr>
    <tr>
        <td colspan="2">analogInput_2</td>
        <td colspan="2">Unsigned 16bit integer</td>
        <td colspan="3">Actual value of analog input 2.<br>0 .. 0V , 32767 .. 10V</td>
    </tr>
    <tr>
        <td colspan="2">currentqActValue_1</td>
        <td colspan="2">Signed 16bit integer</td>
        <td colspan="3">-32768 .. -M-Ipeak, 32767 .. M-Ipeak<br>I = M-Ipeak * currentqActValue / 32767</td>
    </tr>
    <tr>
        <td colspan="2">currentqActValue_2</td>
        <td colspan="2">Signed 16bit integer</td>
        <td colspan="3">-32768 .. -M-Ipeak, 32767 .. M-Ipeak<br>I = M-Ipeak * currentqActValue / 32767</td>
    </tr>
    <tr>
        <td colspan="2">mappedParameter_1</td>
        <td colspan="2">Unsigned 32 bit integer</td>
        <td colspan="3">Register value defined in parameter C-MappingPar1</td>
    </tr>
    <tr>
        <td colspan="2">mappedParameter_2</td>
        <td colspan="2">Unsigned 32 bit integer</td>
        <td colspan="3">Register value defined in parameter C-MappingPar2</td>
    </tr>
</table>
		
##Service data objects (SDO)
For SDO the used protocol is CAN Open over EtherCAT (CoE).

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;MailBox output&quot;}"><b>MailBox output</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;MailBox input&quot;}"><b>MailBox input</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}">Byte 0</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Length of the data (Low Byte)&quot;}">Length of the data (Low Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}">Byte 1</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Length of the data (High Byte)&quot;}">Length of the data (High Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}">Byte 2</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Address (Low Byte)&quot;}">Address (Low Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}">Byte 3</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Address (High Byte)&quot;}">Address (High Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}">Byte 4</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 0 to 5: Channel<br>Bit 6 to 7: Priority&quot;}">Bit 0 to 5: Channel<br>Bit 6 to 7: Priority</td>
	</tr>
	<tr>
		<td rowspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}">Byte 5</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 0 to 3: Type =<br>3 : Can over EtherCAT&quot;}">Bit 0 to 3: Type =<br>3 : Can over EtherCAT</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 4 to 7: Reserved&quot;}">Bit 4 to 7: Reserved</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}">Byte 6</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PDO Number (with PDO transmissions only, Bit 0 = LSB of the PDO number, see Byte 7 for MSB)&quot;}">PDO Number (with PDO transmissions only, Bit 0 = LSB of the PDO number, see Byte 7 for MSB)</td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}">Byte 7</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 0: MSB of the PDO number, see Byte 6&quot;}">Bit 0: MSB of the PDO number, see Byte 6</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 1 to 3: Reserved&quot;}">Bit 1 to 3: Reserved</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 4 to 7: CoE specific type =<br>2 : SDO request&quot;}">Bit 4 to 7: CoE specific type =<br>2 : SDO request</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 4 to 7: CoE specific type =<br>3: SDO response&quot;}">Bit 4 to 7: CoE specific type =<br>3: SDO response</td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}">Byte 8</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Control-Byte in the CAN telegram:&quot;}">Control-Byte in the CAN telegram:</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Write access 0x2? .. 4byte&quot;}">Write access 0x2? .. 4byte</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Write: OK 0x2? Error 0x80&quot;}">Write: OK 0x2? Error 0x80</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Read access 0x4? .. 4byte&quot;}">Read access 0x4? .. 4byte</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Read: OK 0x4? Error 0x80&quot;}">Read: OK 0x4? Error 0x80</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}">Byte 9</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Low Byte of the CAN object number (Parameter number)&quot;}">Low Byte of the CAN object number (Parameter number)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}">Byte 10</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;High Byte of the CAN object number (Parameter group number)&quot;}">High Byte of the CAN object number (Parameter group number)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}">Byte 11</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Subindex according to CANopen Specification (not used)&quot;}">Subindex according to CANopen Specification (not used)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}">Byte 12</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data (Low Byte)&quot;}">Data (Low Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}">Byte 13</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data&quot;}">Data</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}">Byte 14</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data&quot;}">Data</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}">Byte 15</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data (High Byte)&quot;}">Data (High Byte)</td>
	</tr>
</table>

##Registers

| Name                 | Description                                                                                     |
|----------------------|-------------------------------------------------------------------------------------------------|
| C-ID                 | TGZ EtherCAT alias.                                                                            |
| C-SetCycleTime       | Parameter must be set to the right value of the fieldbus communication period.                 |
| C-SyncTime           | Actual measured period of generated sync signal (only for DC).                                 |
| C-MapingPar1         | Address of selected parameter for PDO mapping 1.                                                |
| C-MapingPar2         | Address of selected parameter for PDO mapping 2.                                                |
| Monitoring-PacketTime| Actual measured period between fieldbus packets.                                                |

