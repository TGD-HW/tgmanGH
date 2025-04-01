## Režimy homing (reference)

Pohon musí být v provozním stavu s nastaveným polohovacím režimem (telegramy `7`, `9` nebo `111`). Nesmí být aktivní žádná polohová úloha (task)  pohon musí být v klidovém stavu. Režim se vybírá parametrem `Homing_Mode` v aplikaci TGZ_GUI. K zahájení homing procedury nastavte v řídicím slovu `STW1` bit `11` na hodnotu 1. Během běhu homing procedury jsou bity `10, 11 a 13` ve stavovém slovu `ZSW1` vynulovány. Po úspěšném dokončení homingu přejdou bity `10, 11 a 13` na hodnotu 1. V případě chyby během homingu se nastaví pouze bit `13`. Proceduru homing lze přerušit nastavením `STW1 bit 11` na 0. Pro dokončení úspěšného homingu je rovněž nutné nastavit `STW1 bit 11` zpět na 0. Teprve poté se pohon vrátí do základního provozního stavu.

### Dostupné režimy:

| Číslo režimu | Popis režimu |
|-------------|-------------|
| 0   | Nastavení nulové polohy na aktuální pozici. Používá aktuální pozici jako referenční bod pro home. |
| 1   | Nalezení koncového spínače. Pohyb se spustí kladným nebo záporným směrem, dokud není detekován koncový spínač. Poté se provede reverzní pohyb, dokud koncový spínač nepřestane být aktivní. Aktuální pozice se nastaví jako home. Parametry `Homing_NegLimSwitchMask` a `Homing_PosLimitSwitchMask` určují digitální vstup odpovídající koncovému spínači. Směr homingu určuje znaménko parametru `Homing_Velocity_Direction`. |
| 2   | Nalezení koncového spínače, poté nulový úhel. Podobné jako režim 1, ale po nastavení home polohy se motor přesune na nulový úhel zpětné vazby. |
| 4   | Nalezení homing spínače. Podobné jako režim 1, ale jako vstup se používá homing spínač (`Homing_ReferenceSwitchMask`). Počáteční směr určuje znaménko parametru `Homing_Velocity_Direction`. Algoritmus rovněž zohledňuje kladný a záporný koncový spínač. |
| 5   | Nalezení homing spínače, poté nulový úhel. Podobné jako režim 4, ale po nastavení home polohy se motor přesune na nulový úhel zpětné vazby. |
| 8   | Pohyb k mechanickému dorazu. Pohon se pohybuje, dokud nenarazí na pevnou mechanickou překážku, což způsobí překročení polohové chyby. Poté se pohyb zastaví a home poloha se nastaví. |
| 9   | Pohyb k mechanickému dorazu, poté nulový úhel. Podobné jako režim 8, ale po nastavení home polohy se motor přesune na nulový úhel zpětné vazby. |

## Polohové úlohy (Tasks)

Zesilovač TGZ umožňuje používat až deset úloh v režimu polohování.
Čísla úloh se nastavují signálem `SATZANW` v telegramu `7, 9 nebo 111`.
Parametry úlohy lze nastavit pomocí rozhraní TGZ_GUI.
Cílová poloha je vždy 64bitová (v jednotkách TGZ), aby byla umožněna plná přesnost hodnoty.
Režim úlohy je buď 0 - relativní polohování, nebo 1 - absolutní cílová hodnota.
Pro neplatné číslo úlohy se neprovede žádná akce.
Platné hodnoty jsou 0 - 9 `(PD_Task1 - PD_Task10`).
Podrobný popis úlohy a přímého režimu **Manual data input (MDI)** naleznete v dokumentaci k **PROFIdrive Profile** .
Popis registrů TGZ pro polohové úlohy naleznete v [popisu registrů](#registry-pro-polohové-úlohy-pd_task).

## Jog

Funkce jog je podporována jak v polohovém (telegramy `7, 9, 111`), tak v rychlostním režimu (telegramy `1, 3, 352`).
Všechny parametry funkce jog lze nastavit pomocí aplikace TGZ_GUI.
Pomocí řídicího slova `STW1 bitů 8 a 9` jsou k dispozici dvě nastavené hodnoty jog.
Pokud jsou nastaveny oba bity, pohon se buď zastaví v režimu rychlosti, nebo v režimu polohování nedělá nic.

Pohon pracuje v rychlostním režimu, když je jog aktivní, tj. pohybuje osou požadovanou rychlostí jog nekonečně dlouho, dokud se nezastaví.

Funkce je implementována podle standardu popsaného v dokumentaci PROFIdrive Profile.

## Chybový buffer

TGZ využívá standardní mechanismus chybového bufferu PROFIdrive. Protože standardní položka v chybovém bufferu má šířku 16 bitů, ale TGZ používá 32bitová chybová čísla, každá chybová situace zabírá dvě po sobě jdoucí položky v bufferu (PNU 947). Buffer může uložit až osm chybových situací, což tvoří pole o 16 položkách (každá položka je 2 bajty dlouhá).  
K přečtení chybové situace se používá index parametru. Jelikož každá chyba zabírá dva 16bitové hodnoty, jsou nutná dvě čtení:

- Sudý index → Dolních 16 bitů chyby  
- Lichý index → Horních 16 bitů chyby  

Typicky se k získání nejnovější chyby používají indexy 0 a 1.  

### Čtení chyb

PROFIdrive podporuje vícenásobné čtení registrů, což umožňuje efektivní načítání chyb. Funkční blok SinaPara lze použít následujícím způsobem:

- Nastavte `sxParameter[0].siParaNo = 947` a `sxParameter[1].siParaNo = 947`  
(PNU číslo).  
- Nastavte `sxParameter[0].siIndex = 0` a `sxParameter[1].siIndex = 1`.  
- Nastavte `ParaNo = 2` (pro čtení dvou parametrů).  
- TGZ automaticky nastaví formát čtení na `16#42` (42h znamená 16bitovou hodnotu).  

Alternativně lze pro jednodušší implementaci použít funkční blok SinaParaS.  

### Počitadla chyb  

- **PNU 944 (Čítač chybových hlášení)**: Zvyšuje se o 2 při každé nové chybové situaci.  
- **PNU 952 (Čítač chybových situací)**: Zvyšuje se o 1 při každé nové chybě.  

### Potvrzování chyb  

Když je chyba potvrzena prostřednictvím bitu 7 v řídicím slovu, chybový buffer se posune dolů a nejnovější chyba je odstraněna.  
Chybový buffer lze zcela vymazat zapsáním nuly do parametru **PNU 952**.  
Podrobnosti naleznete v PROFIdrive Profile Manual.  

## Chybové kódy

V případě jakékoli chyby pohonu se chybový kód zkopíruje do vyrovnávací paměti chyb.
Používá se standardní mechanismus vyrovnávací paměti chyb PROFIdrive.
Protože standardní chybový kód PROFIdrive má šířku pouze 16 bitů a TGZ používá 32bitové chyby, existují vždy dvě chybové zprávy obsahující celé 32bitové chybové slovo.
Proto je parametr `947` organizován s 8 chybovými situacemi se 2 chybovými zprávami.
Zpráva s indexem `0` obsahuje dolních 16 bitů chybového kódu a zpráva s indexem `1` horních 16 bitů.
Vyrovnávací paměť poruch lze zcela vymazat zápisem nuly do parametru `952`.

Telegram `111` obsahuje prostor pro poslední aktivní chybový kód, přičemž pole `WARN code (PZD11)` obsahuje dolních 16 bitů a pole `FAULT code (PZD10)` obsahuje horních 16 bitů chybového kódu TGZ.
Podobně má telegram `352` pole pro `WARN (PZD5) a FAULT (PZD6)`. Jsou kódovány stejným způsobem.
Chybové kódy TGZ jsou bitově orientované, tj. je možných až 32 chyb, a jsou kumulativní, tj. může být nastaveno několik bitů současně.

| Bit | Popis chyby |
|-----|------------|
| 2  | rezervováno (interní chyba) |
| 3  | Přepětí na DC sběrnici |
| 4  | Podpětí na DC sběrnici |
| 5  | Diagnostika STO |
| 6  | Chyba zadržovací brzdy |
| 9  | Teplota motoru |
| 11 | Teplota pohonu |
| 12 | Zpětná vazba |
| 14 | Překročená rychlost |
| 15 | Polohová chyba (konturování) |
| 17 | Průmyslová sběrnice (ztráta komunikace) |
| 19 | Chyba regulátoru proudu |
| 20 | Nouzové zastavení |
| 21 | Saturace budiče |
| 22 | Regenerativní výkon |
| 27 | Neplatný parametr |

## Vztah mezi souřadnicemi TGZ a hodnotami PROFIdrive

Jednotka TGZ používá pro polohu 64bitové hodnoty.
Tato hodnota se skládá z počtu otáček v horních 32 bitech a počtu přírůstků v rámci jedné otáčky.
Naproti tomu standard PROFIdrive používá pro polohu pouze 32bitové hodnoty.
Z tohoto důvodu je nutný určitý druh škálování.
Hledaná hodnota polohy z telegramu PROFIdrive je rozšířena na 64 bitů a poté posunuta doleva o 32 minus počet bitů uvedený v nastavení TGZ - hodnota `BitsPerRevol` generátoru profilu (PG).
Pokud je například `BitsPerRevol=20`, pak je hodnota z PROFIdrive posunuta doleva o 12 bitů.
Posunutí má stejný účinek jako vynásobení hodnoty 212 (tj. 4096).
Podobné snížení se provádí při odesílání aktuální hodnoty polohy z TGZ do řídicí jednotky PROFIdrive: 64bitová poloha TGZ se posune doprava o 32 - `BitsPerRevol` (což je stejná operace jako dělení 2(32-B itsPerRevol) ) a výsledných dolních 32 bitů se odešle v telegramu PROFIdrive.   

Hodnoty rychlosti nejsou vůbec škálovány, protože telegramy TGZ i PROFIdrive používají 32bitové hodnoty.
Význam rychlosti je proto stejný jako význam rychlosti pro profil generátor.  

Akcelerace a decelerace musí být nastaveny přímo v TGZ servisním programem TGZ_GUI v sekci PROFIdrive a můžou být změněny telegramy PROFIdrive pouze pomocí přepisovacích (procentuálních) hodnot obsažených v příslušných telegramech.

## Kompenzace vůle

Firmware ze srpna 2023 nebo novější implementuje kompenzaci vůle.
Pro hodnotu vůle se používá standardní parametr `PNU 2583`.
Je uložen jako celočíselná 32bitová hodnota se znaménkem a má stejný fyzikální význam jako požadovaná nebo skutečná poloha v telegramu `9` nebo `111`.

Chcete-li použít kompenzaci vůle, je třeba nejprve provést úspěšnou [referenci](#režimy-homing-reference) (homing).

**Kladný** směr pohybu se provádí při inkrementaci skutečné polohy.
Stejně tak je definován **záporný** směr pohybu, když je pozice dekrementována.

Samotná kompenzace závisí na znaménku vůle:

- Kladná hodnota vůle: pokud je požadovaná poloha v kladném směru, je k hodnotě přičtena hodnota vůle.
  Naopak při záporném pohybu se k požadované poloze nepřičítá žádná hodnota.
- Záporná hodnota vůle: při záporném pohybu se vůle odečítá od požadované polohy, takže výsledek je zápornější.
  Při kladném směru se ke konečné požadované poloze nepřičítá žádná hodnota.
  
Použití kladné nebo záporné vůle závisí na zvoleném postupu polohování a jeho konečném pohybu.
Pokud polohování končí záporným pohybem, použijte kladnou vůli, protože vůle je již nastavena na levou stranu.
Stejně tak zvolte zápornou hodnotu vůle, pokud poslední naváděcí pohyb probíhá v kladném směru.

Hodnotu vůle lze nastavit pouze pomocí parametru `PNU 2583` v PLC, v oblasti registru TGZ není žádný ekvivalent.

Pro nastavení `PNU 2583` lze v portálu TIA použít programový blok s názvem **SinParaS**.

![Profinet img](../../../../source/img/profinet10.webp){: style="width:50%;" }

Vstup `hardwareId je` nastaven na stejnou hodnotu jako vstup `HWIDSTW` bloku SinaPos, tj. identifikátor telegramu TGZ.
AxisNo může být 0 pro první osu nebo 1 pro druhou osu.
Protože je vůle typu DINT (celé číslo se znaménkem 32bit), musí být požadovaná hodnota vůle zapsána na vstup `ValueWrite2`.
Zápis se provede přepnutím Start z False na True.

## Režim regulace otáček a normalizované hodnoty

Telegramy `1, 3 a 352` se používají pro režim regulace otáček.
Tyto telegramy používají normalizované hodnoty otáček ve formátu N2 nebo N4 (kapitola 6.3.4.5 příručky PROFIdrive).
Požadované a skutečné otáčky jsou vyjádřeny v procentech referenční hodnoty.
Servozesilovač TGZ k tomuto účelu používá registr jmenovitých otáček s názvem `M-Nn` - ten musí být nenulový, jinak by režim regulace otáček nefungoval.
Normalizované hodnoty N2 nebo N4 v telegramu jsou v rozsahu od -200 % do 200 % referenční hodnoty `M-Nn`.
Registr `M-Nn` lze číst pomocí standardního parametru `PNU 60 000` **Velocity reference value**.
Kompletní přístup (čtení/zápis) je možný přímým přístupem k parametrům TGZ, čísla registrů jsou `0x211B` pro osu 1 a `0x221B` pro osu 2.
Viz. také Registry TGZ.

!!! note "Poznámka"
	Všimněte si, že `PNU 60 000` se čte jako desetinné číslo (FLOAT32), zatímco přímý [přístup](#registry-tgz) k registrům TGZ je vždy 32bitovým celým číslem.

Interní generátor rychlostního profilu používá při změně rychlosti jako hodnotu zrychlení registr `PD_Dec (0x355F / 0x365F)`.

## Parametry pohonu PROFIdrive

Servopohon TGZ podporuje přístup k parametrům prostřednictvím slotů 1 a 2 (slot 2 pouze pro variantu se dvěma osami).
Pro přístup k parametrům TGZ lze použít tři indexy datových objektů záznamu:

- `47` - údaje ze starších záznamů. Osa je uvedena přímo v záhlaví požadavku.
- `0xB02E` - přístup k lokálním základním parametrům. Osa je určena slotem, který provádí přístup.
- `0xB02F` - přístup ke globálním základním parametrům. Osa je uvedena přímo v hlavičce požadavku.

## Podporované standardní jednotky PROFIdrive PNU

Servopohon TGZ podporuje následující standardní a povinné parametry PROFIdrive (PNU):

| Číslo | Popis | Datový typ |
|-------|-------|------------|
| 922   | Výběr telegramu | Unsigned16 |
| 930   | Provozní režim | Unsigned16 |
| 944   | Počítadlo chybových zpráv | Unsigned16 |
| 947   | Číslo chyby | Pole Unsigned16 |
| 964   | Identifikace jednotky | Struktura |
| 965   | Identifikace režimu | Struktura |
| 975   | Identifikace objektu jednotky | Struktura |

!!! info "Info"
	Popis standardních parametrů PROFIdrive naleznete v dokumentaci PROFIdrive. PNU 922, 930, 944 a 947 jsou pro každou osu jedinečné.
	
## Referenční hodnoty PNU

| Číslo | Popis                  | Datový typ | Název registru TGZ  | Registrační číslo TGZ |
|-------|------------------------|------------|---------------------|-----------------------|
| 2000  | Referenční rychlost    | Float32    | M-Nn                | 0x2118, 0x2218        |
| 2001  | Referenční napětí      | Float32    | M-Un                | 0x2117, 0x2217        |
| 2002  | Referenční proud       | Float32    | M-In                | 0x211B, 0x221B        |
| 2003  | Referenční točivý moment | Float32  | M-Mn                | 0x2119, 0x2219        |
| 2007  | Referenční zrychlení   | Float32    | PG-PD_Acc           | 0x395E, 0x3A5E        |

Výše uvedené parametry jsou pro každou osu jedinečné.
Použijte příslušný identifikátor osy spolu s indexem datového objektu.

## Další parametry PROFIdrive

| Číslo | Popis                    | Datový typ  |
|-------|--------------------------|-------------|
| 2583  | Kompenzace vůle | Signed32 |

Čísla parametrů od `2010` do `8191` jsou vyhrazena pro budoucí rozšíření firmwaru.
PNU `2583` se používají pro kompenzaci vůle a jsou jedinečné pro každou osu.

## Registry TGZ

Všechny registry TGZ jsou přístupné jako specifické registry PROFIdrive výrobce, počínaje číslem `0x2000` (`16#2000`, tj. `8192 DEC`).
Seznam použitelných registrů lze stáhnout z webových stránek TG Drives.
Všechny parametry TGZ jsou seskupeny dohromady.
Existuje několik skupin - společné, motor, pohon, generátor profilů atd.
Skupiny jsou číslovány od nuly, stejně jako parametry ve skupině.
První dvě hexadecimální čísla tvoří číslo skupiny, `0x2000` je první skupina.
Poslední dvě hexadecimální čísla určují index parametru v rámci skupiny.
Například číslo parametru `0x2119` patří do skupiny 1 (Motor) a jeho index je 25 (`0x19 = 16#19 = 25 DEC`).
Jednoosá varianta TGZ nepoužívá parametry osy 2.
Pro přístup k parametrům prostřednictvím sítě PROFINET je k úplnému určení správného parametru zapotřebí pouze číslo parametru.
Položka osy v hlavičce zprávy **PROFIdrive request** je ignorována.

Všechny registry TGZ jsou vždy 32bitové integer hodnoty.

| Číslo skupiny | Název                       |
|---------------|-----------------------------|
| 0x2000        | Společné                    |
| 0x2100        | Motor, osa 1                |
| 0x2200        | Motor, osa 2                |
| 0x2300        | Drive, osa 1                |
| 0x2400        | Drive, osa 2                |
| 0x2500        | Proudový regulátor, osa 1   |
| 0x2600        | Proudový regulátor, osa 2   |
| 0x2700        | Regulátor rychlosti, osa 1  |
| 0x2800        | Regulátor rychlosti, osa 2  |
| 0x2900        | Regulátor polohy, osa 1     |
| 0x2A00        | Regulátor polohy, osa 2     |
| 0x2B00        | Zpětná vazba, osa 1         |
| 0x2C00        | Zpětná vazba, osa 2         |
| 0x3100        | Command, osa 1               |
| 0x3200        | Command, osa 2               |
| 0x3300        | Monitorování, osa 1         |
| 0x3400        | Monitorování, osa 2         |
| 0x3900        | Profile generator, osa 1    |
| 0x3A00        | Profile generator, osa 2    |

Parametry související s PROFINET jsou přístupné pomocí indexových čísel parametrů TGZ:

| Název parametru TGZ  | Název PROFINET                | Popis                                                           | Číslo pro osu 1 | Číslo pro osu 2 |
|----------------------|-------------------------------|-----------------------------------------------------------------|---------------|---------------|
| PD_TelegramNumber    | Výběr telegramu (PNU922)      |                                                                 | 0x2321        | 0x2421        |
| PD_DisplayInfo       | Zobrazení ladicích zpráv      | Zobrazení ladicích zpráv na výstupu grafického rozhraní TGZ     | 0x2323        | NEUPLATŇUJE SE|
| PD_SetDataCounter    |                                | Počítá cyklické zprávy PROFINET z řadiče I/O                    | 0x2324        | 0x2424        |
| PD_StatusWord_ZSW1   | Stavové slovo 1 (ZSW1)        | Kopie stavového slova PROFIdrive odeslaná do řadiče I/O         | 0x3500        | 0x3600        |
| PD_ControlWord_STW1  | Řídicí slovo 1 (STW1)         |                                                                 | 0x3501        | 0x3601        |
| PD_SATZANW           | SATZANW                       | Výběr bloku procházení                                          | 0x3503        | 0x3603        |
| PD_AKTSATZ           | AKTSATZ                       | Skutečný procházející blok                                      | 0x3504        | 0x3604        |
| PD_State             |                                | Režim stavového diagramu                                        | 0x3505        | 0x3605        |

### Registry pro polohové úlohy (PD_Task)

TGZ podporuje až 10 polohových úloh (task) pro nezávislé použití.
Každá úloha se skládá z režimu, zrychlení, zpomalení, rychlosti a cílové polohy:

### PD_Task1

| Název         | Popis                                | Číslo pro osu 1 | Číslo pro osu 2 |
|---------------|--------------------------------------|---------------|---------------|
| mod           | Režim (0 - relativní, 1 - absolutní) | 0x3922        | 0x3A22        |
| acc           | Zrychlení                            | 0x3923        | 0x3A23        |
| dec           | Zpomalení                            | 0x3924        | 0x3A24        |
| rychlost      | Rychlost                             | 0x3925        | 0x3A25        |
| tarPosAngle   | Cílová poloha - úhel                 | 0x3926        | 0x3A26        |
| tarPosRevol   | Cílová poloha - otáčky               | 0x3927        | 0x3A27        |

- PD_Task2 - Čísla parametrů jsou `0x3928` - `0x392D` pro osu 1 a `0x3A28` - `0x3A2D` pro osu 2.
- PD_Task3 - Čísla parametrů jsou `0x392E` - `0x3933` pro osu 1 a `0x3A2E` - `0x3A33` pro osu 2.
- PD_Task4 - Čísla parametrů jsou `0x3934` - `0x3939` pro osu 1 a `0x3A34` - `0x3A39` pro osu 2.
- PD_Task5 - Čísla parametrů jsou `0x393A` - `0x393F` pro osu 1 a `0x3A3A` - `0x3A3F` pro osu 2.
- PD_Task6 - Čísla parametrů jsou `0x3940` - `0x3945` pro osu 1 a `0x3A40` - `0x3A45` pro osu 2.
- PD_Task7 - Čísla parametrů jsou `0x3946` - `0x394B` pro osu 1 a `0x3A46` - `0x3A4B` pro osu 2.
- PD_Task8 - Čísla parametrů jsou `0x394C` - `0x3951` pro osu 1 a `0x3A4C` - `0x3A51` pro osu 2.
- PD_Task9 - Čísla parametrů jsou `0x3952` - `0x3957` pro osu 1 a `0x3A52` - `0x3A57` pro osu 2.
- PD_Task10 - Čísla parametrů jsou `0x3958` - `0x395D` pro osu 1 a `0x3A58` - `0x3A5D` pro osu 2.
