<!--##Connectors-->
___
### View of the ENET/ECAT side
___

![TGMcontroller power side](../img/PWRside.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X1 - Control supply voltage**

    ---
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/1940760000.svg){: style="width:70%;" }

-    Weidmüller BCZ 3.81/05/180 SN OR BX

	---

	--8<-- "md/X1_24V_5pin_BCZ_TGM.en.md"
	
	!!! info "EIx"
		Extended inputs work as standard digital inputs 0 – 24 V. 
		See also [IO mapping](software.md#ControllerINI)).
	
-   **X11 - TGMotion service connector**

    ---
	![X11 service RJ45](../../../../source/img/RJ45_X11_service.png){: style="width:60%;" }

-   RJ45

	---

	It is used for connecting the TGMotion system (TCP or UDP protocol) by Control Observer and other user applications.
	Additional supported protocols are Modbus/TCP and Profinet IO (see below).
		
-   **X12 - FSP port**

    ---
	![X12 FSP RJ45](../../../../source/img/RJ45_X12_FSP.png){: style="width:60%;" }

-   RJ45

	---

	This port is used for so called Fast Service Port.
	Serves for very fast peer-to-peer connection between TGMcontroller and PC.
	Special custom raw protocol is used.
	The PC must install [Winpcap](https://www.winpcap.org/) or [Npcap](https://npcap.com/) driver.
	No setting is necessary, the communication DLL finds the correct PC network adapter.
	For best performance, use the built-in or PCIe NIC adapters.
	The USB-Ethernet adapters can be also used, but suffer of worse performance.
	Some low cost USB to Ethernet adapters don’t work at all with the FSP protocol.
	The adapter must have space for at least 32 packets at one time.
	
-   **X13 - EtherCAT master**

    ---
	![X13 ECAT master RJ45](../../../../source/img/RJ45_X13_master.png){: style="width:60%;" }

-   RJ45

	---

	EtherCAT master connector – use this port for connecting the EtherCAT devices in the EtherCAT fieldbus.
	No setting is necessary.
	The port is capable of 100 Mbit or 1 Gbit speeds, depending of the first connected device.
	There are a few 1 Gbit EtherCAT devices available, e.g.	TGZ servo drives or several EtherCAT bridges from other manufacturers.
	If using the 1 Gbit fieldbus, all the devices in the chain must be using the 1 Gbit speed.
	
</div>	

___
### View of the CAN/IO/SD Side
___

![TGMcontroller IO/CAN/SD side](../img/IOside.png){: style="width:80%;" }

<div class="grid cards" markdown>

-   **X8 - Digital I/O, analog inputs**

    ---
	Cable side view   
	
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/1277370000.svg){: style="width:100%;" }
	3D view - cable side   
	
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/1277370000_1.svg){: style="width:100%;" }
	Front view (TGZ side)   
	
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/1277370000_2.svg){: style="width:100%;" }

-    Weidmüller BCZ 3.81/22/180 SN OR BX

	---

	--8<-- "md/X8_IO_22pin_B2CF.en.md"
	
	!!! warning "Warning"	
	
		For proper operation of the DI(1-6) it is necessary to supply at least one of the VCC DO (pin 11 and 12).
		Inputs DI7,8 are independent of the DO VCC supply voltage and work correctly even without it.
	
-   **X9 - MicroSD card**

    ---
![uSD card connector](../../../../source/img/uSD.png){: style="width:60%;" }

-    Use a standard microSD card.

-   **X10 - CAN**

    ---
	Cable side view   
	![CAN connector](../../../../source/img/1277270000.svg){: style="width:25%;" }
	
	3D view - cable side   
	![CAN connector](../../../../source/img/1277270000_1.svg){: style="width:45%;" }
	
	Front view (TGZ side)   
	![CAN connector](../../../../source/img/1277270000_2.svg){: style="width:35%;" }

-    Weidmüller BCZ 3.81/04/180 SN OR BX

    ---

	--8<-- "md/X10_CAN_4pin_B2CF.en.md"
	
-	**LED display**

	---
	
	![LED display](../../../../source/img/TGZ_LED.png){: style="width:60%;" }
	
-	The LED display shows the device IP address during startup.
	The text “IP” is followed by numbers.
	Since the numbers can have up to 3 digits, each complete number is separated by a dot.
	For example to display the number “`192`”, first a single “1” is displayed (without a dot) and then “92.” (with the dot).
	Complex IP addresses like `192.168.128.179` can be displayed in this way.

-	**status LEDs**

	---
	
	![status LEDs](../../../../source/img/statusLedsECAT.svg){: style="width:100%;" }
	
-	There are four additional LED diodes labeled as ERROR (red color) and READY (green color) for two axes.
	The READY shows that this particular axis is enabled in the `TGM.INI` file, on the other hand ERROR means the axis is not mapped to TGMotion by the `TGM.INI` file.
	See also [IO mapping](software.md#ControllerINI) about the entries in the `TGM.INI` file.
	

</div>

___
### Feedback side view
___

![TGMcontroller feedback side](../img/FBside.png){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X5 - External encoder (FBE)**

    ---
	Cable side view 	
	![FBE connector](../../../../source/img/1277320000.svg){: style="width:60%;" }
	
	3D view - cable side   
	![FBE connector](../../../../source/img/1277320000_1.svg){: style="width:60%;" }
	
	Front view (TGZ side)   
	![FBE connector](../../../../source/img/1277320000_2.svg){: style="width:60%;" }	

-    Weidmüller BCZ 3.81/12/180 SN OR BX

	---

	--8<-- "md/X5_FBE_12pin_B2CF_TGM.en.md"
	The X5 connector is used for an incremental encoder (IRC).

-   **X6 - Feedback axis 1**

    ---
	
	Cable side view 	
	![FB1 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D view - cable side   
	![FB1 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Front view (TGZ side)   
	![FB1 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller BCZ 3.81/08/180 SN OR BX

    ---

	--8<-- "md/X6_FB1_8pin_B2CF_TGM.en.md"
	
	!!! note "FB1"
		The X6 connector supports either Hiperface DSL feedback or EnDAT 2.2 standard.
		The type of the used feedback communication standard is given in the `TGM.INI` file: `Servo[xx].FeedbackType=1` is for **DSL** and `Servo[xx].FeedbackType=2` is for **EnDAT**.
	
-   **X7 - Feedback axis 2**

    ---
	
	Cable side view 	
	![FB2 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D view - cable side   
	![FB2 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Front view (TGZ side)   
	![FB2 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller BCZ 3.81/08/180 SN OR BX

    ---

	--8<-- "md/X7_FB2_8pin_B2CF_TGM.en.md"
	
	!!! note ""
		The X7 connector can be used with DSL or SSI feedback.
		Use the following settings in the `TGM.INI`: `Servo[xx].FeedbackType=1` for the DSL and `Servo[xx].FeedbackType=3` for the SSI.
