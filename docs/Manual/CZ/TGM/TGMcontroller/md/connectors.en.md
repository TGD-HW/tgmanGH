<!--##Konektory-->
___
### Strana komunikace/ethernet/ethercat
___

![TGMcontroller power side](../img/PWRside.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/1940760000.svg){: style="width:70%;" }

-    Weidmüller BCZ 3.81/05/180 SN OR BX

	---

	--8<-- "md/X1_24V_5pin_BCZ_TGM.en.md"
	
-   **X11 - TGMotion systémový konektor**

    ---
	![X11 service RJ45](../../../../source/img/RJ45_X11_service.png){: style="width:60%;" }

-   RJ45

	---

	Slouží k připojení systému TGMotion (protokol TCP nebo UDP) pomocí programu Control Observer a dalších uživatelských aplikací.
	Dalšími podporovanými protokoly jsou Modbus/TCP a Profinet IO.
		
-   **X12 - FSP port**

    ---
	![X12 FSP RJ45](../../../../source/img/RJ45_X12_FSP.png){: style="width:60%;" }

-   RJ45

	---

	Tento port se používá jako tzv. Fast Service Port. 
	Slouží pro velmi rychlé peer-to-peer spojení mezi TGMcontrollerem a PC.
	Používá se speciální protokol.
	V počítači musí být nainstalován ovladač [Winpcap](https://www.winpcap.org/) nebo [Npcap](https://npcap.com/). 
	Není nutné žádné nastavení, komunikační DLL sama najde správný síťový adaptér PC. 
	Pro dosažení nejlepšího výkonu použijte PCIe síťový adaptér.
	Adaptéry USB-Ethernet lze také použít, ale mají menší výkon.
	Některé levné adaptéry USB-Ethernet s protokolem FSP vůbec nefungují.
	Adaptér musí mít paměť pro alespoň 32 paketů najednou.
	
-   **X13 - EtherCAT master**

    ---
	![X13 ECAT master RJ45](../../../../source/img/RJ45_X13_master.png){: style="width:60%;" }

-   RJ45

	---

	Tento port slouží k připojení zařízení EtherCAT na sběrnici EtherCAT.
	Není nutné žádné nastavení.
	Port je schopen pracovat rychlostí 100 Mbit nebo 1 Gbit v závislosti na prvním připojeném zařízení.
	K dispozici je několik 1 Gbitových zařízení EtherCAT, např. servopohony TGZ nebo několik EtherCAT bridge zařízení od jiných výrobců.
	Při použití sběrnice 1 Gbit musí všechna zařízení v řetězci podporovat tuto rychlost.
	
	

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

-    Použijte microSD kartu průmyslové specifikace. Karta je součástí dodávky servozesilovače TGZ.

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
	
-	Při spuštění se na LED displayi zobrazuje IP adresa zařízení.
	Za textem "IP" následují čísla.
	Protože čísla mohou mít až 3 číslice, je každé celé číslo odděleno tečkou.
	Například pro zobrazení čísla "192" se nejprve zobrazí jedna číslice "1" (bez tečky) a poté "92" (s tečkou).
	Tímto způsobem lze zobrazit i složité IP adresy, například 192.168.128.179.

-	**status LEDs**

	---
	
	![status LEDs](../../../../source/img/LEDsig.png){: style="width:80%;" }
	
-	K dispozici jsou čtyři další LED diody označené jako ERROR (červená barva) a READY (zelená barva).
	READY ukazuje, že daná osa je v souboru `TGM.INI` povolena, naopak ERROR znamená, že osa není v souboru `TGM.INI` namapována na TGMotion.
	

</div>

___
### Strana feedback
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
	
	!!! note ""
		Konektor X6 podporuje buď zpětnou vazbu Hiperface DSL, nebo standard EnDAT 2.2.
		Typ použitého komunikačního standardu zpětné vazby je uveden v souboru `TGM.INI`: `Servo[xx].FeedbackType=1` pro DSL a `Servo[xx].FeedbackType=2` pro EnDAT.
	
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
		Konektor X7 lze použít pro připojení zpětné vazby DSL nebo SSI.
		Použijte následující nastavení v souboru `TGM.INI`: `Servo[xx].FeedbackType=1` pro DSL a `Servo[xx].FeedbackType=3` pro SSI. 
