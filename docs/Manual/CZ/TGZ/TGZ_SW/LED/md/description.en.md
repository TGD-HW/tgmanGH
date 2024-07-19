##Meaning of LED indicators and status display {#LED_sigs}
![TGZ LED display](../img/TGZ_LED1.png){: style="width:25%;" }

Integrated LED indicators and a two-digit seven-segment LED display show the status of the servo amplifier when the 24V power supply is switched on.
There are always two LED indicators on the servo amplifier (red LED and green LED) for each controlled axis, they detect the status of the individual controlled axes and if a fault or error occurs, the corresponding fault codes are displayed on the status display.
There is also a EtherCAT status LED common to both axes next to TGZ status LEDs.
Possible states of the LED indicators and their meaning, as well as error signaling and their description, are listed in the tables below.
**After restart of servo amplifier TGZ**

| Error code | Description |
|---|---|
| Bu | date and time of Firmware creation |
| iP | IP address of the TGZ servo amplifier for the UDP protocol |
| id | TGZ servo amplifier identification (“slave alias” for EtherCAT) |

**Error / fault indication**

| Chybový kód | Popis |
|---|---|
| F.1 | axis 1 error |
| F.2 | axis 2 error |

After code F.1 (or F.2), a sequence of numbers is displayed - these numbers are bit numbers in the error register.
Their description is given in chapter [Description of drive errors](description.md#errors)

** LED indicators**   

![TGZ status LEDs](../../../../../source/img/statusLedsECAT.svg){: style="width:70%;" }

Possible servo amplifier states are indicated by the **Ready** and **Error** LED diodes:   

| Drive state                 | Red LED state | Green LED state     |
|-----------------------------|---------------|---------------------|
| Mode = 0 (off)              | Flashing      | Flashing            |
| Drive error                 | ON            | OFF                 |
| Drive ready, no HW ENABLE   | OFF           | Slow blinking       |
| Drive ready, HW ENABLE on   | OFF           | Blinking            |
| Drive ready and enabled     | OFF           | ON                  |


If the servo amplifier is loaded with suitable firmware with EtherCAT bus support, the bus status is indicated by the **ECAT RUN** LED.
A detailed description of the individual EtherCAT states can be found in the documentation [EtherCAT Indicator and Labeling - ETG.1300 S](https://www.ethercat.org/memberarea/download/ETG1300_V1i1i1_S_R_IndicatorLabelingSpecification.pdf).

| Indicator States | Device State       | Description                           |
|------------------|--------------------|---------------------------------------|
| Off              | INITIALISATION     | Device is in INIT state               |
| Blinking         | PRE-OPERATIONAL    | Device is in PRE-OPERATIONAL state    |
| Single flash     | SAFE-OPERATIONAL   | Device is in SAFE-OPERATIONAL state   |
| On               | OPERATIONAL        | Device is in OPERATIONAL state        |


##Description of drive errors {#errors}

| Fault                      | Fault value in `aDriveError` reg. | Fault number on display | Error description / possible cause / solution                                                                                                                                                                                                                                                                                 |
|----------------------------|-------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Internal                   | 0x00000004                          | 2                       | Reason: Internal hardware error.<br>Solution: Contact the service department.                                                                                                                                                                                                                                                  |
| Over voltage               | 0x00000008                          | 3                       | DC voltage (connector X2) is too high.<br>Cause 1: DC power supply source is wrongly designed or wrongly adjusted or has error.<br>Solution 1: Check power supply source.<br>Cause 2: Recuperation energy of servo drive is higher than DC power supply source can take back. (Chopper resistor power is too low.)<br>Solution 2a: Change deceleration ramp of drive to longer time.<br>Solution 2b: Change DC power supply hardware or chopper resistor.<br>Reason 3: D-VoltDCLinkMaxErrLim parameter is set to low value.<br>Solution 3: Correct D-VoltDCLinkMaxErrLim parameter. |
| Low voltagex1              | 0x00000010                          | 4                       | DC voltage (connector X2) is too low.<br>Cause 1: DC power supply source is not connected or is in fault state or is off.<br>Solution 1: Check power supply.<br>Cause 2: D-VoltDCLinkMinErrLim parameter is set to high value.<br>Solution 2: Correct D-VoltDCLinkMinErrLim parameter.<br>Cause 3: Short circuit on DC-link.<br>Solution 3: Contact the service department.               |
| STO diagnostic error       | 0x00000020                          | 5                       | Diagnostics evaluated a fault in the safe torque off circuitry.<br>Cause: internal hardware error.<br>Solution: Contact the service department.                                                                                                                                                                                |
| Static brake error         | 0x00000040                          | 6                       | Diagnostics have evaluated a static brake fault.<br>Cause 1: Brake is disconnected or is incorrectly specified M-StaticBrake parameter in TGZ GUI.<br>Solution 1a: Check the motor type and set the M-StaticBrake parameter accordingly.<br>Solution 1b: Check the wiring of the brake cables and the wiring of the brake power supply to the servo amplifier.             |
| Current measurement error  | 0x00000100                          | 8                       | The motor current measurement circuits have a fault.<br>Cause: internal hardware error.<br>Solution: Contact the service department.                                                                                                                                                                                            |
| Motor over temperature     | 0x00000200                          | 9                       | Motor is overheated.<br>Cause 1: The ambient temperature is too high or the cooling conditions are unsuitable.<br>Solution 1: Consider improving the cooling conditions.<br>Cause 2: The engine is overloaded with power.<br>Solution 2: Check drive sizing and motor parameter settings against motor manufacturer's data.<br>Cause 3: Temperature sensor wiring error.<br>Solution 3: If possible, check the wiring of the temperature sensor or contact the service department.<br>Cause 4: Parameter setting error.<br>Solution 4: Check the temperature limit parameter settings and consult the service department. Verify engine parameters against manufacturer's data.<br>Cause 5: Mechanical or electrical fault on the motor.<br>Solution 5: Contact the service department. |
| Drive over temperature     | 0x00000800                          | 11                      | The TGZ servo amplifier is overheating.<br>Cause 1: The ambient temperature is too high or the cooling conditions are unsuitable.<br>Solution 1: Consider improving the cooling conditions.<br>Cause 2: Parameter setting error.<br>Solution 2: Check the temperature limit parameter settings.<br>Cause 3: Failure of the servo amplifier.<br>Solution 3: Contact the service department. |
| Feedback error             | 0x00001000                          | 12                      | Position feedback error.<br>Cause 1: Wiring and connector connection error.<br>Solution 1: Recheck and repair the wiring and connector connections of feedback connectors.<br>Cause 2: Motor position sensor error.<br>Solution 2: Contact the service department.<br>Cause 3: Fault in the servo amplifier circuitry.<br>Solution 3: Contact the service department.                   |
| Overspeed error            | 0x00004000                          | 14                      | Contact supplier of drive for more information.<br>The speed measured by the position sensor is greater than the value of the M-Nmax parameter.<br>Cause 1: Improperly set M-Nmax parameter<br>Solution 1: Adjust the parameter according to the data supplied by the motor manufacturer.<br>Cause 2: Incorrectly set speed controller.<br>Solution 2: Adjust the speed and slave controller settings to avoid oscillation.<br>Cause 3: Position (speed) measurement error.<br>Solution 3: Contact the service department of the motor supplier.                        |
| Position error             | 0x00008000                          | 15                      | The deviation between the desired and actual position of the position controller has exceeded the specified limit.<br>Cause 1: Improperly set parameters of the control structure.<br>Solution 1: Check and adjust the controller settings within the duty cycle to avoid oscillation and minimize position error.<br>Cause 2: The servo amplifier is unable to deliver the required torque to maintain the desired position. This may also be a mechanical failure of the driven system.<br>Solution 2: Check the drive sizing for dynamics and torque. If necessary, adjust the acceleration, deceleration of the system. Verify that there is no mechanical failure of the driven system, no excessive friction or mechanical stopping of the device, etc.               |
| Trajectory error           | 0x00010000                          | 16                      | The deviation of the requested position from the parent system (ethercat) from the actual position exceeded the specified limit.<br>Cause 1: Discontinuity in the position sent by the parent system.<br>Solution 1: Contact the supplier of the higher-level system.<br>Cause 2: Related to position error.<br>Solution 2: See. Resolution of position error.                |
| Fieldbus error             | 0x00020000                          | 17                      | Valid data did not arrive over the industrial bus within the specified time.<br>Cause 1: Wiring fault.<br>Solution 1: Check wiring, connectors.<br>Cause 2: Fault on another device on the bus.<br>Solution 2: Diagnose if there is a fault on another device on the bus, or disable it.<br>Cause 3: Control system problem.<br>Solution 3: Check the system parameters and settings or contact the control system supplier.                                                                                                         |
| Emergency stop             | 0x00100000                          | 20                      | Emergency stop has been activated, see. [Emergency braking](../../../../SW/REG/md/ESTOP.md).                                                                                                                                                                                                                                                                            |
| Over current error         | 0x00200000                          | 21                      | Motor overload current (short circuit).<br>Cause 1: Short circuit in the motor, wiring or connectors.<br>Solution 1: Check the individual components and remove the short circuit.<br>Cause 2: Low value of the D-Ierr_level parameter.<br>Solution 2: Set the value according to the motor parameters (20% higher than the maximum motor current).<br>Cause 3: Incorrect setting of the current controller.<br>Solution 3: Set the current regulator according to the motor parameters.<br>Cause 4: Failure of the servo amplifier.<br>Solution 4: Contact the service department. |
| Brake resistance error     | 0x00400000                          | 22                      | Brake resistance error (TGZS servo amplifiers).<br>Cause 1: Incorrect wiring.<br>Solution 1: Check the wiring according to the diagram.<br>Cause 2: Brake resistor is overheated or damaged.<br>Solution 2: Check the sizing of the brake resistor.                                                                                                                |
| Servo amplifier parameter error | 0x08000000                          | 27                      | Servo amplifier parameter error.<br>Cause 1: SD card is not inserted and reading parameters from SD card is requested.<br>Solution 1: Verify the SD card is inserted correctly.<br>Cause 2: The parameter structure has changed, e.g. after a firmware reload.<br>Solution 2: Read the parameters from a backup file or set the parameters manually and save them to the desired location.<br>Cause 3: The SD card is damaged.<br>Solution 3: Replace the card with a similar type and save the parameters from the backup.<br>Cause 4: The default saving of parameters to flash was not performed. It is necessary even when using the SD card.<br>Solution 4: Save the parameters to flash memory. |
