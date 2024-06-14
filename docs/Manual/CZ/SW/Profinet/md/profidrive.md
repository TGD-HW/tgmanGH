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

