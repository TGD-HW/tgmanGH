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

<img src="../../../../../source/CZ/img/TGZ-S-230-5_15_enetCon.png" alt="ENET/ECAT/LogicPWR connectors" style="width:60%;">


<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	<img src="../../../../../source/common/img/1940760000.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:70%;">

-    Weidmüller BCZ 3.81/05/180 SN OR BX

	---

	--8<-- "CZ/md/X1_24V_5pin_BCZ.md"

</div>

___
### Strana CAN/IO/SD
___

<img src="../../../../../source/CZ/img/TGZ-S-230-5_15_IO.png" alt="IO/CAN/SD connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X8 - Digitální I/O, analogové vstupy**

    ---
	<img src="../../../../../source/common/img/1277370000.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:100%;">

-    Weidmüller B2CF 3.50/22/180 SN OR BX

	---

	--8<-- "CZ/md/X8_IO_22pin_B2CF.md"
	
	!!! warning "Pozor"	
	
		Pro správnou funkci DI(1-6) je potřeba připojit alespoň jedno z VCC DO (pin 11 a 12). Vstupy DI7,8 jsou nezávislé na napájecím napětí DO VCC a fungují korektně i bez něj.
	
-   **X9 - MicroSD karta**

    ---
<img src="../../../../../source/common/img/uSD.png" alt="uSD card connector" style="width:60%;">

-    Použijte standardní microSD kartu. Karta je součástí dodávky servozesilovače TGZ. Více informací naleznete v sekci [SD karty](../../TGZ_SW/SD/md/SD.md#SDparams).

-   **X10 - CAN**

    ---
	
	<img src="../../../../../source/common/img/1277270000.svg" alt="CAN connector" style="width:25%;">

-    Weidmüller B2CF 3.50/04/180 SN OR BX

    ---

	--8<-- "CZ/md/X10_CAN_4pin_B2CF.md"
	
-	**LED displej**

	---
	
	<img src="../../../../../source/common/img/TGZ_LED.png" alt="LED displej" style="width:60%;">
	
-	LED displej signalizuje stavy viz. [Význam stavových indikátorů TGZ](../../TGZ_SW/LED/md/description.md#LED_sigs)

-	**LED signalizace**

	---
	
	<img src="../../../../../source/CZ/img/LEDsig.png" alt="LED signalizace" style="width:80%;">
	
-	LED diody

	---
	
	--8<-- "CZ/md/LEDsigAx12.md"
	
	Kompletní popis významu stavových LED diod naleznete zde: [Význam stavových indikátorů TGZ](../../TGZ_SW/LED/md/description.md#LED_sigs)

</div>

   
___
### Strana FB/motor
___

<img src="../../../../../source/CZ/img/TGZ-S-230-5_15_FBconns.png" alt="Motor/Feedback connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X5 - Externí enkodér (FBE)**

    ---
	
	<img src="../../../../../source/common/img/1277320000.svg" alt="FBE connector" style="width:60%;">

-    Weidmüller B2CF 3.50/12/180 SN OR BX

	---

	--8<-- "CZ/md/X5_FBE_12pin_B2CF.md"

-   **X6 - Zpětná vazba - osa 1**

    ---
	
	<img src="../../../../../source/common/img/1277290000.svg" alt="FB1 connector" style="width:50%;">

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X6_FB1_8pin_B2CF.md"
	
-   **X7 - Zpětná vazba - osa 2**

    ---
	
	<img src="../../../../../source/common/img/1277290000.svg" alt="FB2 connector" style="width:50%;">

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X7_FB2_8pin_B2CF.md"
	
	!!! note "Poznámka"
	
		Servozesilovač TGZ-S-230-5/15 je jednoosý. Konektor X7 se běžně nezapojuje.
	
-   **X4 - Motorový konektor**

    ---
	
	<img src="../../../../../source/common/img/1846250000.svg" alt="Motor connector" style="width:70%;">

-    Weidmüller SLS 5.08/06/180FI SN OR BX

    ---

	--8<-- "CZ/md/X4_M1_6pin_SLS.md"
	
-   **X2 - Napájení silové části**

    ---
	
	<img src="../../../../../source/common/img/1943660000.svg" alt="PWR connector" style="width:100%;">

-    Weidmüller BLZP 5.08HC/10/180 SN OR BX

    ---

	--8<-- "CZ/md/X2_PWR_10pin_BLZP.md"
	

</div>


