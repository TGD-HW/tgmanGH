##3D náhled
<img src="../../img/IOside.svg" alt="TGZ-S-48-50/100 IO side" style="width:70%;">
<br>
<br>
<img src="../../img/MotSide.svg" alt="TGZ-S-48-50/100 Feedback side" style="width:70%;">

##Konektory
___
### Strana komunikace/ethernet/ethercat
___

<img src="../../../../../source/CZ/img/TGZ-S-48-50_100_enetCon.png" alt="TGZ-S-48-50/100 ENET/ECAT/LogicPWR side" style="width:60%;">


<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	<img src="../../../../../source/common/img/5055700501.svg" alt="Molex Microlock 5055700501" style="width:70%;">

-    Molex Microlock 5055700501

	---

	--8<-- "CZ/md/X1_24V_5pin_Microlock.md"

</div>

___
### Strana CAN/IO/SD
___

<img src="../../../../../source/CZ/img/TGZ-S-48-50_100_IO.png" alt="IO/CAN/SD connectors" style="width:60%;">

<div class="grid cards" markdown>

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
### Strana FB/motor
___

<img src="../../../../../source/CZ/img/TGZ-S-48-50_100_FBconns.png" alt="Motor/Feedback connectors" style="width:60%;">

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
	
-   **X3 - Napájení silové části**

    ---
	
	<img src="../../../../../source/common/img/S-48pressfit5.svg" alt="DC bus connection" style="width:70%;">

-    Pressfit M5

    ---

	--8<-- "CZ/md/X3_DCbus_2pin_pressfit.md"
	
-   **X3 - Připojení motoru**

    ---
	
	<img src="../../../../../source/common/img/S-48pressfit5.svg" alt="Motor connection" style="width:70%;">

-    Pressfit M5

    ---
	
	--8<-- "CZ/md/X3_M1_3pin_pressfit.md"


-   **X4 - Připojení brzdy**

    ---
	
	<img src="../../../../../source/common/img/5055700401.svg" alt="Brake connection" style="width:70%;">

-    Molex Micro-lock 505570-0401

    ---

	--8<-- "CZ/md/X4_BR_4pin_Microlock.md"

</div>


