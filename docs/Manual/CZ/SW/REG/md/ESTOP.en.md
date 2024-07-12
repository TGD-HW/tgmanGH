After activating the emergency stop, the drive decelerates via an adjustable deceleration ramp and the servo amplifier then disconnects the power supply to the motor.
If a static brake is implemented, it will be activated when the drive is stopped.   

The emergency stop function can be activated via:

- a fault in the drive that allows an emergency stop
- digital input
- protection function – for protection of communication buses.

Emergency stop function is available in `position` and `speed` modes: `2,3,6,7`

##Registers and parameters
###D-EmerDecRamp

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 21 | read-write |
| Drive | 4 | 21 | read-write |

mergency deceleration ramp deg/s, 1 up to 3600000 deg/s
	
###D-ErrorMaskEmerDec

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 23 | read-write |
| Drive | 4 | 23 | read-write |

Drive error mask for emergency deceleration, bits have the same meaning as the bits in the `aDriveError` register.
If the corresponding bit is set in the event of an error, the drive will perform an emergency stop if possible.
	
###D-DI_MaskEmerStop

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 24 | read-write |
| Drive | 4 | 24 | read-write |

The mask for digital inputs, inputs 1, 3, 5 can be assigned to axis 1 and inputs 2, 4, 6 can be assigned to axis 2.  
*Example: `D-DI_MaskEmerStop` (Ax.2) = 5, inputs 2 and 6 are assigned for an emergency stop. If one or both are not active, an emergency stop is performed.*   

###D-GuardTimeEmerStop

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 25 | read-write |
| Drive | 4 | 25 | read-write |

Protection timeout in ms. If the protection counter is not reset by this time, an emergency stop routine is performed. A value of 0 deactivates this function.   

###aDriveStatus

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 37 | read only |
| Monitoring | 20 | 37 | read only |

Bit 8 ... emergency stop ramp active   
Bit 9 ... emergency stop ramp completed   

###aDriveError

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 38 | read only |
| Monitoring | 20 | 38 | read only |

Bit 20 ... emergency stop activated by digital input or protection function.  

###aDriveWarning

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 39 | read only |
| Monitoring | 20 | 39 | read only |

Bit 20 ...condition for activating the emergency stop by a digital input or protection function. If the drive is not enabled.   

###GuardingCounter

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 126 | read only |
| Monitoring | 20 | 126 | read only |

Millisecond counter for protection function.
Can be reset by registering `K-ResetGuarding`.   

###ResetGuarding

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Command | 17 | 13 | read-write |
| Command | 18 | 13 | read-write |

Reset `GuardingCounter` by writing a value of `0xAA55`.
The value will be deleted automatically.

!!! Note "Note"
	The calculation of the emergency deceleration ramp is derived from the actual speed and position.
	In the event of a large position or speed error before performing an emergency stop, it can be observed that the speed and position curves are not smooth.
	The speed values in the user profile generator are now set to 0 after an error.