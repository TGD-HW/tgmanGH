Popis komunikace průmyslové sběrnice EtherCAT.

##Distribuované hodiny (DC)
Funkce distribuovaných hodin (DC) je podporována. Perioda synchronizovaného signálu 1 musí být nastavena na stejnou periodu jako komunikační perioda PDO.

##Procesní datové objekty (PDO) {#ECAT_PDO}
Ethercat master může použít následující komunikační periody PDO: 250us, 500us, 1000us, 2000us, (50us pro konkrétní konfiguraci).
Servopohon používá fixní mapování PDO, které je popsáno v tabulce níže. Délka PDO je 44 bajtů.

**Výstup PDO pro servopohon**

<table style="text-align: left;">
<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název&quot;}"><b>Název</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typ&quot;}"><b>Typ</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Popis&quot;}"><b>Popis</b></td>
	</tr>
	<tr>
		<td rowspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;PositionSetPoint_1 or&yen;u000aSpeedSetPoint_1&quot;}">PositionSetPoint_1 or<br>SpeedSetPoint_1</td>
		<td rowspan="5" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 64bit integer&quot;}">Signed 64bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Poziční režim (3):&quot;}"><b>Poziční režim (3):</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná poloha pro servopohon 1. Rozlišení 32 bitů&yen;/ot.&yen;u000aPříklad :&yen;u000a1.5 otáčky :&yen;u000a6442450944 = 0x0000000180000000&yen;u000a-1.5 otáčky :&yen;u000a-6442450944 = 0xFFFFFFFE80000000&quot;}">Žádaná poloha pro servopohon 1. Rozlišení 32 bitů/ot.<br>Příklad :<br>1.5 otáčky :<br>6442450944 = 0x0000000180000000<br>-1.5 otáčky :<br>-6442450944 = 0xFFFFFFFE80000000</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rychlostní režim (10):&quot;}"><b>Rychlostní režim (10):</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost pro servopohon 1. &yen;u000aRozlišení 1 ot&yen;/min ~ 2^32&yen;u000aPříklad 500 ot&yen;/min :&yen;u000a2147483648000 = 0x1F4 0000 0000&quot;}">Žádaná rychlost pro servopohon 1.<br>Rozlišení 1 ot/min ~ 2^32<br>Příklad 500 ot/min :<br>2147483648000 = 0x1F4 0000 0000</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-500 ot&yen;/min :&yen;u000a-2147483648000 = 0xFFFF FE0C 0000 0000&quot;}">-500 ot/min :<br>-2147483648000 = 0xFFFF FE0C 0000 0000</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;control_1&quot;}">control_1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32bit integer&quot;}">Unsigned 32bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ovládací příkazy pro servopohon 1. &yen;u000aBit0 .. Vymazat chyby.&yen;u000aBit1 .. Povolení výkonového stupně.&yen;u000aBit28 .. Digitální výstup 1 &yen;u000aBit29 .. Digitální výstup 3 &yen;u000aBit30 .. Digitální výstup 5&quot;}">Ovládací příkazy pro servopohon 1.<br>Bit0 .. Vymazat chyby.<br>Bit1 .. Povolení výkonového stupně.<br>Bit28 .. Digitální výstup 1<br>Bit29 .. Digitální výstup 3<br>Bit30 .. Digitální výstup 5</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;currentSetPoint_1&quot;}">currentSetPoint_1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 16bit integer&quot;}">Signed 16bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud pro servopohon 1. &yen;u000aIqSetPoint = currentSetPoint_1 * M-Ipeak &yen;/ 32767&quot;}">Žádaný proud pro servopohon 1.<br>IqSetPoint = currentSetPoint_1 * M-Ipeak / 32767</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;currentLimit_1&quot;}">currentLimit_1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 16bit integer&quot;}">Unsigned 16bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení proudu pro servopohon 1. &yen;u000aIqLim = (32767 - currentLimit_1)* M-Ipeak &yen;/ 32767&yen;u000a32767 .. plné omezení&yen;u000a0 .. bez omezení (maximální proud = M- Ipeak)&quot;}">Omezení proudu pro servopohon 1.<br>IqLim = (32767 - currentLimit_1)* M-Ipeak / 32767<br>32767 .. plné omezení<br>0 .. bez omezení (maximální proud = M- Ipeak)</td>
	</tr>
	<tr>
		<td rowspan="13" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;positionSetPoint_2&yen;u000aor&yen;u000aspeedSetPoint_2&quot;}">positionSetPoint_2<br>or<br>speedSetPoint_2</td>
		<td rowspan="13" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 64bit integer&quot;}">Signed 64bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Poziční režim (3):&yen;u000aŽádaná poloha pro servopohon 2.&quot;}">Poziční režim (3):<br>Žádaná poloha pro servopohon 2.</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rozlišení 32 bitů&yen;/ot.&quot;}">Rozlišení 32 bitů/ot.</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Příklad pozičního režimu (0x3):&quot;}">Příklad pozičního režimu (0x3):</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;1.5 otáčky :&quot;}">1.5 otáčky :</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;6442450944 = 0x0000000180000000&quot;}">6442450944 = 0x0000000180000000</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-1.5 otáčky :&quot;}">-1.5 otáčky :</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-6442450944 = 0xFFFFFFFE80000000&quot;}">-6442450944 = 0xFFFFFFFE80000000</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rychlostní režim (10):&quot;}"><b>Rychlostní režim (10):</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaná rychlost pro servopohon 2.&quot;}">Žádaná rychlost pro servopohon 2.</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rozlišení 1 ot&yen;/min ~ 2^32&quot;}">Rozlišení 1 ot/min ~ 2^32</td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Příklad :&yen;u000a500 ot&yen;/min :&yen;u000a2147483648000 = 0x1F4 0000 0000&yen;u000a-500 ot&yen;/min :&yen;u000a-2147483648000 = 0xFFFF FE0C 0000 0000&quot;}">Příklad :<br>500 ot/min :<br>2147483648000 = 0x1F4 0000 0000<br>-500 ot/min :<br>-2147483648000 = 0xFFFF FE0C 0000 0000</td>
	</tr>
	<tr>
	</tr>
	<tr>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;control_2&quot;}">control_2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32bit integer&quot;}">Unsigned 32bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Ovládací příkazy pro servopohon 2. &yen;u000aBit0 .. Vymazat chyby.&yen;u000aBit1 .. Enable power stage.&yen;u000aBit28 .. Digitální výstup 2&yen;u000aBit29 .. Digitální výstup 4&yen;u000aBit30 .. Digitální výstup 6&quot;}">Ovládací příkazy pro servopohon 2.<br>Bit0 .. Vymazat chyby.<br>Bit1 .. Enable power -stage.<br>Bit28 .. Digitální výstup 2<br>Bit29 .. Digitální výstup 4<br>Bit30 .. Digitální výstup 6</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;currentSetPoint_2&quot;}">currentSetPoint_2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 16bit integer&quot;}">Signed 16bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Žádaný proud pro servopohon 2. &yen;u000aIqSetPoint = currentSetPoint_2 * M-Ipeak &yen;/ 32767&quot;}">Žádaný proud pro servopohon 2.<br>IqSetPoint = currentSetPoint_2 * M-Ipeak / 32767</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;currentLimit_2&quot;}">currentLimit_2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 16bit integer&quot;}">Unsigned 16bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Omezení proudu pro servopohon 2. &yen;u000aIqLim = (32767 - currentLimit_2)* M-Ipeak &yen;/ 32767&yen;u000a32767 .. plné omezení&yen;u000a0 .. bez omezení (maximální proud = M- Ipeak)&quot;}">Omezení proudu pro servopohon 2.<br>IqLim = (32767 - currentLimit_2)* M-Ipeak / 32767<br>32767 .. plné omezení<br>0 .. bez omezení (maximální proud = M- Ipeak)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Reserved_1&quot;}">Reserved_1</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32bit integer&quot;}">Unsigned 32bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Reserved_2&quot;}">Reserved_2</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32bit integer&quot;}">Unsigned 32bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Reserved_3&quot;}">Reserved_3</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32bit integer&quot;}">Unsigned 32bit integer</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
</table>

**Vstup PDO od servopohonu**

<table style="text-align: left;">
		<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Název&quot;}"><b>Název</b></td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Typ&quot;}"><b>Typ</b></td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Popis&quot;}"><b>Popis</b></td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;positionActValue_1&quot;}">positionActValue_1</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 64bit integer&quot;}">Signed 64bit integer</td>
		<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální pozice servopohonu 1. &yen;u000aRozlišení 32 bitů&yen;/ot.&yen;u000a&yen;u000aPříklad:&yen;u000a1.5 otáčky :&yen;u000a6442450944 = 0x0000000180000000&yen;u000a-1.5 otáčky :&yen;u000a-6442450944 = 0xFFFFFFFE80000000&quot;}">Aktuální pozice servopohonu 1.<br>Rozlišení 32 bitů/ot.<br></tr>
		<tr>
			<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;positionActValue_2&quot;}">positionActValue_2</td>
			<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 64bit integer&quot;}">Signed 64bit integer</td>
			<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální pozice servopohonu 2. &yen;u000aRozlišení 32 bitů&yen;/ot.&yen;u000a&yen;u000aPříklad:&yen;u000a1.5 otáčky :&yen;u000a6442450944 = 0x0000000180000000&yen;u000a-1.5 otáčky :&yen;u000a-6442450944 = 0xFFFFFFFE80000000&quot;}">Aktuální pozice servopohonu 2.<br>Rozlišení 32 bitů/ot.<br></tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;positionActValueExt&quot;}">positionActValueExt</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 32bit integer&quot;}">Signed 32bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Externí pozice zpětné vazby E.&quot;}">Externí pozice zpětné vazby E.</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;status_1&quot;}">status_1</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32bit integer&quot;}">Unsigned 32bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stav servopohonu 1.&yen;u000aBit0 .. Výkonový stupeň povolen – pod&yen;u000anapětím.&yen;u000aBit1 .. aktivní HW enable.&yen;u000aBit2 .. aktivní Software enable. &yen;u000aBit3 .. brzda motoru uvolněna. &yen;u000aBit4 .. Žádná chyba.&yen;u000aBit5 .. Inicializace. &yen;u000aBit6 .. režim Fieldbus.&yen;u000aBit28 .. Digitální vstup 1 &yen;u000aBit29 .. Digitální vstup 3 &yen;u000aBit30 .. Digitální vstup 5&yen;u000aBit31 .. Digitální vstup 7&quot;}">Stav servopohonu 1.<br>Bit0 .. Výkonový stupeň povolen – pod<br>napětím.<br>Bit1 .. aktivní HW enable.<br>Bit2 .. aktivní Software enable.<br>Bit3 .. brzda motoru uvolněna.<br>Bit4 .. Žádná chyba.<br>Bit5 .. Inicializace.<br>Bit6 .. režim Fieldbus.<br>Bit28 .. Digitální vstup 1<br>Bit29 .. Digitální vstup 3<br>Bit30 .. Digitální vstup 5<br>Bit31 .. Digitální vstup 7</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;status_2&quot;}">status_2</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32bit integer&quot;}">Unsigned 32bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Stav servopohonu 2.&yen;u000aBit0 .. Výkonový stupeň povolen – pod&yen;u000anapětím&yen;u000aBit1 .. aktivní HW enable.&yen;u000aBit2 .. aktivní Software enable. &yen;u000aBit3 .. brzda motoru uvolněna. &yen;u000aBit4 .. Žádná chyba.&yen;u000aBit5 .. Inicializace. &yen;u000aBit6 .. režim Fieldbus.&yen;u000aBit28 .. Digitální vstup 2 &yen;u000aBit29 .. Digitální vstup 4 &yen;u000aBit30 .. Digitální vstup 6&yen;u000aBit31 .. Digitální vstup 8&quot;}">Stav servopohonu 2.<br>Bit0 .. Výkonový stupeň povolen – pod<br>napětím<br>Bit1 .. aktivní HW enable.<br>Bit2 .. aktivní Software enable.<br>Bit3 .. brzda motoru uvolněna.<br>Bit4 .. Žádná chyba.<br>Bit5 .. Inicializace.<br>Bit6 .. režim Fieldbus.<br>Bit28 .. Digitální vstup 2<br>Bit29 .. Digitální vstup 4<br>Bit30 .. Digitální vstup 6<br>Bit31 .. Digitální vstup 8</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;analogInput_1&quot;}">analogInput_1</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 16bit integer&quot;}">Unsigned 16bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální hodnota analogového vstupu 1.&yen;u000a0 .. 0V , 32767 .. 10V&quot;}">Aktuální hodnota analogového vstupu 1.<br>0 .. 0V , 32767 .. 10V</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;analogInput_2&quot;}">analogInput_2</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 16bit integer&quot;}">Unsigned 16bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Aktuální hodnota analogového vstupu 2.&yen;u000a0 .. 0V , 32767 .. 10V&quot;}">Aktuální hodnota analogového vstupu 2.<br>0 .. 0V , 32767 .. 10V</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;currentqActValue_1&quot;}">currentqActValue_1</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 16bit integer&quot;}">Signed 16bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-32768 .. -M-Ipeak, 32767 .. M-Ipeak&yen;u000aI = M-Ipeak * currentqActValue &yen;/ 32767&quot;}">-32768 .. -M-Ipeak, 32767 .. M-Ipeak<br>I = M-Ipeak * currentqActValue / 32767</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;currentqActValue_2&quot;}">currentqActValue_2</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Signed 16bit integer&quot;}">Signed 16bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;-32768 .. -M-Ipeak, 32767 .. M-Ipeak&yen;u000aI = M-Ipeak * currentqActValue &yen;/ 32767&quot;}">-32768 .. -M-Ipeak, 32767 .. M-Ipeak<br>I = M-Ipeak * currentqActValue / 32767</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mappedParameter_1&quot;}">mappedParameter_1</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32 bit integer&quot;}">Unsigned 32 bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Hodnota registru definovaná v parametru C-MapingPar1&quot;}">Hodnota registru definovaná v parametru C-MapingPar1</td>
			</tr>
			<tr>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;mappedParameter_2&quot;}">mappedParameter_2</td>
				<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Unsigned 32 bit integer&quot;}">Unsigned 32 bit integer</td>
				<td colspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Hodnota registru definovaná v parametru C- MapingPar2&quot;}">Hodnota registru definovaná v parametru C- MapingPar2</td>
			</tr>
		</table>
		
##Servisní datové objekty (SDO)
Pro SDO se používá protokol CAN Open over EtherCat.

<table>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Schránka - výstup&quot;}"><b>Schránka - výstup</b></td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Schránka - vstup&quot;}"><b>Schránka - vstup</b></td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 0&quot;}">Byte 0</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Datová délka (Low Byte)&quot;}">Datová délka (Low Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 1&quot;}">Byte 1</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Datová délka (High Byte)&quot;}">Datová délka (High Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 2&quot;}">Byte 2</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Adresa (Low Byte)&quot;}">Adresa (Low Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 3&quot;}">Byte 3</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Adresa (High Byte)&quot;}">Adresa (High Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 4&quot;}">Byte 4</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 0 až 5: Kanál&yen;u000aBit 6 až 7: Priorita&quot;}">Bit 0 až 5: Kanál<br>Bit 6 až 7: Priorita</td>
	</tr>
	<tr>
		<td rowspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 5&quot;}">Byte 5</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 0 až 3: Typ =&yen;u000a3 : Can přes EtherCAT&quot;}">Bit 0 až 3: Typ =<br>3 : Can přes EtherCAT</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 4 až 7: Rezervováno&quot;}">Bit 4 až 7: Rezervováno</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 6&quot;}">Byte 6</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;číslo PDO (pouze s přenosem PDO, Bit 0 = LSB čísla PDO, viz. Byte 7 pro MSB)&quot;}">číslo PDO (pouze s přenosem PDO, Bit 0 = LSB čísla PDO, viz. Byte 7 pro MSB)</td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 7&quot;}">Byte 7</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 0: MSB čísla PDO, viz Byte 6&quot;}">Bit 0: MSB čísla PDO, viz Byte 6</td>
	</tr>
	<tr>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 1 až 3: Rezervováno&quot;}">Bit 1 až 3: Rezervováno</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 4 až 7: konkrétní typ CoE =&yen;u000a2 : požadavek SDO&quot;}">Bit 4 až 7: konkrétní typ CoE =<br>2 : požadavek SDO</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Bit 4 až 7: konkrétní typ CoE=&yen;u000a3: odpověď SDO&quot;}">Bit 4 až 7: konkrétní typ CoE=<br>3: odpověď SDO</td>
	</tr>
	<tr>
		<td rowspan="3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 8&quot;}">Byte 8</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Control-Byte v CAN datovém bloku:&quot;}">Control-Byte v CAN datovém bloku:</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Write access 0x2? .. 4byte&quot;}">Write access 0x2? .. 4byte</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Write: OK 0x2? Error 0x80&quot;}">Write: OK 0x2? Error 0x80</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Read access 0x4? .. 4byte&quot;}">Read access 0x4? .. 4byte</td>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Read: OK 0x4? Error 0x80&quot;}">Read: OK 0x4? Error 0x80</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 9&quot;}">Byte 9</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Nižší Byte čísla objektu CAN (číslo parametru)&quot;}">Nižší Byte čísla objektu CAN (číslo parametru)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 10&quot;}">Byte 10</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Vyšší Byte čísla objektu CAN (číslo skupiny parametrů)&quot;}">Vyšší Byte čísla objektu CAN (číslo skupiny parametrů)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 11&quot;}">Byte 11</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Subindex podle specifikace CANopen (nepoužívá se)&quot;}">Subindex podle specifikace CANopen (nepoužívá se)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 12&quot;}">Byte 12</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data (Nejnižší Byte)&quot;}">Data (Nejnižší Byte)</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 13&quot;}">Byte 13</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data&quot;}">Data</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 14&quot;}">Byte 14</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data&quot;}">Data</td>
	</tr>
	<tr>
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Byte 15&quot;}">Byte 15</td>
		<td colspan="2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Data (Nejvyšší Byte)&quot;}">Data (Nejvyšší Byte)</td>
	</tr>
</table>

##Registry

| Název | Popis |
|---|---|
| C-ID  | TGZ EtherCat alias. |
| C-SetCycleTime | Parametr C-SetCycleTime musí být nastaven na správnou hodnotu komunikační periody EtherCatu. |
| C-SyncTime | Skutečná naměřená perioda generovaného synchronizovaného signálu - jen pro distribuované hodiny (DC). |
| C-MapingPar1 | Adresa parametru zvoleného pro PDO mapování 1. |
| C-MapingPar2 | Adresa parametru zvoleného pro PDO mapování 2. |
| Monitoring-PacketTime | Skutečná naměřená perioda mezi EtherCat packety. |
