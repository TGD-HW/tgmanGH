##3D view
![3D view IO side](../img/IOside.en.webp){: style="width:75%;" }
<br>
<br>
![3D view FB side](../img/MotSide.en.webp){: style="width:60%;" }

##Connectors
___
### View of the ENET/ECAT side
___

![ENET/ECAT/24V connectors](../../../../source/img/TGZ-D-560-10_20_enetCon.webp){: style="width:80%;" }


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

</div>
___
### View of the CAN/IO/SD Side
___

![IO/CAN/SD connectors](../../../../source/img/TGZ-D-560-10_20_IO.webp){: style="width:80%;" }

<div class="grid cards" markdown>

-   **X8 - Digital I/O, analog inputs**

    ---
	Cable side view   
	
	![X8 pinout](../../../../source/img/1277370000.svg){: style="width:100%;" }
	3D view - cable side   
	
	![X8 pinout 3D](../../../../source/img/1277370000_1.svg){: style="width:100%;" }
	Front view (TGZ side)   
	
	![X8 pinout front](../../../../source/img/1277370000_2.svg){: style="width:100%;" }

	Please see details about
	[digital inputs DI1-8](../../../../source/md/commonHW_DI.md#commonDI1-8), 
	[digital outputs DO1-6](../../../../source/md/commonHW_DO.md#commonDO1-6) and
	[analog inputs AI1-2](../../../../source/md/commonHW_AI.md#commonAI1-2) 
	in the [Common hardware section](../../../../source/md/commonHW_DI.md#commonDI1-8).
	

-    Weidmüller B2CF 3.50/22/180 SN OR BX

	---

	--8<-- "md/X8_IO_22pin_B2CF.en.md"
	
	!!! warning "Warning"	
	
		For proper operation of the DI(1-6) it is necessary to supply at least one of the VCC DO (pin 11 and 12).
		Inputs DI7,8 are independent of the DO VCC supply voltage and work correctly even without it.
	
-   **X9 - MicroSD card**

    ---
![uSD card connector](../../../../source/img/uSD.png){: style="width:60%;" }

-    Use a standard microSD card. The card is included with the TGZ servo amplifier. For more information, see [SD cards](../../TGZ_SW/SD/md/SD.md#SDparams).

-   **X10 - CAN**

    ---
	Cable side view   
	![CAN connector](../../../../source/img/1277270000.svg){: style="width:25%;" }
	
	3D view - cable side   
	![CAN connector](../../../../source/img/1277270000_1.svg){: style="width:45%;" }
	
	Front view (TGZ side)   
	![CAN connector](../../../../source/img/1277270000_2.svg){: style="width:35%;" }

-    Weidmüller B2CF 3.50/04/180 SN OR BX

    ---

	--8<-- "md/X10_CAN_4pin_B2CF.en.md"
	
	For more information on the HW version of the CAN bus, see [CAN bus](../../../../source/md/commonHW_CAN.md#commonCAN).
	
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

![Motor/Feedback connectors 1](../../../../source/img/TGZ-D-560-10_20_FBconns.webp){: style="width:80%;" }

<div class="grid cards" markdown>

-   **X5 - External encoder (FBE)**

    ---
	Cable side view 	
	![FBE connector](../../../../source/img/1277320000.svg){: style="width:60%;" }
	
	3D view - cable side   
	![FBE connector](../../../../source/img/1277320000_1.svg){: style="width:60%;" }
	
	Front view (TGZ side)   
	![FBE connector](../../../../source/img/1277320000_2.svg){: style="width:60%;" }	

-    Weidmüller B2CF 3.50/12/180 SN OR BX

	---

	--8<-- "md/X5_FBE_12pin_B2CF.en.md"
	
	For more information on external feedback, see [FBE Feedback](../../../../source/md/commonHW_FBE.md#commonFBE).

-   **X6 - Feedback axis 1**

    ---
	
	Cable side view 	
	![FB1 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D view - cable side   
	![FB1 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Front view (TGZ side)   
	![FB1 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "md/X6_FB1_8pin_B2CF.en.md"
	
	For more information regarding Feedback 1, please see [Feedback FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
-   **X7 - Feedback axis 2**

    ---
	
	Cable side view 	
	![FB2 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D view - cable side   
	![FB2 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Front view (TGZ side)   
	![FB2 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "md/X7_FB2_8pin_B2CF.en.md"
	
	For more information regarding Feedback 2, please see [Feedback FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
-   **X3 - Motor connector axis 1**

    ---
	
	Housing back side view (wire side):
	
	![Motor connector](../../../../source/img/1164960000.webp){: style="width:70%;" }   
	
	![Motor connector angle](../../../../source/img/1164960000_1.webp){: style="width:70%;" } 	
	
	
-    Weidmüller BLZ 7.62HP/06/180LR SN BK BX

    ---

	--8<-- "md/X3_M1_6pin_BLZ__7_62.en.md"

	!!! warning "Connector orientation"
	
		Be careful to connect the terminals correctly	
		
-   **X4 - Motor connector axis 2**

    ---
	
	Housing back side view (wire side):
	
	![Motor connector](../../../../source/img/1164960000.webp){: style="width:70%;" }   
	
	![Motor connector angle](../../../../source/img/1164960000_1.webp){: style="width:70%;" } 	
	
	
-    Weidmüller BLZ 7.62HP/06/180LR SN BK BX

    ---

	--8<-- "md/X4_M2_6pin_BLZ__7_62.en.md"

	!!! warning "Connector orientation"
	
		Be careful to connect the terminals correctly		
	
-   **X2 - Power supply voltage**

    ---
	
	Housing back side view (wire side):
	![PWR connector back view](../../../../source/img/1093440000.webp){: style="width:50%;" }   
	
	![PWR connector 3D view](../../../../source/img/1093440000_1.webp){: style="width:50%;" }	

-    Weidmüller BLZ 7.62HP/03/180LR SN BK BX

    ---

	--8<-- "md/X2_560_DC_3pin_BLZ__7_62.en.md"
	
	!!! warning "Connector orientation"
	
		Be careful to connect the terminals correctly	

</div>


