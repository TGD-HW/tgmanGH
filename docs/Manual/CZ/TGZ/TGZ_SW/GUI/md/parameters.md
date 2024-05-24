##Záložka **Parameters**

V záložce **Parameters** je dostupné nastavení veškerých parametrů servozesilovače TGZ.
Kromě tohoto podrobného nastavení je zde možné najít i detailní informace o připojeném servozesilovači (typ, výrobní číslo, atd.).

<img src="../../img/GUIparams.png" alt="TGZ GUI servo parameters" style="width:100%;">

Otevřené okno se dále skládá z několika podoken:

- BASIC GROUPS - seznam skupin parametrů (v jednotlivých skupinách je možné nalézt a nastavit veškeré parametry servozesilovače).
- USER GROUPS - uživatelské skupiny (umožňují nastavení zobrazování vybraných skupin parametrů).
- DRIVE INFO - zobrazí informace o daném servozesilovači (typ, sériové číslo, verze HW, verze firmware, atd.).
- PARAMETERS - zobrazení a editování parametrů aktivní skupiny.
- MONITORED VALUES - AXIS 1 - zobrazuje základní informace o stavu (poloha, rychlost, proud atd.) osy 1 servozesilovače TGZ, zobrazí kód případné chyby a umožňuje její reset.
- MONITORED VALUES - AXIS 2 - zobrazuje základní informace o stavu (poloha, rychlost, proud atd.) osy 2 servozesilovače TGZ, zobrazí kód případné chyby a umožňuje její reset.

V dolní části okna se pak nachází informativní stavový řádek s několika funkčními tlačítky:

<div class="grid cards" markdown>

-   **COMMON**

    ---
	<img src="../../../../../../source/common/img/icoCommon.png" alt="Icon Common" style="width:50%;">

-	informace o stavu HW ENABLE

-   **AXIS 1**

    ---
	<img src="../../../../../../source/common/img/icoAx1.png" alt="Icon Ax1" style="width:85%;">

-	- zobrazení informací o stavu osy 1 (chyba, varovné hlášení SW Enable)
    - funkční tlačítko Enable umožňuje zapnutí SW ENABLE u osy 1
    - funkční tlačítko Disable umožňuje vypnutí SW ENABLE u osy 1
	
-   **AXIS 2**

    ---
	<img src="../../../../../../source/common/img/icoAx2.png" alt="Icon Ax2" style="width:85%;">

-	- zobrazení informací o stavu osy 2 (chyba, varovné hlášení SW Enable)
    - funkční tlačítko Enable umožňuje zapnutí SW ENABLE u osy 2
    - funkční tlačítko Disable umožňuje vypnutí SW ENABLE u osy 2
		
</div>

##Popis parametrů
Seznam všech parametrů servozesilovače TGZ včetně jejich popisu je uveden ve zvláštním dokumentu `TGZ_registers_fw_build_1605.xlsx`.
Tento dokument je volně ke stažení zde: [ TGZ_registers_fw_build_1605.zip](https://www.tgdrives.cz/fileadmin/user_upload/download-TGZ/TGZ_registers_fw_build_1605.zip).