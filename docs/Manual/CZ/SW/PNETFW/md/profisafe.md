# TGZ
# PROFIsafe internal technical specification

Document revision:

REVISION | COMMENT
---------|-------
11/2024	 | Initial document version

PROFINET is registered trademark of PROFIBUS and PROFINET International (PI).  
Note: Technical changes that improve the properties of the device may be made without prior notice!  
This document is the intellectual property of TG Drives. All rights reserved. No part of this work may be reproduced in any form (by copying or otherwise), processed, copied or distributed electronically without the written permission of TG Drives.  
Printed in the Czech Republic.
 
 
#	About this technical description

 
#	General
##	Available safety functions

Abbr. | Function                              | Category      | PROFIsafe | DI  | Permanent
------|---------------------------------------|---------------|-----------|-----|----------
STO	  | Safe torque off                       | Safe stop     | Yes       | Yes | No
SS1	  | Safe stop 1 (time based)              | Safe stop     | Yes       | Yes | No
SS2	  | Safe stop 2 (deceleration monitoring) | Safe stop     | Yes       | Yes | No
SOS	  | Safe operating stop                   | Safe stop     | Yes       | Yes | No
SLS	  | Safe limit speed                      | Safe speed    | Yes       | Yes | Yes
SLP	  | Safe limit position                   | Safe position | Yes       | Yes | Yes

Each safety function can be activated by PROFIsafe, digital inputs (DI) or both. SLS and SLP can be also activated permanently by using the safety parameters.

###	PROFIsafe
One or more of the safety functions can be activated. The standard PROFIsafe telegram 902 is used. There is a standard library LdrvSafe_SinaTlg902 available. The telegram 902 allows detailed control of each safety function with additional parameters and also returns a safe axis position together with the time stamp for velocity calculation.

###	Digital inputs
Each axis can use two dedicated digital inputs pins for a safety function invoke. Only ONE function can be activated in a time. The selection is done via the safety parameters independently for each axis. The first axis uses digital inputs pins DI 5 and DI 7, the second axis uses DI6 and DI8 pins. Function is active by setting the mentioned pins low. Both inputs (DI5 & 7 or DI6 & 8) must be changed simultaneously within 10 ms. If this time is violated, the safety function is activated forever till restart of the TGZ.

###	Permanent safety function selection
Two of the safety functions can be also selected permanently via the safety parameters: Safe limit speed (SLS) and safe limit position (SLP). The SLS can work simultaneously with the PROFIsafe control – fine selection of the limited speed percent value is possible by telegram 902. On the other hand, the permanent SLP uses always the safety position 1 only.

###	Active safety function signaling by digital outputs
Digital output pins 3&5 for the first axis or 4&6 can be selected for signaling a selected safety function. Only ONE function can be selected for signaling. The normal digital outputs function is not available in that case. Active safety function is signaled by setting both the outputs low. 

##	Principle of operation
All safety functions assume that the PLC controller invokes the desired action. The TGZ monitors the speed and/or position and invokes the appropriate safety reaction in the case the conditions are not met. Additionally, when a safety function is selected, the TGZ also activates the wanted action internally (i.e. stops the motion, sets internal position limits, limits the speed, etc.).  
The safety functions monitoring is done in a safety manner by using two independent processors.  
Disabling the power motor output is done in a safety manner by using two independent FPGA disablers connected in sequence.

##	Safe torque off – STO
In addition to already available hardware STO safety function, which has its dedicated input pins, additional STO is available. STO turns off the drive output that powers the motor.

###	STO activation
STO can be activated by any of the following inputs or events:
- PROFIsafe STO bit in control word set to zero
- SS1
- SS2 in case of deceleration or standstill speed monitor fail
- SOS in case of standstill speed monitor fail
- SLS in case of speed threshold violation
- SLP in case of position range overflow/underflow and when the SLP’s stop function is set to STO
- Digital inputs (5&7 – axis 1, 6&8 – axis 2) set to low if mapped by the safety parameters

###	STO signaling
STO active status can be evaluated by:
- PROFIsafe status bit STO set to logical one
- Digital outputs (3&5 – axis 1, 4&6 – axis 2) set to low if mapped by the safety parameters

###	STO sequence
When the STO is activated the following actions are done simultaneously:
- Output driver power stage is set to zero
- The axis is disabled (software disable) and its PROFIdrive state goes to S1 – Switching On Inhibited.
- The motor velocity goes to zero and the motor cannot be started accidentally.

> **Warning: After the energy feed has been disconnected (STO active) the motor can undesirably move (e.g. the motor can coast down), therefore presenting risk to persons.**

###	STO deactivation
- Deselect the function by PROFIsafe control word and/or by settings both mapped digital inputs to high level.
- Enable the axis by PROFIdrive control word (i.e. traverse through PROFIdrive state diagram from S1 to S4).

## SS1 – time based safe stop
Definition according to EN 61800-5-2:

> "The function SS1 brakes the motor and trips the function STO after a delay time."

In other words the drive decelerates once SS1 has been selected, and goes into the STO state once the delay time has expired. The STO state is always selected after the timeout regardless the axis is still moving or not.

### SS1 activation
The SS1 function can be activated by any of the following events:
- PROFIsafe SS1 bit in the control word set to zero
- SLP in case of position range overflow/underflow and when the SLP’s stop function is set to SS1
- Digital inputs (5&7 – axis 1, 6&8 – axis 2) set to low if mapped by the safety parameters

### SS1 signaling
STO active status can be evaluated by:
- PROFIsafe status bit SS1 set to logical one
- Digital outputs (3&5 – axis 1, 4&6 – axis 2) set to low if mapped by the safety parameters

### SS1 sequence

### SS1 deactivation


#	Technical implementation

