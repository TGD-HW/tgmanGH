##3D náhled
<img src="../../img/IOside.png" alt="3D view IO side" style="width:75%;">
<br>
<br>
<img src="../../img/Motside.png" alt="3D view FB side" style="width:60%;">

##Konektory
___
### Strana komunikace/ethernet/ethercat a DCbus
___

<img src="../../../../../source/img/TGZ-D-560-30_50_DCbus.svg" alt="ENET/ECAT/DCbus connectors" style="width:60%;">


<div class="grid cards" markdown>

-   **X2 - DC bus konektor**

    ---
	<img src="../../../../../source/img/D560DCbusCon.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:70%;">

-    Šroubovací svorky M8

	---

	--8<-- "CZ/md/X2_D560DCbus.md"

</div>

___
### Strana CAN/IO/SD, +24V napájení, motor
___

<img src="../../../../../source/img/TGZ-D-560-30_50_Mot.svg" alt="IO/CAN/SD + motor connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	<img src="../../../../../source/img/1940760000.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:70%;">

-    Weidmüller BCZ 3.81/05/180 SN OR BX

	---

	--8<-- "CZ/md/X1_24V_5pin_BCZ.md"

-   **X3 - Motorový konektor osa 1**

    ---
	
	<img src="../../../../../source/img/2626-1104.svg" alt="Motor connector 1" style="width:70%;">

-    Wago push-in svorky

    ---

	--8<-- "CZ/md/X3_M1_4pin_wago_2636.md"
	
-   **X4 - Motorový konektor osa 2**

    ---
	
	<img src="../../../../../source/img/2626-1104.svg" alt="Motor connector 2" style="width:70%;">

-    Wago push-in svorky

    ---

	--8<-- "CZ/md/X4_M2_4pin_wago_2636.md"
	
-   **X14 - Brzda/Termistor osa 1**

    ---
	
	<img src="../../../../../source/img/1876530000R.svg" alt="Brake/Thermistor 1" style="width:70%;">

-    Wago LSF svorky

    ---

	--8<-- "CZ/md/X14_BR1_4pin_LSF.md"
	
-   **X15 - Brzda/Termistor osa 2**

    ---
	
	<img src="../../../../../source/img/1876530000R.svg" alt="Brake/Thermistor 2" style="width:70%;">

-    Wago LSF svorky

    ---

	--8<-- "CZ/md/X15_BR2_4pin_LSF.md"

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
### Strana Feedback
___

<img src="../../../../../source/img/TGZ-D-560-30_50_FBconns.svg" alt="Feedback connectors" style="width:60%;">

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

</div>


