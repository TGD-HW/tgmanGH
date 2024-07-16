<!--##Connectors-->
___
### View of the ENET/ECAT side
___

![TGMmini power side](../img/PWRside.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X3 - Input power**

    ---
	![24V connector 2439670000](../../../../source/img/2439670000.svg){: style="width:60%;" }

-    Weidmüller BLF 2.50/04/180 SN OR BX

	---

	--8<-- "md/X3_24V_BLF_2_5.en.md"


-   **X4 - CAN**

    ---
	
	![CAN connector](../../../../source/img/1277270000.svg){: style="width:25%;" }

-    Weidmüller BCZ 3.81/04/180 SN OR BX

    ---

	--8<-- "md/X10_CAN_4pin_B2CF.en.md"
	
</div>	

___
### IO/USB/SD side view
___

![TGMmini IO side](../img/IOside.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X5 - Digital inputs**

    ---
	
	![DI connector](../../../../source/img/1277310000.svg){: style="width:60%;" }

-    Weidmüller B2CF 3.50/10/180 SN OR BX

    ---

	--8<-- "md/X5_DI_10pin_B2CF.en.md"
	
-   **X10 - Digital outputs**

    ---
	
	![DO connector](../../../../source/img/1277310000.svg){: style="width:60%;" }

-    Weidmüller B2CF 3.50/10/180 SN OR BX

    ---

	--8<-- "md/X10_DO_10pin_B2CF.en.md"
	
	!!! warning "DO supply"
		The power supply of the digital outputs must be complete, i.e. the OUTCOM and OUTPWR 24 V pins must be properly connected.
		In the case the ground wire to OUTCOM is broken, on all output pins OUT0 – OUT7 appears voltage of about 21 V.
		The outputs can subsequently and unexpectedly switch ON the devices connected to these outputs.
		To alleviate this problem, a safety relay (like OMRON K8AK-AS1) must be used and properly connected.
		
		**TGDrives, s.r.o. is not responsible to any damages and/or injuries caused by wrong 24 V power connection.**
		**Only properly qualified personnel are permitted to make the device installation and start up.**
	
-   **S1 - CAN bus termination**

    ---
	
	![CAN termination switch](../../../../source/img/BPA01B.png){: style="width:40%;" }

-    DIP switch

    ---

	--8<-- "md/S1_SWITCH_CAN.en.md"

</div>