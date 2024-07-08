##Základní popis {#commonFBE}
Servozesilovač TGZ obsahuje ve standardním provedení (UNI) na konektoru **X5** obvody pro připojení externí zpětné vazby.
Je možné připojit zpětnou vazbu typu Endat, SSI, BISS, inkrementální enkodér a po aplikaci propojky FBSELx také Hiperface DSL.
Dále je zde na pinech 1-2 dostupné 5V/1A napájení pro různé účely.
Nejčastěji se používá k napájení snímačů polohy na 5V.   

Zjednodušené vnitřní schéma zapojení je na obrázku níže.

<img src="../../../common/img/FBEinternals.svg" alt="Simplified TGZ FBE schematic" style="width:80%;">

Jedná se o 3 velmi rychlé budiče sběrnice RS485 schopné pracovat s datovým tokem až 20 Mbit/s.

!!! note "Délka kabelu"
	Maximální přenosová rychlost klesá s délkou zpětnovazebního kabelu.
	V rámci zvýšení odolnosti zařízení proti rušení se ujistěte, že používáte originální kabel vhodné délky.
	Zbytečně dlouhý kabel (rezervní smyčky/klubka) může zapříčinit snížení odolnosti zařízení.

Každá linka RS485 je interně symetricky zakončena odporem 112 Ω.
Dále je zde soufázová tlumivka pro větší odolnost komunikace vůči rušení.
Konektor X5 je reprezentován piny 1-12.   

V případě, že požadujeme typ zpětné vazby Hiperface DSL, je potřeba propojit piny 5-7 a 6-8.
Tím se propojí signál RS_485_2 s výstupním obvodem pro napájení linky.
Poté stačí připojit vhodný snímač na piny 11-12.   

Budič RS485_3 je zapojen pouze jednosměrně (jen příjem dat).
Nejčastěji se využívá pro čtení nulového "zero" impulzu v rámci otáčky motoru.

!!! warning "Firmware"
	Ujistěte se, že pro zvolený typ zpětné vazby používáte správný firmware.
	Kontaktujte dodavatele pro další podrobnosti.