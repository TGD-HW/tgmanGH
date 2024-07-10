##3D náhled
![3D view IO side](../img/IOside.svg){: style="width:75%;" }
<br>
<br>
![3D view FB side](../img/Motside.svg){: style="width:60%;" }

##Konektory
___
### Strana komunikace/ethernet/ethercat a DCbus
___

![ENET/ECAT/DCbus connectors](../../../../source/img/TGZ-D-560-30_50_DCbus.svg){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X2 - DC bus konektor**

    ---
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/D560DCbusCon.svg){: style="width:70%;" }

-    Šroubovací svorky M8

	---

	--8<-- "md/X2_D560DCbus.en.md"

</div>

___
### View of the CAN/IO/SD Side, +24V napájení, motor
___

![IO/CAN/SD + motor connectors](../../../../source/img/TGZ-D-560-30_50_Mot.svg){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/1940760000.svg){: style="width:70%;" }

-    Weidmüller BCZ 3.81/05/180 SN OR BX

	---

	--8<-- "md/X1_24V_5pin_BCZ.en.md"

-   **X3 - Motorový konektor osa 1**

    ---
	
	![Motor connector 1](../../../../source/img/2626-1104.svg){: style="width:70%;" }

-    Wago push-in svorky

    ---

	--8<-- "md/X3_M1_4pin_wago_2636.en.md"
	
-   **X4 - Motorový konektor osa 2**

    ---
	
	![Motor connector 2](../../../../source/img/2626-1104.svg){: style="width:70%;" }

-    Wago push-in svorky

    ---

	--8<-- "md/X4_M2_4pin_wago_2636.en.md"
	
-   **X14 - Brzda/Termistor osa 1**

    ---
	
	![Brake/Thermistor 1](../../../../source/img/1876530000R.svg){: style="width:70%;" }

-    Wago LSF svorky

    ---

	--8<-- "md/X14_BR1_4pin_LSF.en.md"
	
-   **X15 - Brzda/Termistor osa 2**

    ---
	
	![Brake/Thermistor 2](../../../../source/img/1876530000R.svg){: style="width:70%;" }

-    Wago LSF svorky

    ---

	--8<-- "md/X15_BR2_4pin_LSF.en.md"

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
### Strana Feedback
___

![Feedback connectors](../../../../source/img/TGZ-D-560-30_50_FBconns.svg){: style="width:60%;" }

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

</div>


