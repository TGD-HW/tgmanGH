<!--##Connectors-->
___
### View of the ENET/ECAT side
___

![TGMmini power side](../img/PWRside.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X3 - Napájení řídicí části**

    ---
	![24V connector 2439670000](../../../../source/img/2439670000.svg){: style="width:60%;" }

-    Weidmüller BLF 2.50/04/180 SN OR BX

	---

	--8<-- "md/X3_24V_BLF_2_5.en.md"


-   **X4 - CAN**

    ---
	
	![CAN connector](../../../../source/img/1277270000.svg){: style="width:25%;" }

-    Weidmüller BCZ 3.81/04/180 SN OR BX

    ---

	--8<-- "md/X10_CAN_4pin_B2CF.en.md"
	
</div>	

___
### Strana IO/USB/SD
___

![TGMmini IO side](../img/IOside.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X5 - Digital inputs**

    ---
	
	![DI connector](../../../../source/img/1277310000.svg){: style="width:60%;" }

-    Weidmüller B2CF 3.50/10/180 SN OR BX

    ---

	--8<-- "md/X5_DI_10pin_B2CF.en.md"
	
-   **X10 - Digital výstupy**

    ---
	
	![DO connector](../../../../source/img/1277310000.svg){: style="width:60%;" }

-    Weidmüller B2CF 3.50/10/180 SN OR BX

    ---

	--8<-- "md/X10_DO_10pin_B2CF.en.md"
	
	!!! warning "Důležité upozornění"	
	
		Napájení digitálních výstupů musí být kompletní, tj. musí být správně připojen zemnící vodič OUTCOM (pin 9) a kladný vodič +24 V (OUTPWR, pin 10).
		V případě, že je zemnící vodič přerušen, na všech výstupech se po cca jedné sekundě objeví přibližně 21&nbsp;V. 
		Výstupy pak můžou sepnout připojené zařízení a přepnout je tak do nechtěného stavu. 
		Pokud by bylo potřeba tento stav ošetřit, je potřeba připojit zemnící vodič přes bezpečnostní relé (např. OMRON K8AKAS1), které bude monitorovat proud tekoucí do výstupního obvodu TGMmini. 
		**TGDrives, s.r.o. nenese žádnou zodpovědnost za nesprávně zapojené napájení TGMmini a za případné následné chybové situace. 
		Správné a bezchybné zapojení je plně v kompetenci uživatele TGMmini a musí být provedeno odborným pracovníkem s příslušnou kvalifikací pro montáž elektrických zařízení.**
	
-   **S1 - CAN terminace linky**

    ---
	
	![CAN termination switch](../../../../source/img/BPA01B.png){: style="width:40%;" }

-    DIP switch

    ---

	--8<-- "md/S1_SWITCH_CAN.en.md"

</div>