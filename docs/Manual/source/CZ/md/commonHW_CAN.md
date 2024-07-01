##Základní popis {#commonCAN}
Servozesilovač TGZ obsahuje ve standardním provedení (UNI) na konektoru **X10** obvody plnohodnotné galvanicky oddělené sběrnice CAN s vnitřním odděleným napájením.
Sběrnice je díky izolaci odolnější.
Je možné propojit CANGND (pin 3) s dalším zařízeními na sběrnici a tak mezi mezi nimi udržet stejný potenciál (doporučeno).
Zařízení neobsahuje žádný interní terminační rezistor.
V případě potřeby terminovat linku je nutné použít rezistor externí. 
Jeden z možných způsobů je nalisování rezistoru 120R velikosti 0207 do společné dutinky na pinech CANH, resp. CANL (1 a 2).

##Kabeláž
Doporučujeme použít kabel s charakteristickou impedancí 100 - 120 Ω.
Maximální možná délka kabelu klesá s rostoucí požadovanou přenosovou rychlostí sběrnice.
Jsou podporovány všechny standardní rychlosti sběrnice CAN: 10, 20, 50, 100, 125, 250, 500, 800 a 1000 Kbit/s.
Rychlost se volí pomocí registru `CAN_BaudRate` v servisním programu [TGZ GUI](../../../CZ/TGZ/TGZ_SW/GUI/md/parameters.md#GUIbasicParams).