##Základní popis {#common_UNIR_HALL_desc}
Servozesilovač TGZ má ve zodolněném provedení (UNIR-RI) na konektoru **X7** připraveny 3 rychlé vstupy pro Hallovy sondy (pin 7, 9, 11).
Jedná se o elektricky neoddělené vstupy aktivní v log. 0. Připojený snímač polohy (nejčastější případ) s Hallovými čidly tedy spíná 0V (GND).

##Použití {#common_UNIR_HALL_usage}
Pro správnou funkci je nutné dodat externí napájení na pinu č. 12 (VHI).
Rozsah tohoto napájecího napětí je 5-30VDC.
Napájení jednotlivých Hallových čidel se objeví na pinu č. 10 (VHO).
Jedná se o úroveň totožnou jako na pinu č. 12 (VHI) avšak je zde implementována ochrana proti přetížení a zkratu.
0V (common) Hallových snímačů je potřeba připojit na pin č. 8 (HGND).
Pokud je snímač odpojen, nebo jeho výstup neaktivní, objeví se na vstupu napájecí napětí úměrné externímu (připojenému na VHI).

##Příklad zapojení {#common_UNIR_HALL_schematic}
Příkad zapojení v sekci "Příklad zapojení" u každého odpovídajícího zařízeni TGZ, které tuto funkci podporuje.
![HallExample1](../img/UNIR_HALL_example1.webp){: style="width:40%;" }

!!! warning "Firmware"
	Ujistěte se, že pro zvolený typ zpětné vazby používáte správný firmware.

