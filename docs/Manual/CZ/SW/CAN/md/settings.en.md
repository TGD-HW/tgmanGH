## Communication Speed Setting CAN
You can find it in the registry group called *Common*.

<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Register</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Description</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">C-CAN_Baudrate</td>
        <td bgcolor="#F2F2F2" style="color: black;">Register to enter the CAN communication speed in kilobauds (20,50,100,125,250,500,800,1000).<br>To receive the speed, the C-CAN_Settings register must be 0. The sampling point is fixed at 75%</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">C-CAN_Settings</td>
        <td bgcolor="#F2F2F2" style="color: black;">Register for more detailed CAN bus settings. If a non-zero value is entered, the C-CAN_Baudrate register is overwritten at the calculated rate.<br>Byte 0: TS1<br>Byte 1: TS2<br>Byte 2: SJ<br>Byte 3: Frequency divisor, the fundamental frequency is 16MHz.</td>
    </tr>
</table>

Example of setting the speed to 500kbaud:

| Parameter           | Value       |
|---------------------|-------------|
| SJ                  | 2           |
| TS1                 | 2           |
| SJ                  | 4           |
| Frequency divisor   | 11          |
| C-CAN_Settings      | **0x0202040b** |

## Receiving and Sending Messages

Settings for receiving and sending messages via CAN communication. You will find them in the *UserProg* registry group.

### CAN Status
<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Register</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Description</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Status</td>
        <td bgcolor="#F2F2F2" style="color: black;">bit 0: data sent, ready for the next one.<br>bit 1 - bit 8: new data in buffers 1-8.</td>
    </tr>
</table>

### Sending Messages
<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Register</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Description</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_ID</td>
        <td bgcolor="#F2F2F2" style="color: black;">CAN ID messages</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Len</td>
        <td bgcolor="#F2F2F2" style="color: black;">message length in bytes</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Data_Lo</td>
        <td bgcolor="#F2F2F2" style="color: black;">Sends the lower 32 bits of the message</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Data_Hi</td>
        <td bgcolor="#F2F2F2" style="color: black;">Sends the upper 32 bits of the message</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Control</td>
        <td bgcolor="#F2F2F2" style="color: black;">bit 1: sends a message<br>bit 2: sends an RTR request (remote transmission request). Then it must be set to 0</td>
    </tr>
</table>

To send a message, type `1` in the `CAN_Transmit_Control` registry. Before sending another message, it is necessary to write `0` to this register and wait for processing by the system. You can then send another message.

### Receiving Messages
<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Register</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Description</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Control</td>
        <td bgcolor="#F2F2F2" style="color: black;">Receipt control register.</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Recieve_Buffx_ID</td>
        <td bgcolor="#F2F2F2" style="color: black;">Receive ID for buffer x (x = 1 - 8).</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Buffx_Len</td>
        <td bgcolor="#F2F2F2" style="color: black;">Number of bytes in the received message.</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Buffx_Data_Lo</td>
        <td bgcolor="#F2F2F2" style="color: black;">Receives the bottom 32 bits of the message</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Buffx_Data_Hi</td>
        <td bgcolor="#F2F2F2" style="color: black;">Receives the top 32 bits of the message</td>
    </tr>
</table>

There are 8 buffers for receiving messages.
Not all messages from CAN are received, but only those to which the buffers are set.
`CAN_Recieve_Buff0_ID` (or another selected buffer) is set to the required ID.
A message with the corresponding ID is loaded into this buffer.
Subsequently, writing `0x1000` to the `CAN_Receive_Control` registry resets the message reception and accepts the `CAN_Receive_Buffx_ID` changes.
After the system processes the message, the `CAN_Receive_Control` registry value must be set to `0`.
After receiving the message, the bit for the specific buffer is set in the `CAN_Status` register.
To acknowledge receipt of the message, the corresponding buffer bit (same bit as in `CAN_Status`) is set in the `CAN_Recieve Control` register.
After processing by the system, the registers must be reset again.

!!! Note "Note"
    The standardized CAN protocol for TGZ is under development.
