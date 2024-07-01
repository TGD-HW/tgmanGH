##Základní popis {#commonDI1-8}
Servozesilovač TGZ má ve standardním provedení (UNI) na konektoru **X8** integrováno osm rychlých izolovaných digitálních vstupů.
Šest z nich (DI1-6) lze u výrobce nakonfigurovat buď pro klasickou funkci digitálního vstupu, nebo jako přímé vstupy pro hallovy sondy.
V obou případech je nutné připojit napájecí napětí na VDDIO proti GNDIO, jelikož jsou vstupy aktivní a vyžadují napájení.
Stačí připojení napájecího napětí na jeden ze dvou napájecích vstupu VDDIO, aby aktivní vstupy fungovaly správně.
Zbývající digitální vstupy č. 7 a č. 8 jsou standardní, pasivní, s nominální vstupní úrovní +24V a nevyžadují připojení VDDIO.
Všechny digitální vstupy 1-8 mají integrovanou ochranu proti přepólování (až do -70 V) a proti přepětí (nad 30 V).

##Parametry DI

--8<-- "CZ/md/X8_commonHW_DI_tab.md"

##Použití s hallovými sondami
Pokud chcete využít přímého připojení hallových sond určených pro komutaci motoru do konektoru **X8** na vstupy `1,3,5` (osa 1) nebo `2,4,6` (osa 2) je potřeba požádat výrobce předem o správně HW uzpůsobenou verzi.
Tato verze se liší jak v hardware, tak ve firmware.
Dbejte na to, aby takto použité hallovy sondy byly **přizpůsobeny pro napájecí napětí až 30V**, jelikož digitální vstupy servozesilovače TGZ pracují na nominální hladině **24V**.
Použití hallových sond s napájecím napětím 5V nebo 12V nebude v tomto případě fungovat.   

Pokud není možné z nějakého důvodu zajistit vhodné hallovy sondy a jejich napájecí napětí 24V, doporučujeme použít speciální přizpůsobovací modul [TGHall](../../../CZ/ETC/TGHall/md/description.md#TGhall_1), který si vyžádejte u společnosti TG Drives.