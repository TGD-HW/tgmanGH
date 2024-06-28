##Základní popis {#commonDO1-6}
Servozesilovač TGZ má na konektoru **X8** integrováno šest rychlých izolovaných digitálních výstupů typu push-pull (totem pole).
Výstupy ke své funkci potřebují napájení přivedné na VDDIO (značeno také "VCC DO").
Napájení je rozděleno na dvě skupiny.
Výstupy DO1,3,5 jsou napájeny ze vstupu VCC DO1,3,5 (pin 12 konektoru X8).
Výstupy DO2,4,6 jsou napájeny ze vstupu VCC DO2,4,6 (pin 11 konektoru X8).

Parametry vstupů jsou shrnuty v tabulce:

##Parametry DO

##Použití s hallovými sondami
Pokud chcete využít přímého připojení hallových sond určených pro komutaci motoru do konektoru **X8** na vstupy `1,3,5` (osa 1) nebo `2,4,6` (osa 2) je potřeba požádat výrobce předem o správně HW uzpůsobenou verzi.
Tato verze se liší jak v hardware, tak ve firmware.
Dbejte na to, aby takto použité hallovy sondy byly **přizpůsobeny pro napájecí napětí až 30V**, jelikož digitální vstupy servozesilovače TGZ pracují na nominální hladině **24V**.
Použití hallových sond s napájecím napětím 5V nebo 12V nebude v tomto případě fungovat.   

Pokud není možné z nějakého důvodu zajistit vhodné hallovy sondy a jejich napájecí napětí 24V, doporučujeme použít speciální přizpůsobovací modul [TGHall](../../../CZ/ETC/TGHall/md/description.md#TGhall_1), který si vyžádejte u společnosti TG Drives.