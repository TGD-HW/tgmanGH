##Technická specifikace
Servozesilovač TGZ používá PROFIdrive podle uvedené technické specifikace: 

- Třída použití 1 (*Standard Drive* - regulátor otáček)
- Třída použití 3 (jednoosý polohovací pohon s lokálním *Motion Control* - regulátor polohy).

Pro ovládání TGZ je k dispozici několik telegramů PROFIdrive pro použití s PLC:

- Standardní telegram 1 - rozhraní n-údajů, 16 bitů
- Standardní telegram 3 - rozhraní n-údajů, 32 bitů, s jedním senzorem
- Standardní telegram 7 - polohovací rozhraní
- Standardní telegram 9 - polohovací rozhraní plus podrežim MDI
- Telegram 111 - SinaPos basic positioner
- Telegram 352 - rozšířený telegram 1 s dalšími stavovými informacemi

Podrobný popis telegramů naleznete v příslušné dokumentaci.   

Podle specifikace PROFINET podporuje servopohon TGZ třídu shody A.
Parametry PROFIdrive lze číst a zapisovat přes síť PROFINET, stejně jako cyklická data.
Synchronizace mezi zařízeními se provádí pouze prostřednictvím PLC v rámci doby cyklu dat RT.
U dvouosé varianty servopohonu je možná i přesná synchronizace (elektronický převod) uvnitř jednoho TGZ.

##Doba cyklu dat RT
Nejrychlejší doba cyklu TGZ pro data PROFINET RT je 1 ms (firmware od srpna 2022 nebo novější).
Maximální jitter je 250 µs.

##Servo typu TGZ-S-48-xxx
Tato verze má zvláštní zacházení s firmwarem: vzhledem k podobnosti s verzí TGZ-D musí být naprogramována firmwarem určeným pro variantu TGZ-D.
Proto je nutné použít také soubor `GSDML` s názvem `GSDML-V2.4-TGDrives-TGZ-D-xxxxxxxx.xml`, tj. soubor pro dvouosou variantu.
Při uvádění pohonu do provozu lze použít pouze první osu.
Druhá osa zůstává vždy v chybovém stavu.
