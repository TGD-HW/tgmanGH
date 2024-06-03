##Základní popis
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

<img src="../../../../../source/common/img/TGZrampType1.webp" alt="TGZ servo ramp type" style="width:70%;"> {#Ramptype}

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
	Nahrávání parametrů je umožněno pomocí modré obálky v pravém horním rohu (*LOAD PARAMETERS FROM FILE*), viz. [Návod k TGZ GUI](../../../TGZ/TGZ_SW/GUI/md/intro.md##GUIstart)
	
###Řízení polohy motoru (TGZ GUI)
| Krok | Základní skupina | Parametr   | Hodnota*   | Popis                                                                                                              |
|------|--------------|------------|----------|--------------------------------------------------------------------------------------------------------------------------|
| 1    | -            | -          | -        | Načíst parametry pohonu.                                                                                                  |
| 2    | Drive        | D-mode     | 7        | Generátor profilů - režim polohy.                                                                                        |
| 3    | Command      | K-Command  | 1        | SW enable. Lze jej také zapnout pomocí tlačítka enable pro příslušnou osu na spodní liště. Motor generuje točivý moment.  |
| 4    | PG           | Acc        | 5 000 000| [inc/s²] Požadovaná akcelerace.                                                                                           |
| 5    | PG           | Dec        | 5 000 000| [inc/s²] Požadované zpomalení.                                                                                            |
| 6    | PG           | PosSpeed   | 1 000 000| [inc/s] Požadovaná rychlost pohybu v pozičním režimu.                                                                     |
| 7    | PG           | Mode       | 1        | Poziční režim.                                                                                                            |
| 8    | PG           | Type       | 1        | Požadovaný typ rampy. Viz Obrázek 1.                                                                                      |
| 9    | PG           | DPosAngle  | 0        | [inc] Požadovaná poloha v rozsahu jedné otáčky. Po zadání hodnoty a stisknutí klávesy Enter se motor otočí do požadované polohy.|
| 10   | PG           | DPosRevol  | 20       | [inc] Požadovaná poloha v rozsahu víceotáčkového pohybu. Po zadání hodnoty a stisknutí klávesy Enter se motor otočí do požadované polohy.|

