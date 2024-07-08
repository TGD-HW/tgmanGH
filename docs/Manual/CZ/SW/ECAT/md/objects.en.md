Ke všem prvkům ve slovníku objektů lze přistupovat buď pomocí EtherCATu, nebo pomocí CANu.

##Komunikační objekty CANopen

Podporovány jsou následující standardní objekty.
Některé objekty jsou společné pro komunikaci CAN a EtherCAT, jiné se používají pouze při komunikaci CAN nebo EtherCAT (CoE).

| Index  | Název                                  | Oprávnění | Používá se v | Mapování CAN PDO |
|--------|----------------------------------------|------------|--------------|------------------|
| 0x1000 | typ zařízení                           | ro         | CoE/CAN      | Ne               |
| 0x1001 | registr chyb                           | ro         | CoE/CAN      | TPDO             |
| 0x1003 | předdefinované chybové pole            | ro         | CoE/CAN      | Ne               |
| 0x1010 | ukládat parametry                      | rw         | CoE/CAN      | Ne               |
| 0x1011 | obnovení výchozích parametrů           | rw         | CoE/CAN      | Ne               |
| 0x1018 | objekt identity                        | ro         | CoE/CAN      | Ne               |
| 0x1400 | 1. komunikační parametr RPDO           | rw         | CAN          | Ne               |
| 0x1401 | 2. komunikační parametr RPDO           | rw         | CAN          | Ne               |
| 0x1402 | 3. komunikační parametr RPDO           | rw         | CAN          | Ne               |
| 0x1403 | 4. komunikační parametr RPDO           | rw         | CAN          | Ne               |
| 0x1600 | 1. parametr mapování RPDO              | rw         | CAN          | Ne               |
| 0x1601 | 2. parametr mapování RPDO              | rw         | CAN          | Ne               |
| 0x1602 | 3. parametr mapování RPDO              | rw         | CAN          | Ne               |
| 0x1603 | 4. parametr mapování RPDO              | rw         | CAN          | Ne               |
| 0x1800 | 1. komunikační parametr TPDO           | rw         | CAN          | Ne               |
| 0x1801 | 2. komunikační parametr TPDO           | rw         | CAN          | Ne               |
| 0x1802 | 3. komunikační parametr TPDO           | rw         | CAN          | Ne               |
| 0x1803 | 4. komunikační parametr TPDO           | rw         | CAN          | Ne               |
| 0x1A00 | 1. parametr mapování TPDO              | rw         | CAN          | Ne               |
| 0x1A01 | 2. parametr mapování TPDO              | rw         | CAN          | Ne               |
| 0x1A02 | 3. parametr mapování TPDO              | rw         | CAN          | Ne               |
| 0x1A03 | 4. parametr mapování TPDO              | rw         | CAN          | Ne               |
| 0x1C12 | Přiřazení správce synchronizace 2      | rw         | CoE          | Ne               |
| 0x1C13 | Přiřazení správce synchronizace 3      | rw         | CoE          | Ne               |
| 0x1C32 | Synchronizace Správce synchronizace 2  | rw         | CoE          | Ne               |
| 0x1C33 | Správce synchronizace 3 synchronizace  | rw         | CoE          | Ne               |

##Specifické objekty TGZ
Kromě registrů TGZ (indexy `0x2000` - `0x3FF`) jsou definovány speciální objekty pro snadný přístup k nativním registrům TGZ.

###Digitální vstupy `0x4000`
Tento objekt je definován jako hodnota `UNSIGNED8` a obsahuje všechny digitální vstupy servopohonu TGZ.
Slouží ke snadnému mapování TPDO v síti CAN.
Objekt lze mapovat pouze pro CAN TPDO.

###Digitální výstupy `0x4001`
Podobně jsou digitální výstupy jako `UNSIGNED8` (používá se pouze prvních 6 bitů) také přímo namapovány na tento objekt pro snadné mapování RPDO.
Objekt lze mapovat pro CAN RPDO.

###Analogové vstupy `0x4002`
Podindex 0 je konstantní a je roven dvěma - k dispozici jsou dva analogové vstupy.
Podindexy 1 a 2 obsahují hodnotu analogového vstupu typu `UNSIGNED16` pouze pro čtení.
Tyto objekty jsou kopií nativních registrů TGZ `0x3328` a `0x3428`, zmenšené na hodnotu `UNSIGNED16`.
Lze je snadno namapovat na CAN TPDO, čímž se ušetří délka PDO.

###Stav pohonu `0x4003`
Podindex 0 je konstantní a je roven dvěma - řídí hodnotu stavu dvou os.
Podindexy 1 a 2 obsahují stav jednotky pouze pro čtení - dolních 16 bitů nativních registrů TGZ `0x3325` a `0x3425`.
Lze je snadno namapovat na CAN TPDO, čímž se ušetří délka PDO.

##Objekty profilu zařízení (DSP402)
Podporovány jsou následující standardní objekty DSP402.
První osa používá objekty v rozsahu `0x6000` - `0x67FF`, druhá osa přidává k indexům objektů offset `0x800`, tj. rozsah je `0x6800` - `0x6FFF`.
Například řídicí slovo pro první osu se nachází na indexu `0x6040`, zatímco druhá osa používá řídicí slovo na indexu `0x6840`.
Popis objektů naleznete v dokumentaci k DSP402.
Některé objekty jsou popsány pod tabulkou.
Ke všem objektům DSP402 lze přistupovat jak z CAN, tak z EtherCAT (CoE).
Varianta TGZ-S servo umožňuje přístup k objektům `0x6800` - `0x6FFF`, ale hodnoty jsou ignorovány.

| 1. osa | 2. osa | Název                          | Mapování CAN PDO     |
|---------|---------|--------------------------------|----------------------|
| 0x6040  | 0x6840  | kontrolní slovo                | RPDO                 |
| 0x6041  | 0x6841  | stavové slovo                  | TPDO                 |
| 0x6060  | 0x6860  | provozní režimy                | RPDO                 |
| 0x6061  | 0x6861  | zobrazení provozních režimů    | TPDO                 |
| 0x6064  | 0x6864  | skutečná hodnota polohy        | TPDO                 |
| 0x6065  | 0x6865  | následující chybové okno       | RPDO                 |
| 0x6066  | 0x6866  | následující chybový time out   | RPDO                 |
| 0x606B  | 0x686B  | požadovaná rychlost            | TPDO                 |
| 0x606C  | 0x686C  | skutečná rychlost              | TPDO                 |
| 0x6071  | 0x6871  | požadovaný točivý moment       | RPDO                 |
| 0x6077  | 0x6877  | skutečný točivého moment       | TPDO             |
| 0x607A  | 0x687A  | cílová poloha                  | RPDO                 |
| 0x607C  | 0x687C  | offset nulové polohy           | RPDO                 |
| 0x607D  | 0x687D  | softwarové limity polohy       | RPDO (sub1, sub2)    |
| 0x6081  | 0x6881  | profil rychlosti               | RPDO                 |
| 0x6083  | 0x6883  | profil akcelerace              | RPDO                 |
| 0x6084  | 0x6884  | profil decelarace              | RPDO                 |
| 0x6085  | 0x6885  | rychlé zastavení               | RPDO                |
| 0x6086  | 0x6886  | typ pohybu                     | RPDO                 |
| 0x608F  | 0x688F  | rozlišení snímače polohy       | RPDO (sub1, sub2)    |
| 0x6094  | 0x6894  | rozlišení snímače rychlosti    | RPDO (sub1, sub2)    |
| 0x6098  | 0x6898  | metoda přejezdu do výchozí polohy               | RPDO                 |
| 0x6099  | 0x6899  | rychlost přejezdu do výchozí polohy              | RPDO (sub1, sub2)    |
| 0x609A  | 0x689A  | zrychlení přejezdu do výchozí polohy             | RPDO                 |
| 0x60B2  | 0x68B2  | offset točivého momentu      | RPDO                 |
| 0x60C1  | 0x68C1  | interpolace hledané polohy     | RPDO (sub1)          |
| 0x60C2  | 0x68C2  | interpolace časové periody      | RPDO (sub1, sub2)    |
| 0x60D9  | 0x68D9  | podporované synchronizační funkce | Ne                |
| 0x60E3  | 0x68E3  | podporované metody přejezdu do výchozí polohy    | Ne                   |
| 0x60F4  | 0x68F4  | skutečná hodnota následující chyby  | TPDO             |
| 0x60FD  | 0x68FD  | digitální vstupy               | TPDO                 |
| 0x60FE  | 0x68FE  | digitální výstupy              | RPDO                 |
| 0x60FF  | 0x68FF  | požadovaná rychlost                | RPDO                 |
| 0x6502  | 0x6D02  | podporované režimy pohonu      | Ne                   |

###Režimy provozu `0x6060` {#0x6060}
Servopohon TGZ podporuje následující provozní režimy:

| Hodnota | Popis                                           | Požadovaný režim TGZ (D-Mode) |
|---------|-------------------------------------------------|-------------------------------|
| 1       | Polohový režim (PP)                       | 7: Polohový režim PG            |
| 3       | Rychlostní režim (PV)                  | 6: Rychlostní režim PG             |
| 4       | Proudový (torque) režim (PT)             | 1: Proudový režim            |
| 6       | Režim navádění do výchozí polohy                                  | 7: Polohový režim PG            |
| 7       | Režim interpolované polohy (IP)                 | 3: Polohový režim               |
| 8       | Cyklický synchronní polohový režim (CSP)        | 3: Polohový režim               |
| 9       | Režim cyklické synchronní rychlosti (CSV)       | 2: Rychlostní režim          |
| 10      | Režim cyklického synchronního momentu (CST)     | 1: Proudový režim             |

!!! warning "Důležité upozornění"
	Objekt `0x6060` (`0x6860`) NEMĚNÍ režim pohonu TGZ.
	Registr `D-Mode` musí být nastaven na správnou hodnotu buď servisním programem TGZ_GUI a uložen do servozesilovače, nebo musí být nastaven samostatně objektem SDO `0x2303` (první osa) nebo `0x2403` (druhá osa) masterem při spuštění.
	Pokud provozní režim DSP402 neodpovídá příslušné hodnotě `D-Mode` (podle výše uvedené tabulky), bude servozesilovač TGZ příkazy nadřazené sítě EtherCAT/CANopen ignorovat.
	Tato funkce umožňuje virtuálně "odpojit" servozesilovač od nadřazeného systému a provádět testy nebo jog přímo z programu TGZ_GUI pouhým nastavením hodnoty `D-Mode` na jinou (servisem potřebnou) hodnotu.
	
!!! note "Poznámka"
	Proudový režim (PT) a režim cyklického synchronního momentu (CST) je v implementaci TGZ funkčně totožný.
	Rovněž režim interpolované polohy (IP) a režim cyklické synchronní polohy (CSP) se chovají identicky.
	Režim IR používá objekt `0x60C1sub1`, který je interně mapován na cílovou polohu `0x607A`.
	
!!! note "Poznámka"
	Provozní režim (spolu s režimem D) lze kdykoli změnit, ale doporučuje se, aby byl pohon v klidovém stavu.
	V opačném případě může dojít k chybě polohy.
	
###Požadovaný točivý moment `0x6071`
Objekt požadovaného momentu se používá především v režimech momentu PT nebo CST jako požadovaná hodnota.
Jeho rozsah je `-32767 - 32767` a je vyjádřen jako normalizovaná hodnota `M-Ipeak` motoru, kde `-32767 je -100 %, 0 je 0 % a 32767 je 100 % M-Ipeak` proudu.
Lze ji použít také v režimech cyklického polohování IP a CSP jako hodnotu posuvného momentu.
Poté se tato hodnota přičte k požadované hodnotě do regulátoru proudu.

###Žádaná poloha `0x607A`
Je to poloha, do které se má pohon přesunout v režimu PP, IP nebo CSP.
Hodnota se násobí poměrem daným objektem *Rozlišení snímače polohy* (`0x608F`).
Poté se použije jako vstupní hodnota profil generátor TGZ (režim PP) nebo přímo jako požadovaná 64bitová poloha v přírůstcích (IP nebo CSP).

$$
DesiredTGZposition=TargetPosition607A \times \frac{PositionEncoderNumerator608F_1}{PositionEncoderDivisor608F_2}
$$

Výchozí hodnota čitatele zlomku je 4096 a jmenovatele je 1.

###Profil rychlosti `0x6081`
Konečná požadovaná rychlost TGZ pro režim PP, PV nebo CSV se vypočítá z objektu *Profile velocity* podle rovnice

$$
DesiredTGZvelocity=ProfileVelocity6081 \times \frac{VelocityEncoderNumerator6094_1}{VelocityEncoderDivisor6094_2}
$$

Výchozí hodnota čitatele i jmenovatele zlomku je 1.

###Typ profilu pohybu `0x6086`
Podporované typy profilů pro režim PP jsou následující.

| Hodnota | Režim                                             |
|---------|---------------------------------------------------|
|-3       | Sinusový (režim TGZ PG 2)                         |
|-2       | Rychlé zrychlení, rychlé zpomalení (režim TGZ PG 1) |
|-1       | Rychlé zrychlení, pomalé zpomalení (režim TGZ PG 0) |
| 0       | Trapézový (režim TGZ 3)                           |
| 1       | sin2 (režim TGZ 4)                                |

###Metoda přejezdu do výchozí polohy `0x6098`
Režim přejezdu do výchozí polohy se aktivuje nastavením hodnoty objektu `0x6060` na hodnotu 6.
Samotný postup navádění je pak řízen řídicím slovem `0x6040`.
Další informace naleznete v dokumentaci k DSP402.
Objekt `0x60E3` je implementován a vrací počet podporovaných režimů polohování (subindex 0) spolu s jejich hodnotami (subindexy 1 - 10).   

K dispozici jsou následující standardní režimy polohování DSP402:

| Režim | Popis                                                                                                                                                                                             |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1       | Najetí na záporný koncový spínač a indexový impulz. Počáteční pohyb je doleva, dokud není aktivní záporný koncový spínač. Pohyb pokračuje doprava při prvním indexovém impulsu, kdy se záporný koncový spínač stane neaktivním. Registr `Homing_NegLimSwitchMask` určuje záporný koncový spínač. |
| 2       | Navádění na kladný koncový spínač a indexový impulz. Podobně jako v režimu 1, ale pohyby probíhají v opačných směrech a parametr `Homing_PosLimSwitchMask` slouží k určení kladného koncového spínače. |
| 3       | Navádění na kladný domovský spínač a indexový impulz. Stejné jako režim 2, ale domovský spínač je definován pomocí `Homing_ReferenceSwitchMask`. Počáteční směr pohybu závisí na stavu domovského spínače. |
| 5       | Navádění na záporný domovský spínač a indexový impulz. Podobně jako režim 3, ale pohyby jsou obrácené.                                                                                                                                   |
| 17      | Najetí na záporný koncový spínač. Podobně jako v režimu 1, ale poloha navádění není závislá na indexovém impulsu, ale pouze na přechodu koncového spínače.                                        |
| 18      | Najetí na kladný koncový spínač. Podobně jako režim 2, bez vyhledávání indexových impulzů.                                                                                                        |
| 19      | Navádění na pozitivní domovský spínač. Stejně jako režim 3 bez indexového impulzu.                                                                                                                |
| 21      | Najetí na záporný koncový spínač. Rovná se režimu 5 bez vyhledávání indexových impulzů.                                                                                                           |
| 35      | Nastavit nulu v aktuální poloze. Používá skutečnou polohu jako referenční bod výchozího bodu. Tato metoda je pro CoE zastaralá.                                                                 |
| 37      | Nastavit nulu v aktuální poloze. Používá skutečnou polohu jako referenční bod výchozího bodu. Tento režim je pro CoE doporučen.                                                           |

###Digitální vstupy `0x60FD`
Podle standardu DSP402 jsou všechny digitální vstupy namapovány na horních 16 bitů hodnoty `UNSIGNED32` (servopohon TGZ má 8 digitálních vstupů, takže digitálním vstupům odpovídají pouze bity 16 - 23).
Dolních 16 bitů je nastaveno na nulu.
Tento objekt existuje také pro druhou osu jako `0x68FD`, ale je namapován na stejné vstupy, takže oba objekty vracejí stejnou hodnotu.
Pro snadnější přístup k digitálním vstupům lze použít také objekt `0x4000`.

###Digitální výstupy 0x60FE<sub>1</sub> a maska 0x60FE<sub>2</sub>
Vyšších 16 bitů hodnoty `UNSIGNED32` se používá jako digitální výstupy (servopohon TGZ má 6 digitálních výstupů, na výstupní piny jsou připojeny pouze bity 16 - 21).
Nižších 16 bitů se ignoruje.
To platí i pro masku digitálního výstupu.
Tyto objekty existují také pro druhou osu jako 0x68FE<sub>1</sub> a 0x68FE<sub>2</sub>, ale jsou namapovány na stejné digitální výstupy.
Změna objektu jedné osy změní i objekt druhé osy.
Pro snadnější přístup k digitálním výstupům lze použít objekt `0x4001`.

##Chybové kódy
Pro zjištění možných chyb se používají dva standardní objekty:
- Registr chyb `0x1001`
- Předdefinované chybové pole `0x1003`

###Registr chyb `0x1001`

| Bit | Význam            | Chybovýbit TGZ            | Hodnotachybového bitu TGZ        |
|-----|-------------------|---------------------------|----------------------------------|
| 0   | Obecná chyba.     | Jakýkoli aktivní bit      |                                  |
| 1   | Aktuální          | 8 nebo 19 nebo 21        | 0x100 nebo 0x80000 nebo 0x200000 |
| 2   | Napětí            | 3 nebo 4                 | 0x8 nebo 0x10                    |
| 3   | Teplota           | 9 nebo 11                | 0x200 nebo 0x800                 |
| 4   | Komunikace        | 12 nebo 17               | 0x1000 nebo 0x20000              |
| 5   | Nepoužívá se      |                           |                                  |
| 6   | Rezervováno       |                           |                                  |
| 7   | Osa               | Nastavení pro druhou osu |                                  |

Bity v registru chyb jsou *ORovány* pro obě osy, takže poskytují pouze obecný přehled o typu chyby a příslušné ose.

###Předdefinované chybové pole `0x1003`
Podindex 0 obsahuje počet skutečných chyb v poli.
Maximální počet je 64.
Chyby jsou ukládány v pořadí first-in last-out, tj. nová chyba je uložena na subindex 1 a ostatní chyby jsou posunuty dolů.   

Zápisem nuly do dílčího indexu 0 se vymaže celá historie chyb.   

Každý chybový bit z registru chyb TGZ generuje jeden záznam v historii chyb.
Čísla chyb jsou 32bitové bezznaménkové hodnoty složené z 16bitového standardního kódu chyby DSP402 (viz tabulka níže),
identifikátoru osy v bitu 16 (0: první osa, 1: druhá osa) a původní hodnoty bitového čísla chyby TGZ v bitech 24 - 29 (obsahují tedy hodnoty 0 - 31).

| 31 30 | 29 24                       | 23 17 | 16  | 15 0                  |
|-------|-----------------------------|-------|-----|-----------------------|
| 0     | číslo chyby TGZ | 0     | osa | Chybový kód DSP402   |

| Chybový kód DSP402 | Symbolický název      | Chybový bit TGZ |
|-------------------|----------------------|----------------|
| 0x3130            | MAINS_PHASE          | 0              |
| 0x3100            | MAINS_SUPPLY         | 1              |
| 0x8A00            | INTERNAL_ERROR       | 2              |
| 0x3110            | OVER_VOLTAGE         | 3              |
| 0x3120            | UNDER_VOLTAGE        | 4              |
| 0x5430            | STO                  | 5              |
| 0x7110            | HOLDING_BRAKE        | 6              |
| 0x7111            | HOLDING_BRAKE_SWITCH | 7              |
| 0x2300            | CURRENT_MEASUREMENT  | 8              |
| 0x4310            | MOTOR_THERMOSTAT     | 9              |
| 0x4110            | AMBIENT_TEMPERATURE  | 10             |
| 0x4210            | HEAT_SINK_TEMPERATURE| 11             |
| 0x7303            | ZPĚTNÁ VAZBA         | 12             |
| 0x7122            | KOMUNIKACE           | 13             |
| 0x8400            | OVER_SPEED           | 14             |
| 0x8612            | CONTOURING           | 15             |
| 0x8611            | TRAJEKTORIE          | 16             |
| 0x8100            | HOST_COMMUNICATION   | 17             |
| 0x8600            | DRIVE_RAMP_E2        | 18             |
| 0x2200            | CURRENT_REGULATION   | 19             |
| 0xF001            | EMERGENCY_STOP       | 20             |
| 0x5110            | IGBT_DRIVER_VOLTAGE  | 21             |
| 0x7113            | BRAKE_RESINTANCE     | 22             |
| 0x5112            | 24V_BRAKE_SUPPLY     | 23             |
| 0x1000            | Rezervováno          | 24             |
| 0x8310            | I2T                  | 25             |
| 0x4311            | MOTOR_TEMPERATURE    | 26             |
| 0x6320            | MOTOR_PARAMETER      | 27             |
| 0x1000            | Rezervováno          | 28             |
| 0x1000            | Rezervováno          | 29             |
| 0x1000            | Rezervováno          | 30             |
| 0x1000            | Rezervováno          | 31             |

##Mapování PDO a varianty jednotky TGZ {#PDO_TGZ}
Existují dvě varianty servozesilovačů TGZ: TGZ-D je určen pro řízení dvou os, zatímco TGZ-S je varianta pro jednu osu.
Obě verze používají stejné popisné soubory XML (EtherCAT) nebo EDS (CANopen) a používají stejnou strukturu PDO a stejné objekty slovníku objektů.
Pro verzi TGZ-S objekty druhé osy sice existují, ale nemají žádný význam, tj. jejich změna nemá žádný vliv na chování.
Druhá osa ve variantě TGZ-S vždy reaguje chybou ve stavovém slově.
Tuto chybu je třeba ignorovat.

##Výchozí mapování CAN PDO
Volné mapování PDO lze použít pouze pro síť CAN.
Výchozí mapování je vybráno tak, aby byly použity nejdůležitější a nejpoužitelnější objekty.

###Výchozí mapování CAN RPDO
Výchozí mapování PDO pro příjem (směrový regulátor → TGZ):

<table>
	<tr>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Index&quot;}"><b>Index</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Sub-index&quot;}"><b>Sub-index</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Hodnota&quot;}"><b>Hodnota</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Popis&quot;}"><b>Popis</b></td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RPDO1 používá 8 bajtů (první osa)&quot;}"><b>RPDO1 používá 8 bajtů (první osa)</b></td>
	</tr>
	<tr>
		<td rowspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1600&quot;}"><b>0x1600</b></td>
		<td>0</td>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60400010&quot;}">0x60400010</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Řídicí slovo 0x6040&quot;}">Řídicí slovo 0x6040</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x607A0020&quot;}">0x607A0020</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cílová pozice 0x607A&quot;}">Cílová pozice 0x607A</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">3</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60600008&quot;}">0x60600008</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Režimy provozu 0x6060&quot;}">Režimy provozu 0x6060</td>
	</tr>
	<tr>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40010008&quot;}">0x40010008</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digitální výstupy 0x4001&quot;}">Digitální výstupy 0x4001</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RPDO2 používá 7 bajtů (druhá osa)&quot;}"><b>RPDO2 používá 7 bajtů (druhá osa)</b></td>
	</tr>
	<tr>
		<td rowspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1601&quot;}"><b>0x1601</b></td>
		<td>0</td>
		<td>3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68400010&quot;}">0x68400010</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Řídicí slovo 0x6840&quot;}">Řídicí slovo 0x6840</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x687A0020&quot;}">0x687A0020</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cílová pozice 0x687A&quot;}">Cílová pozice 0x687A</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">3</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68600008&quot;}">0x68600008</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Režimy provozu 0x6860&quot;}">Režimy provozu 0x6860</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RPDO3 používá 4 bajty (první osa)&quot;}"><b>RPDO3 používá 4 bajty (první osa)</b></td>
	</tr>
	<tr>
		<td rowspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1602&quot;}"><b>0x1602</b></td>
		<td>0</td>
		<td>1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60810020&quot;}">0x60810020</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rychlost profilu&quot;}">Rychlost profilu</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RPDO4 používá 4 bajty (druhá osa)&quot;}"><b>RPDO4 používá 4 bajty (druhá osa)</b></td>
	</tr>
	<tr>
		<td rowspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1603&quot;}"><b>0x1603</b></td>
		<td>0</td>
		<td>1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68810020&quot;}">0x68810020</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rychlost profilu&quot;}">Rychlost profilu</td>
	</tr>
</table>

###Výchozí mapování CAN TPDO

<table>
	<tr>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Index&quot;}"><b>Index</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Sub-index&quot;}"><b>Sub-index</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Hodnota&quot;}"><b>Hodnota</b></td>
		<td bgcolor="#70AD47" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Popis&quot;}"><b>Popis</b></td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO1 (první osa, 8 bajtů)&quot;}"><b>TPDO1 (první osa, 8 bajtů)</b></td>
	</tr>
	<tr>
		<td rowspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A00&quot;}"><b>0x1A00</b></td>
		<td>0</td>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60410010&quot;}">0x60410010</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stavové slovo 0x6041&quot;}">Stavové slovo 0x6041</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60640020&quot;}">0x60640020</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální hodnota polohy 0x6064&quot;}">Aktuální hodnota polohy 0x6064</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">3</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x60610008&quot;}">0x60610008</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zobrazení provozních režimů 0x6061&quot;}">Zobrazení provozních režimů 0x6061</td>
	</tr>
	<tr>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x10010008&quot;}">0x10010008</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Registr chyb 0x1001&quot;}">Registr chyb 0x1001</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO2 (druhá osa, 8 bajtů)&quot;}"><b>TPDO2 (druhá osa, 8 bajtů)</b></td>
	</tr>
	<tr>
		<td rowspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A01&quot;}"><b>0x1A01</b></td>
		<td>0</td>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68410010&quot;}">0x68410010</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stavové slovo 0x6841&quot;}">Stavové slovo 0x6841</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68640020&quot;}">0x68640020</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální hodnota polohy 0x6864&quot;}">Aktuální hodnota polohy 0x6864</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">3</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x68610008&quot;}">0x68610008</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zobrazení provozních režimů 0x6861&quot;}">Zobrazení provozních režimů 0x6861</td>
	</tr>
	<tr>
		<td>4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40000008&quot;}">0x40000008</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digitální vstupy 0x4000&quot;}">Digitální vstupy 0x4000</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO3 (první osa, 6 bajtů)&quot;}"><b>TPDO3 (první osa, 6 bajtů)</b></td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A02&quot;}"><b>0x1A02</b></td>
		<td>0</td>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x606C0020&quot;}">0x606C0020</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Skutečná rychlost 0x606C&quot;}">Skutečná rychlost 0x606C</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40020110&quot;}">0x40020110</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analogový vstup 1 0x4002sub1&quot;}">Analogový vstup 1 0x4002sub1</td>
	</tr>
	<tr>
		<td colspan="4" bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;TPDO4 (druhá osa, 6 bajtů)&quot;}"><b>TPDO4 (druhá osa, 6 bajtů)</b></td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td>0</td>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet záznamů&quot;}">Počet záznamů</td>
	</tr>
	<tr>
		<td bgcolor="#E2EFD9">1</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x686C0020&quot;}">0x686C0020</td>
		<td bgcolor="#E2EFD9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Skutečná rychlost 0x686C&quot;}">Skutečná rychlost 0x686C</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40020210&quot;}">0x40020210</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analogový vstup 2 0x4002sub2&quot;}">Analogový vstup 2 0x4002sub2</td>
	</tr>
</table>

##Mapování PDO pro CANopen over EtherCAT (CoE)
Při použití komunikace EtherCAT jsou k dispozici dvě pevná mapování PDO:

- Nativní mapování TGZ
- Mapování kompatibilní s CoE

###Nativní mapování TGZ PDO
Toto mapování PDO využívá plné 64bitové hodnoty polohy, což umožňuje řídicí jednotce EtherCAT Master řídit servopohon s plnou přesností. 
Pohon pracuje pouze v režimu cyklické synchronní polohy. Režim pohonu (`D-Mode`) musí být servisním programem TGZ_GUI nastaven na hodnotu 3 (režim polohy).
Pro výběr nativního mapování PDO musí EtherCAT master provést následující sekvenci ve stavu `PRE-OPERATIONAL` pomocí přístupu SDO:

- Nastavení objektu 0x1C12<sub>0</sub> na `0` (velikost dat `UNSIGNED8`)
- Nastavení objektu 0x1C12<sub>1</sub> na `0x1721` (velikost dat `UNSIGNED16`)
- Nastavení objektu 0x1C12<sub>0</sub> na `1`  (velikost dat `UNSIGNED8`)
- Nastavení objektu 0x1C13<sub>0</sub> na `0`  (velikost dat `UNSIGNED8`)
- Nastavení objektu 0x1C13<sub>1</sub> na `0x1B21` (velikost dat `UNSIGNED16`)
- Nastavení objektu 0x1C13<sub>0</sub> na `1` (velikost dat `UNSIGNED8`)

Alternativně lze mapovací čísla `0x1721` a `0x1B21` nastavit pomocí programu TGZ_GUI pomocí registrů `PDO_Out_Mapping_1C12_1` a `PDO_In_Mapping_1C13_1`.   

Nativní RPDO má následující strukturu (44 bajtů):

``` cpp
int64_t positionSetPoint_1;
uint32_t control_1;
int16_t currentSetPoint_1;
uint16_t currentLimit_1;
int64_t positionSetPoint_2;
uint32_t control_2;
int16_t currentSetPoint_2;
uint16_t currentLimit_2;
uint32_t Reserved_1;
uint32_t Reserved_2;
uint32_t Reserved_3;
```

Nativní TPDO má následující strukturu (44 bajtů):

``` cpp
int64_t positionActValue_1;
int64_t positionActValue_2;
uint32_t positionActValueExt;
uint32_t status_1;
uint32_t status_2;
uint16_t analogInput_1;
uint16_t analogInput_2;
int16_t currentqActValue_1;
int16_t currentqActValue_2;
uint32_t mappedParameter_1;
uint32_t mappedParameter_2;
```

Objekty PDO jsou popsány [ZDE](packet.md#ECAT_PDO).

###Mapování CoE TGZ PDO
Toto mapování používá standardní objekty CANopen.
Některé položky se používají pouze v některých provozních režimech.
Příslušný režim pohonu TGZ **NENÍ** zvolen automaticky při zápisu objektu `0x6060` (`0x6860`) pomocí SDO, musí být nastaven programem TGZ_GUI nebo SDO.
Viz také [Režimy provozu 0x6060](objects.md#0x6060).
Hodnoty polohy se přepočítávají poměrem daným objektem *Rozlišení snímače polohy* `0x608F` nebo `0x688F`.
Úplný stavový stroj DSP402 je implementován pomocí řídicího slova `0x6040` (`0x6840`) a stavového slova `0x6041` (`0x6841`).   

K dispozici jsou následující pevná vstupní mapování PDO (směrový regulátor -> TGZ):

| Režim                            | Hodnota     |
|----------------------------------|---------|
| Cyklická synchronní poloha (CSP) | 0x1701  |
| Cyklická synchronní rychlost (CSV) | 0x1702  |
| Cyklický synchronní moment (CST) | 0x1703  |

Existuje pouze jedno vysílací PDO CoE `0x1B01`, které obsahuje všechny potřebné aktuální hodnoty.   

Pro výběr mapování CoE musí master použít následující sekvenci pomocí zápisu SDO ve stavu PRE-OPERATIONAL:

- Nastavení objektu 0x1C12<sub>0</sub> na `0` (velikost dat `UNSIGNED8`)
- Nastavení objektu 0x1C12<sub>1</sub> na `0x1701` (velikost dat `UNSIGNED16`)
- Nastavení objektu 0x1C12<sub>0</sub> na `1` (velikost dat `UNSIGNED8`)
- Nastavení objektu 0x1C13<sub>0</sub> na `0` (velikost dat `UNSIGNED8`)
- Nastavení objektu 0x1C13<sub>1</sub> na `0x1B01` (velikost dat `UNSIGNED16`)
- Nastavení objektu 0x1C13<sub>0</sub> na `1` (velikost dat `UNSIGNED8`)

Alternativně lze mapovací čísla `0x1701` (`0x1702`, `0x1703`) a `0x1B01` nastavit pomocí programu TGZ_GUI pomocí registrů `PDO_Out_Mapping_1C12_1` a `PDO_In_Mapping_1C13_1`.
CoE RPDO pro režim CSP, IP nebo PP (`0x1701`) má následující strukturu (40 bajtů):

``` cpp
// První osa
int32_t position_setpoint_1; // SDO objekt 0x607A (režimy PP, IP, CSP)
uint32_t velocity_setpoint_1; // SDO objekt 0x60FF (režimy PP a PV)
uint32_t digital_outputs; // SDO objekt 0x60FE sub 1 
uint16_t control_word_1; // SDO objekt 0x6040
int16_t current_setpoint_1; // SDO objekt 0x6071 (PP, CSP, PT, CST)
uint16_t current_limit_1; // viz rovnice níže
int16_t padding_1; // nepoužívá se
// Druhá osa
int32_t position_setpoint_2; // SDO objekt 0x687A (režimy PP, IP, CSP)
uint32_t velocity_setpoint_2; // SDO objekt 0x68FF (režimy PP a PV)
uint32_t reserved_2; // nepoužívá se
uint16_t control_word_2; // SDO objekt 0x6840
int16_t current_setpoint_2; // SDO objekt 0x6871 (PP, CSP, PT, CST)
uint16_t current_limit_2; // viz rovnice níže
int16_t padding_2; // nepoužívá se
```

CoE RPDO pro režim CSV nebo PV (`0x1702`) má následující strukturu (40 bajtů):

``` cpp
// První osa
int32_t reserved_1; // nepoužívá se
uint32_t velocity_setpoint_1; // SDO objekt 0x60FF (režimy PP a PV)
uint32_t digital_outputs; // SDO objekt 0x60FE sub 1 
uint16_t control_word_1; // SDO objekt 0x6040
int16_t current_setpoint_1; // SDO objekt 0x6071 (PP, CSP, PT, CST)
uint16_t current_limit_1; // viz rovnice níže
int16_t padding_1; // nepoužívá se
// Druhá osa
int32_t reserved_2; // nepoužívá se
uint32_t velocity_setpoint_2; // SDO objekt 0x68FF (režimy PP a PV)
uint32_t reserved_3; // nepoužívá se
uint16_t control_word_2; // SDO objekt 0x6840
int16_t current_setpoint_2; // SDO objekt 0x6871 (PP, CSP, PT, CST)
uint16_t current_limit_2; // viz rovnice níže
int16_t padding_2; // nepoužívá se
```

CoE RPDO pro režim CST nebo PT (`0x1703`) má následující strukturu (40 bajtů):

``` cpp
// První osa
int32_t reserved_1; // SDO objekt 0x607A (režimy PP, IP, CSP)
uint32_t reserved_2; // SDO objekt 0x60FF (režimy PP a PV)
uint32_t digital_outputs; // SDO objekt 0x60FE sub 1 
uint16_t control_word_1; // SDO objekt 0x6040
int16_t current_setpoint_1; // SDO objekt 0x6071 (PP, CSP, PT, CST)
uint16_t current_limit_1; // viz rovnice níže
int16_t padding_1; // nepoužívá se
// Druhá osa
int32_t reserved_3; // nepoužívá se
uint32_t reserved_4; // nepoužívá se
uint32_t reserved_5; // nepoužívá se
uint16_t control_word_2; // SDO objekt 0x6840
int16_t current_setpoint_2; // SDO objekt 0x6871 (PP, CSP, PT, CST)
uint16_t current_limit_2; // viz rovnice níže
int16_t padding_2; // nepoužívá se
```

Nastavené hodnoty jsou aktivní podle zvoleného provozního režimu.
Mezní hodnoty proudu se vypočítají jako

$$
Iq_{lim}=(32767-CurrentLimit) \times \frac{M I_{peak}}{32767}
$$

Pro úplné omezení nastavte hodnotu `current_setpoint_x` na `32767`.
Pro žádné omezení, kdy je požadován maximální proud = `M-Ipeak`, nastavte limit na `0`.
CoE TPDO (`0x1B01`) má následující strukturu (40 bajtů):

``` cpp
// První osa
int32_t position_actual_value_1; // SDO objekt 0x6064
int32_t velocity_actual_value_1; // SDO objekt 0x606C
uint32_t digital_inputs; // SDO objekt 0x60FD 
uint16_t status_word_1; // SDO objekt 0x6041
int16_t torque_actual_value_1; // SDO objekt 0x6077
uint16_t analog_input_1; // SDO objekt 0x4002sub1
uint16_t drive_status_1; // SDO objekt 0x4003sub1
// Druhá osa
int32_t position_actual_value_2; // SDO objekt 0x6864
int32_t velocity_actual_value_2; // SDO objekt 0x686C
int32_t external_encoder; // SDO objekt 0x333E
uint16_t status_word_2; // SDO objekt 0x6841
int16_t torque_actual_value_2; // SDO objekt 0x6877
uint16_t analog_input_2; // SDO objekt 0x4002sub2
uint16_t drive_status_2; // SDO objekt 0x4003sub2
```

Všechny aktuální hodnoty jsou aktualizovány bez ohledu na aktivní provozní režim.