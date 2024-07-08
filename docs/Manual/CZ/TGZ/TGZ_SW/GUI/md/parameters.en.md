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
	<img src="../../../../../../source/img/icoCommon.png" alt="Icon Common" style="width:50%;">

-	informace o stavu HW ENABLE

-   **AXIS 1**

    ---
	<img src="../../../../../../source/img/icoAx1.png" alt="Icon Ax1" style="width:85%;">

-	- zobrazení informací o stavu osy 1 (chyba, varovné hlášení SW Enable)
    - funkční tlačítko Enable umožňuje zapnutí SW ENABLE u osy 1
    - funkční tlačítko Disable umožňuje vypnutí SW ENABLE u osy 1
	
-   **AXIS 2**

    ---
	<img src="../../../../../../source/img/icoAx2.png" alt="Icon Ax2" style="width:85%;">

-	- zobrazení informací o stavu osy 2 (chyba, varovné hlášení SW Enable)
    - funkční tlačítko Enable umožňuje zapnutí SW ENABLE u osy 2
    - funkční tlačítko Disable umožňuje vypnutí SW ENABLE u osy 2
		
</div>

##Popis parametrů
Seznam všech parametrů servozesilovače TGZ včetně jejich popisu je uveden ve zvláštním dokumentu `TGZ_registers_fw_build_1605.xlsx`.

##Základní parametry TGZ v TGZ GUI {#GUIbasicParams}
<table>
	<tr>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Name&quot;}">Name</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis&quot;}">Axis</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Basic Group&quot;}">Basic Group</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Index (ETH)&quot;}">Index (ETH)</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Group&yen;u000aIndex&quot;}">Group<br>Index</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Item&yen;u000aIndex&quot;}">Item<br>Index</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Access&quot;}">Access</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unit&quot;}">Unit</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Size&quot;}">Size</td>
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Popis [CZ]&quot;}">Popis [CZ]</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Type1&quot;}">C-Type1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2000&quot;}">0x2000</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typové označení servozesilovače 1&yen;/5&quot;}">Typové označení servozesilovače 1/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Type2&quot;}">C-Type2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2001&quot;}">0x2001</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typové označení servozesilovače 2&yen;/5&quot;}">Typové označení servozesilovače 2/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Type3&quot;}">C-Type3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2002&quot;}">0x2002</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typové označení servozesilovače 3&yen;/5&quot;}">Typové označení servozesilovače 3/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Type4&quot;}">C-Type4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2003&quot;}">0x2003</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typové označení servozesilovače 4&yen;/5&quot;}">Typové označení servozesilovače 4/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Type5&quot;}">C-Type5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2004&quot;}">0x2004</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typové označení servozesilovače 5&yen;/5&quot;}">Typové označení servozesilovače 5/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-HWVer&quot;}">C-HWVer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2005&quot;}">0x2005</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Verze HW&quot;}">Verze HW</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-FWVer&quot;}">C-FWVer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2006&quot;}">0x2006</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Verze firmware&quot;}">Verze firmware</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-FWBuild1&quot;}">C-FWBuild1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2007&quot;}">0x2007</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Datum a cas vytvoreni firmware 1&yen;/5&quot;}">Datum a cas vytvoreni firmware 1/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-FWBuild2&quot;}">C-FWBuild2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2008&quot;}">0x2008</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Datum a cas vytvoreni firmware 2&yen;/5&quot;}">Datum a cas vytvoreni firmware 2/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-FWBuild3&quot;}">C-FWBuild3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2009&quot;}">0x2009</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Datum a cas vytvoreni firmware 3&yen;/5&quot;}">Datum a cas vytvoreni firmware 3/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-FWBuild4&quot;}">C-FWBuild4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x200A&quot;}">0x200A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Datum a cas vytvoreni firmware 4&yen;/5&quot;}">Datum a cas vytvoreni firmware 4/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-FWBuild5&quot;}">C-FWBuild5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x200B&quot;}">0x200B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Datum a cas vytvoreni firmware 5&yen;/5&quot;}">Datum a cas vytvoreni firmware 5/5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-IPAddress&quot;}">C-IPAddress</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x200C&quot;}">0x200C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;IP adresa servisního UDP kanálu X11&quot;}">IP adresa servisního UDP kanálu X11</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-ID&quot;}">C-ID</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x200D&quot;}">0x200D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 13}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">13</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ID pro využití na sběrnici&quot;}">ID pro využití na sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-SyncTime&quot;}">C-SyncTime</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x200E&quot;}">0x200E</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 14}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">14</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Měřený čas mezi synchronizačními pulsy na&yen;u000asběrnicei (pokud je využito DC)&quot;}">Měřený čas mezi synchronizačními pulsy na<br>sběrnicei (pokud je využito DC)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Enable_1G&quot;}">C-Enable_1G</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x200F&quot;}">0x200F</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 15}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">15</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Povolení rychlosti sběrnice 1G (v přípravě)&quot;}">Povolení rychlosti sběrnice 1G (v přípravě)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-SetCycleTime&quot;}">C-SetCycleTime</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2010&quot;}">0x2010</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 16}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">16</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;us&quot;}">us</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Očekáváná komunikační perioda na sběrnici&yen;u000a(pokud není využito DC)&quot;}">Očekáváná komunikační perioda na sběrnici<br>(pokud není využito DC)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-UserProgStart&quot;}">C-UserProgStart</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FFFF00" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Common&quot;}">Common</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2011&quot;}">0x2011</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Povolení automatického startu uživatelského programu : 0 .. Nespouští se, 1 .. Spouští se z interní flash,(2 .. Zpouští se z SD karty .. V&yen;u000apřípravě)&quot;}">Povolení automatického startu uživatelského programu : 0 .. Nespouští se, 1 .. Spouští se z interní flash,(2 .. Zpouští se z SD karty .. V<br>přípravě)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name1&quot;}">M-Name1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2100&quot;}">0x2100</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 1 1&yen;/6&quot;}">Název motoru 1 1/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name1&quot;}">M-Name1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2200&quot;}">0x2200</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 2 1&yen;/6&quot;}">Název motoru 2 1/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name2&quot;}">M-Name2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2101&quot;}">0x2101</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 1 2&yen;/6&quot;}">Název motoru 1 2/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name2&quot;}">M-Name2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2201&quot;}">0x2201</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 2 2&yen;/6&quot;}">Název motoru 2 2/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name3&quot;}">M-Name3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2102&quot;}">0x2102</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 1 3&yen;/6&quot;}">Název motoru 1 3/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name3&quot;}">M-Name3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2202&quot;}">0x2202</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 2 3&yen;/6&quot;}">Název motoru 2 3/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name4&quot;}">M-Name4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2103&quot;}">0x2103</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 1 4&yen;/6&quot;}">Název motoru 1 4/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name4&quot;}">M-Name4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2203&quot;}">0x2203</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 2 4&yen;/6&quot;}">Název motoru 2 4/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name5&quot;}">M-Name5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2104&quot;}">0x2104</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 1 5&yen;/6&quot;}">Název motoru 1 5/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name5&quot;}">M-Name5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2204&quot;}">0x2204</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 2 5&yen;/6&quot;}">Název motoru 2 5/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name6&quot;}">M-Name6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2105&quot;}">0x2105</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 1 6&yen;/6&quot;}">Název motoru 1 6/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Name6&quot;}">M-Name6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2205&quot;}">0x2205</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název motoru 2 6&yen;/6&quot;}">Název motoru 2 6/6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Inull&quot;}">M-Inull</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2106&quot;}">0x2106</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA(rms)&quot;}">mA(rms)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Povolený trvalý efektivní proud pro motor 1&quot;}">Povolený trvalý efektivní proud pro motor 1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Inull&quot;}">M-Inull</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2206&quot;}">0x2206</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA(rms)&quot;}">mA(rms)</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Povolený trvalý efektivní proud pro motor 2&quot;}">Povolený trvalý efektivní proud pro motor 2</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Ipeak&quot;}">M-Ipeak</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2107&quot;}">0x2107</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Povolená špičková hodnota amplitudy proudu&yen;u000apro motor 1 (Iamp = 1.41 * Irms)&quot;}">Povolená špičková hodnota amplitudy proudu<br>pro motor 1 (Iamp = 1.41 * Irms)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Ipeak&quot;}">M-Ipeak</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2207&quot;}">0x2207</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Povolená špičková hodnota amplitudy proudu&yen;u000apro motor 2 (Iamp = 1.41 * Irms)&quot;}">Povolená špičková hodnota amplitudy proudu<br>pro motor 2 (Iamp = 1.41 * Irms)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Nmax&quot;}">M-Nmax</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2108&quot;}">0x2108</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximální povolená rychlost motoru 1&quot;}">Maximální povolená rychlost motoru 1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Nmax&quot;}">M-Nmax</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2208&quot;}">0x2208</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximální povolená rychlost motoru 2&quot;}">Maximální povolená rychlost motoru 2</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Polepairs&quot;}">M-Polepairs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2109&quot;}">0x2109</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet pólpárů motoru 1 ( pólpáry = póly &yen;/ 2)&quot;}">Počet pólpárů motoru 1 ( pólpáry = póly / 2)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-Polepairs&quot;}">M-Polepairs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2209&quot;}">0x2209</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet pólpárů motoru 2 ( pólpáry = póly &yen;/ 2)&quot;}">Počet pólpárů motoru 2 ( pólpáry = póly / 2)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-CommutOffset&quot;}">M-CommutOffset</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x210A&quot;}">0x210A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Úhlové posunutí nuly snímače vůči statorovému&yen;u000avinutí motoru 1&quot;}">Úhlové posunutí nuly snímače vůči statorovému<br>vinutí motoru 1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-CommutOffset&quot;}">M-CommutOffset</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x220A&quot;}">0x220A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Úhlové posunutí nuly snímače vůči statorovému&yen;u000avinutí motoru 2&quot;}">Úhlové posunutí nuly snímače vůči statorovému<br>vinutí motoru 2</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-MinResTerm&quot;}">M-MinResTerm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x210B&quot;}">0x210B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ohm&quot;}">Ohm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Minimální odpor teplotního snímače motoru 1 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)&quot;}">Minimální odpor teplotního snímače motoru 1 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-MinResTerm&quot;}">M-MinResTerm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x220B&quot;}">0x220B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ohm&quot;}">Ohm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Minimální odpor teplotního snímače motoru 2 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)&quot;}">Minimální odpor teplotního snímače motoru 2 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-MaxResTerm&quot;}">M-MaxResTerm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x210C&quot;}">0x210C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ohm&quot;}">Ohm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximální odpor teplotního snímače motoru 1 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)&quot;}">Maximální odpor teplotního snímače motoru 1 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-MaxResTerm&quot;}">M-MaxResTerm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x220C&quot;}">0x220C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ohm&quot;}">Ohm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximální odpor teplotního snímače motoru 2 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)&quot;}">Maximální odpor teplotního snímače motoru 2 pro vyhodnocení poruchy - vysoká teplota (pouze pro digitální snímače polohy s připojeným teplotním čidlem)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-StaticBrake&quot;}">M-StaticBrake</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x210D&quot;}">0x210D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 13}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">13</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Statická brzda motoru 1 : 1 = ano, 0 = ne&quot;}">Statická brzda motoru 1 : 1 = ano, 0 = ne</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-StaticBrake&quot;}">M-StaticBrake</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x220D&quot;}">0x220D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 13}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">13</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Statická brzda motoru 2 : 1 = ano, 0 = ne&quot;}">Statická brzda motoru 2 : 1 = ano, 0 = ne</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-ThermTimeConst&quot;}">M-ThermTimeConst</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x210E&quot;}">0x210E</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 14}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">14</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;s&quot;}">s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Teplotní časová konstanta motoru 1&quot;}">Teplotní časová konstanta motoru 1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;M-ThermTimeConst&quot;}">M-ThermTimeConst</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FFC000" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor&quot;}">Motor</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x220E&quot;}">0x220E</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 14}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">14</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;s&quot;}">s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Teplotní časová konstanta motoru 2&quot;}">Teplotní časová konstanta motoru 2</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Name1&quot;}">D-Name1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2300&quot;}">0x2300</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název pohonu 1 1&yen;/3&quot;}">Název pohonu 1 1/3</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Name1&quot;}">D-Name1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2400&quot;}">0x2400</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název pohonu 2 1&yen;/3&quot;}">Název pohonu 2 1/3</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Name2&quot;}">D-Name2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2301&quot;}">0x2301</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název pohonu 1 2&yen;/3&quot;}">Název pohonu 1 2/3</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Name2&quot;}">D-Name2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2401&quot;}">0x2401</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název pohonu 2 2&yen;/3&quot;}">Název pohonu 2 2/3</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Name3&quot;}">D-Name3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2302&quot;}">0x2302</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název pohonu 1 3&yen;/3&quot;}">Název pohonu 1 3/3</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Name3&quot;}">D-Name3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2402&quot;}">0x2402</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;chars&quot;}">chars</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název pohonu 2 3&yen;/3&quot;}">Název pohonu 2 3/3</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Mode&quot;}">D-Mode</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2303&quot;}">0x2303</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Režim pohonu 1 - popis v manuálu&quot;}">Režim pohonu 1 - popis v manuálu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-Mode&quot;}">D-Mode</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2403&quot;}">0x2403</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Režim pohonu 2 - popis v manuálu&quot;}">Režim pohonu 2 - popis v manuálu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-DelayEnable_Hwen&quot;}">D-DelayEnable_Hwen</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x230A&quot;}">0x230A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.1ms&quot;}">0.1ms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zpoždění enable pohonu 1 po nastupné hraně&yen;u000asignálu hw enable X1&quot;}">Zpoždění enable pohonu 1 po nastupné hraně<br>signálu hw enable X1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-DelayEnable_Hwen&quot;}">D-DelayEnable_Hwen</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x240A&quot;}">0x240A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.1ms&quot;}">0.1ms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zpoždění enable pohonu 2 po nastupné hraně&yen;u000asignálu hw enable X1&quot;}">Zpoždění enable pohonu 2 po nastupné hraně<br>signálu hw enable X1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-DelayUnbrake_Enable&quot;}">D-DelayUnbrake_Enable</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x230B&quot;}">0x230B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.1ms&quot;}">0.1ms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zpoždění uvolnění brzdy motoru 1 po enable&yen;u000apohonu&quot;}">Zpoždění uvolnění brzdy motoru 1 po enable<br>pohonu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-DelayUnbrake_Enable&quot;}">D-DelayUnbrake_Enable</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x240B&quot;}">0x240B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.1ms&quot;}">0.1ms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zpoždění uvolnění brzdy motoru 2 po enable&yen;u000apohonu&quot;}">Zpoždění uvolnění brzdy motoru 2 po enable<br>pohonu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-DelayDisable_Brake&quot;}">D-DelayDisable_Brake</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x230C&quot;}">0x230C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.1ms&quot;}">0.1ms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zpoždění disble pohonu 1 po zabrždění motoru&quot;}">Zpoždění disble pohonu 1 po zabrždění motoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-DelayDisable_Brake&quot;}">D-DelayDisable_Brake</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x240C&quot;}">0x240C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.1ms&quot;}">0.1ms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zpoždění disble pohonu 2 po zabrždění motoru&quot;}">Zpoždění disble pohonu 2 po zabrždění motoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-VoltDCLinkMinErrLim&quot;}">D-VoltDCLinkMinErrLim</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x230D&quot;}">0x230D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 13}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">13</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V&quot;}">V</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Minimální napětí meziobvodu pro vyhodnocení&yen;u000achyby podpětí&quot;}">Minimální napětí meziobvodu pro vyhodnocení<br>chyby podpětí</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;D-VoltDCLinkMaxErrLim&quot;}">D-VoltDCLinkMaxErrLim</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#FF7474" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive&quot;}">Drive</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x230E&quot;}">0x230E</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 14}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">14</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V&quot;}">V</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximální napětí meziobvodu pro vyhodnocení&yen;u000achyby přepětí&quot;}">Maximální napětí meziobvodu pro vyhodnocení<br>chyby přepětí</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-K&quot;}">C-K</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2500&quot;}">0x2500</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mV&yen;/A&quot;}">mV/A</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení proudového regulátoru složky Q&quot;}">Zesílení proudového regulátoru složky Q</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-K&quot;}">C-K</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2600&quot;}">0x2600</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mV&yen;/A&quot;}">mV/A</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení proudového regulátoru složky Q&quot;}">Zesílení proudového regulátoru složky Q</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Ti&quot;}">C-Ti</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2501&quot;}">0x2501</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Integrační čas proudového regulátoru&quot;}">Integrační čas proudového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Ti&quot;}">C-Ti</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2601&quot;}">0x2601</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Integrační čas proudového regulátoru&quot;}">Integrační čas proudového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-KDr&quot;}">C-KDr</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2502&quot;}">0x2502</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení proudového regulátoru složky D&yen;u000arelativně k zesílení složky Q K&quot;}">Zesílení proudového regulátoru složky D<br>relativně k zesílení složky Q K</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-KDr&quot;}">C-KDr</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2602&quot;}">0x2602</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení proudového regulátoru složky D&yen;u000arelativně k zesílení složky Q K&quot;}">Zesílení proudového regulátoru složky D<br>relativně k zesílení složky Q K</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Tc&quot;}">C-Tc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2503&quot;}">0x2503</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Časová konstanta filtru žádaného proudu&yen;u000a(nevyužito)&quot;}">Časová konstanta filtru žádaného proudu<br>(nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Tc&quot;}">C-Tc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2603&quot;}">0x2603</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Časová konstanta filtru žádaného proudu&yen;u000a(nevyužito)&quot;}">Časová konstanta filtru žádaného proudu<br>(nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Filt&quot;}">C-Filt</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2504&quot;}">0x2504</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Procentuální hodnota filtrované části žádaného proudu (100 = 100% filtrováno) (nevyužito)&quot;}">Procentuální hodnota filtrované části žádaného proudu (100 = 100% filtrováno) (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-Filt&quot;}">C-Filt</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2604&quot;}">0x2604</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Procentuální hodnota filtrované části žádaného proudu (100 = 100% filtrováno) (nevyužito)&quot;}">Procentuální hodnota filtrované části žádaného proudu (100 = 100% filtrováno) (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-LimN&quot;}">C-LimN</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2505&quot;}">0x2505</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení záporné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull&quot;}">Omezení záporné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-LimN&quot;}">C-LimN</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2605&quot;}">0x2605</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení záporné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull&quot;}">Omezení záporné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-LimP&quot;}">C-LimP</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2506&quot;}">0x2506</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení kladné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull&quot;}">Omezení kladné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-LimP&quot;}">C-LimP</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2606&quot;}">0x2606</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení kladné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull&quot;}">Omezení kladné amplitudy proudu (na výstupu rychlostního regulátoru) relativně k M-Inull</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-VoltLimMin&quot;}">C-VoltLimMin</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2507&quot;}">0x2507</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení záporného napětí na výstupu&yen;u000aproudového regulátoru&quot;}">Omezení záporného napětí na výstupu<br>proudového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-VoltLimMin&quot;}">C-VoltLimMin</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2607&quot;}">0x2607</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení záporného napětí na výstupu&yen;u000aproudového regulátoru&quot;}">Omezení záporného napětí na výstupu<br>proudového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-VoltLimMax&quot;}">C-VoltLimMax</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2508&quot;}">0x2508</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení kladného napětí na výstupu&yen;u000aproudového regulátoru&quot;}">Omezení kladného napětí na výstupu<br>proudového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-VoltLimMax&quot;}">C-VoltLimMax</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2608&quot;}">0x2608</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení kladného napětí na výstupu&yen;u000aproudového regulátoru&quot;}">Omezení kladného napětí na výstupu<br>proudového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-CogCompFac&quot;}">C-CogCompFac</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2509&quot;}">0x2509</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Faktor kompenzace coggingu 0.. Vypnuto&yen;u000a(před zapnutím musí být změřena kompenzační tabulka pro daný motor)&quot;}">Faktor kompenzace coggingu 0.. Vypnuto<br>(před zapnutím musí být změřena kompenzační tabulka pro daný motor)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-CogCompFac&quot;}">C-CogCompFac</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#C198E0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Currentcontroller&quot;}">Currentcontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2609&quot;}">0x2609</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;%&quot;}">%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Faktor kompenzace coggingu 0.. Vypnuto (před zapnutím musí být změřena kompenzační&yen;u000atabulka pro daný motor)&quot;}">Faktor kompenzace coggingu 0.. Vypnuto (před zapnutím musí být změřena kompenzační<br>tabulka pro daný motor)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-K&quot;}">V-K</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2700&quot;}">0x2700</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&yen;/1000rpm&quot;}">mA/1000rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení rychlostního regulátoru&quot;}">Zesílení rychlostního regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-K&quot;}">V-K</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2800&quot;}">0x2800</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&yen;/1000rpm&quot;}">mA/1000rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení rychlostního regulátoru&quot;}">Zesílení rychlostního regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-Ti&quot;}">V-Ti</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2701&quot;}">0x2701</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Integrační čas rychlostního regulátoru&quot;}">Integrační čas rychlostního regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-Ti&quot;}">V-Ti</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2801&quot;}">0x2801</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Integrační čas rychlostního regulátoru&quot;}">Integrační čas rychlostního regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-LimN&quot;}">V-LimN</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2702&quot;}">0x2702</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení maximální záporné rychlosti (na&yen;u000avýstupu polohového regulátoru)&quot;}">Omezení maximální záporné rychlosti (na<br>výstupu polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-LimN&quot;}">V-LimN</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2802&quot;}">0x2802</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení maximální záporné rychlosti (na&yen;u000avýstupu polohového regulátoru)&quot;}">Omezení maximální záporné rychlosti (na<br>výstupu polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-LimP&quot;}">V-LimP</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2703&quot;}">0x2703</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení maximální kladné rychlosti (na výstupu&yen;u000apolohového regulátoru)&quot;}">Omezení maximální kladné rychlosti (na výstupu<br>polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-LimP&quot;}">V-LimP</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2803&quot;}">0x2803</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení maximální kladné rychlosti (na výstupu&yen;u000apolohového regulátoru)&quot;}">Omezení maximální kladné rychlosti (na výstupu<br>polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-Tfb&quot;}">V-Tfb</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2704&quot;}">0x2704</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;časová konstanta filtru (dolní propust) skutečné&yen;u000arychlosti (nevyužito)&quot;}">časová konstanta filtru (dolní propust) skutečné<br>rychlosti (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-Tfb&quot;}">V-Tfb</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2804&quot;}">0x2804</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;časová konstanta filtru (dolní propust) skutečné&yen;u000arychlosti (nevyužito)&quot;}">časová konstanta filtru (dolní propust) skutečné<br>rychlosti (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-Tv&quot;}">V-Tv</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2705&quot;}">0x2705</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;časová konstanta filtru (dolní propust) žádané&yen;u000arychlosti (nevyužito)&quot;}">časová konstanta filtru (dolní propust) žádané<br>rychlosti (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-Tv&quot;}">V-Tv</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2805&quot;}">0x2805</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;µs&quot;}">µs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;časová konstanta filtru (dolní propust) žádané&yen;u000arychlosti (nevyužito)&quot;}">časová konstanta filtru (dolní propust) žádané<br>rychlosti (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-FiFact&quot;}">V-FiFact</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2706&quot;}">0x2706</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Faktor filtrace rychlosti 0..nefiltrováno&yen;u000a(nevyužito)&quot;}">Faktor filtrace rychlosti 0..nefiltrováno<br>(nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V-FiFact&quot;}">V-FiFact</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#B3DCE7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocitycontroller&quot;}">Velocitycontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2806&quot;}">0x2806</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Faktor filtrace rychlosti 0..nefiltrováno&yen;u000a(nevyužito)&quot;}">Faktor filtrace rychlosti 0..nefiltrováno<br>(nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-K&quot;}">P-K</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2900&quot;}">0x2900</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.001 1&yen;/s&quot;}">0.001 1/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení polohového regulátoru&quot;}">Zesílení polohového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-K&quot;}">P-K</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2A00&quot;}">0x2A00</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0.001 1&yen;/s&quot;}">0.001 1/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Zesílení polohového regulátoru&quot;}">Zesílení polohového regulátoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-SFF&quot;}">P-SFF</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2901&quot;}">0x2901</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rychlostní předkorekce&quot;}">Rychlostní předkorekce</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-SFF&quot;}">P-SFF</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2A01&quot;}">0x2A01</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rychlostní předkorekce&quot;}">Rychlostní předkorekce</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-MaxAngleError&quot;}">P-MaxAngleError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2902&quot;}">0x2902</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;---&quot;}">---</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximální poziční chyba - úhel&quot;}">maximální poziční chyba - úhel</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-MaxAngleError&quot;}">P-MaxAngleError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2A02&quot;}">0x2A02</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;---&quot;}">---</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximální poziční chyba - úhel&quot;}">maximální poziční chyba - úhel</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-MaxRevolError&quot;}">P-MaxRevolError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2903&quot;}">0x2903</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;---&quot;}">---</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximální poziční chyba - otáčky&quot;}">maximální poziční chyba - otáčky</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;P-MaxRevolError&quot;}">P-MaxRevolError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#00B0F0" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Positioncontroller&quot;}">Positioncontroller</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2A03&quot;}">0x2A03</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;---&quot;}">---</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximální poziční chyba - otáčky&quot;}">maximální poziční chyba - otáčky</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-Type&quot;}">F-Type</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2B00&quot;}">0x2B00</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typ zpětné vazby : 1.. Hiperface DSL, 2.. Endat&yen;u000a2, 3..SSI, 4.. Incremental&quot;}">Typ zpětné vazby : 1.. Hiperface DSL, 2.. Endat<br>2, 3..SSI, 4.. Incremental</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-Type&quot;}">F-Type</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2C00&quot;}">0x2C00</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typ zpětné vazby : 1.. Hiperface DSL, 2.. Endat&yen;u000a2, 3..SSI, 4.. Incremental&quot;}">Typ zpětné vazby : 1.. Hiperface DSL, 2.. Endat<br>2, 3..SSI, 4.. Incremental</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-Resolution&quot;}">F-Resolution</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2B01&quot;}">0x2B01</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rozlišení zpětné vazby v rámci jedné otáčky (jen pro čtení pro digitální zpětné vzby 1 a 2)&quot;}">Rozlišení zpětné vazby v rámci jedné otáčky (jen pro čtení pro digitální zpětné vzby 1 a 2)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-Resolution&quot;}">F-Resolution</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2C01&quot;}">0x2C01</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rozlišení zpětné vazby v rámci jedné otáčky (jen pro čtení pro digitální zpětné vzby 1 a 2)&quot;}">Rozlišení zpětné vazby v rámci jedné otáčky (jen pro čtení pro digitální zpětné vzby 1 a 2)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-IncrEnc&quot;}">F-IncrEnc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2B02&quot;}">0x2B02</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pulses&quot;}">pulses</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rozlišení inkrementálního snímače&quot;}">Rozlišení inkrementálního snímače</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-IncrEnc&quot;}">F-IncrEnc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2C02&quot;}">0x2C02</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pulses&quot;}">pulses</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rozlišení inkrementálního snímače&quot;}">Rozlišení inkrementálního snímače</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-ExtIncrEnc&quot;}">F-ExtIncrEnc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2B03&quot;}">0x2B03</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pulses&quot;}">pulses</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rozlišení externího inkrementálního snímače&quot;}">Rozlišení externího inkrementálního snímače</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-ResolverPoles&quot;}">F-ResolverPoles</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2B04&quot;}">0x2B04</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet pólů resolveru (nevyužito - pouze pro&yen;u000arozšiřující desku)&quot;}">Počet pólů resolveru (nevyužito - pouze pro<br>rozšiřující desku)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;F-ResolverPoles&quot;}">F-ResolverPoles</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#D8E4BC" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback&quot;}">Feedback</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x2C04&quot;}">0x2C04</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet pólů resolveru (nevyužito - pouze pro&yen;u000arozšiřující desku)&quot;}">Počet pólů resolveru (nevyužito - pouze pro<br>rozšiřující desku)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-Command&quot;}">K-Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3100&quot;}">0x3100</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Příkaz bity[1,0]=01 .. SW enable bit[3] = 1 ..&yen;u000aReset chyb&quot;}">Příkaz bity[1,0]=01 .. SW enable bit[3] = 1 ..<br>Reset chyb</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-Command&quot;}">K-Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3200&quot;}">0x3200</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Příkaz bity[1,0]=01 .. SW enable bit[3] = 1 ..&yen;u000aReset chyb&quot;}">Příkaz bity[1,0]=01 .. SW enable bit[3] = 1 ..<br>Reset chyb</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-I&quot;}">K-I</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3101&quot;}">0x3101</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud (proudový režim = 1)&quot;}">Žádaný proud (proudový režim = 1)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-I&quot;}">K-I</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3201&quot;}">0x3201</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud (proudový režim = 1)&quot;}">Žádaný proud (proudový režim = 1)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-V&quot;}">K-V</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3102&quot;}">0x3102</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost (rychlostní režim = 2)&quot;}">Žádaná rychlost (rychlostní režim = 2)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-V&quot;}">K-V</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3202&quot;}">0x3202</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost (rychlostní režim = 2)&quot;}">Žádaná rychlost (rychlostní režim = 2)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-P_Angle&quot;}">K-P_Angle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3103&quot;}">0x3103</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná poloha - úhel (polohový režim = 3)&quot;}">Žádaná poloha - úhel (polohový režim = 3)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-P_Angle&quot;}">K-P_Angle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3203&quot;}">0x3203</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná poloha - úhel (polohový režim = 3)&quot;}">Žádaná poloha - úhel (polohový režim = 3)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-P_Revol&quot;}">K-P_Revol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3104&quot;}">0x3104</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná poloha - otáčky (polohový režim = 3)&quot;}">Žádaná poloha - otáčky (polohový režim = 3)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-P_Revol&quot;}">K-P_Revol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3204&quot;}">0x3204</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná poloha - otáčky (polohový režim = 3)&quot;}">Žádaná poloha - otáčky (polohový režim = 3)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-DigitalOutputForce_Set&quot;}">K-DigitalOutputForce_Set</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3109&quot;}">0x3109</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;nastavení výstupů s vyšší prioritou do 1&quot;}">nastavení výstupů s vyšší prioritou do 1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-DigitalOutputForce_Set&quot;}">K-DigitalOutputForce_Set</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3209&quot;}">0x3209</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;nastavení výstupů s vyšší prioritou do 1&quot;}">nastavení výstupů s vyšší prioritou do 1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-DigitalOutputForce_Clr&quot;}">K-DigitalOutputForce_Clr</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x310A&quot;}">0x310A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;nastavení výstupů s vyšší prioritou do 0&quot;}">nastavení výstupů s vyšší prioritou do 0</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;K-DigitalOutputForce_Clr&quot;}">K-DigitalOutputForce_Clr</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#4EFF4E" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command&quot;}">Command</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x320A&quot;}">0x320A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;nastavení výstupů s vyšší prioritou do 0&quot;}">nastavení výstupů s vyšší prioritou do 0</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitor-Counter&quot;}">Monitor-Counter</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3300&quot;}">0x3300</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Hlavní čítač&quot;}">Hlavní čítač</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIa&quot;}">aIa</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3301&quot;}">0x3301</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud ve fázi A&quot;}">Aktuální proud ve fázi A</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIa&quot;}">aIa</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3401&quot;}">0x3401</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud ve fázi A&quot;}">Aktuální proud ve fázi A</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIb&quot;}">aIb</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3302&quot;}">0x3302</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud ve fázi B&quot;}">Aktuální proud ve fázi B</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIb&quot;}">aIb</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3402&quot;}">0x3402</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud ve fázi B&quot;}">Aktuální proud ve fázi B</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIc&quot;}">aIc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3303&quot;}">0x3303</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud ve fázi C&quot;}">Aktuální proud ve fázi C</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIc&quot;}">aIc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3403&quot;}">0x3403</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud ve fázi C&quot;}">Aktuální proud ve fázi C</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIq&quot;}">aIq</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3306&quot;}">0x3306</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud složka Q&quot;}">Aktuální proud složka Q</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aIq&quot;}">aIq</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3406&quot;}">0x3406</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud složka Q&quot;}">Aktuální proud složka Q</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aId&quot;}">aId</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3307&quot;}">0x3307</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud složka D&quot;}">Aktuální proud složka D</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aId&quot;}">aId</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3407&quot;}">0x3407</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální proud složka D&quot;}">Aktuální proud složka D</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aAngle&quot;}">aAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3310&quot;}">0x3310</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 16}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">16</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha v rámci otáčky (rozlišení : 32&yen;u000abitů na otáčku)&quot;}">Aktuální poloha v rámci otáčky (rozlišení : 32<br>bitů na otáčku)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aAngle&quot;}">aAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3410&quot;}">0x3410</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 16}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">16</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha v rámci otáčky (rozlišení : 32&yen;u000abitů na otáčku)&quot;}">Aktuální poloha v rámci otáčky (rozlišení : 32<br>bitů na otáčku)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aRevol&quot;}">aRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3311&quot;}">0x3311</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha - počet otáček&quot;}">Aktuální poloha - počet otáček</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aRevol&quot;}">aRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3411&quot;}">0x3411</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 17}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">17</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha - počet otáček&quot;}">Aktuální poloha - počet otáček</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aSpeed&quot;}">aSpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3312&quot;}">0x3312</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální rychlost motoru&quot;}">Aktuální rychlost motoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aSpeed&quot;}">aSpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3412&quot;}">0x3412</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 18}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">18</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální rychlost motoru&quot;}">Aktuální rychlost motoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aSpeedError&quot;}">aSpeedError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3314&quot;}">0x3314</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální regulační odchylka rychlosti&quot;}">Aktuální regulační odchylka rychlosti</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aSpeedError&quot;}">aSpeedError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3414&quot;}">0x3414</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální regulační odchylka rychlosti&quot;}">Aktuální regulační odchylka rychlosti</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aAngleError&quot;}">aAngleError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x331C&quot;}">0x331C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 28}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">28</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální regulační odchylka polohy - úhel&quot;}">Aktuální regulační odchylka polohy - úhel</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aAngleError&quot;}">aAngleError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x341C&quot;}">0x341C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 28}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">28</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální regulační odchylka polohy - úhel&quot;}">Aktuální regulační odchylka polohy - úhel</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aRevolError&quot;}">aRevolError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x331D&quot;}">0x331D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 29}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">29</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální regulační odchylka polohy - otáčky&quot;}">Aktuální regulační odchylka polohy - otáčky</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aRevolError&quot;}">aRevolError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x341D&quot;}">0x341D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 29}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">29</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální regulační odchylka polohy - otáčky&quot;}">Aktuální regulační odchylka polohy - otáčky</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aDriveStatus&quot;}">aDriveStatus</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3325&quot;}">0x3325</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 37}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">37</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;--&quot;}">--</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stav servozesilovače : bit[0] = 1 .. Enabled, bit[1]&yen;u000a= 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6]&yen;u000a= 1 ..fieldbus mode, ..............&quot;}">Stav servozesilovače : bit[0] = 1 .. Enabled, bit[1]<br>= 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6]<br>= 1 ..fieldbus mode, ..............</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aDriveStatus&quot;}">aDriveStatus</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3425&quot;}">0x3425</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 37}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">37</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;--&quot;}">--</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stav servozesilovače : bit[0] = 1 .. Enabled, bit[1]&yen;u000a= 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6]&yen;u000a= 1 ..fieldbus mode, ..............&quot;}">Stav servozesilovače : bit[0] = 1 .. Enabled, bit[1]<br>= 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6]<br>= 1 ..fieldbus mode, ..............</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aDriveError&quot;}">aDriveError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3326&quot;}">0x3326</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 38}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">38</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;--&quot;}">--</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Chyba servozesilovače (viz manuál)&quot;}">Chyba servozesilovače (viz manuál)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aDriveError&quot;}">aDriveError</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3426&quot;}">0x3426</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 38}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">38</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;--&quot;}">--</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Chyba servozesilovače (viz manuál)&quot;}">Chyba servozesilovače (viz manuál)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aDriveWarning&quot;}">aDriveWarning</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3327&quot;}">0x3327</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 39}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">39</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;--&quot;}">--</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Varování (nevyužito)&quot;}">Varování (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aDriveWarning&quot;}">aDriveWarning</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3427&quot;}">0x3427</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 39}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">39</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;--&quot;}">--</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Varování (nevyužito)&quot;}">Varování (nevyužito)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;AnInput&quot;}">AnInput</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3328&quot;}">0x3328</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 40}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">40</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analogový vstup 1&quot;}">Analogový vstup 1</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;AnInput&quot;}">AnInput</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3428&quot;}">0x3428</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 40}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">40</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0,0%&quot;, &quot;3&quot;: 1}">0,1%</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analogový vstup 2&quot;}">Analogový vstup 2</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;VoltDCLink&quot;}">VoltDCLink</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3329&quot;}">0x3329</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 41}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">41</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;V&quot;}">V</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Napětí meziobvodu&quot;}">Napětí meziobvodu</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OnChipTemp&quot;}">OnChipTemp</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x332A&quot;}">0x332A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 42}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">42</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;deg&quot;}">deg</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Teplota procesoru&quot;}">Teplota procesoru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_SetPointAngle&quot;}">ec_SetPointAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x332B&quot;}">0x332B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 43}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">43</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadovaná poloha v rámci otáčky - řízení přes&yen;u000asběrnici&quot;}">Požadovaná poloha v rámci otáčky - řízení přes<br>sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_SetPointAngle&quot;}">ec_SetPointAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x342B&quot;}">0x342B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 43}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">43</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadovaná poloha v rámci otáčky - řízení přes&yen;u000asběrnici&quot;}">Požadovaná poloha v rámci otáčky - řízení přes<br>sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_SetPointRevol&quot;}">ec_SetPointRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x332C&quot;}">0x332C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 44}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">44</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadovaná poloha počet otáček - řízení přes&yen;u000asběrnici&quot;}">Požadovaná poloha počet otáček - řízení přes<br>sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_SetPointRevol&quot;}">ec_SetPointRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x342C&quot;}">0x342C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 44}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">44</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Požadovaná poloha počet otáček - řízení přes&yen;u000asběrnici&quot;}">Požadovaná poloha počet otáček - řízení přes<br>sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_control&quot;}">ec_control</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x332D&quot;}">0x332D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 45}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">45</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Řídící registr - řízení přes sběrnici&quot;}">Řídící registr - řízení přes sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_control&quot;}">ec_control</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x342D&quot;}">0x342D</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 45}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">45</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Řídící registr - řízení přes sběrnici&quot;}">Řídící registr - řízení přes sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_currentSetPoint&quot;}">ec_currentSetPoint</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x332E&quot;}">0x332E</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 46}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">46</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud - řízení přes sběrnici&quot;}">Žádaný proud - řízení přes sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_currentSetPoint&quot;}">ec_currentSetPoint</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x342E&quot;}">0x342E</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 46}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">46</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud - řízení přes sběrnici&quot;}">Žádaný proud - řízení přes sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_currentLimit&quot;}">ec_currentLimit</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x332F&quot;}">0x332F</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 47}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">47</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Proudové omezení - řízení přes sběrnici&quot;}">Proudové omezení - řízení přes sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ec_currentLimit&quot;}">ec_currentLimit</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x342F&quot;}">0x342F</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 47}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">47</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Proudové omezení - řízení přes sběrnici&quot;}">Proudové omezení - řízení přes sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digital_Inputs&quot;}">Digital_Inputs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3330&quot;}">0x3330</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 48}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">48</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digitální vstupy : bit[0] .. IN1,bit[1] .. IN3,bit[2]&yen;u000a.. IN5,bit[3] .. IN7&quot;}">Digitální vstupy : bit[0] .. IN1,bit[1] .. IN3,bit[2]<br>.. IN5,bit[3] .. IN7</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digital_Inputs&quot;}">Digital_Inputs</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3430&quot;}">0x3430</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 48}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">48</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digitální vstupy : bit[0] .. IN2,bit[1] .. IN4,bit[2]&yen;u000a.. IN6,bit[3] .. IN8&quot;}">Digitální vstupy : bit[0] .. IN2,bit[1] .. IN4,bit[2]<br>.. IN6,bit[3] .. IN8</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor_temperature&quot;}">Motor_temperature</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3331&quot;}">0x3331</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 49}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">49</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ohm&quot;}">Ohm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpor teplotního čidla motoru (pouze pro digitální zpětnou vazbu s připojeným teplotním&yen;u000ačidlem)&quot;}">Odpor teplotního čidla motoru (pouze pro digitální zpětnou vazbu s připojeným teplotním<br>čidlem)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor_temperature&quot;}">Motor_temperature</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3431&quot;}">0x3431</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 49}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">49</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ohm&quot;}">Ohm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Odpor teplotního čidla motoru (pouze pro&yen;u000adigitální zpětnou vazbu s připojeným teplotním čidlem)&quot;}">Odpor teplotního čidla motoru (pouze pro<br>digitální zpětnou vazbu s připojeným teplotním čidlem)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rIq&quot;}">rIq</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3332&quot;}">0x3332</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 50}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">50</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud (vstup do proudového regulátoru)&quot;}">Žádaný proud (vstup do proudového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rIq&quot;}">rIq</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3432&quot;}">0x3432</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 50}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">50</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud (vstup do proudového regulátoru)&quot;}">Žádaný proud (vstup do proudového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ia_rms&quot;}">Ia_rms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3333&quot;}">0x3333</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 51}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">51</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Efektivní hodnota proudu Ia&quot;}">Efektivní hodnota proudu Ia</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ia_rms&quot;}">Ia_rms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3433&quot;}">0x3433</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 51}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">51</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Efektivní hodnota proudu Ia&quot;}">Efektivní hodnota proudu Ia</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ib_rms&quot;}">Ib_rms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3334&quot;}">0x3334</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 52}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">52</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Efektivní hodnota proudu Ib&quot;}">Efektivní hodnota proudu Ib</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ib_rms&quot;}">Ib_rms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3434&quot;}">0x3434</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 52}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">52</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Efektivní hodnota proudu Ib&quot;}">Efektivní hodnota proudu Ib</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ic_rms&quot;}">Ic_rms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3335&quot;}">0x3335</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 53}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">53</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Efektivní hodnota proudu Ic&quot;}">Efektivní hodnota proudu Ic</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ic_rms&quot;}">Ic_rms</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3435&quot;}">0x3435</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 53}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">53</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Efektivní hodnota proudu Ic&quot;}">Efektivní hodnota proudu Ic</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aI2t&quot;}">aI2t</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3337&quot;}">0x3337</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 55}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">55</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Hodnota I2t&quot;}">Hodnota I2t</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;aI2t&quot;}">aI2t</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3437&quot;}">0x3437</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 55}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">55</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mA&quot;}">mA</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Hodnota i2t&quot;}">Hodnota i2t</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rAngle&quot;}">rAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3338&quot;}">0x3338</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 56}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">56</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná hodnota polohy - v rámci otáčky (vstup&yen;u000apolohového regulátoru)&quot;}">Žádaná hodnota polohy - v rámci otáčky (vstup<br>polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rAngle&quot;}">rAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3438&quot;}">0x3438</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 56}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">56</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná hodnota polohy - v rámci otáčky (vstup&yen;u000apolohového regulátoru)&quot;}">Žádaná hodnota polohy - v rámci otáčky (vstup<br>polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rRevol&quot;}">rRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3339&quot;}">0x3339</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 57}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">57</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná hodnota polohy - počet otáček (vstup&yen;u000apolohového regulátoru)&quot;}">Žádaná hodnota polohy - počet otáček (vstup<br>polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rRevol&quot;}">rRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3439&quot;}">0x3439</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 57}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">57</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná hodnota polohy - počet otáček (vstup&yen;u000apolohového regulátoru)&quot;}">Žádaná hodnota polohy - počet otáček (vstup<br>polohového regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rSpeed&quot;}">rSpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x333A&quot;}">0x333A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 58}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">58</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost (vstup rychlostního regulátoru)&quot;}">Žádaná rychlost (vstup rychlostního regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rSpeed&quot;}">rSpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x343A&quot;}">0x343A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 58}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">58</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;rpm&quot;}">rpm</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost (vstup rychlostního regulátoru)&quot;}">Žádaná rychlost (vstup rychlostního regulátoru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DSL_status&quot;}">DSL_status</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x333B&quot;}">0x333B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 59}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">59</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;bit&quot;}">bit</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stav DSL enkodéru&quot;}">Stav DSL enkodéru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DSL_status&quot;}">DSL_status</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x343B&quot;}">0x343B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 59}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">59</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;bit&quot;}">bit</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stav DSL enkodéru&quot;}">Stav DSL enkodéru</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DO&quot;}">DO</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x333C&quot;}">0x333C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 60}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">60</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;bit&quot;}">bit</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digitální výstupy: bit[0] .. Out1, bit[1] .. Out3,&yen;u000abit[2] .. Out5&quot;}">Digitální výstupy: bit[0] .. Out1, bit[1] .. Out3,<br>bit[2] .. Out5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DO&quot;}">DO</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x343C&quot;}">0x343C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 20}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">20</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 60}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">60</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;bit&quot;}">bit</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digitální výstupy: bit[0] .. Out2, bit[1] .. Out4,&yen;u000abit[2] .. Out6&quot;}">Digitální výstupy: bit[0] .. Out2, bit[1] .. Out4,<br>bit[2] .. Out6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;C-PackeTime&quot;}">C-PackeTime</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#8CAF46" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Monitoring&quot;}">Monitoring</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3340&quot;}">0x3340</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 19}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">19</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 64}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">64</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Měřený čas mezi pakety při řízení po sběrnici&quot;}">Měřený čas mezi pakety při řízení po sběrnici</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Acc&quot;}">Acc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3900&quot;}">0x3900</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s2&quot;}">pginc/s2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádané zrychlení pohybu [ inc&yen;/s2 ] .. Viz funkční&yen;u000amanuál&quot;}">Žádané zrychlení pohybu [ inc/s2 ] .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Acc&quot;}">Acc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A00&quot;}">0x3A00</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 0}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">0</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s2&quot;}">pginc/s2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádané zrychlení pohybu [ inc&yen;/s2 ] .. Viz funkční&yen;u000amanuál&quot;}">Žádané zrychlení pohybu [ inc/s2 ] .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Dec&quot;}">Dec</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3901&quot;}">0x3901</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s2&quot;}">pginc/s2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádané zpomalení pohybu [ inc&yen;/s2 ] .. Viz&yen;u000afunkční manuál&quot;}">Žádané zpomalení pohybu [ inc/s2 ] .. Viz<br>funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Dec&quot;}">Dec</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A01&quot;}">0x3A01</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 1}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s2&quot;}">pginc/s2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádané zpomalení pohybu [ inc&yen;/s2 ] .. Viz&yen;u000afunkční manuál&quot;}">Žádané zpomalení pohybu [ inc/s2 ] .. Viz<br>funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;APosAngle&quot;}">APosAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3902&quot;}">0x3902</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha na výstupu pg .. Viz funkční&yen;u000amanuál&quot;}">Aktuální poloha na výstupu pg .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;APosAngle&quot;}">APosAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A02&quot;}">0x3A02</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 2}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha na výstupu pg .. Viz funkční&yen;u000amanuál&quot;}">Aktuální poloha na výstupu pg .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;APosRevol&quot;}">APosRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3903&quot;}">0x3903</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha na výstupu pg .. Viz funkční&yen;u000amanuál&quot;}">Aktuální poloha na výstupu pg .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;APosRevol&quot;}">APosRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A03&quot;}">0x3A03</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 3}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální poloha na výstupu pg .. Viz funkční&yen;u000amanuál&quot;}">Aktuální poloha na výstupu pg .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DPosAngle&quot;}">DPosAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3904&quot;}">0x3904</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cílová poloha .. Viz funkční manuál&quot;}">Cílová poloha .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DPosAngle&quot;}">DPosAngle</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A04&quot;}">0x3A04</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 4}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">4</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cílová poloha .. Viz funkční manuál&quot;}">Cílová poloha .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DPosRevol&quot;}">DPosRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3905&quot;}">0x3905</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cílová poloha .. Viz funkční manuál&quot;}">Cílová poloha .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DPosRevol&quot;}">DPosRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A05&quot;}">0x3A05</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 5}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">5</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;inc&quot;}">inc</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cílová poloha .. Viz funkční manuál&quot;}">Cílová poloha .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ASpeed&quot;}">ASpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3906&quot;}">0x3906</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s&quot;}">pginc/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální rychlost na výstupu pg .. Viz funkční&yen;u000amanuál&quot;}">Aktuální rychlost na výstupu pg .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ASpeed&quot;}">ASpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A06&quot;}">0x3A06</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 6}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">6</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-only&quot;}">read-only</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s&quot;}">pginc/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální rychlost na výstupu pg .. Viz funkční&yen;u000amanuál&quot;}">Aktuální rychlost na výstupu pg .. Viz funkční<br>manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PosSpeed&quot;}">PosSpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3907&quot;}">0x3907</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s&quot;}">pginc/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost v polohovém módu .. Viz&yen;u000afunkční manuál&quot;}">Žádaná rychlost v polohovém módu .. Viz<br>funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PosSpeed&quot;}">PosSpeed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A07&quot;}">0x3A07</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 7}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">7</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s&quot;}">pginc/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost v polohovém módu .. Viz&yen;u000afunkční manuál&quot;}">Žádaná rychlost v polohovém módu .. Viz<br>funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Speed&quot;}">Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3908&quot;}">0x3908</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s&quot;}">pginc/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost v rychlostním módu .. Viz&yen;u000afunkční manuál&quot;}">Žádaná rychlost v rychlostním módu .. Viz<br>funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Speed&quot;}">Speed</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A08&quot;}">0x3A08</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 8}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">8</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;pginc&yen;/s&quot;}">pginc/s</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost v rychlostním módu .. Viz&yen;u000afunkční manuál&quot;}">Žádaná rychlost v rychlostním módu .. Viz<br>funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Mode&quot;}">Mode</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3909&quot;}">0x3909</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Režim generátoru profilu 0 = rychlostní režim, 1&yen;u000a= polohový režim, 2 = (pouze pro čtení) zpomalování v polohovém režimu .. Viz manuál&quot;}">Režim generátoru profilu 0 = rychlostní režim, 1<br>= polohový režim, 2 = (pouze pro čtení) zpomalování v polohovém režimu .. Viz manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Mode&quot;}">Mode</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A09&quot;}">0x3A09</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 9}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">9</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Režim generátoru profilu 0 = rychlostní režim, 1&yen;u000a= polohový režim, 2 = (pouze pro čtení) zpomalování v polohovém režimu .. Viz manuál&quot;}">Režim generátoru profilu 0 = rychlostní režim, 1<br>= polohový režim, 2 = (pouze pro čtení) zpomalování v polohovém režimu .. Viz manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rdy&quot;}">Rdy</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x390A&quot;}">0x390A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signalizace polohování: 1 = dosažena cílová&yen;u000apoloha .. Viz funkční manuál&quot;}">Signalizace polohování: 1 = dosažena cílová<br>poloha .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rdy&quot;}">Rdy</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A0A&quot;}">0x3A0A</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 10}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">10</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signalizace polohování: 1 = dosažena cílová&yen;u000apoloha .. Viz funkční manuál&quot;}">Signalizace polohování: 1 = dosažena cílová<br>poloha .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Type&quot;}">Type</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x390B&quot;}">0x390B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typ rychlostního profilu : 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. Viz funkční manuál&quot;}">Typ rychlostního profilu : 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Type&quot;}">Type</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A0B&quot;}">0x3A0B</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 11}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">11</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typ rychlostního profilu : 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. Viz funkční manuál&quot;}">Typ rychlostního profilu : 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;BitsPerRevol&quot;}">BitsPerRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 1&quot;}">Axis 1</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x390C&quot;}">0x390C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 25}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">25</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet bitů na otáčku pro vnitřní výpočty pg. Ovlivňuje rozlišení rychlostí a zrychlení&yen;u000a(zpomalení) .. Viz funkční manuál&quot;}">Počet bitů na otáčku pro vnitřní výpočty pg. Ovlivňuje rozlišení rychlostí a zrychlení<br>(zpomalení) .. Viz funkční manuál</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;BitsPerRevol&quot;}">BitsPerRevol</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Axis 2&quot;}">Axis 2</td>
		<td bgcolor="#E26A09" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PG&quot;}">PG</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0x3A0C&quot;}">0x3A0C</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 26}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">26</td>
		<td data-sheets-value="{ &quot;1&quot;: 3, &quot;3&quot;: 12}" data-sheets-numberformat="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;0&quot;, &quot;3&quot;: 1}">12</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;read-write&quot;}">read-write</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-&quot;}">-</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;32 bits&quot;}">32 bits</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Počet bitů na otáčku pro vnitřní výpočty pg.&yen;u000aOvlivňuje rozlišení rychlostí a zrychlení (zpomalení) .. Viz funkční manuál&quot;}">Počet bitů na otáčku pro vnitřní výpočty pg.<br>Ovlivňuje rozlišení rychlostí a zrychlení (zpomalení) .. Viz funkční manuál</td>
	</tr>
</table>
