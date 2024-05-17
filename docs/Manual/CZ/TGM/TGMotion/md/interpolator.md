#Interpolátor
##CNC modul

CNC je softwarový modul, který vykonává sekvenci pohybových (G-instrukce) a vstupně/výstupních příkazů (M-funkce) danou G-kódem.
Jeho součástí je modul Interpolátor.

##Interpolátor
Modul interpolátoru počítá polohy a rychlosti jednotlivých servopohonů (os) tak, aby byl výsledný pohyb všemi osami rovnoměrně prováděn.
K dispozici je lineární interpolace (pohyb po přímce), kruhová interpolace (pohyb po kružnici prováděný dvěma libovolnými osami), případně šroubová interpolace (dvě osy vykonávají pohyb po kružnici, ostatní vykonávají lineární pohyb).
K výpočtu tří nezávislých finálních trajektorií víceosého pohybu nabízí systém TG Motion tři nezávislé interpolátory, z nichž každý může pracovat až s deseti servopohony.
Sdílená paměť `TGM_Interpolator` slouží jako rozhraní mezi CNC modulem a ostatními aplikacemi (PLC, Win aplikace).
Většina registrů je určena jen pro čtení a zobrazuje aktuální hodnoty CNC modulu.
Protože G-kód je většinou psán v jednotkách [mm], pracují i Interpolátory s jednotkami [mm].
K nastavení převodu [mm] na [inc] slouží struktura Command nebo registr Ratio (viz dále).

<img src="../../img/interpolatorBlock.png" alt="Blokové schéma Interpolátoru"  style="width:100%;">

##Kompetence PLC a Windows aplikací
###PLC 
Nastavuje základní parametry Interpolátoru, obsluhuje M-funkce a řeší havarijní zastavení Interpolátoru.
Z PLC Interpolátor spustit nelze.

###Windows aplikace
Převádějí G-kód do binárního mezikódu, plní jím buffer Interpolátoru ve sdílené paměti a spouštějí i zastavují Interpolátor.
Buffer Interpolátoru není z PLC ani Windows aplikací přístupný.

##G-kód
G-kód je název programovacího jazyka, který řídí NC a CNC obráběcí stroje.
Jedná se o kód v textovém formátu, který říká obráběcímu stroji, jakou akci má vykonat.
V G-kódu mezi nejpoužívanější příkazy patří Ginstrukce a M-funkce.
Jsou vždy uvozeny písmenem (G, M) a číselným parametrem, který specifikuje, co má daná instrukce vykonávat.
Jednotlivé G-instrukce jsou přesně definovány, většinu M-funkcí může definovat uživatel.

###Ukázka části G-kódu

``` gcode
G00 X60.6051 Y40.7723
G42
M51
G02 X0 Y-2.5202 I3.0336 J-1.2601
G02 X0.922 Y-1.5646 I6.0604 J2.5173
G02 X1.079 Y-1.0269 I4.2143 J3.3479
G02 X2.2624 Y-1.3678 I9.8772 J13.7817
G02 X1.9856 Y-0.8109 I6.1778 J12.2908
G02 X3.015 Y-0.7892 I8.8515 J27.6632
G02 X6.2889 Y0 I3.1444 J33.011
M50
G40
G00 X-28.9085 Y30.4365
G42
M51
G40
M2
```

###G-instrukce
Slouží většinou k rychlému polohování, posuvnému pohybu po přímce nebo oblouku, vrtání nebo řezání.
O jejich plnění se stará Interpolátor. Průběh vykonávání G-instrukcí může být přerušen plněním M-funkcí.
V tom případě Interpolátor může čekat na vykonání M-funkce a pak pokračovat dále ve vykonávání G-kódu.

###Tabulka G-instrukcí

| Označení | Popis |
|---|---|
| **Základní G-instrukce** | |
| G0 | Rychloposuv |
| G1 | Lineární interpolace |
| G2 | Kruhová interpolace CW |
| G3 | Kruhová interpolace CCW |
| G4 | Prodleva [sec] |
| G25 | Volání podprogramu |
| G26 | Volání cyklu |
| G27 | Programový skok |
| G29 | Návěští nebo textová poznámka |
| G40 | Zrušení korekce |
| G41 | Korekce vlevo od kontury |
| G42 | Korekce vpravo od kontury |
| G53 | Zrušení posunutí nulového bodu |
| G54 | Posunutí nulového bodu |
| **Rozšířené G-instrukce** | |
| G90 | Absolutní programování |
| G91 | Inkrementální (přírůstkové) programování |
| G92 | Nastavení hodnot souřadnic |

###M-funkce
Pokud je součástí kódu libovolná M-funkce, její obsloužení je třeba zabezpečit v uživatelském PLC kódu.
Interpolátor se M-funkcemi nezabývá, jen u některých čeká na jejich obsloužení.
M-funkce mohou být až na výjimky uživatelsky definovány (viz registr M_Funkce_Parametr).

###Pohybové a průběžné M-funkce
Pohybové M-funkce (Mx, kde x < 1000) – vykonávání G-kódu se zastaví, PLC obslouží M-Funkci a po jejím dokončení nastaví registr `M_Func = 0`.
Interpolátor pak pokračuje ve vykonávání G-kódu další instrukcí.
Průběžné M-funkce (Mx, kde x > 1000) – PLC spustí obsluhu M-funkce, ale Interpolátor nečeká na obsloužení M-funkce a pokračuje dál ve vykonávání G-kódu.

###Tabulka podporovaných M-funkcí

| Označení | Popis |
|---|---|
| M0 | Programový stop |
| M2 | Ukončení G-kódu, lze předefinovat |
| M3 | Roztáčení vřetene CW, lze předefinovat |
| M4 | Roztáčení vřetene CCW, lze předefinovat |
| M5 | Zastavení vřetene, lze předefinovat |
| M6 | Výměna nástroje, lze předefinovat |
| M7 | Zapnutí chlazení, lze předefinovat |
| M8 | Zapnutí mazání, lze předefinovat |
| M9 | Vypnutí chlazení i mazání, lze předefinovat |
| M17 | Návrat z podprogramu (RETURN), lze předefinovat |
| M29 | Výstup textového hlášení (PRINT), lze předefinovat |
| M30 | Ukončení G-kódu, lze předefinovat |
| M80 | Vypnutí zrcadlení |
| M81 | Zrcadlení v ose x |
| M82 | Zrcadlení v ose y |
| M83 | Zrcadlení v ose z |
| M84 | Zrcadlení v osách x a y |
| M85 | Zrcadlení v osách x a z |
| M86 | Zrcadlení v osách y a z |
| M87 | Zrcadlení v osách x, y a z |
| M99 | Definování výchozí hodnoty posuvu, lze předefinovat |

##Vyhlazení trajektorie
G-kód často pracuje s polynomy složenými z krátkých úseček, někdy může také docházet k okamžitým změnám rychlosti vlivem nesprávně zapsaného kódu.
Všechny okamžité změny rychlosti se mohou projevit nežádoucím zrychlením v některých z os, a tím i mechanickým rázem v některých servopohonech.
K vyhlazení vypočtené trajektorie slouží dva nástroje.

##Spline
###Spline – funkce vyhlazení

Funkci Spline je vhodné použít v případě nekorektně vytvořených G-kódů, ve kterých jednotlivé úseky na
sebe plynule či spojitě nenavazují, nebo v případě G-kódů, v nichž je výsledná trajektorie vytvořena pomocí
lineárních úseků s hrubým dělením. Spline je také vhodný k vyhlazení skokové změny rychlosti, která vyplývá
z matematického modelu mechaniky (např. naklápěcí hlavy).   

Funkce Spline se aktivuje ve všech osách současně, nelze ji aplikovat jen na některé osy. Po její aktivaci
je v každé ose kontrolována změna zrychlení (jerk). V případě, že je nalezena změna vetší než povolená, proloží
se daným místem spline křivka.

!!! info "Upozornění"
	Čím je větší délka spline (velikost Spline bufferu), tím je vyhlazení lepší.
	Vyhlazení pomocí funkce Spline je na úkor přesnosti polohování.
	
###Aktivace a parametrizace Spline
Funkce Spline se aktivuje a parametrizuje pomocí struktury Command daného Interpolátoru.
Pro hodnotu registru `Command = −2` mají Command parametry následující význam:

`Command_Parametr[0]` – určuje počet bodů, kterými se prokládá spline. Potažmo se tak určuje velikost Spline bufferu. 
Rozsah nastavení parametru je 50–500 bodů/kroků. 
Při `Cycle_Time = 500 μs` je krok výpočtu 100 μs, při `Cycle_Time = 250 μs` je krok výpočtu 50 μs.
Vypnutí funkce Spline je možné nastavením délky spline na nulu (`Command_Parametr[0] = 0`).   

`Command_Parametr[1]` – určuje mez vyhodnocení změny zrychlení (jerk), tedy od jakého zrychlení se funkce Spline aktivuje.
Udává se v jednotkách [mm/s³].
Vhodná hodnota nastavení je 1 000 000 mm/s³.   

Po nastavení obou parametrů je třeba nastavit registr Command na hodnotu −2.
Po provedení příkazu TG Motion tento registr vynuluje.

###Zpoždění pohybu
Pohyb po průchodu funkcí Spline je oproti polohování vypočteného interpolátorem zpožděn o délku Spline bufferu.
Všechny osy polohují neustále synchronně, protože velikost bufferů je pro všechny osy stejná.
I M-funkce jsou volány synchronně s výsledným pohybem, protože je pro ně použit buffer stejné velikosti.

###Příklad nastavení Spline
Příklad zapnutí funkce Spline s délkou spline 20 ms (při `Cycle_Time = 500 μs`).
Nejdříve je třeba nastavit hodnoty Command_Parametrů a jako poslední hodnotu registru `Command = −2`.

``` cpp
Interpolator.Command_Parametr[0] = 200;
Interpolator.Command_Parametr[1] = 1000000;
Interpolator.Command = -2;
```

##IIR Filtr
###IIR Filtr – funkce vyhlazení

K vyhlazení výsledné rychlosti pohybu a odstranění nežádoucích rychlých změn lze použít IIR Filtr (Infinite Impulse Response).
Jedná se o matematický model lineárního filtru typu dolní propust (Low-pass) se strmostí 12 dB na oktávu (2-Pole) počítaný podle vztahu:

$$
H(s) = \frac{q}{s^2 + p \cdot s + q}
$$

s možností nastavení tří parametrů:

-	*p, q* – parametry nastavující průběh filtru (viz tabulku)
-	*f (cutoff)* – čas, za který se filtrovaná trajektorie vrátí k původní vypočtené trajektorii

###Hodnoty parametrů pro některé typy filtrů

| p   | q   | typ filtru      | popis                                            |
| --- | --- | --------------- | ------------------------------------------------ |
| √2  | 2   | Butterworth     | před f dochází ke zdvihu, malé zpoždění         |
| 3   | 3   | Bessel          | mírný zdvih, hladký průběh, větší zpoždění       |
| 2   | 1   | critically damped | hladký pozvolný průběh bez zdvihu, největší zpoždění |

<img src="../../img/filterChar.png" alt="Grafické znázornění průběhu některých typů filtrů"  style="width:50%;">

###Aktivace a parametrizace IIR Filtru
Hodnoty parametrů IIR Filtru lze nastavit pomocí struktury Command.
Pro hodnotu registru `Command = −1` mají Command parametry následující význam:

-	`Command_Parametr[0]` – nastavuje parametr p filtru.
-	`Command_Parametr[1]` – nastavuje parametr q filtru.
-	`Command_Parametr[2]` – určuje f – čas návratu k původní trajektorii.

!!! info "Upozornění"
	Hodnoty parametrů jsou typu `Integer`, skutečné fyzické hodnoty parametru se dosáhne dělením hodnoty parametru číslem $1 \cdot 10^6$ (`Command_Parametr[1] = 1000000`, parametr filtru = 1,0).
	
-	`Command_Parametr[3]` – nastavuje bitovou masku aktivity filtrů pro jednotlivé osy.
							Používá se pouze prvních 10 bitů pro 10 os, ostatní bity jsou ignorovány (viz registry).

###Zpoždění pohybu
**IIR Filtry** vypočítaný pohyb zpožďují.
Zpoždění je závislé na vstupních datech, dynamicky se mění a jeho velikost nelze předem určit.
M-funkce jsou z běžícího G-kódu signalizovány při „stojícím“ Interpolátoru, fyzický pohyb servopohonů ale nemusí být ještě ukončen.							

!!! info "Upozornění"
	Při použití IIR Filtru bude servopohon „plavat“ za Interpolátorem a je vždy třeba počkat, až je fyzický pohyb všech servopohonů skutečně dokončen.

Nastavení parametrů IIR Filtrů je společné pro všechny osy Interpolátoru.
Filtr je možné aktivovat nezávisle pro jednotlivé osy podle bitové masky registru `Command_Parametr[3]`.
Je tedy třeba počítat s tím, že výsledný pohyb os po aplikaci filtru nemusí být vzájemně synchronní tak, jak byl původně vypočten.

##Struktura Command
###Registry Command_Parametr

V kapitole je popsán význam registrů `Command_Parametr[ ]` pro vybrané hodnoty registru Command.

###Nastavení převodového poměru mm na inc – Command = 1024
V G-kódu se většinou implicitně pracuje s jednotkou [mm], proto Interpolátor pracuje také v jednotkách [mm].
Protože servopohony pracují s inkrementy [inc], je třeba podle počtu inc/otáčku servopohonu (`Servo[x].Resolution`) stanovit převodový poměr *inc/mm*.
Ten se nastavuje pomocí struktury Command příslušného Interpolátoru.
Převodovým poměrem se pak násobí vypočítaná poloha v dané ose a takto přepočtená se pak posílá do servopohonu.

| Command_Parametr | popis                                     |
| ---------------- | ----------------------------------------- |
| 0                | určuje číslo osy, u níž se poměr nastavuje [0–9] |
| 1                | čitatel převodového poměru [inc]         |
| 2                | jmenovatel převodového poměru [mm]       |

###Nastavení aktuální polohy – Command = 2048 a Command = 2049
Pomocí Command = 2048 a Command = 2049 se nastavuje aktuální poloha interpolátoru.
Po provedení příkazu 2048 systém hlásí polohu na trajektorii, v druhém případě polohu mimo trajektorii.
Pro obě varianty nabývají všechny Command_Parametr[0-9] stejného významu.

| Command_Parametr | popis                             |
| ---------------- | --------------------------------- |
| 0                | aktuální poloha v ose 0 [inc]    |
| ...              | ...                               |
| 9                | aktuální poloha v ose 9 [inc]    |

###Nastavení parametrů IIR Filtru – Command = −1

| Command_Parametr | popis                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------- |
| 0                | parametr p filtru – nastavení průběhu filtru (v kombinaci s parametrem q)              |
| 1                | parametr q filtru – nastavení průběhu filtru (v kombinaci s parametrem p)              |
| 2                | parametr f filtru – čas, za který se filtrovaná trajektorie vrátí k původní trajektorii |
| 3                | bitová maska aktivity IIR Filtrů pro jednotlivé osy Interpolátoru. Příklad: xxxx xx00 0000 0101 – aktivní je pouze IIR Filtr pro osu 0 a osu 2  |

###Nastavení parametrů Spline – Command = −2

| Command_Parametr | popis                                                                       |
| ---------------- | --------------------------------------------------------------------------- |
| 0                | určuje počet bodů, kterými se spline prokládá; rozsah nastavení je 50–500 bodů |
| 1                | horní mez vyhodnocení změny zrychlení [mm/s³]                               |

##Struktura LookAheadBuffer
###Popis struktury

Struktura **LookAheadBuffer** je tabulka důležitých parametrů osmi úseků – položek G-kódu jdoucích po
sobě. První položkou tabulky je vždy právě prováděný úsek, dalšími položkami je sedm bezprostředně
následujících úseků.   

**LookAheadBuffer** funguje jako posuvný buffer. Po provedení aktuálního úseku se data tabulky posunou,
první je opět vykonávaný úsek a na poslední místo se vloží 8. následující úsek od aktuálně vykonávaného.
Strukturu LookAheadBuffer naplňuje Interpolátor. Z hlediska PLC jsou její registry pouze ke čtení.

###Úsek G-kódu
Úsekem se rozumí jedna položka G-kódu, a to buď G-instrukce (G0–G3) nebo pohybová M-funkce, která má význam z hlediska pohybu (M3–M999).

##Použití struktury
Struktura **LookAheadBuffer** slouží k přizpůsobení technologií podle instrukcí a funkcí následujících úseků,
případně podle jejich hodnot. Protože z PLC nelze Interpolátor spustit ani zastavit (kromě havarijního stop), je
třeba během obsluhy existujících M-funkcí obhospodařit vše potřebné. To musí zabezpečit tvůrce PLC kódu.
PLC může během M-funkce například změnit úhel obráběcí hlavy v rohu čtverce podle tangenty následující
funkce; může pomocí registru Rel_Speed zpomalit pohyb, pokud ví, že bude následovat velká změna tangenty.
Při pohybu po kružnici je k dispozici neustále aktuální tangenta, která se dá použít pro natáčení hlavy. Při
krátkých úsečkách lze také postupným natáčením hlavy vyhladit lomenou úsečku. K vykonání všech těchto úkonů
je nutné vědět, co bude následovat za právě vykonávaným úsekem. K tomu lze právě využít struktury
LookAheadBuffer.

!!! info "Upozornění"
	Někdy se pro `Movement_Type = 2` může v registru `Movement_Code` objevit záporné číslo M-funkce.
	Jedná se o vnitřní funkci TG Motion, s níž není třeba nijak pracovat.
	
Jednotlivé registry struktury LookAheadBuffer jsou popsány v kapitole Apendix.

##Apendix
###Přehled a popis registrů struktury Interpolátor

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;název&quot;}"><b>název</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;přístup&quot;}"><b>přístup</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;popis&quot;}"><b>popis</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number&quot;}">Number</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="0" sdnum="1029;">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;číslo interpolátoru, může nabývat hodnot 0, 1, 2&quot;}">číslo interpolátoru, může nabývat hodnot 0, 1, 2</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number_Axes&quot;}">Number_Axes</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="4" sdnum="1029;">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;počet os, se kterými interpolátor pracuje; povolené rozmezí je 1–10&quot;}">počet os, se kterými interpolátor pracuje; povolené rozmezí je 1–10</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Buffer_Size&quot;}">Buffer_Size</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="8" sdnum="1029;">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximální počet úseků G-kódu, povolené hodnoty jsou 1000–100000&quot;}">maximální počet úseků G-kódu, povolené hodnoty jsou 1000–100000</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="12" sdnum="1029;">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;příkaz:&yen;u000a4 = havarijní stop na trajektorii&yen;u000a5 = havarijní stop (po stopu hlásí mimo trajektorii) 8 = normální stop na trajektorii&yen;u000a9 = normální stop (mimo trajektorii)&yen;u000a1024 = nastavení převodních poměrů (mm na inc) – viz kap. Command 2048 = nastavení aktuální polohy (na trajektorii) – viz kap. Command 2049 = nastavení aktuální polohy (mimo trajektorii) – viz kap. Command&yen;u000a−1 = nastavení parametrů IIR Filtru – viz kap. Command&yen;u000a−2 = nastavení parametrů Spline – viz kap. Command&quot;}">příkaz:<br>4 = havarijní stop na trajektorii<br>5 = havarijní stop (po stopu hlásí mimo trajektorii) 8 = normální stop na trajektorii<br>9 = normální stop (mimo trajektorii)<br>1024 = nastavení převodních poměrů (mm na inc) – viz kap. Command 2048 = nastavení aktuální polohy (na trajektorii) – viz kap. Command 2049 = nastavení aktuální polohy (mimo trajektorii) – viz kap. Command<br>−1 = nastavení parametrů IIR Filtru – viz kap. Command<br>−2 = nastavení parametrů Spline – viz kap. Command</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command_Parametr [0-11]&yen;u000a(12 registrů)&quot;}">Command_Parametr [0-11]<br>(12 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="16" sdnum="1029;">16</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;12 parametrů typu integer, jejichž význam a hodnoty závisejí na typu funkce Command&quot;}">12 parametrů typu integer, jejichž význam a hodnoty závisejí na typu funkce Command</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command_Status&quot;}">Command_Status</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="64" sdnum="1029;">64</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální stav prováděného příkazu:&yen;u000a0 = předchozí příkaz byl úspěšně vykonán a lze aktivovat další příkaz 1 = aktuální příkaz se provádí&yen;u000a−1 = během vykonávání příkazu došlo k chybě&quot;}">aktuální stav prováděného příkazu:<br>0 = předchozí příkaz byl úspěšně vykonán a lze aktivovat další příkaz 1 = aktuální příkaz se provádí<br>−1 = během vykonávání příkazu došlo k chybě</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status&quot;}">Status</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="68" sdnum="1029;">68</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální stav interpolátoru:&yen;u000a1 = probíhá pohyb po trajektorii 3 = stop na konci trajektorie&yen;u000a4 = v bufferu je nejméně jeden úsek trajektorie, lze volat start 6 = zastavování po havarijní rampě&yen;u000a7 = interpolátor se zastavil po havarijním stopu&yen;u000a8 = interpolátor byl zastaven během plnění bufferu&quot;}">aktuální stav interpolátoru:<br>1 = probíhá pohyb po trajektorii 3 = stop na konci trajektorie<br>4 = v bufferu je nejméně jeden úsek trajektorie, lze volat start 6 = zastavování po havarijní rampě<br>7 = interpolátor se zastavil po havarijním stopu<br>8 = interpolátor byl zastaven během plnění bufferu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_Part&quot;}">Act_Part</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="72" sdnum="1029;">72</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;číslo aktuálně prováděného úseku&quot;}">číslo aktuálně prováděného úseku</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Address_External_Position&quot;}">Address_External_Position</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="76" sdnum="1029;">76</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset adresy TGM_Data, kde je uložena poloha externího snímače; hodnota je typu integer&quot;}">offset adresy TGM_Data, kde je uložena poloha externího snímače; hodnota je typu integer</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M_Func&quot;}">M_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="80" sdnum="1029;">80</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;hodnota M-funkce; pro M< 1000 Interpolátor zastaví a čeká na vynulování této hodnoty; pak pokračuje dalším úsekem; pro M>1000 se pokračuje ve vykonávání G-kódu&quot;}">hodnota M-funkce; pro M &lt; 1000 Interpolátor zastaví a čeká na vynulování této hodnoty; pak pokračuje dalším úsekem; pro M &gt; 1000 se pokračuje ve vykonávání G-kódu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_G_Func&quot;}">Act_G_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="84" sdnum="1029;">84</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;hodnota právě prováděné G-instrukce&quot;}">hodnota právě prováděné G-instrukce</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_M_Func&quot;}">Act_M_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="88" sdnum="1029;">88</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;hodnota právě prováděné M-funkce&quot;}">hodnota právě prováděné M-funkce</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Last_Cont_M_Func&quot;}">Last_Cont_M_Func</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="92" sdnum="1029;">92</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;uložená hodnota poslední průběžné M-funkce (M>1000)&quot;}">uložená hodnota poslední průběžné M-funkce (M &gt; 1000)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Run_Flag&quot;}">Run_Flag</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="96" sdnum="1029;">96</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;- spodních 16 bitů ukazuje stav aktuálního úseku:&yen;u000a0 = STOP (interpolátor je neaktivní)&yen;u000a1 = RUN (vykonává se pohybová G-instrukce) 2 = WAIT_WINDOW (pro otáčkové obrábění) 3 = WAIT_PULSE (pro otáčkové obrábění)&yen;u000a4 = WAIT_MFUNC (začalo provádění M-funkce)&yen;u000a5 = WAIT_MFUNC_WAIT_FOR_END (čekání na ukončení M-funkce)&yen;u000a- horních 16 bitů pak stav rychlostního průběhu:&yen;u000a1 = žádný pohyb 2 = zrychlování&yen;u000a3 = dosažena požadovaná rychlost pohybu 4 = zpomalování&yen;u000a5 = další rychlostní úsek&yen;u000a6 = zpomalování na posledním úseku 7 = zpomalování po havarijní rampě&yen;u000apozn.: od verze TGM420&quot;}">- spodních 16 bitů ukazuje stav aktuálního úseku:<br>0 = STOP (interpolátor je neaktivní)<br>1 = RUN (vykonává se pohybová G-instrukce) 2 = WAIT_WINDOW (pro otáčkové obrábění) 3 = WAIT_PULSE (pro otáčkové obrábění)<br>4 = WAIT_MFUNC (začalo provádění M-funkce)<br>5 = WAIT_MFUNC_WAIT_FOR_END (čekání na ukončení M-funkce)<br>- horních 16 bitů pak stav rychlostního průběhu:<br>1 = žádný pohyb 2 = zrychlování<br>3 = dosažena požadovaná rychlost pohybu 4 = zpomalování<br>5 = další rychlostní úsek<br>6 = zpomalování na posledním úseku 7 = zpomalování po havarijní rampě<br>pozn.: od verze TGM420</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tool_Number&quot;}">Tool_Number</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="100" sdnum="1029;">100</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;číslo aktuálního nástroje (vrtání, fréza, …)&yen;u000apozn.: od verze TGM420&quot;}">číslo aktuálního nástroje (vrtání, fréza, …)<br>pozn.: od verze TGM420</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Orig_Position (10 registrů)&quot;}">Orig_Position (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="376" sdnum="1029;">376</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;vypočítané souřadnice všech os [mm]&quot;}">vypočítané souřadnice všech os [mm]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Position (10 registrů)&quot;}">Position (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="456" sdnum="1029;">456</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;souřadnice upravené funkcí Spline nebo IIR Filtrem [mm]&quot;}">souřadnice upravené funkcí Spline nebo IIR Filtrem [mm]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PositionInc (10 registrů)&quot;}">PositionInc (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="536" sdnum="1029;">536</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;souřadnice Position vynásobené převodním poměrem Ratio [inc]&quot;}">souřadnice Position vynásobené převodním poměrem Ratio [inc]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Backlash (10 registrů)&quot;}">Backlash (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="616" sdnum="1029;">616</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální hodnota vůle pro jednotlivé osy [inc]&quot;}">aktuální hodnota vůle pro jednotlivé osy [inc]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Offset (10 registrů)&quot;}">Offset (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="696" sdnum="1029;">696</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;hodnoty offsetu se připočítávají k poloze PositionInc, tyto hodnoty nastavuje uživatel [inc]&quot;}">hodnoty offsetu se připočítávají k poloze PositionInc, tyto hodnoty nastavuje uživatel [inc]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Speed (10 registrů)&quot;}">Speed (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="776" sdnum="1029;">776</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální rychlost jednotlivých os po Spline a IIR [mm&yen;/s]&quot;}">aktuální rychlost jednotlivých os po Spline a IIR [mm/s]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ratio (10 registrů)&quot;}">Ratio (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="856" sdnum="1029;">856</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;převodní poměr (násobitel) jednotek G-kódu (obvykle mm) na inkrementy (polohy servopohonů)&quot;}">převodní poměr (násobitel) jednotek G-kódu (obvykle mm) na inkrementy (polohy servopohonů)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M_Funkce_Parametr&yen;u000a(32 registrů)&quot;}">M_Funkce_Parametr<br>(32 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="936" sdnum="1029;">936</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;parametry M funkce z G-kódu, celkem 26 hodnot podle písmen v abecedě; některá písmena nelze použít, protože jsou vyhrazena systémem&yen;u000arezervované parametry (indexy jsou počítány od 0): G = index 6&yen;u000aM = index 12 N = index 13&yen;u000aP = index 15&quot;}">parametry M funkce z G-kódu, celkem 26 hodnot podle písmen v abecedě; některá písmena nelze použít, protože jsou vyhrazena systémem<br>rezervované parametry (indexy jsou počítány od 0): G = index 6<br>M = index 12 N = index 13<br>P = index 15</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rel_Speed&quot;}">Rel_Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;RW&quot;}">RW</td>
		<td sdval="1192" sdnum="1029;">1192</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;relativní rychlost interpolovaného pohybu, koeficient v rozmezí 0,01–2 (1–200 %)&quot;}">relativní rychlost interpolovaného pohybu, koeficient v rozmezí 0,01–2 (1–200 %)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Set_Speed&quot;}">Set_Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="1200" sdnum="1029;">1200</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;požadovaná rychlost z G-kódu (daná F-instrukcí G-kódu nebo tabulkou rychlostí) [mm&yen;/min]&quot;}">požadovaná rychlost z G-kódu (daná F-instrukcí G-kódu nebo tabulkou rychlostí) [mm/min]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Act_Speed&quot;}">Act_Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="1208" sdnum="1029;">1208</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální rychlost [mm&yen;/min]&quot;}">aktuální rychlost [mm/min]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Move_Distance&quot;}">Move_Distance</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="1216" sdnum="1029;">1216</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální celková ujetá vzdálenost [mm]&quot;}">aktuální celková ujetá vzdálenost [mm]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;LookAheadBuffer&quot;}">LookAheadBuffer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="2048" sdnum="1029;">2048</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;tabulka informací o úsecích, které budou následovat; celkem 8 položek struktury popsané&yen;u000av následující tabulce; první položka popisuje právě prováděný úsek; velikost každé položky je 1792 bytů&yen;u000apozn.: od verze TGM420&quot;}">tabulka informací o úsecích, které budou následovat; celkem 8 položek struktury popsané<br>v následující tabulce; první položka popisuje právě prováděný úsek; velikost každé položky je 1792 bytů<br>pozn.: od verze TGM420</td>
	</tr>
</table>


###Přehled a popis registrů struktury LookAheadBuffer

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;název&quot;}"><b>název</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;přístup&quot;}"><b>přístup</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;offset&quot;}"><b>offset</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;popis&quot;}"><b>popis</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;AllParams&yen;u000a(26 registrů)&quot;}">AllParams<br>(26 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="0" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;všechny zadané adresy M-funkcí z konkrétního G-kódu pro daný úsek (26 písmen anglické&yen;u000aabecedy)&quot;}">všechny zadané adresy M-funkcí z konkrétního G-kódu pro daný úsek (26 písmen anglické<br>abecedy)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tangens&quot;}">Tangens</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="208" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 208}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">208</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aktuální tečna pohybu v rovině XY; pokud je právě prováděný úsek oblouk (G2 nebo G3),&yen;u000atečna se mění průběžně; pro budoucí úseky určuje počáteční tečnu pohybu&quot;}">aktuální tečna pohybu v rovině XY; pokud je právě prováděný úsek oblouk (G2 nebo G3),<br>tečna se mění průběžně; pro budoucí úseky určuje počáteční tečnu pohybu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;MovementType&quot;}">MovementType</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="216" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 216}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">216</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;typ záznamu:&yen;u000a0 = neplatný záznam (počet zbývajících úseků k provedení je menší než aktuální index tabulky LookAheadBuffer), do konce provedení pohybu zbývá méně než 8 úseků&yen;u000a1 = pohybová funkce (G0, G1, G2, G3) 2 = M funkce&quot;}">typ záznamu:<br>0 = neplatný záznam (počet zbývajících úseků k provedení je menší než aktuální index tabulky LookAheadBuffer), do konce provedení pohybu zbývá méně než 8 úseků<br>1 = pohybová funkce (G0, G1, G2, G3) 2 = M funkce</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;MovementCode&quot;}">MovementCode</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="220" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 220}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">220</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;číslo G-instrukce nebo pohybové M-funkce (číslo průběžné M-funkce se v tomto registru neobjeví, ale objeví se v AllParams v písmenu M)&quot;}">číslo G-instrukce nebo pohybové M-funkce (číslo průběžné M-funkce se v tomto registru neobjeví, ale objeví se v AllParams v písmenu M)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Plane&quot;}">Plane</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="224" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 224}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">224</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;- rovina kruhové interpolace: 17 = XY&yen;u000a18 = XZ&yen;u000a19 = YZ&yen;u000a- ostatní roviny nejsou definovány&quot;}">- rovina kruhové interpolace: 17 = XY<br>18 = XZ<br>19 = YZ<br>- ostatní roviny nejsou definovány</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Tool&quot;}">Tool</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="228" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 228}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">228</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;číslo nástroje&quot;}">číslo nástroje</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;EndPos (10 registrů)&quot;}">EndPos (10 registrů)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="232" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 232}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">232</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;koncová poloha úseku jednotlivých os [mm] (absolutní souřadnice)&quot;}">koncová poloha úseku jednotlivých os [mm] (absolutní souřadnice)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;StartAngle&quot;}">StartAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="312" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 312}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">312</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;počáteční úhel oblouku [°] – úhel spojnice středu oblouku s počátečním bodem; hodnota&yen;u000aregistru je cyklická (0–360); pro lineární pohyb či M-funkce je hodnota registru větší než 1038&quot;}">počáteční úhel oblouku [°] – úhel spojnice středu oblouku s počátečním bodem; hodnota<br>registru je cyklická (0–360); pro lineární pohyb či M-funkce je hodnota registru větší než 1038</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;EndAngle&quot;}">EndAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="320" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 320}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">320</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;koncový úhel oblouku [°] – úhel spojnice středu oblouku s koncovým bodem; hodnota registru je cyklická (0–360); pro lineární pohyb či M-funkce je větší než 1038&quot;}">koncový úhel oblouku [°] – úhel spojnice středu oblouku s koncovým bodem; hodnota registru je cyklická (0–360); pro lineární pohyb či M-funkce je větší než 1038</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Radius&quot;}">Radius</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;R&quot;}">R</td>
		<td sdval="328" sdnum="1029;0;0" data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 328}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">328</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;- poloměr oblouku [mm]&yen;u000a- pro lineární pohyb či M-funkce je registr nulový&quot;}">- poloměr oblouku [mm]<br>- pro lineární pohyb či M-funkce je registr nulový</td>
	</tr>
</table>






