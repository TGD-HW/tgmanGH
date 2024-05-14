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

#Vyhlazení trajektorie
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

#Struktura Command
##Registry Command_Parametr

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

#Struktura LookAheadBuffer
##Popis struktury

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

#Apendix
##Přehled a popis registrů struktury Interpolátor
###Interpolátor

<table>
    <tr>
        <td>název</td>
        <td>přístup</td>
        <td>offset</td>
        <td>popis</td>
    </tr>
    <tr>
        <td>Number</td>
        <td>R</td>
        <td>0</td>
        <td>číslo interpolátoru, může nabývat hodnot 0, 1, 2</td>
    </tr>
    <tr>
        <td>Number_Axes</td>
        <td>RW</td>
        <td>4</td>
        <td>počet os, se kterými interpolátor pracuje; povolené rozmezí je 1–10</td>
    </tr>
    <tr>
        <td>Buffer_Size</td>
        <td>R</td>
        <td>8</td>
        <td>maximální počet úseků G-kódu, povolené hodnoty jsou 1000–100000</td>
    </tr>
    <tr>
        <td>Command</td>
        <td>RW</td>
        <td>12</td>
        <td>&quot;příkaz:</td>
    </tr>
    <tr>
        <td>4 = havarijní stop na trajektorii</td>
    </tr>
    <tr>
        <td>5 = havarijní stop (po stopu hlásí mimo trajektorii) 8 = normální stop na trajektorii</td>
    </tr>
    <tr>
        <td>9 = normální stop (mimo trajektorii)</td>
    </tr>
    <tr>
        <td>1024 = nastavení převodních poměrů (mm na inc) – viz kap. Command 2048 = nastavení aktuální polohy (na trajektorii) – viz kap. Command 2049 = nastavení aktuální polohy (mimo trajektorii) – viz kap. Command</td>
    </tr>
    <tr>
        <td>−1 = nastavení parametrů IIR Filtru – viz kap. Command</td>
    </tr>
    <tr>
        <td>−2 = nastavení parametrů Spline – viz kap. Command&quot;</td>
    </tr>
    <tr>
        <td>&quot;Command_Parametr [0-11]</td>
    </tr>
    <tr>
        <td>(12 registrů)&quot;</td>
        <td>RW</td>
        <td>16</td>
        <td>12 parametrů typu integer, jejichž význam a hodnoty závisejí na typu funkce Command</td>
    </tr>
    <tr>
        <td>Command_Status</td>
        <td>R</td>
        <td>64</td>
        <td>&quot;aktuální stav prováděného příkazu:</td>
    </tr>
    <tr>
        <td>0 = předchozí příkaz byl úspěšně vykonán a lze aktivovat další příkaz 1 = aktuální příkaz se provádí</td>
    </tr>
    <tr>
        <td>−1 = během vykonávání příkazu došlo k chybě&quot;</td>
    </tr>
    <tr>
        <td>Status</td>
        <td>R</td>
        <td>68</td>
        <td>&quot;aktuální stav interpolátoru:</td>
    </tr>
    <tr>
        <td>1 = probíhá pohyb po trajektorii 3 = stop na konci trajektorie</td>
    </tr>
    <tr>
        <td>4 = v bufferu je nejméně jeden úsek trajektorie, lze volat start 6 = zastavování po havarijní rampě</td>
    </tr>
    <tr>
        <td>7 = interpolátor se zastavil po havarijním stopu</td>
    </tr>
    <tr>
        <td>8 = interpolátor byl zastaven během plnění bufferu&quot;</td>
    </tr>
    <tr>
        <td>Act_Part</td>
        <td>R</td>
        <td>72</td>
        <td>číslo aktuálně prováděného úseku</td>
    </tr>
    <tr>
        <td>Address_External_Position</td>
        <td>RW</td>
        <td>76</td>
        <td>offset adresy TGM_Data, kde je uložena poloha externího snímače; hodnota je typu integer</td>
    </tr>
    <tr>
        <td>M_Func</td>
        <td>RW</td>
        <td>80</td>
        <td>hodnota M-funkce; pro M &lt; 1000 Interpolátor zastaví a čeká na vynulování této hodnoty; pak pokračuje dalším úsekem; pro M &gt; 1000 se pokračuje ve vykonávání G-kódu</td>
    </tr>
    <tr>
        <td>Act_G_Func</td>
        <td>R</td>
        <td>84</td>
        <td>hodnota právě prováděné G-instrukce</td>
    </tr>
    <tr>
        <td>Act_M_Func</td>
        <td>R</td>
        <td>88</td>
        <td>hodnota právě prováděné M-funkce</td>
    </tr>
    <tr>
        <td>Last_Cont_M_Func</td>
        <td>R</td>
        <td>92</td>
        <td>uložená hodnota poslední průběžné M-funkce (M &gt; 1000)</td>
    </tr>
    <tr>
        <td>Run_Flag</td>
        <td>R</td>
        <td>96</td>
        <td>&quot;- spodních 16 bitů ukazuje stav aktuálního úseku:</td>
    </tr>
    <tr>
        <td>0 = STOP (interpolátor je neaktivní)</td>
    </tr>
    <tr>
        <td>1 = RUN (vykonává se pohybová G-instrukce) 2 = WAIT_WINDOW (pro otáčkové obrábění) 3 = WAIT_PULSE (pro otáčkové obrábění)</td>
    </tr>
    <tr>
        <td>4 = WAIT_MFUNC (začalo provádění M-funkce)</td>
    </tr>
    <tr>
        <td>5 = WAIT_MFUNC_WAIT_FOR_END (čekání na ukončení M-funkce)</td>
    </tr>
    <tr>
        <td>- horních 16 bitů pak stav rychlostního průběhu:</td>
    </tr>
    <tr>
        <td>1 = žádný pohyb 2 = zrychlování</td>
    </tr>
    <tr>
        <td>3 = dosažena požadovaná rychlost pohybu 4 = zpomalování</td>
    </tr>
    <tr>
        <td>5 = další rychlostní úsek</td>
    </tr>
    <tr>
        <td>6 = zpomalování na posledním úseku 7 = zpomalování po havarijní rampě</td>
    </tr>
    <tr>
        <td>pozn.: od verze TGM420&quot;</td>
    </tr>
    <tr>
        <td>Tool_Number</td>
        <td>R</td>
        <td>100</td>
        <td>&quot;číslo aktuálního nástroje (vrtání, fréza, …)</td>
    </tr>
    <tr>
        <td>pozn.: od verze TGM420&quot;</td>
    </tr>
    <tr>
        <td>Orig_Position (10 registrů)</td>
        <td>R</td>
        <td>376</td>
        <td>vypočítané souřadnice všech os [mm]</td>
    </tr>
    <tr>
        <td>Position (10 registrů)</td>
        <td>R</td>
        <td>456</td>
        <td>souřadnice upravené funkcí Spline nebo IIR Filtrem [mm]</td>
    </tr>
    <tr>
        <td>PositionInc (10 registrů)</td>
        <td>R</td>
        <td>536</td>
        <td>souřadnice Position vynásobené převodním poměrem Ratio [inc]</td>
    </tr>
    <tr>
        <td>Backlash (10 registrů)</td>
        <td>R</td>
        <td>616</td>
        <td>aktuální hodnota vůle pro jednotlivé osy [inc]</td>
    </tr>
    <tr>
        <td>Offset (10 registrů)</td>
        <td>RW</td>
        <td>696</td>
        <td>hodnoty offsetu se připočítávají k poloze PositionInc, tyto hodnoty nastavuje uživatel [inc]</td>
    </tr>
    <tr>
        <td>Speed (10 registrů)</td>
        <td>R</td>
        <td>776</td>
        <td>aktuální rychlost jednotlivých os po Spline a IIR [mm/s]</td>
    </tr>
    <tr>
        <td>Ratio (10 registrů)</td>
        <td>RW</td>
        <td>856</td>
        <td>převodní poměr (násobitel) jednotek G-kódu (obvykle mm) na inkrementy (polohy servopohonů)</td>
    </tr>
</table>








