<!--##Konektory-->
___
### Strana komunikace/ethernet/ethercat
___

<img src="../../img/PWRside.png" alt="TGMmini power side" style="width:60%;">


<div class="grid cards" markdown>

-   **X3 - Napájení řídicí části**

    ---
	<img src="../../../../../source/img/2439670000.svg" alt="24V connector 2439670000" style="width:60%;">

-    Weidmüller BLF 2.50/04/180 SN OR BX

	---

	--8<-- "CZ/md/X3_24V_BLF_2_5.md"


-   **X4 - CAN**

    ---
	
	<img src="../../../../../source/img/1277270000.svg" alt="CAN connector" style="width:25%;">

-    Weidmüller BCZ 3.81/04/180 SN OR BX

    ---

	--8<-- "CZ/md/X10_CAN_4pin_B2CF.md"
	
</div>	

___
### Strana IO/USB/SD
___

<img src="../../img/IOside.png" alt="TGMmini IO side" style="width:60%;">


<div class="grid cards" markdown>

-   **X5 - Digitální vstupy**

    ---
	
	<img src="../../../../../source/img/1277310000.svg" alt="DI connector" style="width:60%;">

-    Weidmüller B2CF 3.50/10/180 SN OR BX

    ---

	--8<-- "CZ/md/X5_DI_10pin_B2CF.md"
	
-   **X10 - Digitální výstupy**

    ---
	
	<img src="../../../../../source/img/1277310000.svg" alt="DO connector" style="width:60%;">

-    Weidmüller B2CF 3.50/10/180 SN OR BX

    ---

	--8<-- "CZ/md/X10_DO_10pin_B2CF.md"
	
	!!! warning "Důležité upozornění"	
	
		Napájení digitálních výstupů musí být kompletní, tj. musí být správně připojen zemnící vodič OUTCOM (pin 9) a kladný vodič +24 V (OUTPWR, pin 10).
		V případě, že je zemnící vodič přerušen, na všech výstupech se po cca jedné sekundě objeví přibližně 21&nbsp;V. 
		Výstupy pak můžou sepnout připojené zařízení a přepnout je tak do nechtěného stavu. 
		Pokud by bylo potřeba tento stav ošetřit, je potřeba připojit zemnící vodič přes bezpečnostní relé (např. OMRON K8AKAS1), které bude monitorovat proud tekoucí do výstupního obvodu TGMmini. 
		**TGDrives, s.r.o. nenese žádnou zodpovědnost za nesprávně zapojené napájení TGMmini a za případné následné chybové situace. 
		Správné a bezchybné zapojení je plně v kompetenci uživatele TGMmini a musí být provedeno odborným pracovníkem s příslušnou kvalifikací pro montáž elektrických zařízení.**
	
-   **S1 - CAN terminace linky**

    ---
	
	<img src="../../../../../source/img/BPA01B.png" alt="CAN termination switch" style="width:40%;">

-    DIP switch

    ---

	--8<-- "CZ/md/S1_SWITCH_CAN.md"

</div>