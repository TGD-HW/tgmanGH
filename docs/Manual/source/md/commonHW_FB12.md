##Základní popis {#commonFB12}
Servozesilovač TGZ obsahuje ve standardním provedení (UNI) na konektoru **X6** a **X7** obvody pro připojení zpětné vazby pro osu 1, resp. osu 2.
Je možné připojit zpětnou vazbu typu Endat, SSI, BISS, inkrementální enkodér a po aplikaci propojky FBSELx také Hiperface DSL.   

Zjednodušené vnitřní schéma zapojení je na obrázku níže.

<img src="../../../common/img/FB12internals.svg" alt="Simplified TGZ FB12 schematic" style="width:80%;">

Jedná se o 2 velmi rychlé budiče sběrnice RS485 schopné pracovat s datovým tokem až 20 Mbit/s.

!!! note "Délka kabelu"
	Maximální přenosová rychlost klesá s délkou zpětnovazebního kabelu.
	V rámci zvýšení odolnosti zařízení proti rušení se ujistěte, že používáte originální kabel vhodné délky.
	Zbytečně dlouhý kabel (rezervní smyčky/klubka) může zapříčinit snížení odolnosti zařízení.

Každá linka RS485 je interně symetricky zakončena odporem 112 Ω.
Dále je zde soufázová tlumivka pro větší odolnost komunikace vůči rušení.
Konektor X6 a X7 je reprezentován piny 1-8.   

V případě, že požadujeme typ zpětné vazby Hiperface DSL, je potřeba propojit piny 1-3 a 2-4.
Tím se propojí signál RS_485_2 s výstupním obvodem pro napájení linky.
Poté stačí připojit vhodný snímač na piny 7-8.   

!!! warning "Firmware"
	Ujistěte se, že pro zvolený typ zpětné vazby používáte správný firmware.
	Kontaktujte dodavatele pro další podrobnosti.