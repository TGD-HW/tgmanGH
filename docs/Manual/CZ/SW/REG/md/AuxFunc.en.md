###Řízení ASM ve skalárním režimu (bez snímače)
| Parametr | Popis |
|---|---|
| D-Mode | 20 = režim řízení U/f |
| M-Inull | jmenovitý proud, pro každou fázi se počítá i²t, při překročení vypadne do chyby |
| M-polepairs | počet pólpárů motoru |
| M-CommutationSource | 10 = režim ASM |
| M-Un | jmenovité napětí ASM |
| IM-fn | jmenovitá/synchronní frekvence |
| IM-Umin_u_f | minimální napětí při řízení U/f , pro zvýšení momentu při malých otáčkách |
| IM-Umax_u_f | maximální napětí při řízení U/f, pro omezení výkonu motoru. Špičková hodnota napětí je rovna napětí meziobvodu jen efektivní hodnota je omezena. |

Řízení motoru je umožněno prostřednictvím PG jako v režimech se synchronním motorem.
Neprobíhá zde ovšem ani polohová ani rychlostní regulace.
Výstupem PG je v tomto případě synchronní frekvence.

###Vektorové řízení ASM (se snímačem Hiperface DSL)
<img src="../../../../../source/img/ASMschematic1.webp" alt="ASM simplified schematic" style="width:50%;">

| Parametr | Popis |
|---|---|
| M-CommutationSource | 10 = režim ASM |
| IM-Rs | odpor statoru |
| IM-Ls | Indukčnost statoru = Lsσ + Lm |
| IM-Rr | Odpor rotoru |
| IM-Lr | Indukčnost rotoru = Lrσ + Lm |
| IM-Lm | Magnetizační indukčnost |
| IM-Id_rms | nominální budící proud Id (efektivní hodnota) |

Řízení motoru je možné ve všech režimech jako u synchronního motoru.

###Gear (Elektronický převod)
Tato funkcionalita umožňuje implementaci elektronické převodovky a elektronické vačky.

!!! Note "Poznámka"
	 Elektronická vačka je v kontinuálním vývoji a prozatím není implementována.
	 
Elektronická převodovka prostřednictvím vstupní polohy a převodového poměru a určuje polohu motoru.
Nahrazuje méně účinné mechanické převodovky.

| Parametr | Popis | Čtení/zápis | Popis |
|---|---|---|---|
| PositionAngle | [inc] | čtení/zápis | Výstupní poloha v rámci jedné otáčky pro lineární převod nebo ukazatel na CAM pro vačkové převody |
| PositionRevol | [inc] | čtení/zápis | Výstupní poloha v rámci více otáček pro lineární převod nebo ukazatel na CAM pro vačkové převody |
| CamPositionAngle | [inc] | čtení/zápis | Výstupní poloha v rámci jedné otáčky pro vačkové převody |
| CamPositionRevol | [inc] | čtení/zápis | Výstupní poloha v rámci více otáček pro vačkové převody |
| OffsetAngle | [inc] | čtení/zápis | Offset výstupní polohy |
| OffsetRevol | [inc] | čtení/zápis | Offset výstupní polohy |
| Shift | [inc] | čtení/zápis | Požadovaný posun ukazatele na vačku |
| ActualShiftAngle | [inc] | čtení | Skutečný posun ukazatele na vačku |
| IncShift | [inc/servotick] | čtení/zápis | Přírůstek ukazatele řazení na vačku |
| IncIn | [inc/servotick] | čtení/zápis | Přírůstek rampy Gear.ActualIn |
| CamIncPosition | [inc] | čtení | Přírůstek polohy inkrementální vačky |
| CamScale | [-] | čtení/zápis | Faktor změny měřítka profilu vačky |
| SourceNumber | [-] | čtení | Číslo logického serva použitého pro zdroj hlavního polohování |
| SourcePosition | [-] | čtení | Typ hlavní pozice 1 = Pozice zápisu, 2 = Pozice, 3 = servotick, 4 = Expozice |
| Mode | [-] | čtení/zápis | **Režimy** generátoru převodů 0 = vypnutý generátor převodů, 1 = lineární převod je aktivní, 2 = vačkový převod je aktivní |
| In | [-] | čtení/zápis | Čitatel převodového poměru |
| Out | [-] | čtení/zápis | Jmenovatel převodového poměru |
| ActualIn | [-] | čtení/zápis | Skutečná hodnota převodového poměru čitatele |
| CamLine | [-] | čtení/zápis | Offset v bajtech na první data profilu vačky v CAM_PROFILE_MEMORY nebo DATA_MEMORY |
| CamLen | [-] | čtení/zápis | Číslo dat profilu vačky |
| CamType | [-] | čtení/zápis | Typ vačky 0 = otočná vačka, 1 = přední vačka |
| CamTab | [-] | čtení/zápis | Umístění dat o profilu vačky: 0 = na flash paměť, 1 = na SD kartu. |