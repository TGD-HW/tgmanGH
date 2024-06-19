##3D náhled
<img src="../../img/connectors.png" alt="TGZ-S-48-50/100RI connectors" style="width:90%;">

##Konektory
___
### Strana komunikace/ethernet/ethercat
___

<img src="../../../../../source/CZ/img/TGZ-S-48-50_100RI_enetCon.svg" alt="TGZ-S-48-50/100 ENET/ECAT/LogicPWR side" style="width:80%;">

<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
    <img src="../../../../../source/common/img/5055700501.svg" alt="Molex Microlock 5055700501" style="width:70%;">
	
-    Molex Microlock 5055700501

    --8<-- "CZ/md/X1_24V_5pin_Microlock.md"

-   **X11 - Zpětná vazba 3 - RS422**

    ---
    <img src="../../../../../source/common/img/5031491000.svg" alt="Molex ClikMate 5031491000" style="width:70%;">
	
-    Molex ClikMate 5031491000

    --8<-- "CZ/md/X11_FB3_10pin_ClikMate.md"
	
	!!! warning "Pozor"	
		Při použití tohoto typu zpětné vazby se ujistěte, že používáte vhodný TGZ firmware, který tyto funkce podporuje.

-   **X12 - Ethernet UDP - servisní**

    ---
    <img src="../../../../../source/common/img/5031490800.svg" alt="Molex ClikMate 5031490800" style="width:70%;">
	
-    Molex ClikMate 5031490800

    --8<-- "CZ/md/X12_UDP_8pin_ClikMate.md"

-   **X13 - EtherCAT 2 - Fieldbus out**

    ---
    <img src="../../../../../source/common/img/5031490800.svg" alt="Molex ClikMate 5031490800" style="width:70%;">
	
-    Molex ClikMate 5031490800

    --8<-- "CZ/md/X12_UDP_8pin_ClikMate.md"

-   **X13 - EtherCAT 1 - Fieldbus in**

    ---
    <img src="../../../../../source/common/img/5031490800.svg" alt="Molex ClikMate 5031490800" style="width:70%;">
	
-    Molex ClikMate 5031490800

    --8<-- "CZ/md/X12_UDP_8pin_ClikMate.md"

</div>


___
### Strana CAN/IO/SD
___

<img src="../../../../../source/CZ/img/TGZ-S-48-50_100RI_IO.svg" alt="IO/CAN/SD connectors" style="width:80%;">

<div class="grid cards" markdown>

-   **X7 - Digitální vstupy TTL + Analogové vstupy**

    ---
	<img src="../../../../../source/common/img/5031491200.svg" alt="DITTL + AIN + PT1000" style="width:70%;">

-    Molex ClikMate 5031491200

	---

	--8<-- "CZ/md/X7_AIN_12pin_ClikMate.md"

-   **X8 - Digitální I/O**

    ---
	<img src="../../../../../source/common/img/5031491800.svg" alt="ENET/ECAT/LogicPWR connectors" style="width:100%;">

-    Molex ClikMate 5031491800

	---

	--8<-- "CZ/md/X8_DIO_18pin_ClikMate.md"
		
-   **X9 - MicroSD slot**

    ---
	<img src="../../../../../source/common/img/uSD.png" alt="uSD card connector" style="width:40%;">

-   Použijte microSD kartu. Vhodná karta je součástí dodávky servozesilovače TGZ.

-   **X10 - CAN**

    ---
	
	<img src="../../../../../source/common/img/5031490800.svg" alt="CAN connector" style="width:70%;">

-    Molex ClikMate 5031490800

    ---

	--8<-- "CZ/md/X10_CAN_8pin_ClikMate.md"
	
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

<img src="../../../../../source/CZ/img/TGZ-S-48-50_100RI_FBconns.svg" alt="Motor/Feedback connectors" style="width:80%;">

<div class="grid cards" markdown>

-   **X4 - Externí enkodér (FBE)**

    ---
	
	<img src="../../../../../source/common/img/5031491200.svg" alt="FBE connector" style="width:80%;">

-    Molex ClikMate 5031491200

	---

	--8<-- "CZ/md/X4_FBE_12pin_ClikMate.md"

-   **X5 - Zpětná vazba - osa 1**

    ---
	
	<img src="../../../../../source/common/img/5031491000.svg" alt="FB1 connector" style="width:80%;">

-    Molex ClikMate 5031491000

    ---

	--8<-- "CZ/md/X5_FB1_10pin_ClikMate.md"
	
-   **X6 - Zpětná vazba - osa 2**

    ---
	
	<img src="../../../../../source/common/img/5031491000.svg" alt="FB2 connector" style="width:80%;">

-    Molex ClikMate 5031491000

    ---

	--8<-- "CZ/md/X6_FB2_10pin_ClikMate.md"
	
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


