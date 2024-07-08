Po aktivaci nouzového zastavení dojde k zpomalení pohonu prostřednictvím nastavitelné zpomalovací rampy a servozesilovač poté odpojí přívod energie do motoru.
Pokud je k dispozici statická brzda, dojde po zastavení pohonu k její aktivaci.
Funkci nouzového zastavení lze aktivovat:

- Chybou pohonu umožňující nouzové zastavení.
- Digitálním vstupem.
- Ochrannou funkcí - pro ochranu komunikačních sběrnic.

Funkce nouzového zastavení je přístupná v `position` a `speed` režimech: `2,3,6,7`

##Registry a parametry
###D-EmerDecRamp

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 21 | read-write |
| Drive | 4 | 21 | read-write |

Nouzová zpomalovací rampa deg/s, 1 až 3600000 deg/s
	
###D-ErrorMaskEmerDec

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 23 | read-write |
| Drive | 4 | 23 | read-write |

Maska chyby pohonu pro nouzové zpomalení, bity mají stejný význam jako bity v registru `aDriveError`.
Pokud je v případě chyby nastaven odpovídající bit, měnič provede nouzové zastavení, pokud je to možné.
	
###D-DI_MaskEmerStop

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 24 | read-write |
| Drive | 4 | 24 | read-write |

Maska pro digitální vstupy. Vstupy 1, 3, 5 lze přiřadit k ose 1 a vstupy 2, 4, 6 lze přiřadit k ose 2.   
*Příklad: D-DI_MaskEmerStop (Ax.2) = 5, vstupy 2 a 6 jsou přiřazeny pro nouzové zastavení.*
*Pokud jeden nebo oba nejsou aktivní, provede se nouzové zastavení.*   

###D-GuardTimeEmerStop

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Drive | 3 | 25 | read-write |
| Drive | 4 | 25 | read-write |

*Ochranný časový limit v ms. Pokud do této doby není vynulován ochranný čítač, provede se rutina nouzového zastavení. Hodnota 0 deaktivuje tuto funkci.*   

###aDriveStatus

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 37 | read only |
| Monitoring | 20 | 37 | read only |

*Bit 8 ... rampa nouzového zastavení aktivní*   
*Bit 9 ... rampa nouzového zastavení dokončena*   

###aDriveError

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 38 | read only |
| Monitoring | 20 | 38 | read only |

*Bit 20 ... nouzové zastavení aktivováno digitálním vstupem nebo ochrannou funkcí.*   

###aDriveWarning

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 39 | read only |
| Monitoring | 20 | 39 | read only |

*Bit 20 ... podmínka aktivace nouzového zastavení digitálním vstupem nebo ochrannou funkcí. V případě, že pohon není povolen.*   

###GuardingCounter

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Monitoring | 19 | 126 | read only |
| Monitoring | 20 | 126 | read only |

*Počítadlo milisekund pro ochrannou funkci. Lze resetovat registrací* `K-ResetGuarding`.   

###ResetGuarding

| Parameter group name | Group index | Item index | Access |
|---|---|---|---|
| Command | 17 | 13 | read-write |
| Command | 18 | 13 | read-write |

*Resetujte `GuardingCounter` zápisem hodnoty* `0xAA55`*. Hodnota bude automaticky vymazána.*

!!! Note "Poznámka"
	Výpočet rampy nouzového zpomalení je odvozen od skutečné rychlosti a polohy.
	V případě velké chyby polohy nebo rychlosti před provedením nouzového zastavení lze pozorovat, že křivky rychlosti a polohy nejsou plynulé.
	Nově jsou hodnoty rychlostí v generátoru uživatelských profilů nastaveny na `0` po chybě.
