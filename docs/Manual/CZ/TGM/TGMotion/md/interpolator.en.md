The CNC is a software module that executes a sequence of motion (G-instruction) and input/output commands (M-function) given by the G-code.
It includes the Interpolator module.

##Interpolator
The interpolator module calculates the positions and speeds of the individual servo drives (axes) so that the resulting motion is uniformly performed by all axes.
There is linear interpolation (motion along a straight line), circular interpolation (motion along a circle performed by two arbitrary axes), or helical interpolation (two axes perform motion along a circle, the others perform linear motion).
To calculate three independent final trajectories for multi-axis motion, TG Motion offers three independent interpolators, each of which can operate up to ten actuators.
The shared memory `TGM_Interpolator` serves as an interface between the CNC module and other applications (PLC, Win applications).
Most registers are read-only and display the current CNC module values.
Since the G-code is usually written in units of [mm], the Interpolators also work with units of [mm].
To set the conversion [mm] to [inc], use the Command structure or the Ratio register (see below).

![Interpolator Block Diagram](../img/interpolatorBlock.png){: style="width:100%;" }

## PLC and Windows application competence
###PLC 
It sets the basic parameters of the Interpolator, operates M-functions and solves the emergency stop of the Interpolator.
The Interpolator cannot be started from the PLC.

###Windows applications
They convert the G-code into binary intercode, fill the Interpolator buffer in shared memory with it, and start and stop the Interpolator.
The Interpolator buffer is not accessible from PLC or Windows applications.

##G-code
G-code is the name of the programming language that controls NC and CNC machine tools.
This is a code in text format that tells the machine tool what action to perform.
In G-code, the most commonly used commands include Ginstruct and M-function.
They are always prefixed with a letter (G, M) and a numeric parameter that specifies what the instruction should do.
The individual G-instructions are precisely defined, most of the M-functions can be defined by the user.

###Example of part of the G-code

``` gcode
G00 X60.6051 Y40.7723
G42
M51
G02 X0 Y-2.5202 I3.0336 J-1.2601
G02 X0.922 Y-1.5646 I6.0604 J2.5173
G02 X1.079 Y-1.0269 I4.2143 J3.3479
G02 X2.2624 Y-1.3678 I9.8772 J13.7817
G02 X1.9856 Y-0.8109 I6.1778 J12.2908
G02 X3.015 Y-0.7892 I8.8515 J27.6632
G02 X6.2889 Y0 I3.1444 J33.011
M50
G40
G00 X-28.9085 Y30.4365
G42
M51
G40
M2
```

###G-instructions
They are mostly used for fast positioning, sliding movement along a straight line or arc, drilling or cutting.
The Interpolator takes care of their execution. The execution of G-instructions can be interrupted by M-functions.
In this case, the Interpolator can wait for the M-function to execute and then continue executing the G-code.

###Table of G-instructions

| Marking | Description |
|---|---|
| **Basic G-instructions** |
| G0 | Quickdraw |
| G1 | Linear interpolation |
| G2 | Circular interpolation CW |
| G3 | Circular interpolation CCW |
| G4 | Delay [sec] |
| G25 | Calling a subroutine |
| G26 | Cycle call |
| G27 | Program jump |
| G29 | Instructions or text note |
| G40 | Cancel correction |
| G41 | Correction to the left of the contour |
| G42 | Correction to the right of the contour |
| G53 | Zero point offset cancellation |
| G54 | Zero point displacement |
| **Extended G-instructions** | |
| G90 | Absolute Programming |
| G91 | Incremental programming |
| G92 | Setting coordinate values |

###M-functions
If any M-function is part of the code, its handling must be ensured in the user PLC code.
The interpolator does not deal with M-functions, it just waits for some of them to be processed.
M-functions can be user-defined with exceptions (see the M_Function_Parameter register).

###Movement and continuous M-functions
Motion M-functions (Mx, where x < 1000) - the execution of the G-code is stopped, the PLC services the M-function and after its completion sets the register `M_Func = 0`.
The interpolator then continues to execute the G-code with the next instruction.
Continuous M-functions (Mx, where x > 1000) - the PLC starts servicing the M-function, but the Interpolator does not wait for the M-function to be serviced and continues executing the G-code.

###Table of supported M-functions

| Marking | Description |
|---|---|
| M0 | Program stop |
| M2 | G-code termination, can be redefined |
| M3 | CW spindle rotation, can be redefined |
| M4 | CCW spindle rotation, can be redefined |
| M5 | Spindle stop, can be redefined |
| M6 | Tool change, can be redefined |
| M7 | Cooling on, can be redefined |
| M8 | Enable erasing, can be redefined |
| M9 | Cooling and lubrication shutdown, can be redefined |
| M17 | Return from subroutine (RETURN), can be redefined |
| M29 | Text message output (PRINT), can be redefined |
| M30 | G-code termination, can be redefined |
| M80 | Mirroring off |
| M81 | X-axis mirroring |
| M82 | Mirroring in the y-axis |
| M83 | Mirroring in z-axis |
| M84 | Mirroring in x and y axes |
| M85 | Mirroring in x and z axes |
| M86 | Mirroring in y and z axes |
| M87 | Mirroring in x, y and z axes |
| M99 | Define default feed value, can be redefined |

##Trajectory smoothing
G-code often works with polynomials composed of short segments, and sometimes instantaneous speed changes can occur due to incorrectly written code.
Any instantaneous changes in speed can result in undesirable acceleration in some of the axes and thus mechanical shock in some of the actuators.
Two tools are used to smooth the calculated trajectory.

##Spline
###Spline - smoothing function

The Spline function should be used in the case of incorrectly created G-codes, in which individual sections on the
do not follow each other smoothly or continuously, or in the case of G-codes in which the resulting trajectory is created by
of linear segments with coarse division. Spline is also useful for smoothing out the step change in velocity that results from
from a mathematical model of mechanics (e.g. tilting heads).   

The Spline function is activated in all axes at the same time, it cannot be applied to only some axes. When activated
the change in acceleration (jerk) is controlled in each axis. If a change greater than the allowed change is found, it will interleave the
with a spline curve at that location.

!!! info "Warning"
	The longer the spline length (the size of the spline buffer), the better the smoothing.
	Smoothing with Spline is at the expense of positioning accuracy.
	
###Activation and parameterization of Spline
The Spline function is activated and parameterized by the Command structure of the Interpolator.
For the register value `Command = -2` the Command parameters have the following meaning:

`Command_Parameter[0]` - specifies the number of points through which the spline is interleaved. This determines the size of the spline buffer. 
The parameter setting range is 50-500 points/steps. 
With `Cycle_Time = 500 μs` the calculation step is 100 μs, with `Cycle_Time = 250 μs` the calculation step is 50 μs.
Disabling the spline function is possible by setting the spline length to zero (`Command_Parameter[0] = 0`).   

`Command_Parameter[1]` - defines the limit of the acceleration change evaluation (jerk), i.e. from which acceleration the Spline function is activated.
It is expressed in units of [mm/s³].
The appropriate setting value is 1 000 000 mm/s³.   

After setting both parameters, the Command register must be set to -2.
After the TG Motion command is executed, this register is reset.

###Movement delay
The movement after passing the Spline function is delayed by the length of the Spline buffer compared to the positioning calculated by the interpolator.
All axes are always positioned synchronously because the buffer size is the same for all axes.
Even M-functions are called synchronously with the resulting motion, because the same buffer size is used for them.

###Example of Spline setup
Example of enabling the Spline function with a spline length of 20 ms (with `Cycle_Time = 500 μs`).
The Command_Parameter values must be set first and the last register value `Command = -2`.

``` cpp
Interpolator.Command_Parameter[0] = 200;
Interpolator.Command_Parameter[1] = 1000000;
Interpolator.Command = -2;
```

##IIR Filter
###IIR Filter - smoothing function

The IIR Filter (Infinite Impulse Response) can be used to smooth the resulting motion speed and remove unwanted rapid changes.
It is a mathematical model of a linear low-pass filter with a steepness of 12 dB per octave (2-Pole) calculated according to the relation:

$$
H(s) = \frac{q}{s^2 + p \cdot s + q}
$$

with the possibility of setting three parameters:

-	*p, q* - parameters setting the filter waveform (see table)
-	*f (cutoff)* - time for the filtered trajectory to return to the original calculated trajectory

###Parameter values for some filter types

| p | q | filter type | description |
| --- | --- | --------------- | ------------------------------------------------ |
| √2 | 2 | Butterworth | there is a stroke before f, small delay |
| 3 | 3 | Bessel | slight stroke, smooth progression, more delay |
| 2 | 1 | critically damped | smooth gradual progression without stroke, largest delay |

![Graphical representation of the progress of some filter types](../img/filterChar.png){: style="width:50%;" }

###Activation and parameterization of IIR Filter
The IIR Filter parameter values can be set using the Command structure.
For the register value `Command = -1` the Command parameters have the following meaning:

- `Command_Parameter[0]` - sets the parameter p of the filter.
- `Command_Parameter[1]` - sets the q parameter of the filter.
- `Command_Parameter[2]` - specifies f - time of return to the original trajectory.

!!! info "Warning"
	Parameter values are of type `Integer`, the actual physical value of the parameter is obtained by dividing the parameter value by $1 \cdot 10^6$ (`Command_Parameter[1] = 1000000`, filter parameter = 1,0).
	
- `Command_Parameter[3]` - sets the filter activity bit mask for each axis.
   Only the first 10 bits are used for the 10 axes, the other bits are ignored (see registers).

###Movement delay
**IIR Filters** delay the calculated movement.
The delay depends on the input data, it varies dynamically and its size cannot be determined in advance.
The M-functions are signaled from the running G-code when the Interpolator is "stationary", but the physical movement of the actuators does not have to be completed yet.							

!!! info "Warning"
	When using the IIR Filter, the actuator will "float" behind the Interpolator and it is always necessary to wait until the physical movement of all actuators is actually complete.

The setting of IIR Filter parameters is common for all Interpolator axes.
The filter can be activated independently for each axis according to the `Command_Parameter[3]` register bit mask.
It is therefore necessary to take into account that the resulting movement of the axes after the filter application may not be synchronous with each other as originally calculated.

##Command Structure
###Registry Command_Parameter

This chapter describes the meaning of the `Command_Parameter[ ]` registers for selected values of the Command register.

###Setting gear ratio mm to inc - Command = 1024
The G-code usually works implicitly with the unit [mm], so the Interpolator also works in units of [mm].
Since servo drives work with increments [inc], it is necessary to determine the gear ratio *inc/mm* according to the number of inc/turn of the servo drive (`Servo[x].Resolution`).
It is set using the Command structure of the corresponding Interpolator.
The calculated position in the given axis is then multiplied by the transmission ratio and the calculated position is then sent to the actuator.

| Command_Parameter | description |
| ---------------- | ----------------------------------------- |
| 0 | specifies the axis number for which the ratio is set [0-9] |
| 1 | gear ratio counter [inc] |
| 2 | gear ratio denominator [mm] |

###Setting the current position - Command = 2048 and Command = 2049
Use Command = 2048 and Command = 2049 to set the current position of the interpolator.
After executing the 2048 command, the system reports the position on the trajectory, in the second case the position off the trajectory.
For both variants, all Command_Parameter[0-9] take on the same meaning.

| Command_Parameter | description |
| ---------------- | --------------------------------- |
| 0 | current position in axis 0 [inc] |
| ... | ... |
| 9 | current position in axis 9 [inc] |

###Setting IIR Filter parameters - Command = -1

| Command_Parameter | description |
| ---------------- | --------------------------------------------------------------------------------------- |
| 0 | Filter parameter p - setting the filter waveform (in combination with parameter q) |
| 1 | Filter parameter q - setting the filter waveform (in combination with parameter p) |
| 2 | filter parameter f - time for the filtered trajectory to return to the original trajectory |
| 3 | IIR Filters activity bitmask for each axis of the Interpolator. Example: xxxx xx00 0000 0101 - only IIR Filter for axis 0 and axis 2 is active |

###Setting Spline parameters - Command = -2

| Command_Parameter | description |
| ---------------- | --------------------------------------------------------------------------- |
| 0 | Specifies the number of points that the spline is interleaved with; the setting range is 50-500 points |
| 1 | upper limit of acceleration change evaluation [mm/s³] |

##LookAheadBuffer structure
###Description of the structure

The **LookAheadBuffer** structure is a table of important parameters of eight sections - G-code items following
to each other. The first item in the table is always the section currently being performed, the next items are the seven immediately
the following sections.   

**LookAheadBuffer** acts as a shift buffer. When the current section is executed, the table data is shifted,
the first one is again the currently executing section and the 8th following section from the currently executing section is inserted in the last place.
The LookAheadBuffer structure is filled by the Interpolator. From the PLC point of view, its registers are read-only.

###The G-code section
A segment is a single G-code item, either a G-instruction (G0-G3) or a motion M-function that has meaning in terms of motion (M3-M999).

##Using the structure
The **LookAheadBuffer** structure is used to customize the technology according to the instructions and functions of the following sections,
or according to their values. Since the Interpolator cannot be started or stopped from the PLC (except for emergency stops), it is
it is necessary to handle everything necessary during the operation of existing M-functions. This must be ensured by the PLC code author.
During the M-function, the PLC can, for example, change the angle of the machining head in the corner of the square according to the tangent of the following
function; it can use the Rel_Speed register to slow down the motion if it knows that a large tangent change will follow.
When moving in a circle, a tangent is available at all times and can be used to turn the head. When
short segments can also be smoothed by gradually turning the head to smooth the broken line. To perform all these operations
it is necessary to know what will follow the section you are currently performing. For this purpose, the structure can be used
LookAheadBuffer.

!!! info "Warning"
	Sometimes a negative M-function number may appear in the `Movement_Code` register for `Movement_Type = 2`.
	This is an internal function of TG Motion that does not need to be manipulated.
	
The individual registers of the LookAheadBuffer structure are described in the Appendix chapter.

##Apendix
###Overview and description of registers of the Interpolator structure

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;name&quot;}"><b>name</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;access&quot;}"><b>access</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;description&quot;}"><b>description</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number&quot;}">Number</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="0" sdnum="1029;">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;interpolator number, can take values 0, 1, 2&quot;}">interpolator number, can take values 0, 1, 2</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number_Axes&quot;}">Number_Axes</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4" sdnum="1029;">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number of axes the interpolator works with; the allowed range is 1-10&quot;}">number of axes the interpolator works with; the allowed range is 1-10</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Buffer_Size&quot;}">Buffer_Size</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="8" sdnum="1029;">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximum number of G-code sections, values allowed are 1000-100000&quot;}">maximum number of G-code sections, values allowed are 1000-100000</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="12" sdnum="1029;">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;command:&yen;u000a4 = emergency stop on trajectory&yen;u000a5 = emergency stop (after stop reports off trajectory)8 = normal stop on trajectory&yen;u000a9 = normal stop (off trajectory)&yen;u000a1024 = gear ratio setting (mm per inc) - see chap. Command 2048 = current position setting (on trajectory) - see chap. Command 2049 = setting the current position (off-trajectory) - see chap. Command&yen;u000a-1 = setting IIR Filter parameters - see chap. Command&yen;u000a-2 = Spline parameter settings - see chap. Command&quot;}">command:<br>4 = emergency stop on trajectory<br>5 = emergency stop (after stop reports off trajectory)8 = normal stop on trajectory<br>9 = normal stop (off trajectory)<br>1024 = setting of gear ratios (mm per inc) - see chap. Command 2048 = current position setting (on trajectory) - see chap. Command 2049 = set current position (off-trajectory) - see chap. Command<br>-1 = setting IIR Filter parameters - see chap. Command<br>-2 = Spline parameter settings - see chap. Command</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command_Parameter [0-11]&yen;u000a(12 registers)&quot;}">Command_Parameter [0-11]<br>(12 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="16" sdnum="1029;">16</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;12 integer type parameters whose meaning and values depend on the Command function type&quot;}">12 integer type parameters whose meaning and values depend on the Command function type</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command_Status&quot;}">Command_Status</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="64" sdnum="1029;">64</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;current status of the executed command:&yen;u000a0 = the previous command was successfully executed and the next command can be activated 1 = the current command is executing&yen;u000a-1 = an error occurred during the execution of the command&quot;}">current status of the executed command:<br>0 = the previous command was successfully executed and the next command can be activated 1 = the current command is executing<br>-1 = an error occurred during the execution of the command</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status&quot;}">Status</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="68" sdnum="1029;">68</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;current interpolator state:&yen;u000a1 = trajectory movement in progress 3 = stop at end of trajectory&yen;u000a4 = at least one trajectory segment in buffer, start can be called 6 = stopping after crash ramp&yen;u000a7 = interpolator stopped after crash ramp&yen;u000a8 = interpolator stopped during buffer fill&quot;}">current interpolator status:<br>1 = trajectory movement in progress 3 = stop at end of trajectory<br>4 = at least one trajectory segment in buffer, start can be called 6 = stopping after crash ramp<br>7 = interpolator stopped after crash stop<br>8 = interpolator was stopped during buffer filling</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_Part&quot;}">Act_Part</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="72" sdnum="1029;">72</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number of the currently executing section&quot;}">number of the currently executing section</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Address_External_Position&quot;}">Address_External_Position</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="76" sdnum="1029;">76</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset of the TGM_Data address where the position of the external sensor is stored; the value is of type integer&quot;}">offset of the TGM_Data address where the position of the external sensor is stored; the value is of type integer</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M_Func&quot;}">M_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="80" sdnum="1029;">80</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;value of M-function; for M<1000 Interpolator stops and waits for this value to reset; then continues with the next section; for M>1000 continues executing G-code&quot;}">M-function value; for M &lt; 1000 the Interpolator stops and waits for this value to be reset; then continues with the next section; for M &gt; 1000 it continues executing the G-code</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_G_Func&quot;}">Act_G_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="84" sdnum="1029;">84</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;value of the currently executing G-instruction&quot;}">value of the currently executing G-instruction</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_M_Func&quot;}">Act_M_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="88" sdnum="1029;">88</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;value of the currently executing M-function&quot;}">value of the currently executing M-function</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Last_Cont_M_Func&quot;}">Last_Cont_M_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="92" sdnum="1029;">92</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;stored value of the last continuous M-function (M>1000)&quot;}">stored value of the last continuous M-function (M &gt; 1000)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Run_Flag&quot;}">Run_Flag</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="96" sdnum="1029;">96</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;- the lower 16 bits show the state of the current section:&yen;u000a0 = STOP (interpolator is inactive)&yen;u000a1 = RUN (motion G-instruction is executed) 2 = WAIT_WINDOW (for rotary machining) 3 = WAIT_PULSE (for rotary machining)&yen;u000a4 = WAIT_MFUNC (M-function execution has started)&yen;u000a5 = WAIT_MFUNC_WAIT_FOR_END (waiting for M-function to finish)&yen;u000a- the upper 16 bits are the status of the speed progress:&yen;u000a1 = no movement 2 = accelerating&yen;u000a3 = reaching the desired movement speed 4 = decelerating&yen;u000a5 = next speed section&yen;u000a6 = decelerating on the last section 7 = decelerating after a crash ramp&yen;u000note.: from TGM420 version&quot;}">- the lower 16 bits show the status of the current section:<br>0 = STOP (interpolator is inactive)<br>1 = RUN (motion G-instruction is executed) 2 = WAIT_WINDOW (for rotary machining) 3 = WAIT_PULSE (for rotary machining)<br>4 = WAIT_MFUNC (M-function execution has started)<br>5 = WAIT_MFUNC_WAIT_FOR_END (waiting for M-function to finish)<br>- the upper 16 bits are the status of the speed progress:<br>1 = no motion 2 = accelerating<br>3 = desired motion speed reached 4 = decelerating<br>5 = next speed section<br>6 = decelerating on last section 7 = decelerating after emergency ramp<br>notefrom TGM420 version</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tool_Number&quot;}">Tool_Number</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="100" sdnum="1029;">100</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number of the current tool (drilling, milling, ...)&yen;u000apozn.: from version TGM420&quot;}">number of the current tool (drilling, milling, ...)<br>note: from version TGM420</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Orig_Position (10 registers)&quot;}">Orig_Position (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="376" sdnum="1029;">376</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;calculated coordinates of all axes [mm]&quot;}">calculated coordinates of all axes [mm]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Position (10 registers)&quot;}">Position (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="456" sdnum="1029;">456</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Spline or IIR Filter adjusted coordinates [mm]&quot;}">Spline or IIR Filter adjusted coordinates [mm]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PositionInc (10 registers)&quot;}">PositionInc (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="536" sdnum="1029;">536</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Position coordinates multiplied by Ratio [inc]&quot;}">Position coordinates multiplied by Ratio [inc]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Backlash (10 registers)&quot;}">Backlash (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="616" sdnum="1029;">616</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;current clearance value for each axis [inc]&quot;}">current clearance value for each axis [inc]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Offset (10 registers)&quot;}">Offset (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="696" sdnum="1029;">696</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset values are added to PositionInc, these values are set by the user [inc]&quot;}">offset values are added to PositionInc, these values are set by the user [inc]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Speed (10 registers)&quot;}">Speed (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="776" sdnum="1029;">776</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;current speed of each axis after Spline and IIR [mm&yen;/s]&quot;}">current speed of each axis after Spline and IIR [mm/s]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ratio (10 registers)&quot;}">Ratio (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="856" sdnum="1029;">856</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;conversion ratio (multiplier) of G-code units (usually mm) to increments (actuator positions)&quot;}">conversion ratio (multiplier) of G-code units (usually mm) to increments (actuator positions)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M_Function_Parameter&yen;u000a(32 registers)&quot;}">M_Function_Parameter<br>(32 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="936" sdnum="1029;">936</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;parameters of M function from G-code, total of 26 values by letters in alphabet; some letters cannot be used because they are reserved by the system&yen;u000reserved parameters (indexes are counted from 0): G = index 6&yen;u000aM = index 12 N = index 13&yen;u000aP = index 15&quot;}">parameters of the M function from the G-code, a total of 26 values by letters in the alphabet; some letters cannot be used because they are reserved by the system<br>reserved parameters (indices are counted from 0): G = index 6<br>M = index 12 N = index 13<br>P = index 15</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rel_Speed&quot;}">Rel_Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="1192" sdnum="1029;">1192</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;relative rate of interpolated motion, coefficient in the range 0.01-2 (1-200%)&quot;}">relative rate of interpolated motion, coefficient in the range 0.01-2 (1-200%)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Set_Speed&quot;}">Set_Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="1200" sdnum="1029;">1200</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;required speed from G-code (given by G-code F-instruction or speed table) [mm&yen;/min]&quot;}">required speed from G-code (given by G-code F-instruction or speed table) [mm/min]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_Speed&quot;}">Act_Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="1208" sdnum="1029;">1208</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;current speed [mm&yen;/min]&quot;}">current speed [mm/min]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Move_Distance&quot;}">Move_Distance</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="1216" sdnum="1029;">1216</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;current total distance travelled [mm]&quot;}">current total distance travelled [mm]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;LookAheadBuffer&quot;}">LookAheadBuffer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="2048" sdnum="1029;">2048</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;table of information about the sections that will follow; a total of 8 items of the structure described&yen;u000in the following table; the first item describes the section currently being executed; the size of each item is 1792 bytes&yen;u000note.: from TGM420 version&quot;}">table of information about the sections that will follow; a total of 8 structure items described<br>in the following table; the first item describes the section currently being executed; the size of each item is 1792 bytes<br>note: from TGM420 version</td>
	</tr>
</table>


###Overview and description of registers of the LookAheadBuffer structure

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;name&quot;}"><b>name</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;access&quot;}"><b>access</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;description&quot;}"><b>description</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;AllParams&yen;u000a(26 registers)&quot;}">AllParams<br>(26 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="0" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;all specified M-function addresses from a particular G-code for a given section (26 letters of English<br>abecedent)&quot;}">all specified M-function addresses from a particular G-code for a given section (26 letters of English<br>abecedent)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tangent&quot;}">Tangent</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="208" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 208}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">208</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;the current tangent of motion in the XY plane; if the currently executed segment is an arc (G2 or G3),&yen;u000the tangent changes continuously; for future segments, determines the initial tangent of motion&quot;}">current tangent of motion in the XY plane; if the currently executed segment is an arc (G2 or G3),<br>the tangent changes continuously; for future segments it determines the initial tangent of motion</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;MovementType&quot;}">MovementType</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="216" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 216}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">216</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;record-type:&yen;u000a0 = invalid record (number of legs remaining to be executed is less than the current index of the LookAheadBuffer table), less than 8 legs remain before the end of motion execution&yen;u000a1 = motion function (G0, G1, G2, G3) 2 = M function&quot;}">record type:<br>0 = invalid record (number of remaining legs to execute is less than the current index of the LookAheadBuffer table), less than 8 legs remain before the end of motion execution<br>1 = motion function (G0, G1, G2, G3) 2 = M function</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;MovementCode&quot;}">MovementCode</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="220" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 220}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">220</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;G-instruction or motion M-function number (the number of the continuous M-function does not appear in this register but appears in AllParams in the letter M)&quot;}">G-instruction or motion M-function number (the number of the continuous M-function does not appear in this register but appears in AllParams in the letter M)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Plane&quot;}">Plane</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="224" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 224}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">224</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;- plane of circular interpolation: 17 = XY&yen;u000a18 = XZ&yen;u000a19 = YZ&yen;u000a- other planes not defined&quot;}">- plane of circular interpolation: 17 = XY<br>18 = XZ<br>19 = YZ<br>- other planes not defined</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tool&quot;}">Tool</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="228" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 228}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">228</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;tool number&quot;}">tool number</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;EndPos (10 registers)&quot;}">EndPos (10 registers)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="232" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 232}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">232</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;end position of each axis section [mm] (absolute coordinates)&quot;}">end position of each axis section [mm] (absolute coordinates)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;StartAngle&quot;}">StartAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="312" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 312}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">312</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;initial arc angle [°] - angle of the arc center's junction with the origin; the&yen;u000register value is cyclic (0-360); for linear motion or M-functions, the register value is greater than 1038&quot;}">initial arc angle [°] - the angle of the arc center's junction with the initial point; the<br>register value is cyclic (0-360); for linear motion or M-functions, the register value is greater than 1038</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;EndAngle&quot;}">EndAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="320" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 320}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">320</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;arc end angle [°] - the angle of union of the arc center with the end point; the register value is cyclic (0-360); for linear motion or M-functions, it is greater than 1038&quot;}">arc end angle [°] - angle of the arc center's junction with the end point; the register value is cyclic (0-360); for linear motion or M-function it is greater than 1038</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Radius&quot;}">Radius</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="328" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 328}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">328</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;- radius of arc [mm]&yen;u000a- for linear motion or M-functions the register is zero&quot;}">- radius of arc [mm]<br>- for linear motion or M-functions the register is zero</td>
	</tr>
</table>
