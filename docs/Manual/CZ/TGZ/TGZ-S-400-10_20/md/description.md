##3D náhled
![3D view IO side](../img/IOside.webp){: style="width:70%;" }
<br>
<br>
![3D view motor side](../img/MotSide.webp){: style="width:75%;" }

##Konektory
___
### Strana komunikace/ethernet/ethercat
___

![ENET/ECAT/LogicPWR connectors](../../../../source/img/TGZ-S-400-3_9_enetCon.png){: style="width:60%;" }


<div class="grid cards" markdown>

-   **X1 - Napájení řídicí části**

    ---
	Pohled zezadu (strana vodičů)   
	
	![1941040000](../../../../source/img/1941040000.webp){: style="width:60%;" }   
	
	![1941040000_1](../../../../source/img/1941040000_1.webp){: style="width:60%;" }	

-    Weidmüller BCZ 3.81/05/180F SN OR BX

	---

	--8<-- "md/X1_24V_5pin_BCZ.md"
	
	!!! warning "Odrušení přívodu"
	
		Věnujte prosím pozornost instalaci odrušovacího toroidu dle [návodu](../../../../source/md/logicPWR.md#LogicPWR_EMI).

</div>

___
### Strana CAN/IO/SD
___

![IO/CAN/SD connectors](../../../../source/img/TGZ-S-400-3_9_IO.png){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X8 - Digitální I/O, analogové vstupy**

    ---
	Pohled zezadu (strana kabelu)   
	
	![X8 pinout](../../../../source/img/1277370000.svg){: style="width:100%;" }
	3D pohled zezadu   
	
	![X8 pinout 3D](../../../../source/img/1277370000_1.svg){: style="width:100%;" }
	Pohled zepředu (strana TGZ)   
	
	![X8 pinout front](../../../../source/img/1277370000_2.svg){: style="width:100%;" }

	Detailní soupis parametrů 
	[digitálních vstupů DI1-8](../../../../source/md/commonHW_DI.md#commonDI1-8), 
	[digitálních výstupů DO1-6](../../../../source/md/commonHW_DO.md#commonDO1-6) a 
	[analogových vstupů AI1-2](../../../../source/md/commonHW_AI.md#commonAI1-2) 
	naleznete v sekci [Společný HW](../../../../source/md/commonHW_DI.md#commonDI1-8).
	

-    Weidmüller B2CF 3.50/22/180 SN OR BX

	---

	--8<-- "md/X8_IO_22pin_B2CF.md"
	
	!!! warning "Pozor"	
	
		Pro správnou funkci DI(1-6) je potřeba připojit alespoň jedno z VCC DO (pin 11 a 12). Vstupy DI7,8 jsou nezávislé na napájecím napětí DO VCC a fungují korektně i bez něj.
	
-   **X9 - MicroSD karta**

    ---
![uSD card connector](../../../../source/img/uSD.png){: style="width:60%;" }

-    Použijte standardní microSD kartu. Karta je součástí dodávky servozesilovače TGZ. Více informací naleznete v sekci [SD karty](../../TGZ_SW/SD/md/SD.md#SDparams).

-   **X10 - CAN**

    ---
	Pohled zezadu (strana kabelu)   
	![CAN connector](../../../../source/img/1277270000.svg){: style="width:25%;" }
	
	3D pohled zezadu   
	![CAN connector](../../../../source/img/1277270000_1.svg){: style="width:45%;" }
	
	Pohled zepředu (strana TGZ)   
	![CAN connector](../../../../source/img/1277270000_2.svg){: style="width:35%;" }

-    Weidmüller B2CF 3.50/04/180 SN OR BX

    ---

	--8<-- "md/X10_CAN_4pin_B2CF.md"
	
	Další informace o HW provedení sběrnice CAN naleznete v sekci [Sběrnice CAN](../../../../source/md/commonHW_CAN.md#commonCAN).
	
-	**LED displej**

	---
	
	![LED displej](../../../../source/img/TGZ_LED.png){: style="width:60%;" }
	
-	LED displej signalizuje stavy viz. [Význam stavových indikátorů TGZ](../../TGZ_SW/LED/md/description.md#LED_sigs)

-	**LED signalizace**

	---
	
	![LED signalizace](../../../../source/img/statusLedsECAT.svg){: style="width:100%;" }
	
-	LED diody

	---
	
	--8<-- "md/LEDsigAx12.md"
	
	Kompletní popis významu stavových LED diod naleznete zde: [Význam stavových indikátorů TGZ](../../TGZ_SW/LED/md/description.md#LED_sigs)

</div>

   
___
### Strana FB/motor
___

![Motor/Feedback connectors](../../../../source/img/TGZ-S-400-3_9_FBconns.png){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X5 - Externí enkodér (FBE)**

    ---
	Pohled zezadu (strana kabelu) 	
	![FBE connector](../../../../source/img/1277320000.svg){: style="width:60%;" }
	
	3D pohled zezadu   
	![FBE connector](../../../../source/img/1277320000_1.svg){: style="width:60%;" }
	
	Pohled zepředu (strana TGZ)   
	![FBE connector](../../../../source/img/1277320000_2.svg){: style="width:60%;" }	

-    Weidmüller B2CF 3.50/12/180 SN OR BX

	---

	--8<-- "md/X5_FBE_12pin_B2CF.md"
	
	Další informace ohledně externí zpětné vazby naleznete v sekci [Zpětná vazba FBE](../../../../source/md/commonHW_FBE.md#commonFBE).

-   **X6 - Zpětná vazba - osa 1**

    ---
	
	Pohled zezadu (strana kabelu) 	
	![FB1 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D pohled zezadu   
	![FB1 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Pohled zepředu (strana TGZ)   
	![FB1 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "md/X6_FB1_8pin_B2CF.md"
	
	Další informace ohledně zpětné vazby 1 naleznete v sekci [Zpětná vazba FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
-   **X7 - Zpětná vazba - osa 2**

    ---
	
	Pohled zezadu (strana kabelu) 	
	![FB2 connector](../../../../source/img/1277290000.svg){: style="width:50%;" }
	
	3D pohled zezadu   
	![FB2 connector](../../../../source/img/1277290000_1.svg){: style="width:50%;" }
	
	Pohled zepředu (strana TGZ)   
	![FB2 connector](../../../../source/img/1277290000_2.svg){: style="width:50%;" }

-    Weidmüller B2CF 3.50/08/180 SN OR BX

    ---

	--8<-- "md/X7_FB2_8pin_B2CF.md"
	
	Další informace ohledně zpětné vazby 2 naleznete v sekci [Zpětná vazba FB1, FB2](../../../../source/md/commonHW_FB12.md#commonFB12).
	
	!!! note "Poznámka"
	
		Servozesilovač TGZ-S-400 je jednoosý. Konektor X7 se běžně nezapojuje.
	
-   **X4 - Motorový konektor**

    ---
	
	![Motor connector](../../../../source/img/1095720000.svg){: style="width:70%;" }

-    Weidmüller BLZ 7.62HP/06/180F

    ---

	--8<-- "md/X4_M1_6pin_SLS.md"

	!!! warning "Orientace konektoru"
	
		Pozor na správnou orientaci konektoru při zapojování kabeláže.	
	
-   **X2 - Napájení silové části**

    ---
	
	![PWR connector](../../../../source/img/1095780000.svg){: style="width:100%;" }
	
	Konektor X2 je standardně dodáván včetně propojovacích vodičů v konfiguraci pro použítí interního brzdného odporu.
	
	![PWR connector](../../../../source/img/1095780000jumper.svg){: style="width:100%;" }   
	
	V případě použití externího brzdného rezistoru je nutné odstranit propojovací vodiče a rezistor připojit dle [schématu](schematic.md).	

-    Weidmüller  BLZ 7.62HP/12/180F

    ---

	--8<-- "md/X2_PWR_12pin_BLZ.md"
	

</div>


