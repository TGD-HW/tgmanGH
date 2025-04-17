##3D view
![3D view IO side](../img/IOside.en.webp){: style="width:80%;" }
<br>
<br>
![3D view FB side](../img/MotSide.en.webp){: style="width:80%;" }

##Connectors
___
### View of the ENET/ECAT side
___

![ENET/ECAT/LogicPWR connectors](../../../../source/img/TGZ-S-230-5_15-UNI-RI_enetCon.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X1 - Control supply voltage**

    ---
	Housing back side view (wire side):  
	
	![1941040000](../../../../source/img/1941040000.webp){: style="width:60%;" }   
	
	![1941040000_1](../../../../source/img/1941040000_1.webp){: style="width:60%;" }	

-    Weidmüller BCZ 3.81/05/180F SN OR BX

	---

	--8<-- "md/X1_24V_5pin_BCZ.md"
	
	!!! warning "EMI suppression"
	
		Please pay attention to the installation of the suppression toroidal core according to the [instructions](../../../../source/md/logicPWR.en.md#LogicPWR_EMI).

-   **X11 - Feedback 3 - RS422**

    ---
    ![Molex ClikMate 5031491000](../../../../source/img/5031491000.svg){: style="width:70%;" }
	
-    Molex ClikMate 5031491000 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    --8<-- "md/X11_FB3_10pin_ClikMate.en.md"
	
	!!! warning "Warning"	
		When using this type of feedback, make sure you are using the appropriate TGZ firmware that supports these features.

-   **X12 - Ethernet UDP - service**

    ---
    ![Molex ClikMate 5031490800](../../../../source/img/5031490800.svg){: style="width:70%;" }
	
-    Molex ClikMate 5031490800 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    --8<-- "md/X12_UDP_8pin_ClikMate.en.md"

-   **X13 - EtherCAT 2 - Fieldbus out**

    ---
    ![Molex ClikMate 5031490800](../../../../source/img/5031490800.svg){: style="width:70%;" }
	
-    Molex ClikMate 5031490800 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    --8<-- "md/X12_UDP_8pin_ClikMate.en.md"

-   **X14 - EtherCAT 1 - Fieldbus in**

    ---
    ![Molex ClikMate 5031490800](../../../../source/img/5031490800.svg){: style="width:70%;" }
	
-    Molex ClikMate 5031490800 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    --8<-- "md/X12_UDP_8pin_ClikMate.en.md"
	
</div>

___
### View of the CAN/IO/SD Side
___

![IO/CAN/SD connectors](../../../../source/img/TGZ-S-230-5_15-UNI-RI_IO.png){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X7 - Digital inputs + Analog inputs**

    ---
	![DITTL + AIN + PT1000](../../../../source/img/5031491200.svg){: style="width:70%;" }

-    Molex ClikMate 5031491200 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

	---

	--8<-- "md/X7_AIN_12pin_ClikMate.en.md"
	
	!!! warning "Warning"
		Direct PT1000 inputs of X7 pins 3-6 are only available on control board from batch supplied after 06-2024 onwards.
		Older versions of the device have standard AIN1, AIN2 and AIN3 on pins 1-6 of X7.
		For further details of the previous device properties please see older version of this manual.

-   **X8 - Digital I/O**

    ---
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/5031491800.svg){: style="width:100%;" }

-    Molex ClikMate 5031491800 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

	---

	--8<-- "md/X8_DIO_18pin_ClikMate.en.md"
		
-   **X9 - MicroSD slot**

    ---
	![uSD card connector](../../../../source/img/uSD.png){: style="width:40%;" }

-   It is not primarily recommended to use the microSD slot in devices where significant vibrations are expected.
	SD card is not included with the "RI" version of servoamplifiers.
	For more information, see [SD cards](../../TGZ_SW/SD/md/SD.md#SDparams).

-   **X10 - CAN**

    ---
	
	![CAN connector](../../../../source/img/5031490800.svg){: style="width:70%;" }

-    Molex ClikMate 5031490800 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    ---

	--8<-- "md/X10_CAN_8pin_ClikMate.en.md"
	
-	**LED display**

	---
	
	![LED display](../../../../source/img/TGZ_LED.png){: style="width:60%;" }
	
-	LED display indicates the status of the servoamplifier. See [TGZ status indicators](../../TGZ_SW/LED/md/description.md#LED_sigs) for detailed description.

-	**status LEDs**

	---
	
	![status LEDs](../../../../source/img/statusLedsECAT.svg){: style="width:100%;" }
	
-	LED diodes

	---
	
	--8<-- "md/LEDsigAx12.en.md"
	
	A complete description of the meaning of the status LEDs can be found here: [TGZ status indicators](../../TGZ_SW/LED/md/description.md#LED_sigs)

</div>

   
___
### View of the FB/motor side
___

![Motor/Feedback connectors](../../../../source/img/TGZ-S-230-5_15-UNI-RI_FBconns.png){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X4 - External encoder (FBE)**

	---
	
	![FBE connector](../../../../source/img/5031491200.svg){: style="width:80%;" }

-    Molex ClikMate 5031491200 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

	---

	--8<-- "md/X4_FBE_12pin_ClikMate.en.md"

-   **X5 - Feedback axis 1**

    ---
	
	![FB1 connector](../../../../source/img/5031491000.svg){: style="width:80%;" }

-    Molex ClikMate 5031491000 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    ---

	--8<-- "md/X5_FB1_10pin_ClikMate.en.md"
	
	For more information regarding Feedback 1, please see [Feedback FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
	!!! warning "Warning"
		In order to use Hiperface DSL feedback user must tie pins 5-7 and 6-8 together of the FB1 (and FB2 respectively) connector or assembly appropriate shorting resistors to the control PCB.
		This applies from batch supplied after 06-2024 onwards, where no internal connection is done on DSL as a standard.
		Also check whether you have correct firmware uploaded in the device.
	
-   **X6 - Feedback axis 2**

    ---
	
	![FB2 connector](../../../../source/img/5031491000.svg){: style="width:80%;" }

-    Molex ClikMate 5031491000 - recommended crimping contacts [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    ---

	--8<-- "md/X6_FB2_10pin_ClikMate.en.md"
	
	For more information regarding Feedback 2, please see [Feedback FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
	!!! warning "Warning"
		In order to use Hiperface DSL feedback user must tie pins 5-7 and 6-8 together of the FB1 (and FB2 respectively) connector or assembly appropriate shorting resistors to the control PCB.
		This applies from batch supplied after 06-2024 onwards, where no internal connection is done on DSL as a standard.
		Also check whether you have correct firmware uploaded in the device.
		
	!!! note "Note"
	
		Servoamplifier TGZ-S-230-5/15-UNI-RI is single axis version.
		The X6 connector is not normally connected.
	
-   **X3.1 - Motor connector**

    ---
	
	![Motor connector](../../../../source/img/1846250000.svg){: style="width:70%;" }

-    Weidmüller SLS 5.08/06/180FI SN OR BX

    ---

	--8<-- "md/X4_M1_6pin_SLS.en.md"
	
-   **X2 - Power supply voltage**

    ---
	
	Wires side view
	![PWR connector backview](../../../../source/img/1944170000.webp){: style="width:100%;" }
	TGZ side view
	![PWR connector front](../../../../source/img/1944170000_1.webp){: style="width:100%;" }	
	
	The X2 connector comes with jumper wire prepared for use without the external chopper resistor.
	
	![PWR connector jumper](../../../../source/img/1944170000jumper.webp){: style="width:100%;" }   
	
	If an external chopper (brake) resistor is used, the jumper wire must be removed and the resistor connected according to the [schematic](schematic.en.md).		

-    Weidmüller BLZP 5.08HC/10/180F SN OR BX

    ---

	--8<-- "md/X2_PWR_10pin_BLZP.en.md"
	

</div>

[^1]: When crimping and connecting the Molex Clik-Mate connectors, follow the [Molex Clik-Mate Application Guide](https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationspecificationspdf/503/503149/AS-503149-001-001.pdf)
