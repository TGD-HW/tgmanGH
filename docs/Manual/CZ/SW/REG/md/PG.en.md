##Základní popis {#Ramptype}
Generátor žádané polohy.
Umožňuje jednoduchým způsobem polohovat z bodu do bodu a rychlostně řídit servopohon.
Výstupem generátoru je proměnná 64 bitová poloha, která se skládá ze dvou 32 bitových proměnných `APosAngle` a `APosRevol` a dále proměnné `ASpeed` určující aktuální žádanou hodnotu rychlosti.
Parametry generátoru jsou `Acc` a `Dec`, které určují akceleraci resp. deceleraci pohonu, parametr `Type` určuje průběh rychlosti při akceleraci a deceleraci (viz. schéma níže).
Dalším parametrem je `PosSpeed`, který určuje maximální rychlost při zapolohování, parametry `DPosAngle` a `DposRevol` určují cílovou polohu a parametr `Speed` určuje žádanou hodnotu rychlosti.
Pomocí proměnných `Mode` a `Rdy` se realizuje vlastní ovládání generátoru.
Proměnná `Mode` určuje režim PG (hodnota 0 udává rychlostní režim, hodnota 1 udává polohový režim).
Pokud je polohování úspěšně dokončeno a výstupní poloha je shodná se žádanou, pak je tento stav signalizován hodnotou proměnné `Rdy = 1`.
Generátor pracuje tak, že v každé periodě na základě parametrů (`Acc, Dec, Type, PosSpeed, DPosAngle a DPosRevol`) a stavu proměnných `Mode` a `Speed` vypočítá aktuální žádanou hodnotu polohy `APosAngle` a `APosRevol` a aktuální žádanou hodnotu rychlosti `ASpeed`.
Výpočet generátoru probíhá s interním rozlišením daným parametrem `BitsPerRevol`.
Tento parametr pak udává vnitřní počet inkrementů na otáčku.

<img src="../../../../../source/img/TGZrampType1.webp" alt="TGZ servo ramp type" style="width:70%;"> 

- (a) Polohový mód
- (b) rychlostní režim
- (c) typ náběžných a sestupných ramp

Následující parametry pracují s tímto rozlišením:

| Parameter               | Jednotka        |
|-------------------------|-------------|
| Acc, Dec                | [Inc/s²]    |
| ASpeed, DSpeed, Speed   | [Inc/s]     |

Polohové parametry jsou 64 bitové a jsou složeny ze dvou 32 bitových registrů:

- Registr Angle udává polohu v rámci jedné otáčky s rozlišením 32 bitů
- Registr Revol je rozšíření o 32 bitů (počet celých otáček):
	- DPosRevol, DPosAngle
	- APosRevol, APosAngle

V uživatelském programu je možno pro zjednodušení práce s generátorem profilu využívat tyto vestavěné funkce:

- Relativní polohování - jedná se o přejezd o polohu:   
int PosRel(int axis, int Acc, int Dec, int Speed, long long Pos, int AddGear);
- Absolutní polohování - jedná se nájezd do absolutní polohy:   
int PosAbs(int axis, int Acc, int Dec, int Speed, long long Pos, int AddGear);
- Rychlostní přejezd - pohon se roztočí danou rychlostí.   
int RunSpeed(int axis, int Acc, int Speed, int AddGear);

Popis parametrů:
axis - 0 -> osa 1; axis 1 - osa 2
Acc,Dec ... Ve stejném významu jako parametry PG popsané výše
Speed ... Maximální rychlost polohového přejezdu nebo rychlost rychlostního přejezdu
AddGear ... zatím není implementován (bude určovat spolupráci s modulem Gear - převod)

##Příklady řízení motoru prostřednictvím Profil Generátoru
Následující tabulky poskytují příklady použití profilu generátoru, který je nastaven na různé režimy řízení motoru.
Ve sloupci *Základní skupiny* je uveden název stránky.
Přepínání mezi jednotlivými stránkami je povoleno v levém horním rohu grafického uživatelského rozhraní TGZ.

!!! Note "Poznámka"
	V prvním kroku je důležité nastavit / načíst správné parametry pohonu.
	Nahrávání parametrů je umožněno pomocí modré obálky v pravém horním rohu (*LOAD PARAMETERS FROM FILE*), viz. [Návod k TGZ GUI](../../../TGZ/TGZ_SW/GUI/md/intro.md#GUIstart)
	
###Řízení polohy motoru (TGZ GUI)
| Krok | Základní skupina | Parametr   | Hodnota   | Popis                                                                                                              |
|------|--------------|------------|----------|--------------------------------------------------------------------------------------------------------------------------|
| 1    | -            | -          | -        | Načíst parametry pohonu.                                                                                                  |
| 2    | Drive        | D-mode     | 7        | Generátor profilů - režim polohy.                                                                                        |
| 3    | Command      | K-Command  | 1        | SW enable. Lze jej také zapnout pomocí tlačítka enable pro příslušnou osu na spodní liště. Motor generuje točivý moment.  |
| 4    | PG           | Acc        | 5 000 000 [^1]| [inc/s²] Požadovaná akcelerace.                                                                                           |
| 5    | PG           | Dec        | 5 000 000 [^1]| [inc/s²] Požadované zpomalení.                                                                                            |
| 6    | PG           | PosSpeed   | 1 000 000 [^1]| [inc/s] Požadovaná rychlost pohybu v pozičním režimu.                                                                     |
| 7    | PG           | Mode       | 1        | Poziční režim.                                                                                                            |
| 8    | PG           | Type       | 1        | Požadovaný typ rampy. Viz Obrázek 1.                                                                                      |
| 9    | PG           | DPosAngle  | 0        | [inc] Požadovaná poloha v rozsahu jedné otáčky. Po zadání hodnoty a stisknutí klávesy Enter se motor otočí do požadované polohy.|
| 10   | PG           | DPosRevol  | 20 [^1]       | [inc] Požadovaná poloha v rozsahu víceotáčkového pohybu. Po zadání hodnoty a stisknutí klávesy Enter se motor otočí do požadované polohy.|

[^1]: Uvedené hodnoty jsou pouze orientační. Lze je libovolně měnit.

###Řízení polohy motoru (UDP)

**D-mode**   
Popis: Nastavení módu servozesilovače: Profil Generátor – polohový režim.

<table>
    <tr>
        <td colspan="7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram: Požadavek&quot;}"><b>Telegram: Požadavek</b></td>
        <td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
    </tr>
    <tr>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
    </tr>
    <tr>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
        <td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
        <td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
    </tr>
    <tr>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
    </tr>
    <tr>
        <td colspan="7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram: Odpověď&quot;}"><b>Telegram: Odpověď</b></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
    </tr>
    <tr>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
        <td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
        <td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : žádný Error)&quot;}">(Byte 6, 10 = 0 : žádný Error)</td>
    </tr>
    <tr>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
        <td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
        <td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
        <td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
        <td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
        <td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
    </tr>
</table>

**PG – Acc, Dec, PosSpeed, Type, Mode, DPosAngle, DPosRevol**   
Popis: Nastavení požadovaného zrychlení, zpomalení, žádané rychlosti (do najetí do nulové polohy), typu rampy (viz Obrázek 1Obrázek 1), módu Profil Generátoru a nulové požadované hodnoty polohy (počáteční stav).

<table>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 25&quot;}" style="color:white;"><b>Byte 25</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 26&quot;}" style="color:white;"><b>Byte 26</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x42&quot;}">0x42</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0F&quot;}">0x0F</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="3" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 27&quot;}" style="color:white;"><b>Byte 27</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 28&quot;}" style="color:white;"><b>Byte 28</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 29&quot;}" style="color:white;"><b>Byte 29</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 30&quot;}" style="color:white;"><b>Byte 30</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 31&quot;}" style="color:white;"><b>Byte 31</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 32&quot;}" style="color:white;"><b>Byte 32</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 33&quot;}" style="color:white;"><b>Byte 33</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 34&quot;}" style="color:white;"><b>Byte 34</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 35&quot;}" style="color:white;"><b>Byte 35</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="2" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 36&quot;}" style="color:white;"><b>Byte 36</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 37&quot;}" style="color:white;"><b>Byte 37</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 38&quot;}" style="color:white;"><b>Byte 38</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 39&quot;}" style="color:white;"><b>Byte 39</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 40&quot;}" style="color:white;"><b>Byte 40</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 41&quot;}" style="color:white;"><b>Byte 41</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 42&quot;}" style="color:white;"><b>Byte 42</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 43&quot;}" style="color:white;"><b>Byte 43</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 44&quot;}" style="color:white;"><b>Byte 44</b></td>
	</tr>
	<tr>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="2" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 45&quot;}" style="color:white;"><b>Byte 45</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 46&quot;}" style="color:white;"><b>Byte 46</b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="10" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : no Error)&quot;}">(Byte 6, 10 = 0 : no Error)</td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="3" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="4" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="4" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td colspan="4" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td colspan="2" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td colspan="4" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="3" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**K – Command**   
Popis: SW enable.
Po zadání tohoto příkazu je motor pod momentem a provede natočení do požadované polohy z předchozího požadavku.

<table>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="3" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td colspan="2" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : no Error)&quot;}">(Byte 6, 10 = 0 : no Error)</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td colspan="3" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td colspan="2" bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td colspan="2" bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td colspan="2" bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td colspan="3" bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td colspan="2" bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td colspan="2" bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

###Řízení rychlosti motoru (TGZ GUI)

| Krok | Základní skupina | Parametr   | Hodnota  | Popis                                                                                     |
|------|--------------|------------|----------|------------------------------------------------------------------------------------------------|
| 1    | -            | -          | -        | Načíst parametry pohonu.                                                                        |
| 2    | Drive        | D-mode     | 7        | Generátor profilů - režim polohy.                                                              |
| 3    | Command      | K-Command  | 1        | SW povolení. Lze jej také zapnout pomocí aktivačního tlačítka na spodní liště. Motor generuje točivý moment. |
| 4    | PG           | Acc        | 5 000 000 [^1]| [inc /s²] Požadovaná akcelerace.                                                                |
| 5    | PG           | Dec        | 5 000 000[^1]| [inc /s²] Požadovaná dekcelerace.                                                               |
| 6    | PG           | Mode       | 0        | Rychlostní režim.                                                                              |
| 7    | PG           | Type       | 1        | Požadovaný typ rampy. Viz Obrázek 1.                                                            |
| 8    | PG           | PosSpeed   | ±1 000 000 [^1]| [inc /s] Požadovaná rychlost pohybu v pozičním režimu. Po zadání hodnoty a stisknutí klávesy Enter se motor bude točit požadovanou rychlostí. |

[^1]: Uvedené hodnoty jsou pouze orientační. Lze je libovolně měnit.

###Řízení rychlosti motoru (UDP)
**D-Mode**   
Popis: Nastavení módu servozesilovače: Profil Generátor – polohový režim.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : žádný Error)&quot;}">(Byte 6, 10 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – Acc, Dec, PosSpeed, Type, Mode**   
Popis: Nastavení požadovaného zrychlení, zpomalení, rychlosti, typu ramp (viz obr) a módu Profil Generátoru.
Znaménko u rychlosti `PosSpeed` rozhoduje o směru otáčení motoru.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x08&quot;}">0x08</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 25&quot;}" style="color:white;"><b>Byte 25</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 26&quot;}" style="color:white;"><b>Byte 26</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x42&quot;}">0x42</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0F&quot;}">0x0F</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 27&quot;}" style="color:white;"><b>Byte 27</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 28&quot;}" style="color:white;"><b>Byte 28</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 29&quot;}" style="color:white;"><b>Byte 29</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 30&quot;}" style="color:white;"><b>Byte 30</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 31&quot;}" style="color:white;"><b>Byte 31</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 32&quot;}" style="color:white;"><b>Byte 32</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 33&quot;}" style="color:white;"><b>Byte 33</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 34&quot;}" style="color:white;"><b>Byte 34</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5= 0 : žádný Error)&quot;}">(Byte 5= 0 : žádný Error)</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x08&quot;}">0x08</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**K – Command**   
Popis: SW enable.
Po zadání tohoto příkazu je motor pod momentem a zahájí otáčení v požadovaném směru s požadovanou rychlostí.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : žádný Error)&quot;}">(Byte 5 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

###SW limity při rychlostním řízení (TGZ GUI)
| Krok | Základní skupina | Parametr | Hodnota | Popis |
|---|---|---|---|---|
| 1 | - | - | - | Načíst parametry pohonu. |
| 2 | Drive | D-mode | 7 | Generátor profilů -režim polohy. |
| 3 | Command | K-Command | 1 | SW povolení. Lze jej také zapnout pomocí aktivačního tlačítka na spodní liště. **Motor generuje točivý moment.** |
| 4 | PG | Acc | 5000000 [^1] | [inc /s<sup>2</sup>]Požadovaná akcelerace. |
| 5 | PG | Dec | 5000000 [^1] | [inc /s<sup>2</sup>]Požadované zpomalení. |
| 6 | PG | PosSpeed | 1000 000 [^1] | [inc /s] Požadovaná rychlost pohybu vpozičním režimu. |
| 7 | PG | Mode | 1 | Poziční režim. |
| 8 | PG | Type | 1 | [Požadovaný typ rampy](#Ramptype)  |
| 9 | PG | DPosAngle | 0 | [inc]Požadovaná poloha v rozsahu jedné otáčky. Po zadání hodnoty astisknutí klávesy Enter se **motor otočí do požadovaného úhlu**. |
| 10 | PG | DPosRevol | 0 | [inc]Požadovaná poloha v rozsahu víceotáčkového pohybu. Pozadání hodnoty a stisknutí klávesy Enter se **motor otočí do polohy 0**. Počkejte, až se motor otočí. |
| 11 | PG | PosSpeed | 0 | [inc /s] Požadovaná rychlost pohybu vpozičním režimu. |
| 12 | PG | Mode | 0 | Rychlostní režim. |
| 13 | PG | PosLimitAnglePosit | 0 [^1] | Limit kladné polohy v rámci jedné otáčky vrozsahu od -2<sup>16</sup>do 2<sup>16</sup> |
| 14 | PG | PosLimitRevolPosit | 20 [^1] | [± počet otáček] Horní mez polohy v rámci otáček v rozsahu od -2<sup>16</sup>do 2<sup>16</sup> |
| 15 | PG | PosLimitAngleNegat | 0 [^1] | Limit záporné polohy v rámci jedné otáčky v rozsahu od -2<sup>16</sup>do 2<sup>16</sup> |
| 16 | PG | PosLimitRevolNegat | -20 [^1] | [± počet otáček] Dolní mez polohy v rámci otáček v rozsahu od -2<sup>16</sup>do 2<sup>16</sup> |
| 17 | PG | PosSpeed | ± 5000 000 [^1] | [inc /s] Po zadání hodnoty **se motor bude otáčet** rychlostí `PosSpeed` do polohy `PosLimitRevolPosit` nebo `PosLimitRevolNegat`. Směr otáčení je dán znaménkem parametru `PosSpeed`. |

###SW limity při rychlostním řízení (UDP)
**D-Mode**   
Popis: Nastavení módu servozesilovače: Profil Generátor – rychlostní režim.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10 = 0 : žádný Error)&quot;}">(Byte 6, 10 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#BFBFBF" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x03&quot;}">0x03</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – Acc, Dec, PosSpeed, Type, Mode, DPosAngle, DPosRevol**   
Popis: Nastavení požadovaného zrychlení, zpomalení, rychlosti a typu ramp Profil Generátoru.
V posledním kroku je zadána nulová požadovaná poloha (výchozí stav).

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A&quot;}">0x1A</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 25&quot;}" style="color:white;"><b>Byte 25</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 26&quot;}" style="color:white;"><b>Byte 26</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D0A2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F0B08F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 27&quot;}" style="color:white;"><b>Byte 27</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 28&quot;}" style="color:white;"><b>Byte 28</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 29&quot;}" style="color:white;"><b>Byte 29</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 30&quot;}" style="color:white;"><b>Byte 30</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 31&quot;}" style="color:white;"><b>Byte 31</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 32&quot;}" style="color:white;"><b>Byte 32</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 33&quot;}" style="color:white;"><b>Byte 33</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 34&quot;}" style="color:white;"><b>Byte 34</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 35&quot;}" style="color:white;"><b>Byte 35</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 36&quot;}" style="color:white;"><b>Byte 36</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 37&quot;}" style="color:white;"><b>Byte 37</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 38&quot;}" style="color:white;"><b>Byte 38</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 39&quot;}" style="color:white;"><b>Byte 39</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 40&quot;}" style="color:white;"><b>Byte 40</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 41&quot;}" style="color:white;"><b>Byte 41</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 42&quot;}" style="color:white;"><b>Byte 42</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 43&quot;}" style="color:white;"><b>Byte 43</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 44&quot;}" style="color:white;"><b>Byte 44</b></td>
	</tr>
	<tr>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 45&quot;}" style="color:white;"><b>Byte 45</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 46&quot;}" style="color:white;"><b>Byte 46</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 6, 10, 14, 18, 22 = 0 : no Error)&quot;}">(Byte 6, 10, 14, 18, 22 = 0 : no Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**K – Command**   
Popis: SW enable.
Po zadání tohoto příkazu je motor pod momentem a otočí se do požadované polohy (tj. do polohy 0).
Je nutné vyčkat než se motor dotočí.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram&quot;}"><b>Telegram</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram&quot;}"><b>Telegram</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : žádný Error)&quot;}">(Byte 5 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – PosSpeed**   
Popis: Nastavení požadovanou rychlost na nulovou hodnotu.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegramm&quot;}"><b>Telegramm</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : žádný Error)&quot;}">(Byte 5 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x07&quot;}">0x07</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – Mode**   
Popis: Nastavení Profil Generátoru do rychlostního režimu.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : žádný Error)&quot;}">(Byte 5 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x09&quot;}">0x09</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – PosLimitAnglePosit, PosLimitRevolPosit, PosLimitAngleNegat, PosLimitRevolNegat**   
Popis: Nastavení pozičních limitů v rámci jedné otáčky a v rámci více otáček.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b></b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}" style="color:white;"><b>Byte 12</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}" style="color:white;"><b>Byte 13</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}" style="color:white;"><b>Byte 14</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}" style="color:white;"><b>Byte 15</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 16&quot;}" style="color:white;"><b>Byte 16</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 17&quot;}" style="color:white;"><b>Byte 17</b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x40&quot;}">0x40</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4B&quot;}">0x4B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x4C&quot;}">0x4C</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A&quot;}">0x1A</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 18&quot;}" style="color:white;"><b>Byte 18</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 19&quot;}" style="color:white;"><b>Byte 19</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 20&quot;}" style="color:white;"><b>Byte 20</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 21&quot;}" style="color:white;"><b>Byte 21</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 22&quot;}" style="color:white;"><b>Byte 22</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 23&quot;}" style="color:white;"><b>Byte 23</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 24&quot;}" style="color:white;"><b>Byte 24</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x42&quot;}">0x42</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0F&quot;}">0x0F</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x0B&quot;}">0x0B</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5,10 = 0 : žádný Error)&quot;}">(Byte 5,10 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x19&quot;}">0x19</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}"><b>0x04</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x1A&quot;}">0x1A</td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}" style="color:white;"><b>Byte 9</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}" style="color:white;"><b>Byte 10</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}" style="color:white;"><b>Byte 11</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x04&quot;}">0x04</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}">0x02</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**PG – PosSpeed**   
Popis: SW enable.
Po zadání tohoto příkazu je motor pod momentem a provede natočení do požadované polohy z předchozího požadavku.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadavek&quot;}"><b>Požadavek</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}" style="color:white;"><b>Byte 6</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}" style="color:white;"><b>Byte 7</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}" style="color:white;"><b>Byte 8</b></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x01&quot;}">0x01</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Telegram:&quot;}"><b>Telegram:</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpověď&quot;}"><b>Odpověď</b></td>
		<td colspan="4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;(Byte 5 = 0 : žádný Error)&quot;}">(Byte 5 = 0 : žádný Error)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}" style="color:white;"><b>Byte 0</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}" style="color:white;"><b>Byte 1</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}" style="color:white;"><b>Byte 2</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}" style="color:white;"><b>Byte 3</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}" style="color:white;"><b>Byte 4</b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}" style="color:white;"><b>Byte 5</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x47&quot;}"><b>0x47</b></td>
		<td bgcolor="#A6A6A6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x54&quot;}"><b>0x54</b></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x02&quot;}"><b>0x02</b></td>
		<td bgcolor="#A9D08E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x11&quot;}">0x11</td>
		<td bgcolor="#F4B084" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x00&quot;}">0x00</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

##Rozšířený popis parametrů Generátoru profilů

| Název parametru | Popis |
|---|---|
| Acc | Požadované zrychlení pohonu |
| Dec | Požadované zpomalení pohonu |
| APosAngle | Aktuální pozice pohonu v rámci jedné otáčky |
| APosRevol | Aktuální pozice pohonu v rámci počtu otáček |
| DPosAngle | Požadovaná pozice pohonu v rámci jedné otáčky |
| DPosRevol | Požadovaná pozice pohonu v rámci počtu otáček |
| ASpeed | Aktuální rychlost pohonu |
| PosSpeed | Požadovaná rychlost pohybu v polohovém módu |
| Speed | Požadovaná rychlost pohybu v rychlostním módu |
| Mode | Mód profil generátoru. 0 = rychlostní, 1 = poziční, 2 (onlyread) = signalizace zpomalovací rampy v pozičním módu |
| Rdy | Signalizace dokončení pohybu pohonu. 1 = Poloha byla dosažena |
| Type | Typ profilu rychlosti 0 = harmonické nesymetrické, 1 = harmonické symetrické, 2 = plně harmonické, 3 = lichoběžníkové |
| BitsPerRevol | Počet bitů na otáčku pro profil generátorů |
| RotaryMode | Speciální režim polohování v rámci jedné otáčky s přejezdem kratší cestou - využití pro přímé motory. 1 = Rotary mód, 0 = standardní mód |
| PosOffsetAngle | Poziční offset v rámci jedné otáčky |
| PosOffsetRevol | Poziční offset v rámci počtu otáček |
| PosLimitAnglePosit | Kladný poziční limit v rámci jedné otáčky v rozsahu od -2<sup>16</sup> do 2<sup>16</sup> |
| PosLimitRevolPosit | Kladný poziční limit v rámci počtu otáček v rozsahu od -2<sup>16</sup> do 2<sup>16</sup> |
| PosLimitAngleNegat | Záporný poziční limit v rámci jedné otáčky v rozsahu od -2<sup>16</sup> do 2<sup>16</sup> |
| PosLimitRevolNegat | Záporný poziční limit v rámci počtu otáček v rozsahu od -2<sup>16</sup> do 2<sup>16</sup> |
| DPosAngleRotary | V režimu „RotaryMode = 1“ tento parametr určuje požadovanou polohu v rámci jedné otáčky |
| AccMaxCurrentFeedForward | Proudová předkorekce |