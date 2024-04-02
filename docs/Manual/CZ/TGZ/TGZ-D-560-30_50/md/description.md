<!--
# Popis zařízení   

## Konektory
-->
##3D náhled
<img src="../../img/IOside.png" alt="3D view IO side" style="width:75%;">
<img src="../../img/Motside.png" alt="3D view FB side" style="width:60%;">

##Konektory
___
### Strana komunikace/ethernet/ethercat a DCbus
___

<img src="../../../../../source/CZ/img/TGZ-D-560-30_50_DCbus.svg" alt="ENET/ECAT/DCbus connectors" style="width:60%;">


<div class="grid cards" markdown>

-   **X2 - DC bus konektor**

    ---
	<img src="../../../../../source/common/img/D560DCbusCon.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:70%;">

-    Šroubovací svorky M8

	---

	--8<-- "CZ/md/X2_D560DCbus.md"

</div>

___
### Strana CAN/IO/SD a motor
___

<img src="../../../../../source/CZ/img/TGZ-D-560-30_50_Mot.svg" alt="IO/CAN/SD + motor connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X3 - Motorový konektor osa 1**

    ---
	
	<img src="../../../../../source/common/img/2626-1104.svg" alt="Motor connector 1" style="width:70%;">

-    Wago push-in svorky

    ---

	--8<-- "CZ/md/X4_M1_6pin_SLS.md"
	
-   **X4 - Motorový konektor osa 2**

    ---
	
	<img src="../../../../../source/common/img/1846250000.svg" alt="Motor connector" style="width:70%;">

-    Wago push-in svorky

    ---

	--8<-- "CZ/md/X4_M1_6pin_SLS.md"

-   **X8 - Digitální I/O, analogové vstupy**

    ---
	<img src="../../../../../source/common/img/1277370000.png" alt="ENET/ECAT/LogicPWR connectors" style="width:100%;">

-    Weidmüller BCZ 3.81/22/180 SN OR BX

	---

	--8<-- "CZ/md/X8_IO_22pin_BCZ.md"
	
	!!! warning "Pozor"	
	
		Pro správnou funkci DI(1-6) je potřeba připojit alespoň jedno z VCC DO (pin 11 a 12). Vstupy DI7,8 jsou nezávislé na napájecím napětí DO VCC a fungují korektně i bez něj.
	
-   **X9 - MicroSD karta**

    ---
<img src="../../../../../source/common/img/uSD.png" alt="uSD card connector" style="width:60%;">

-    Použijte microSD kartu průmyslové specifikace. Karta je součástí dodávky servozesilovače TGZ.

-   **X10 - CAN**

    ---
	
	<img src="../../../../../source/common/img/1277270000.png" alt="CAN connector" style="width:25%;">

-    Weidmüller BCZ 3.81/04/180 SN OR BX

    ---

	--8<-- "CZ/md/X10_CAN_4pin_BCZ.md"
	
-	**LED displej**

	---
	
	<img src="../../../../../source/common/img/TGZ_LED.png" alt="LED displej" style="width:60%;">
	
-	LED displej signalizuje stavy viz. kap. XY

-	**LED signalizace**

	---
	
	<img src="../../../../../source/CZ/img/LEDsig.png" alt="LED signalizace" style="width:80%;">
	
-	LED diody

	---
	
	--8<-- "CZ/md/LEDsigAx12.md"

</div>

   
___
### Strana Feedback
___

<img src="../../../../../source/CZ/img/TGZ-D-560-30_50_FBconns.svg" alt="Feedback connectors" style="width:60%;">

<div class="grid cards" markdown>

-   **X5 - Externí enkodér (FBE)**

    ---
	
	<img src="../../../../../source/common/img/1277320000.png" alt="FBE connector" style="width:60%;">

-    Weidmüller BCZ 3.81/12/180 SN OR BX

	---

	--8<-- "CZ/md/X5_FBE_12pin_BCZ.md"

-   **X6 - Zpětná vazba - osa 1**

    ---
	
	<img src="../../../../../source/common/img/1277290000.png" alt="FB1 connector" style="width:50%;">

-    Weidmüller BCZ 3.81/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X6_FB1_8pin_BCZ.md"
	
-   **X7 - Zpětná vazba - osa 2**

    ---
	
	<img src="../../../../../source/common/img/1277290000.png" alt="FB2 connector" style="width:50%;">

-    Weidmüller BCZ 3.81/08/180 SN OR BX

    ---

	--8<-- "CZ/md/X7_FB2_8pin_BCZ.md"	

</div>


