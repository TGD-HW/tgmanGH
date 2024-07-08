<!--
# Popis zařízení   

## Konektory
-->
##3D náhled
<img src="../../img/IOside.svg" alt="3D view IO side" style="width:70%;">
<br>
<br>
<img src="../../img/Motside.svg" alt="3D view motor side" style="width:70%;">

##Konektory
___
### Strana komunikace/ethernet/ethercat
___

<img src="../../../../../source/img/TGZ-S-230-5_15_enetCon.png" alt="ENET/ECAT/LogicPWR connectors" style="width:60%;">


<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	<img src="../../../../../source/img/1940760000.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:70%;">

-    Weidmüller BCZ 3.81/05/180 SN OR BX

	---

	--8<-- "CZ/md/X1_24V_5pin_BCZ.md"

</div>

___
### Strana CAN/IO/SD
___

<img src="../../../../../source/img/TGZ-S-230-5_15_IO.png" alt="IO/CAN/SD connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X8 - Digitální I/O, analogové vstupy**

    ---
	Pohled zezadu (strana kabelu)   
	
	<img src="../../../../../source/img/1277370000.svg" alt="X8 pinout" style="width:100%;">
	3D pohled zezadu   
	
	<img src="../../../../../source/img/1277370000_1.svg" alt="X8 pinout 3D" style="width:100%;">
	Pohled zepředu (strana TGZ)   
	
	<img src="../../../../../source/img/1277370000_2.svg" alt="X8 pinout front" style="width:100%;">

	Detailní soupis parametrů 
	[digitálních vstupů DI1-8](../../../../source/md/commonHW_DI.md#commonDI1-8), 
	[digitálních výstupů DO1-6](../../../../source/md/commonHW_DO.md#commonDO1-6) a 
	[analogových vstupů AI1-2](../../../../source/md/commonHW_AI.md#commonAI1-2) 
	naleznete v sekci [Společný HW](../../../../source/md/commonHW_DI.md#commonDI1-8).
	

-    Weidmüller B2CF 3.50/22/180 SN OR BX

	---

	--8<-- "CZ/md/X8_IO_22pin_B2CF.md"
	
	!!! warning "Pozor"	
	
		Pro správnou funkci DI(1-6) je potřeba připojit alespoň jedno z VCC DO (pin 11 a 12). Vstupy DI7,8 jsou nezávislé na napájecím napětí DO VCC a fungují korektně i bez něj.
	
-   **X9 - MicroSD karta**

    ---
<img src="../../../../../source/img/uSD.png" alt="uSD card connector" style="width:60%;">

-    Použijte standardní microSD kartu. Karta je součástí dodávky servozesilovače TGZ. Více informací naleznete v sekci [SD karty](../../TGZ_SW/SD/md/SD.md#SDparams).

-   **X10 - CAN**

    ---
	Pohled zezadu (strana kabelu)   
	<img src="../../../../../source/img/1277270000.svg" alt="CAN connector" style="width:25%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277270000_1.svg" alt="CAN connector" style="width:45%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277270000_2.svg" alt="CAN connector" style="width:35%;">

-    Weidmüller B2CF 3.50/04/180 SN OR BX

    ---

	--8<-- "CZ/md/X10_CAN_4pin_B2CF.md"
	
	Další informace o HW provedení sběrnice CAN naleznete v sekci [Sběrnice CAN](../../../../source/md/commonHW_CAN.md#commonCAN).
	
-	**LED displej**

	---
	
	<img src="../../../../../source/img/TGZ_LED.png" alt="LED displej" style="width:60%;">
	
-	LED displej signalizuje stavy viz. [Význam stavových indikátorů TGZ](../../TGZ_SW/LED/md/description.md#LED_sigs)

-	**LED signalizace**

	---
	
	<img src="../../../../../source/img/LEDsig.png" alt="LED signalizace" style="width:80%;">
	
-	LED diody

	---
	
	--8<-- "CZ/md/LEDsigAx12.md"
	
	Kompletní popis významu stavových LED diod naleznete zde: [Význam stavových indikátorů TGZ](../../TGZ_SW/LED/md/description.md#LED_sigs)

</div>

   
___
### Strana FB/motor
___

<img src="../../../../../source/img/TGZ-S-230-5_15_FBconns.png" alt="Motor/Feedback connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X5 - Externí enkodér (FBE)**

    ---
	Pohled zezadu (strana kabelu) 	
	<img src="../../../../../source/img/1277320000.svg" alt="FBE connector" style="width:60%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277320000_1.svg" alt="FBE connector" style="width:60%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277320000_2.svg" alt="FBE connector" style="width:60%;">	

-    Weidmüller B2CF 3.50/12/180 SN OR BX

	---

	--8<-- "CZ/md/X5_FBE_12pin_B2CF.md"
	
	Další informace ohledně externí zpětné vazby naleznete v sekci [Zpětná vazba FBE](../../../../source/md/commonHW_FBE.md#commonFBE).

-   **X6 - Zpětná vazba - osa 1**

    ---
	
	Pohled zezadu (strana kabelu) 	
	<img src="../../../../../source/img/1277290000.svg" alt="FB1 connector" style="width:50%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277290000_1.svg" alt="FB1 connector" style="width:50%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277290000_2.svg" alt="FB1 connector" style="width:50%;">

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X6_FB1_8pin_B2CF.md"
	
	Další informace ohledně zpětné vazby 1 naleznete v sekci [Zpětná vazba FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
-   **X7 - Zpětná vazba - osa 2**

    ---
	
	Pohled zezadu (strana kabelu) 	
	<img src="../../../../../source/img/1277290000.svg" alt="FB2 connector" style="width:50%;">
	
	3D pohled zezadu   
	<img src="../../../../../source/img/1277290000_1.svg" alt="FB2 connector" style="width:50%;">
	
	Pohled zepředu (strana TGZ)   
	<img src="../../../../../source/img/1277290000_2.svg" alt="FB2 connector" style="width:50%;">

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X7_FB2_8pin_B2CF.md"
	
	Další informace ohledně zpětné vazby 2 naleznete v sekci [Zpětná vazba FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
	!!! note "Poznámka"
	
		Servozesilovač TGZ-S-230-5/15 je jednoosý. Konektor X7 se běžně nezapojuje.
	
-   **X4 - Motorový konektor**

    ---
	
	<img src="../../../../../source/img/1846250000.svg" alt="Motor connector" style="width:70%;">

-    Weidmüller SLS 5.08/06/180FI SN OR BX

    ---

	--8<-- "CZ/md/X4_M1_6pin_SLS.md"
	
-   **X2 - Napájení silové části**

    ---
	
	<img src="../../../../../source/img/1943660000.svg" alt="PWR connector" style="width:100%;">

-    Weidmüller BLZP 5.08HC/10/180 SN OR BX

    ---

	--8<-- "CZ/md/X2_PWR_10pin_BLZP.md"
	

</div>


