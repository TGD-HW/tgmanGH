##Popis funkce {#StandardBrakeDesc}
Pokud je servozesilovač TGZ vybaven standardní funkcí ovládání statické motorové brzdy, obsahuje obvod aktivace a deaktivace brzdy včetně diagnostiky chyb.
Tato funkce neumožňuje snížit spotřebu statické brzdy. Excitační napětí brzdy je tedy po celou dobu sepnutí rovno napájecímu napětí VCC<sub>BR</sub>.

!!! info "Dostupnost funkce"

	Standardní funkce ovládání statické motorové brzdy je dostupná u všech servozesilovačů řady TGZ s výjimkou těch, které jsou vybaveny vylepšenou funkcí [Chytrá brzda](commonHW_SmartBrake.md#SmartBrakeDesc).

##Nastavení a ovládání {#StandardBrakeUsage}
Uživatel může povolit funkci ovládání statické brzdy v programu [TGZ GUI](../../CZ/TGZ/TGZ_SW/GUI/md/intro.md#GUIstart).
Jedná se o parametr `M-StaticBrake` v sekci `Motor`.
![GUI brake enable](../img/GUIbrakeEnable.webp){: style="width:100%;" }
U každé řízené osy je možné individuálně povolit ovládání brzdy.

Dále je možné pro každou osu nastavit tyto parametry zpoždění brzdy v sekci `Drive`:

|  Č. parametru |  Název |  Označení v TGZ GUI | Jednotka | Rozsah | Popis |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  τ<sub>DUE</sub>  | `D-DelayUnbrake_Enable` | 0,1 ms | 0,1 ~ 1e8 ms  | zpoždění mezi enable servozesilovače a odbrždění brzdy |
| 1 |  τ<sub>DDB</sub>  | `D-DelayDisable_Brake` | 0,1 ms | 0,1 ~ 1e8 ms  | zpoždění mezi zabržděním brzdy a disable servozesilovače |

Před použitím funkce spínání brzdy se ujistěte, že:

1.	Máte aktivován parametr `M-StaticBrake` viz. výše.
2.	Je připojeno napájení v dovoleném rozsahu brzdového obvodu na svorce VCC<sub>BR</sub>.
3.	Napájecí zdroj je dostatečně výkonný a odpovídá nebo přesahuje svým výkonem příkon brzdy, a to včetně možné špičky odběru v okamžiku sepnutí (excitace) brzdy.
4.	Statická brzda je k servozesilovači správně připojena na svorkách BR+ a BR- (někdy také B+ a B-), viz. doporučené schéma zapojení konkrétního servozesilovače TGZ. Dbejte na polaritu brzdy.

V případě, že brzdu nelze sepnout, nebo servozesilovač hlásí chybu **Holding brake error** se ujistěte, že:

1.	Napájecí zdroj připojený na VCC<sub>BR</sub> má správnou polaritu, úroveň napětí a je stabilní.
2.	Kabeláž (od zdroje k napájecímu konektoru, výstup pro připojení brzdy, záměna polarity...) je v pořádku.
3.	Elektický odpor brzdy (excitační cívky) je v rámci tolerance, dle typu brzdy.
4.	Připojením brzdy přímo na nezávislý napěťový zdroj vhodné úrovně je možné brzdu aktivovat/deaktivovat a její spotřeba je dle očekávání.

##Parametry {#StandardBrakeParams}
Mezní parametry brzdového spínače jsou uvedeny v tabulce:

|  Č. parametru |  Název |  Jednotka | Rozsah | Popis |
| :---: | :---: | :---: | :---: | :---: |
| 1 |  VCC<sub>BR</sub>  | V | 12 ~ 30 | Napájecí napětí brzdového obvodu |
| 2 |  I<sub>OUT,MAX</sub> @ 25°C  | A | 2,5 | Maximální výstupní proud brzdy |
| 3 |  I<sub>OUT,PK,MIN</sub> @ 25°C  | A | 3 | Výstupní proud při přetížení spínače, nad který spínač začíná přetížení/zkrat interně omezovat |

!!! warning "Maximální výstupní proud brzdy"

	Maximální hodnota výstupního proudu není pevně daná a je závislá na mnoha fakturech, např. teplota servozesilovače, odpor vinutí brzdy atd.
	
##Detekce chyb {#StandardBrakeErrors}
Při splnění všech podmínek správné funkce statické brzdy servozesilovač TGZ signalizuje dva chybových stavy:

1.	Odpojení zátěže/brzdy a to i ve stavu, kdy není brzda excitována, ale je povolena parametrem `M-StaticBrake = 1`.
2.	Přetížení/přehřátí obvodu spínání brzdy.

V obou případech se v programu [TGZ GUI](../../CZ/TGZ/TGZ_SW/GUI/md/intro.md#GUIstart) objeví u příslušné osy chyba **Holding brake error**.