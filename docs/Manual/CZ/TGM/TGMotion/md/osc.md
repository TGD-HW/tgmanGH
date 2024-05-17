##Popis funkce struktury Oscilloscope

Oscilloscope je sofistikovaný nástroj pro záznam až 32 kanálů - hodnot až 32 různých registrů v závislosti na čase.
V určitém časovém intervalu detekuje a ukládá do sdílené paměti `TGM_Oscilloscope` hodnoty zvolených registrů.
S daty pak lze pracovat v jiných částech PLC nebo ve Windows aplikacích.
Sdílená paměť `TGM_Oscilloscope` má zpravidla velikost 1 048 576 bytů. 
Skutečnou velikost je nutno zjistit z hodnoty registru `TGM_System.HEADER.Mem_Size_OSC`.
Paměť `TGM_Oscilloscope` je společná pro data všech zaznamenávaných kanálů.
Při záznamu hodnot jednoho kanálu je jemu vyhrazena celá paměť, při záznamu dat více kanálů je paměť rovnoměrně rozdělena mezi jednotlivé kanály.
Rozložení zaznamenávaných dat v paměti `TGM_Oscilloscope` a jejich offsety určuje TG Motion; tyto parametry uloží do příslušných registrů.

!!! info "Poznámka"
	Rovnoměrnost rozdělení paměti TGM_Oscilloscope je vztažena k počtu bytů potřebných k záznamu hodnot jednotlivých registrů.
	Např. při záznamu dvou registrů, jednoho typu Long Integer (4 byty) a druhého typu Double (8 bytů), rozdělí TG Motion sdílenou paměť `TGM_Oscilloscope` v poměru 1:2, aby u obou kanálů mohl být zaznamenán stejný počet vzorků.
	
!!! warning "Upozornění"
	Se zvyšujícím se počtem zaznamenávaných kanálů klesá čas záznamu
	
Na úrovni TG Motion se načtení a záznam dat utilitou **Oscilloscope** do sdílené paměti `TGM_Oscilloscope` provádí po vykonání *Program_04*.
Tím je zaručena časová synchronizace zaznamenaných hodnot.
Načtení a záznam však nemusí proběhnout každý Cycle_Time; počet Cycle_Time, během nichž dojde k jednomu záznamu, určuje registr `Number_Periods`.

<img src="../../img/OscPeriods.png" alt="Vliv registru Number_Periods na četnost záznamů Oscilloscope"  style="width:60%;">

!!! info "Poznámka"
	Na úrovni Windows nabízí Control Observer utilitu **Oscilloscope**, v níž lze zaznamenaná data zobrazit formou grafu, uložit do souboru, zpětně načíst, měnit parametry záznamu i zobrazování, případně provádět vlastní záznam.
	
!!! warning "Upozornění"
	Oscilloscope funguje jako jedna instance, která může být využívána z PLC i Control Observeru.
	Nelze ji však používat současně z PLC, Control Observeru, případně z jiných aplikací.
	
<img src="../../img/OscScreenshot.png" alt="Utilita Oscilloscope obsažená v Control Observeru"  style="width:60%;">

!!! note "Poznámka"
	Podrobný popis utility Oscilloscope Control Observeru se nachází v kapitole Control Observer.
	
##Registry Oscilloscope a jejich význam

Registry, kterými se utilita Oscilloscope řídí, nebo kam ukládá svá nastavení, se nacházejí ve sdílené paměti `TGM_System` od offsetu `4736`.
Pro přehlednost je lze rozdělit do tří skupin:

-	**obecné registry** – týkají se nastavení utility Oscilloscope jako celku
-	**registry kanálů** – platí pouze pro konkrétní kanály
-	**pomocné registry** – obsahují informace o záznamu

###Obecné registry Oscilloscope
Obecné registry slouží k celkovému nastavení a ovládání utility **Oscilloscope**.   

| Parametr            | Popis                                                                                    |
|---------------------|-------------------------------------------------------------------------------------------------|
| Control             | Slouží k ovládání struktury Oscilloscope.                                                       |
|                     | - 0: Neprobíhá záznam nebo slouží k zastavení záznamu.                                          |
|                     | - >0: Aktivace záznamu; spouští záznam nebo čekání na Trigger (podle registru Status).          |
| Status              | Zobrazuje stav struktury Oscilloscope.                                                           |
|                     | - 0: Neprobíhá záznam ani čekání na Trigger.                                                    |
|                     | - 1: Probíhá záznam.                                                                           |
|                     | - 2: Čekání na Trigger.                                                                        |
| Number_Periods      | Počet servotiků na jeden vzorek. Určuje počet Cycle_Time, za něž se provede jeden záznam dat Oscilloscope. |
| Number_Channels     | Počet zaznamenávaných nebo zaznamenaných kanálů.                                                |
| Memory_Type_Trigger | Typ sdílené paměti, v níž se nachází triggerovací registr.                                       |
|                     | - 0: TGM_System                                                                                |
|                     | - 1: TGM_Data                                                                                  |
|                     | - 2: TGM_Cam_Profile                                                                           |
|                     | - 3: TGM_Oscilloscope                                                                          |
|                     | - 4: TGM_Servo                                                                                 |
|                     | - 5: TGM_Dio                                                                                   |
|                     | - 6: TGM_Interpolator                                                                          |
|                     | - 7: InterpolatorWriteMemory                                                                   |
|                     | - 8: InterpolatorReadMemory                                                                    |
|                     | - 9: TGM_ODS                                                                                   |
|                     | - 10: TGM_CNCEX                                                                                |
|                     | - 11: TGM_GCODE                                                                                |
| Offset_Trigger      | Offset triggerovacího registru v paměti dané registrem Memory_Type_Trigger.                      |
| Mode_Trigger        | Mód triggerovacího algoritmu.                                                                  |
|                     | - 0: Triggerování neaktivní.                                                                   |
|                     | - 1: Triggerování na náběžnou hranu.                                                           |
|                     | - 2: Triggerování na sestupnou hranu.                                                          |
| Type_Trigger        | Datový typ triggerovacího registru.                                                             |
| Level_Trigger       | Hodnota triggerovacího registru, při níž se spustí záznam.                                      |

!!! note "Poznámka"
	Triggerovacím registrem může být jakýkoli registr sdílených pamětí.
	
!!! warning "Upozornění"
	Přesto, že načtené hodnoty triggerovacího registru nemusejí být spojité, triggerovací algoritmus spojitost předpokládá.
	Např. při `Level_Trigger = 20`, `Mode_Trigger = 1` a načtených po sobě jdoucích hodnotách triggerovacího registru 17 a 22 se předpokládá, že hodnoty 20 již bylo dosaženo a záznam Oscilloscope se spustí.
	
###Princip fungování utility Oscilloscope

Je-li Mode_Trigger = 0, pak při nastavení registru Control > 0 spustí utilita Oscilloscope záznam dat.
Záznam lze ukončit nastavením registru Control = 0.
Je-li Mode_Trigger > 0, pak při nastavení registru Control > 0 aktivuje utilita Oscilloscope triggerovací algoritmus, který každý Cycle_Time testuje a vyhodnocuje hodnoty triggerovacího registru.
Při splnění triggerovací podmínky se spustí záznam dat.
Záznam Oscilloscope lze ukončit nastavením registru Control = 0.

!!! info "Poznámka"
	Jestliže během záznamu Oscilloscope dojde k zaplnění vyhrazené paměti TGM_Oscilloscope, dojde automaticky k zastavení záznamu a registry Control a Status jsou nastaveny na hodnotu 0.
	
!!! info "Poznámka"
	Kompletní výčet všech registrů Oscilloscope včetně popisu viz. Apendix.
	
###Registry kanálů

Tyto registry určují parametry týkající se jednotlivých kanálů.
Jedná se o umístění zaznamenaných dat v paměti `TGM_Oscilloscope`, určení zdroje dat (typ paměti a offset) a datový typ zaznamenávaného registru.
Každému kanálu náleží následující čtveřice registrů.

| Paramet r           | Popis                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| Offset              | Offset zaznamenávaných dat kanálu v paměti TGM_Oscilloscope (přidělený systémem TG Motion).      |
| Memory_Type_Value   | Typ sdílené paměti, v níž se nachází zaznamenávaný registr.                                      |
|                     | - 0: TGM_System                                                                                |
|                     | - 1: TGM_Data                                                                                  |
|                     | - 2: TGM_Cam_Profile                                                                           |
|                     | - 3: TGM_Oscilloscope                                                                          |
|                     | - 4: TGM_Servo                                                                                 |
|                     | - 5: TGM_Dio                                                                                   |
|                     | - 6: TGM_Interpolator                                                                          |
|                     | - 7: InterpolatorWriteMemory                                                                   |
|                     | - 8: InterpolatorReadMemory                                                                    |
|                     | - 9: TGM_ODS                                                                                   |
|                     | - 10: TGM_CNCEX                                                                                |
|                     | - 11: TGM_GCODE                                                                                |
| Offset_Value        | Offset zaznamenávaného registru v paměti dané hodnotou Memory_Type_Value.                        |
| Type_Value          | Datový typ zaznamenávaného registru.                                                            |
|                     | - 0–3: Integer 32 bitů                                                                         |
|                     | - 4–7: Integer 64 bitů                                                                         |
|                     | - 8: Double (číslo v plovoucí řádové čárce o velikosti 64 bitů)                                  |
|                     | - 9: Float (číslo v plovoucí řádové čárce o velikosti 32 bitů)                                   |

###Pomocné registry

Pomocné registry informují o parametrech záznamu utility Oscilloscope.
-	**Number_Samples** – počet vzorků k dispozici
-	**Actual_Samples** – aktuální počet zaznamenaných vzorků
-	**Sample_Time** - časový interval vzorkování `(Sample_Time = Cycle_Time × Number_Periods) [μs]`

!!! note "Poznámka"
	Registr Actual_Samples se při probíhajícím záznamu s každým vzorkem zvyšuje o 1.
	Při zastavení vzorkování (např. při nastavení registru `Control = 0`) označuje hodnota registru `Actual_Samples` poslední provedený vzorek.
	
##Přehled a popis registrů Oscilloscope

**Obecné registry Oscilloscope**
<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;název&quot;}"><b>název</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;přístup&quot;}"><b>přístup</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;popis&quot;}"><b>popis</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Control&quot;}">Control</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4736" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4736}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4736</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;slouží k ovládání struktury Oscilloscope&yen;u000a0 – neprobíhá záznam nebo zastavení záznamu&yen;u000a>0 – aktivace záznamu Oscilloscope (spouští záznam nebo čekání na Trigger)&quot;}">slouží k ovládání struktury Oscilloscope<br>0 – neprobíhá záznam nebo zastavení záznamu<br>&gt;0 – aktivace záznamu Oscilloscope (spouští záznam nebo čekání na Trigger)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status&quot;}">Status</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="4740" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4740}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4740</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;stav struktury Oscilloscope 0 – neprobíhá záznam&yen;u000a1 – záznam&yen;u000a2 – čekání na trigger&quot;}">stav struktury Oscilloscope 0 – neprobíhá záznam<br>1 – záznam<br>2 – čekání na trigger</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number_Periods&quot;}">Number_Periods</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4744" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4744}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4744</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;počet servotiků na jeden vzorek. Určuje počet Cycle_Time, za něž se provede jeden záznam&yen;u000adat Oscilloscope&quot;}">počet servotiků na jeden vzorek. Určuje počet Cycle_Time, za něž se provede jeden záznam<br>dat Oscilloscope</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number_Channels&quot;}">Number_Channels</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4748" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4748}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4748</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;počet zaznamenávaných kanálů&quot;}">počet zaznamenávaných kanálů</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Memory_Type_Trigger&quot;}">Memory_Type_Trigger</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4752" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4752}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4752</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;typ sdílené paměti, v níž se nachází triggerovací registr&quot;}">typ sdílené paměti, v níž se nachází triggerovací registr</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Offset_Trigger&quot;}">Offset_Trigger</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4756" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4756}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4756</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset triggerovacího registru v paměti dané registrem Memory_Type_Trigger&quot;}">offset triggerovacího registru v paměti dané registrem Memory_Type_Trigger</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Mode_Trigger&quot;}">Mode_Trigger</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4760" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4760}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4760</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mód triggerovacího algoritmu 0 – triggerování neaktivní&yen;u000a1 – náběžná hrana 2 – sestupná hrana&quot;}">mód triggerovacího algoritmu 0 – triggerování neaktivní<br>1 – náběžná hrana 2 – sestupná hrana</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Type_Trigger&quot;}">Type_Trigger</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4764" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4764}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4764</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;datový typ proměné triggerovacího registru&quot;}">datový typ proměné triggerovacího registru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Level_Trigger&quot;}">Level_Trigger</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4768" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4768}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4768</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;hodnota triggerovacího registru, při níž se spustí záznam&quot;}">hodnota triggerovacího registru, při níž se spustí záznam</td>
	</tr>
</table>

**registry kanálu OSC -> CHANNEL_00**

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;název&quot;}"><b>název</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;přístup&quot;}"><b>přístup</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;popis&quot;}"><b>popis</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Offset&quot;}">Offset</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="4776" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4776}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4776</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset zaznamenávaných dat kanálu v paměti TGM_Oscilloscope&quot;}">offset zaznamenávaných dat kanálu v paměti TGM_Oscilloscope</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Memory_Type_Value&quot;}">Memory_Type_Value</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4780" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4780}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4780</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;typ sdílené paměti, v níž se nachází zaznamenávaný registr 0 – TGM_System&yen;u000a1 – TGM_Data&yen;u000a2 – TGM_Cam_Profile&yen;u000a3 – TGM_Oscilloscope&yen;u000a4 – TGM_Servo&yen;u000a5 – TGM_Dio&yen;u000a6 – TGM_Interpolator&yen;u000a7 – InterpolatorWriteMemory&yen;u000a8 – InterpolatorReadMemory&yen;u000a9 – TGM_ODS&yen;u000a10 – TGM_CNCEX&yen;u000a11 – TGM_GCODE&quot;}">typ sdílené paměti, v níž se nachází zaznamenávaný registr 0 – TGM_System<br>1 – TGM_Data<br>2 – TGM_Cam_Profile<br>3 – TGM_Oscilloscope<br>4 – TGM_Servo<br>5 – TGM_Dio<br>6 – TGM_Interpolator<br>7 – InterpolatorWriteMemory<br>8 – InterpolatorReadMemory<br>9 – TGM_ODS<br>10 – TGM_CNCEX<br>11 – TGM_GCODE</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Offset_Value&quot;}">Offset_Value</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4784" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4784}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4784</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset zaznamenávaného registru v paměti dané hodnotou Memory_Type_Value&quot;}">offset zaznamenávaného registru v paměti dané hodnotou Memory_Type_Value</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Type_Value&quot;}">Type_Value</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4788" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4788}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4788</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;datový typ zaznamenávaného registru 0–3 – integer 32 bitů&yen;u000a4–7 – integer 64 bitů&yen;u000a8 – double (číslo v plovoucí řádové čárce o velikosti 64 bitů) 9 – float (číslo v plovoucí řádové čárce o velikosti 32 bitů)&quot;}">datový typ zaznamenávaného registru 0–3 – integer 32 bitů<br>4–7 – integer 64 bitů<br>8 – double (číslo v plovoucí řádové čárce o velikosti 64 bitů) 9 – float (číslo v plovoucí řádové čárce o velikosti 32 bitů)</td>
	</tr>
</table>

**registry ostatních kanálů OSC -> CHANNEL_01 - CHANNEL_31**

<table>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;název&quot;}"><b>název</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;popis&quot;}"><b>popis</b></td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;CHANNEL_01&quot;}">CHANNEL_01</td>
		<td sdval="4792" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4792}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4792</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;registry náležející kanálu 01&quot;}">registry náležející kanálu 01</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;CHANNEL_02&quot;}">CHANNEL_02</td>
		<td sdval="4808" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4808}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4808</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;registry náležející kanálu 02&quot;}">registry náležející kanálu 02</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;׀&quot;}">׀</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;׀&quot;}">׀</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;׀&quot;}">׀</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;CHANNEL_31&quot;}">CHANNEL_31</td>
		<td sdval="5272" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5272}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5272</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;registry náležející kanálu 31&quot;}">registry náležející kanálu 31</td>
	</tr>
</table>

**pomocné registry**

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;název&quot;}"><b>název</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;přístup&quot;}"><b>přístup</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;popis&quot;}"><b>popis</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number_Samples&quot;}">Number_Samples</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="5288" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5288}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5288</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;počet vzorků k dispozici&quot;}">počet vzorků k dispozici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual_Samples&quot;}">Actual_Samples</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="5292" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5292}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5292</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální počet zaznamenaných vzorků&quot;}">aktuální počet zaznamenaných vzorků</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Sample_Time&quot;}">Sample_Time</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="5296" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5296}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5296</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;časový interval vzorkování (Sample_Time = Cycle_Time × Number_Periods) [μs]&quot;}">časový interval vzorkování (Sample_Time = Cycle_Time × Number_Periods) [μs]</td>
	</tr>
</table>
