##3D view
![TGZ-S-48-60/125-UNI MotSide](../img/MotSide.webp){: style="width:70%;" }
<br>
<br>
![TGZ-S-48-60/125-UNI IO side](../img/IOside.webp){: style="width:70%;" }

##Description of communication, input/output and control
###Communication interfaces
- Ethernet 100/1000 Mb/s with UDP protocol, designed for parameter recording, monitoring, testing, but also online control;
- CAN bus protocol can be modified according to customer requirements;
- Ethernet 100/1000 Mb/s with optional protocol, programmed in the gate array and designed for connection of fast industrial buses for real-time control.
  Currently, this interface is equipped with the EtherCAT protocol (only for standard firmware); according to customer requirements it can be modified to another type of protocol.
  
###Inputs / outputs
TGZ servo amplifiers in this version have 8 digital inputs, 6 digital outputs and two general-purpose analog inputs, 0-10 V.
It is possible to read/control these inputs/outputs using a user program (C language).
The digital outputs can also be controlled using the TGZ GUI service software.

| I/O     | Type             | Count  | Value                                             |
|---------|------------------|--------|----------------------------------------------------|
| input   | analog        | 2      | 0-10 V                                             |
| input   | isolated digital | 8   | 0-24 V (0-10 V low/13-24 V high), 10 mA          |
| output  | isolated digital | 6   | 5-24 V, 300 mA / max. output                     |


| Type  | Standard              | Interface                         | Examples of Possible Connected Devices                                                                                               |
|-------|-----------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| FB1   | RS422/RS485           | Hiperface DSL, EnDat 2.2, SSI, BISS | Absolute magnetic/optical encoder, incremental magnetic/optical encoder with Hall sensors [^2], gyroscope              |
| FB2   | RS422/RS485           | Hiperface DSL, EnDat 2.2, SSI, BISS | Absolute magnetic/optical encoder, incremental magnetic/optical encoder with Hall sensors [^2], gyroscope              |
| FE[^1]   | RS422/RS485           | Hiperface DSL, EnDat 2.2, SSI, BISS | Absolute magnetic/optical encoder, incremental magnetic/optical encoder with Hall sensors [^2], gyroscope              |                                                                             |

[^1]: This type works with modified firmware. It is recommended to always consult with the manufacturer about its use.
[^2]: Hall sensors must be connected to the digital inputs using a special level shifter. For more information see [Hall converter](../../../ETC/TGHall/md/description.md#TGhall_1).

- Hiperface DSL – digital communication, sensors are manufactured with a resolution of 15 to 24 bits per revolution (multi-speed design – 4,096 revolutions).
  This type of feedback is used for motors with a single connector or cable.
- EnDat 2.2 – digital communication, sensors are manufactured with a resolution of 18 to 25 bits per revolution (multi-speed design – 4,096 revolutions).
- SSI – encoders with synchronous system interface.
- BISS – sensors with BISS-C protocol.

###Control
TGZ servoamplifiers can be controlled:

- digital control via EtherCAT, CAN-bus (torque, speed, position profiles, etc.) and via Ethernet UDP protocol;
- via user program (language C) – digital inputs, analog voltage, etc.

##Connectors
___
### View of the ENET/ECAT side
___

![TGZ-S-48-60/125-UNI ENET/ECAT/LogicPWR side](../../../../source/img/TGZ-S-48-60_125-UNI_enetCon.webp){: style="width:80%;" }

<div class="grid cards" markdown>

-   **X1 - Control supply voltage**

    ---
	![Molex Micro-Fit 3.0 436450500](../../../../source/img/436500518.webp){: style="width:90%;" }
	
	Counterpart PCB side view:
	
	![Molex Micro-Fit 3.0 436450500 w wires](../../../../source/img/436450500_60_125_1.webp){: style="width:90%;" }
	
	Counterpart wire side view:
	
	![Molex Micro-Fit 3.0 436450500 w wires back](../../../../source/img/436450500_60_125_2.webp){: style="width:90%;" }	
	
-    Molex Micro-Fit 3.0 - 436450500. Recommended crimping contacts [Molex 43030](https://www.molex.com/en-us/part-list/43030). [^4]

	---

	--8<-- "md/X1_24V_5pin_Microfit_60_125.en.md"
	
	!!! warning "EMI suppression"
	
		Please pay attention to the installation of the suppression toroidal core according to the [instructions](../../../../source/md/logicPWR.en.md#LogicPWR_EMI).

</div>


___
### View of the CAN/IO/SD Side
___

![IO/CAN/SD connectors](../../../../source/img/TGZ-S-48-60_125-UNI_IO.webp){: style="width:80%;" }

<div class="grid cards" markdown>

-   **X8 - Digital I/O, analog inputs**

    ---
	Rear view (cable side)   
	
	![X8 pinout](../../../../source/img/1277370000.svg){: style="width:100%;" }
	3D rear view   
	
	![X8 pinout 3D](../../../../source/img/1277370000_1.svg){: style="width:100%;" }
	Front view (TGZ side)   
	
	![X8 pinout front](../../../../source/img/1277370000_2.svg){: style="width:100%;" }

	For details about 
	[digital inputs DI1-8](../../../../source/md/commonHW_DI.en.md#commonDI1-8), 
	[digital outputs DO1-6](../../../../source/md/commonHW_DO.en.md#commonDO1-6) a 
	[analog inputs AI1-2](../../../../source/md/commonHW_AI.en.md#commonAI1-2) 
	please see [Common hardware section](../../../../source/md/commonHW_DI.en.md#commonDI1-8).
	

-    Weidmüller B2CF 3.50/22/180 SN OR BX

	---

	--8<-- "md/X8_IO_22pin_B2CF.en.md"
	
	!!! warning "Warning"	
	
		For correct operation of DI1-6, at least one DO VCC terminal (pin 11 or 12) must be connected. Inputs DI7 and DI8 are independent of the DO VCC supply voltage and operate correctly without it.
	
-   **X9 - MicroSD slot**

    ---
	
	![uSD card connector](../../../../source/img/uSD.png){: style="width:60%;" }

-    Use a standard microSD card. The card is included with the TGZ servo amplifier. For more information, see [SD cards](../../TGZ_SW/SD/md/SD.md#SDparams).

-   **X10 - CAN**

    ---
	Rear view (cable side)   
	![CAN connector](../../../../source/img/1277270000.svg){: style="width:25%;" }
	
	3D rear view   
	![CAN connector](../../../../source/img/1277270000_1.svg){: style="width:45%;" }
	
	Front view (TGZ side)   
	![CAN connector](../../../../source/img/1277270000_2.svg){: style="width:35%;" }

-    Weidmüller B2CF 3.50/04/180 SN OR BX

    ---

	--8<-- "md/X10_CAN_4pin_B2CF.en.md"
	
	For more information about the CAN bus hardware implementation, see [CAN bus](../../../../source/md/commonHW_CAN.en.md#commonCAN).
	
-	**LED display**

	---
	
	![LED displej](../../../../source/img/TGZ_LED.png){: style="width:60%;" }
	
-	The LED display indicates the status of the servoamplifier. See [TGZ status indicators](../../TGZ_SW/LED/md/description.md#LED_sigs)

-	**status LEDs**

	---
	
	![LED signalizace](../../../../source/img/statusLedsECAT.svg){: style="width:100%;" }
	
-	LED diodes

	---
	
	--8<-- "md/LEDsigAx12.en.md"
	
	A complete description of the meaning of the status LEDs can be found here: [TGZ status indicators](../../TGZ_SW/LED/md/description.md#LED_sigs)

</div>

   
___
### Feedback/motor side view
___

![Feedback connectors](../../../../source/img/TGZ-S-48-60_125-UNI_FBconns.webp){: style="width:80%;" }

<div class="grid cards" markdown>

-   **X5 - External encoder (FBE)**

    ---
	Rear view (cable side) 	
	![FBE connector](../../../../source/img/1277320000.svg){: style="width:60%;" }
	
	3D rear view   
	![FBE connector](../../../../source/img/1277320000_1.svg){: style="width:60%;" }
	
	Front view (TGZ side)   
	![FBE connector](../../../../source/img/1277320000_2.svg){: style="width:60%;" }	

-    Weidmüller B2CF 3.50/12/180 SN OR BX

	---

	--8<-- "md/X5_FBE_12pin_B2CF.en.md"
	
	For more information on external feedback, see [FBE Feedback](../../../../source/md/commonHW_FBE.en.md#commonFBE).

-   **X6 - Feedback axis 1**

    ---
	
	Rear view (cable side) 	
	![FB1 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D rear view   
	![FB1 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Front view (TGZ side)   
	![FB1 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "md/X6_FB1_8pin_B2CF.en.md"
	
	For more information regarding Feedback 1, please see [Feedback FB1, FB2](../../../../source/md/commonHW_FB12.en.md#commonFB12).
	
-   **X7 - Feedback axis 2**

    ---
	
	Rear view (cable side) 	
	![FB2 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D rear view   
	![FB2 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Front view (TGZ side)   
	![FB2 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "md/X7_FB2_8pin_B2CF.en.md"
	
	For more information regarding Feedback 2, please see [Feedback FB1, FB2](../../../../source/md/commonHW_FB12.en.md#commonFB12).

-   **X3 - Power supply voltage**

    ---
	
	![DC bus connection](../../../../source/img/TGZ-S-48-60_125-UNI_X3DC.webp){: style="width:80%;" }

-    Pressfit M5 - recommended cable ring [JST GS5-10](https://www.tme.eu/cz/en/details/gs5-10/non-insulated-terminals/jst/)

    ---

	--8<-- "md/X2_DCbus_2pin_pressfit.en.md"
	
	!!! info "Tightening torque"
	
		The maximum tightening torque for the M5 press-fit is 2.2 Nm.
	
	!!! warning "Regenerative braking"
	
		In cases when the drive is not powered by a battery (e.g., a Li-ion battery pack), 
		it is necessary for machines with greater kinetic energy to ensure its dissipation, for example, in a resistive element using a chopper unit.
		
-   **X3 - Motor connector**

    ---
	
	![Motor connection](../../../../source/img/TGZ-S-48-60_125-UNI_X3mot.webp){: style="width:80%;" }

-    Pressfit M5 - recommended cable ring [JST GS5-10](https://www.tme.eu/cz/en/details/gs5-10/non-insulated-terminals/jst/)

    ---
	
	--8<-- "md/X2_M1_3pin_pressfit.en.md"

	!!! info "Tightening torque"
	
		The maximum tightening torque for the M5 press-fit is 2.2 Nm.	


-   **X4 - Static brake + motor temperature**

    ---
	
	PCB connector top view:
	
	![Brake connector](../../../../source/img/430450401.webp){: style="width:60%;" }
	
	Counterpart PCB side view:
	
	![Molex Micro-Fit 3.0 2147551041 w wires](../../../../source/img/2147551041_1.webp){: style="width:60%;" }
	
	Counterpart wire side view:
	
	![Molex Micro-Fit 3.0 436450500 w wires cable side](../../../../source/img/430250400.webp){: style="width:60%;" }
	
-    Molex Micro-Fit 3.0 - 430250400. Recommended crimping contacts [Molex 43030](https://www.molex.com/en-us/part-list/43030). [^4]

	---

	--8<-- "md/X3_BR_4pin_Microfit.en.md"
	
	The servo amplifier is equipped with an enhanced static motor brake control circuit.
	More information on how to set the key parameters can be found in the [Smart Brake](../../../../source/md/commonHW_SmartBrake.en.md#SmartBrakeDesc).
		
	!!! info "Connector crimp contacts"
	
		Select the crimp contacts according to the chosen wire cross-section.
		
</div>
[^4]: When crimping and connecting the Molex Micro-Fit connectors, follow the [Molex Micro-Fit Application Guide](https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationtoolingspecificationpdf/638/63819/ATS-638190000-001.pdf) and use the recommended crimping tool [638190000](https://www.molex.com/en-us/products/part-detail/638190000).