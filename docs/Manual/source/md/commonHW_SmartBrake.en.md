##Functional description {#SmartBrakeDesc}
The TGZ servo amplifier is equipped with an enhanced static motor brake control function called **Smart Brake**.
This function, among other benefits, reduces the power consumption of the static brake after it has been released (permanently released state).
The reduction in consumption is achieved by lowering the brake holding voltage/current (V<sub>HOLD</sub>, I<sub>HOLD</sub>).
Two static brake control modes are available.

This is voltage control:

![Smart brake voltage mode](../img/SmartBrakeEN_V.webp){: style="width:70%;" }

and current control.
 
![Smart brake current mode](../img/SmartBrakeEN_I.webp){: style="width:70%;" }

##Configuration and control {#SmartBrakeUsage}
The user can configure all required parameters in the program [TGZ GUI](../../CZ/TGZ/TGZ_SW/GUI/md/intro.md#GUIstart).
The parameter set is available in the `Drive` section.
![Smart brake GUI parameters](../img/SmartBrake_GUI1.webp){: style="width:100%;" }
For each controlled axis, user can select either voltage control `voltage control` or current control `current control` of the brake via the parameter **`D-Brake_mode`**.
Each mode has different operating parameters.

##Parameters {#SmartBrakeParams}
In the **voltage mode** of brake control, the following parameters can be set:

|  No. |  Name |  Designation in TGZ GUI | Unit | Range | Description |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  V<sub>EXC</sub>  | `D-BR_L2H_voltage` | V | 0~VCC<sub>BR</sub>  | Excitation voltage (pull-in voltage) |
| 2 |  V<sub>HOLD</sub>  | `D-BR_H_voltage` | V | 0~VCC<sub>BR</sub>  | Holding voltage |
| 3 |  τ<sub>EXC</sub>  | `D-BR_L2H_T_time` | 10 ms | 0~1000  | Excitation time (duration for which the brake is supplied with V<sub>EXC</sub>) 0~10 s |

!!! warning "Maximum brake supply voltage"

	V<sub>ABSMAX</sub> can be set in the range 0~50 V.
	Electronically, the brake-switching circuit is limited to 30 VDC.
	A higher supply voltage applied to the VCC_BR power pin can irreversibly damage the circuit!

In the **current mode** of brake control, the following parameters can be set:

|  No. |  Name |  Designation in TGZ GUI | Unit | Range | Description |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  I<sub>EXC</sub>  | `D-BR_L2H_voltage` | 100 mA | 0~30  | Excitation current (pull-in current) 0~3 A |
| 2 |  I<sub>HOLD</sub>  | `D-BR_H_voltage` | 100 mA | 0~30  | Holding current 0~3 A |
| 3 |  τ<sub>EXC</sub>  | `D-BR_L2H_T_time` | 10 ms | 0~1000  | Excitation time (duration for which the brake coil carries current I<sub>EXC</sub>) 0~10 s |
