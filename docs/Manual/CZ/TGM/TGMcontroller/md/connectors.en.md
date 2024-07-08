<!--##Konektory-->
___
### Strana komunikace/ethernet/ethercat
___

<img src="../../img/PWRside.png" alt="TGMcontroller power side" style="width:60%;">


<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	<img src="../../../../../source/img/1940760000.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:70%;">

-    Weidmüller BCZ 3.81/05/180 SN OR BX

	---

	--8<-- "CZ/md/X1_24V_5pin_BCZ_TGM.md"
	
-   **X11 - TGMotion systémový konektor**

    ---
	<img src="../../../../../source/img/RJ45_X11_service.png" alt="X11 service RJ45" style="width:60%;">

-   RJ45

	---

	Slouží k připojení systému TGMotion (protokol TCP nebo UDP) pomocí programu Control Observer a dalších uživatelských aplikací.
	Dalšími podporovanými protokoly jsou Modbus/TCP a Profinet IO.
		
-   **X12 - FSP port**

    ---
	<img src="../../../../../source/img/RJ45_X12_FSP.png" alt="X12 FSP RJ45" style="width:60%;">

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
	<img src="../../../../../source/img/RJ45_X13_master.png" alt="X13 ECAT master RJ45" style="width:60%;">

-   RJ45

	---

	Tento port slouží k připojení zařízení EtherCAT na sběrnici EtherCAT.
	Není nutné žádné nastavení.
	Port je schopen pracovat rychlostí 100 Mbit nebo 1 Gbit v závislosti na prvním připojeném zařízení.
	K dispozici je několik 1 Gbitových zařízení EtherCAT, např. servopohony TGZ nebo několik EtherCAT bridge zařízení od jiných výrobců.
	Při použití sběrnice 1 Gbit musí všechna zařízení v řetězci podporovat tuto rychlost.
	
	

</div>	

___
### Strana CAN/IO/SD
___

<img src="../../img/IOside.png" alt="TGMcontroller IO/CAN/SD side" style="width:80%;">

<div class="grid cards" markdown>

-   **X8 - Digitální I/O, analogové vstupy**

    ---
	Pohled zezadu (strana kabelu)   
	
	<img src="../../../../../source/img/1277370000.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:100%;">
	3D pohled zezadu   
	
	<img src="../../../../../source/img/1277370000_1.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:100%;">
	Pohled zepředu (strana TGZ)   
	
	<img src="../../../../../source/img/1277370000_2.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:100%;">

-    Weidmüller BCZ 3.81/22/180 SN OR BX

	---

	--8<-- "CZ/md/X8_IO_22pin_B2CF.md"
	
	!!! warning "Pozor"	
	
		Pro správnou funkci DI(1-6) je potřeba připojit alespoň jedno z VCC DO (pin 11 a 12). Vstupy DI7,8 jsou nezávislé na napájecím napětí DO VCC a fungují korektně i bez něj.
	
-   **X9 - MicroSD karta**

    ---
<img src="../../../../../source/img/uSD.png" alt="uSD card connector" style="width:60%;">

-    Použijte microSD kartu průmyslové specifikace. Karta je součástí dodávky servozesilovače TGZ.

-   **X10 - CAN**

    ---
	Pohled zezadu (strana kabelu)   
	<img src="../../../../../source/img/1277270000.svg" alt="CAN connector" style="width:25%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277270000_1.svg" alt="CAN connector" style="width:45%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277270000_2.svg" alt="CAN connector" style="width:35%;">

-    Weidmüller BCZ 3.81/04/180 SN OR BX

    ---

	--8<-- "CZ/md/X10_CAN_4pin_B2CF.md"
	
-	**LED displej**

	---
	
	<img src="../../../../../source/img/TGZ_LED.png" alt="LED displej" style="width:60%;">
	
-	Při spuštění se na LED displeji zobrazuje IP adresa zařízení.
	Za textem "IP" následují čísla.
	Protože čísla mohou mít až 3 číslice, je každé celé číslo odděleno tečkou.
	Například pro zobrazení čísla "192" se nejprve zobrazí jedna číslice "1" (bez tečky) a poté "92" (s tečkou).
	Tímto způsobem lze zobrazit i složité IP adresy, například 192.168.128.179.

-	**LED signalizace**

	---
	
	<img src="../../../../../source/img/LEDsig.png" alt="LED signalizace" style="width:80%;">
	
-	K dispozici jsou čtyři další LED diody označené jako ERROR (červená barva) a READY (zelená barva).
	READY ukazuje, že daná osa je v souboru `TGM.INI` povolena, naopak ERROR znamená, že osa není v souboru `TGM.INI` namapována na TGMotion.
	

</div>

___
### Strana feedback
___

<img src="../../img/FBside.png" alt="TGMcontroller feedback side" style="width:60%;">

<div class="grid cards" markdown>

-   **X5 - Externí enkodér (FBE)**

    ---
	Pohled zezadu (strana kabelu) 	
	<img src="../../../../../source/img/1277320000.svg" alt="FBE connector" style="width:60%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277320000_1.svg" alt="FBE connector" style="width:60%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277320000_2.svg" alt="FBE connector" style="width:60%;">	

-    Weidmüller BCZ 3.81/12/180 SN OR BX

	---

	--8<-- "CZ/md/X5_FBE_12pin_B2CF_TGM.md"

-   **X6 - Zpětná vazba - osa 1**

    ---
	
	Pohled zezadu (strana kabelu) 	
	<img src="../../../../../source/img/1277290000.svg" alt="FB1 connector" style="width:50%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277290000_1.svg" alt="FB1 connector" style="width:50%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277290000_2.svg" alt="FB1 connector" style="width:50%;">

-    Weidmüller BCZ 3.81/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X6_FB1_8pin_B2CF_TGM.md"
	
	!!! note ""
		Konektor X6 podporuje buď zpětnou vazbu Hiperface DSL, nebo standard EnDAT 2.2.
		Typ použitého komunikačního standardu zpětné vazby je uveden v souboru `TGM.INI`: `Servo[xx].FeedbackType=1` pro DSL a `Servo[xx].FeedbackType=2` pro EnDAT.
	
-   **X7 - Zpětná vazba - osa 2**

    ---
	
	Pohled zezadu (strana kabelu) 	
	<img src="../../../../../source/img/1277290000.svg" alt="FB2 connector" style="width:50%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277290000_1.svg" alt="FB2 connector" style="width:50%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277290000_2.svg" alt="FB2 connector" style="width:50%;">

-    Weidmüller BCZ 3.81/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X7_FB2_8pin_B2CF_TGM.md"
	
	!!! note ""
		Konektor X7 lze použít pro připojení zpětné vazby DSL nebo SSI.
		Použijte následující nastavení v souboru `TGM.INI`: `Servo[xx].FeedbackType=1` pro DSL a `Servo[xx].FeedbackType=3` pro SSI. 
