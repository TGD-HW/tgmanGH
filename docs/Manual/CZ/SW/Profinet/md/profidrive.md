##Parametry pohonu PROFIdrive
Servopohon TGZ podporuje přístup k parametrům prostřednictvím slotů 1 a 2 (slot 2 pouze pro variantu se dvěma osami).
Pro přístup k parametrům TGZ lze použít tři indexy datových objektů záznamu:

- `47` - údaje ze starších záznamů. Osa je uvedena přímo v záhlaví požadavku.
- `0xB02E` - přístup k lokálním základním parametrům. Osa je určena slotem, který provádí přístup.
- `0xB02F` - přístup ke globálním základním parametrům. Osa je uvedena přímo v hlavičce požadavku.

##Podporované standardní jednotky PROFIdrive PNU
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
	
##Referenční hodnoty PNU

| Číslo | Popis                  | Datový typ | Název registru TGZ  | Registrační číslo TGZ |
|-------|------------------------|------------|---------------------|-----------------------|
| 2000  | Referenční rychlost    | Float32    | M-Nn                | 0x2118, 0x2218        |
| 2001  | Referenční napětí      | Float32    | M-Un                | 0x2117, 0x2217        |
| 2002  | Referenční proud       | Float32    | M-In                | 0x211B, 0x221B        |
| 2003  | Referenční točivý moment | Float32  | M-Mn                | 0x2119, 0x2219        |
| 2007  | Referenční zrychlení   | Float32    | PG-PD_Acc           | 0x395E, 0x3A5E        |

Výše uvedené parametry jsou pro každou osu jedinečné.
Použijte příslušný identifikátor osy spolu s indexem datového objektu.

##Další parametry PROFIdrive

| Číslo | Popis                    | Datový typ  |
|-------|--------------------------|-------------|
| 2583  | Kompenzace vůle | Signed32 |

Čísla parametrů od `2010` do `8191` jsou vyhrazena pro budoucí rozšíření firmwaru.
PNU `2583` se používají pro kompenzaci vůle a jsou jedinečné pro každou osu.

##Registry TGZ
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

TGZ podporuje až 10 bloků pro nezávislé použití.
Každý blok se skládá z režimu, zrychlení, zpomalení, rychlosti a cílové polohy:   

PD_Task1

| Název         | Popis                                | Číslo pro osu 1 | Číslo pro osu 2 |
|---------------|--------------------------------------|---------------|---------------|
| mod           | Režim (0 - relativní, 1 - absolutní) | 0x3922        | 0x3A22        |
| acc           | Zrychlení                            | 0x3923        | 0x3A23        |
| dec           | Zpomalení                            | 0x3924        | 0x3A24        |
| rychlost      | Rychlost                             | 0x3925        | 0x3A25        |
| tarPosAngle   | Cílová poloha - úhel                 | 0x3926        | 0x3A26        |
| tarPosRevol   | Cílová poloha - otáčky               | 0x3927        | 0x3A27        |


PD_Task2 - Čísla parametrů jsou `0x3928` - `0x392D` pro osu 1 a `0x3A28` - `0x3A2D` pro osu 2.   
PD_Task3 - Čísla parametrů jsou `0x392E` - `0x3933` pro osu 1 a `0x3A2E` - `0x3A33` pro osu 2.   
PD_Task4 - Čísla parametrů jsou `0x3934` - `0x3939` pro osu 1 a `0x3A34` - `0x3A39` pro osu 2.   
PD_Task5 - Čísla parametrů jsou `0x393A` - `0x393F` pro osu 1 a `0x3A3A` - `0x3A3F` pro osu 2.   
PD_Task6 - Čísla parametrů jsou `0x3940` - `0x3945` pro osu 1 a `0x3A40` - `0x3A45` pro osu 2.   
PD_Task7 - Čísla parametrů jsou `0x3946` - `0x394B` pro osu 1 a `0x3A46` - `0x3A4B` pro osu 2.   
PD_Task8 - Čísla parametrů jsou `0x394C` - `0x3951` pro osu 1 a `0x3A4C` - `0x3A51` pro osu 2.   
PD_Task9 - Čísla parametrů jsou `0x3952` - `0x3957` pro osu 1 a `0x3A52` - `0x3A57` pro osu 2.   
PD_Task10 - Čísla parametrů jsou `0x3958` - `0x395D` pro osu 1 a `0x3A58` - `0x3A5D` pro osu 2.   




