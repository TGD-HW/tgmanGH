##3D náhled
![3D view IO side](../img/IOside.webp){: style="width:70%;" }
<br>
<br>
![3D view motor side](../img/MotSide.webp){: style="width:70%;" }

##Popis komunikace, vstupů/výstupů a ovládání:
###Komunikační rozhraní
- Ethernet 100/1000 Mb/s s UDP protokolem, určen pro záznam parametrů, monitorování, testování, ale také online ovládání.
- CAN bus protokol lze upravit podle požadavků zákazníka.
- Ethernet 100/1000 Mb/s s volitelným protokolem, naprogramovaný v hradlovém poli a určený pro připojení rychlých průmyslových sběrnic pro řízení v reálném čase.
  V současné době je toto rozhraní vybaveno protokolem EtherCAT (pouze pro standardní firmware); podle požadavků zákazníka lze upravit na jiný typ protokolu.
- RS422 / RS485, přenos dat přes nepoužívané rozhraní zpětné vazby servomotoru.
  Může být použit pro komunikaci se zařízeními založenými na RI RS422 nebo RS485 (enkodér, gyroskop, nadřazené řízení, jiný systém atd.).
  Toto rozhraní umožňuje vysokorychlostní komunikaci až 20 Mbit/s.
  
###Vstupy / výstupy:
Vestavné servozesilovače TGZ mají 8 digitálních vstupů, 3 digitální vstupy, 6 digitálních výstupů a 2 vstupy pro teplotní čidlo PT1000 a jeden analogový vstup.
Tyto vstupy a výstupy je možné ovládat pomocí uživatelského programu (jazyk C).
Digitální výstupy lze ovládat i přes ovládací servisní software TGZ GUI.

| I/O     | Typ              | Počet | Hodnota                                            |
|---------|------------------|--------|----------------------------------------------------|
| vstup   | analogový        | 1      | 0-10 V                                             |
| vstup   | termistor        | 2      | standard PT1000                                    |
| vstup   | digitální        | 3      | 0-30 VDC (0-0,8 V low/2,4-30 V high)      |
| vstup   | izolovaný digitální | 8   | 0-24 VDC (0-10 V low/13-24 V high), 20 mA      |
| výstup  | izolovaný digitální | 6   | 5-24 VDC, 300 mA / max. výstup                     |

Servozesilovač má čtyři zpětnovazební rozhraní, které mají široké využití.
Kromě zpětné vazby motoru je lze použít k připojení zařízení pracujících na principu RI RS422 nebo RS485.

| Typ   | Standard              | Rozhraní                         | Příklady připojení možných zařízení                                                                                               |
|-------|-----------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| FB1   | RS422/RS485           | Hiperface DSL, EnDat 2.2, SSI, BISS | Absolutní magnetický / optický enkodér, inkrementální magnetický / optický enkodér s Hallovými senzory [^2], gyroskop              |
| FB2   | RS422/RS485           | Hiperface DSL, EnDat 2.2, SSI, BISS | Absolutní magnetický / optický enkodér, inkrementální magnetický / optický enkodér s Hallovými senzory [^2], gyroskop              |
| FE[^1]   | RS422/RS485           | Hiperface DSL, EnDat 2.2, SSI, BISS | Absolutní magnetický / optický enkodér, inkrementální magnetický / optický enkodér s Hallovými senzory [^2], gyroskop              |
| FB3[^1]  | 2 × full-duplex RS422 | -                                | Řídicí systém                                                                                                                     |

[^1]: Tento typ pracuje pouze s upraveným firmwarem. Jeho použití se doporučuje vždy konzultovat s výrobcem.
[^2]: Hallovy senzory musí být připojeny k digitálním vstupům pomocí speciálního převodníku úrovní, viz. [Převodník Hall-TGZ](../../../ETC/TGHall/md/description.md#TGhall_1).

- Hiperface DSL - digitální komunikace, senzory jsou vyráběny s rozlišením 15 až 24 bitů na otáčku (vícerychlostní provedení - 4 096 otáček).
  Tento typ zpětné vazby se používá pro motory s jediným konektorem nebo kabelem.
- EnDat 2.2 - digitální komunikace, senzory jsou vyráběny s rozlišením 18 až 25 bitů na otáčku (vícerychlostní provedení - 4 096 otáček).
- SSI - enkodéry se synchronním systémovým rozhraním.
- BISS - senzory s protokolem BISS-C.

###Řízení
Servozesilovače TGZ je možno řídit:

- digitální ovládání přes EtherCAT, CAN-bus (točivý moment, otáčky, polohové profily atd.) A přes Ethernet UDP protokol;
- uživatelský program (jazyk C) - digitální vstupy, analogové napětí atd.

##Konektory
___
### Strana komunikace
___

![ENET/ECAT/LogicPWR connectors](../../../../source/img/TGZ-S-400-14_30-RI_enetCon.webp){: style="width:60%;" }


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

-   **X11 - Zpětná vazba 3 - RS422**

    ---
    ![Molex ClikMate 5031491000](../../../../source/img/5031491000.svg){: style="width:70%;" }
	
-    Molex ClikMate 5031491000 - doporučené krimpovací kontakty [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    --8<-- "md/X11_FB3_10pin_ClikMate.md"
	
	!!! warning "Pozor"	
		Při použití tohoto typu zpětné vazby se ujistěte, že používáte vhodný TGZ firmware, který tyto funkce podporuje.

-   **X12 - Ethernet UDP - servisní**

    ---
    ![Molex ClikMate 5031490800](../../../../source/img/5031490800.svg){: style="width:70%;" }
	
-    Molex ClikMate 5031490800 - doporučené krimpovací kontakty [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    --8<-- "md/X12_UDP_8pin_ClikMate.md"

</div>

___
### Strana IO/SD
___

![IO/CAN/SD connectors](../../../../source/img/TGZ-S-400-14_30-RI_IO.webp){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X7 - Digitální vstupy + Analogové vstupy**

    ---
	![DITTL + AIN + PT1000](../../../../source/img/5031491200.svg){: style="width:70%;" }

-    Molex ClikMate 5031491200 - doporučené krimpovací kontakty [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

	---

	--8<-- "md/X7_AIN_12pin_ClikMate.md"
	
	!!! warning "Varování"
		Přímé vstupy PT1000 na pinech 3-6 konektoru X7 jsou dostupné pouze na řídicí desce z dodávek po 06-2024.
		Starší verze zařízení mají standardní AIN1, AIN2 a AIN3 na pinech 1-6 konektoru X7.
		Pro další podrobnosti o vlastnostech předchozího zařízení prosím nahlédněte do starší (PDF) verze tohoto manuálu.

-   **X8 - Digitální I/O**

    ---
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/5031491800.svg){: style="width:100%;" }

-    Molex ClikMate 5031491800 - doporučené krimpovací kontakty [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

	---

	--8<-- "md/X8_DIO_18pin_ClikMate.md"
		
-   **X9 - MicroSD slot**

    ---
	![uSD card connector](../../../../source/img/uSD.png){: style="width:40%;" }

-   V servozesilovačích typu "RI" není primárně doporučeno používat microSD slot u zařízení, kde se předpokládají velké vibrace.
	SD karta není u těchto verzí součástí dodávky.
	Pro více informací ohledně SD karet navštivte sekci [SD karty](../../TGZ_SW/SD/md/SD.md#SDparams).

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

![Motor/Feedback connectors](../../../../source/img/TGZ-S-400-14_30-RI_FBconns.webp){: style="width:60%;" }

<div class="grid cards" markdown>

-   **X4 - Externí enkodér (FBE)**

    ---
	
	![FBE connector](../../../../source/img/5031491200.svg){: style="width:80%;" }

-    Molex ClikMate 5031491200 - doporučené krimpovací kontakty [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

	---

	--8<-- "md/X4_FBE_12pin_ClikMate.md"

-   **X5 - Zpětná vazba - osa 1**

    ---
	
	![FB1 connector](../../../../source/img/5031491000.svg){: style="width:80%;" }

-    Molex ClikMate 5031491000 - doporučené krimpovací kontakty [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    ---

	--8<-- "md/X5_FB1_10pin_ClikMate.md"
	
	!!! warning "Upozornění"
		Aby bylo možné použít typ zpětné vazby Hiperface DSL, uživatel musí propojit piny 5-7 a 6-8 konektoru FB1 nebo naletovat odpovídající propojky (rezistory) na řídicí desku TGZcontrol.
		Toto platí pro dodávky po 06-2024, kde není provedeno žádné interní spojení.
		Ověřte také, zda máte v zařízení nahrán správný firmware podporující zvolený typ zpětné vazby.
	
-   **X6 - Zpětná vazba - osa 2**

    ---
	
	![FB2 connector](../../../../source/img/5031491000.svg){: style="width:80%;" }

-    Molex ClikMate 5031491000 - doporučené krimpovací kontakty [Molex 502579](https://www.molex.com/en-us/part-list/502579) [^1]

    ---

	--8<-- "md/X6_FB2_10pin_ClikMate.md"
	
	!!! warning "Upozornění"
		Aby bylo možné použít typ zpětné vazby Hiperface DSL, uživatel musí propojit piny 5-7 a 6-8 konektoru FB2 nebo naletovat odpovídající propojky (rezistory) na řídicí desku TGZcontrol.
		Toto platí pro dodávky po 06-2024, kde není provedeno žádné interní spojení.
		Ověřte také, zda máte v zařízení nahrán správný firmware podporující zvolený typ zpětné vazby.

	!!! note "Poznámka"
	
		Servozesilovač TGZ-S-400 je jednoosý. Konektor X6 se běžně nezapojuje.
	
-   **X3.1 - Motorový konektor**

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

[^1]: Při krimpování a zapojování konektorů systému Molex Clik-Mate postupujte dle [Aplikačního návodu Molex Clik-Mate](https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationspecificationspdf/503/503149/AS-503149-001-001.pdf)
