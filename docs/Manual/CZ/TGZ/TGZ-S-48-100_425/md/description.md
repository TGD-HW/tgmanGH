##3D náhled
<img src="../../img/MotSide.svg" alt="TGZ-S-48-50/100 Feedback side" style="width:75%;">
<br>
<br>
<img src="../../img/IOside.svg" alt="TGZ-S-48-50/100 IO side" style="width:75%;">

##Konektory
___
### Strana ethernet/ethercat
___

<img src="../../../../../source/img/TGZ-S-48-100_250_enetCon.png" alt="TGZ-S-48-100/250 ENET/ECAT side" style="width:60%;">

___
### Strana CAN/IO/SD
___

<img src="../../../../../source/img/TGZ-S-48-100_250_IO.png" alt="IO/CAN/SD connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	<img src="../../../../../source/img/436500518.svg" alt="Molex Micro-Fit 3.0 436450500" style="width:90%;">

-    Molex Micro-Fit 3.0 - 436450500

	---

	--8<-- "CZ/md/X1_24V_5pin_Microfit.md"
	
	!!! warning "Upozornění"
		
		Pin č. 2 konektoru X1 - "Výstup +24 VDC" je nutné externě propojit s pinem č. 2 na konektoru P7 (napájení diagnostiky statické brzdy).
		
		Pozor na orientaci konektoru - zajišťovací páčka nahoře = pin č. 1 vpravo.
		
	!!! info "Konektorové krimpy"
	
		Přizpůsobte typ krimpů zvolenému průřezu vodiče.

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
### Strana feedback
___

<img src="../../../../../source/img/TGZ-S-48-100_250_FBconns.png" alt="Motor/Feedback connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X5 - Externí enkodér (FBE)**

    ---
	
	<img src="../../../../../source/img/1277320000.svg" alt="FBE connector" style="width:80%;">

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
___
### Pohled na PCB
___

<img src="../../../../../source/img/TGZ-S-48-100_250_brd.png" alt="PCB connections" style="width:70%;">


<div class="grid cards" markdown>

-   **P7 - Statická brzda**

    ---
	
	<img src="../../../../../source/img/430450412.svg" alt="Brake connector" style="width:60%;">

-    Molex Micro-Fit 3.0 - 430250400

	---

	--8<-- "CZ/md/P7_BR_4pin_Microfit.md"
	
	!!! info "Konektorové krimpy"
	
		Přizpůsobte typ krimpů zvolenému průřezu vodiče.
		
-   **P8 - Statická brzda - doplňkový konektor**

    ---
	
	<img src="../../../../../source/img/430450412.svg" alt="Brake connector aux" style="width:60%;">

-    Molex Micro-Fit 3.0 - 430250400

	---

	--8<-- "CZ/md/P8_BR_4pin_Microfit.md"
	
	!!! note "Konektor P8"
	
		Tento konektor se pro standardní použití jednoosého servozesilovače <nobr>TGZ-S-48-100/250</nobr> nezapojuje
	
	!!! info "Konektorové krimpy"
	
		Přizpůsobte typ krimpů zvolenému průřezu vodiče.
		
-   **P3 - Externí termistor PT1000**

    ---
	
	<img src="../../../../../source/img/436500215.svg" alt="External thermistor" style="width:60%;">

-    Molex Micro-Fit 3.0 - 436500215

	---

	--8<-- "CZ/md/P3_Term_2pin_Microfit.md"
	
	!!! note "Polarita"
	
		Teplotní čidlo PT1000 nemá určenou polaritu napájení.
	
	!!! info "Konektorové krimpy"
	
		Přizpůsobte typ krimpů zvolenému průřezu vodiče.		

</div>