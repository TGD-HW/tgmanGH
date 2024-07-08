##Struktura UDP dat
První dva bajty dat jsou identifikátor.
Konstantní dva znaky jsou „GT“ `0x4754`.
Následující bajty označené jako Byte `0`, `1` atd. v následující tabulce představují vlastní příkazy a data.
Popis je níže.

<table>
	<tr>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b><i></i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 0&quot;}"><b><i>byte 0</i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 1&quot;}"><b><i>byte 1</i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 2&quot;}"><b><i>byte 2</i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 3&quot;}"><b><i>byte 3</i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 4&quot;}"><b><i>byte 4</i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 5&quot;}"><b><i>byte 5</i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 6&quot;}"><b><i>byte 6</i></b></td>
		<td bgcolor="#005050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 7&quot;}"><b><i>byte 7</i></b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;request (m ->sl)&quot;}">request (m -&gt; sl)</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;1 – Reading a32 bit register&quot;}">1 – Reading a32 bit register</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;1 (OK)&quot;}">1 (OK)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#C6E0B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OK&quot;}">OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;1 (Err)&quot;}">1 (Err)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#F07C7C" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;err&quot;}">err</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;request (m ->sl)&quot;}">request (m -&gt; sl)</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;2 – write a32-bit register&quot;}">2 – write a32-bit register</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;2 (OK)&quot;}">2 (OK)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#C6E0B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OK&quot;}">OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;2 (Err)&quot;}">2 (Err)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#F07C7C" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;err&quot;}">err</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;request (m ->sl)&quot;}">request (m -&gt; sl)</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;3 – Read acontiguous area of ​​32 bit registers&quot;}">3 – Read acontiguous area of ​​32 bit registers</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;3 (OK)&quot;}">3 (OK)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#C6E0B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OK&quot;}">OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;...&quot;}">...</td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;3 (Err)&quot;}">3 (Err)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#F07C7C" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;err&quot;}">err</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;# OK&quot;}"># OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data &yen;/?&quot;}">data /?</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data &yen;/?&quot;}">data /?</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;...&quot;}">...</td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;request (m ->sl)&quot;}">request (m -&gt; sl)</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;4 – writing acontiguous area of ​​32 bit registers&quot;}">4 – writing acontiguous area of ​​32 bit registers</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;...&quot;}">...</td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;4 (OK)&quot;}">4 (OK)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#C6E0B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OK&quot;}">OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;4 (Err)&quot;}">4 (Err)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;group #&quot;}">group #</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;param#&quot;}">param#</td>
		<td bgcolor="#F07C7C" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;err&quot;}">err</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;# OK&quot;}"># OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F8CBAD" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;request (m ->sl)&quot;}">request (m -&gt; sl)</td>
		<td bgcolor="#F8CBAD" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;11 – Read acontiguous oscilloscope area &quot;}">11 – Read acontiguous oscilloscope area</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.offs_L&quot;}">a.offs_L</td>
		<td bgcolor="#BDD7EE" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.offs_H&quot;}">a.offs_H</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#FCE4D6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#FCE4D6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;11 (OK)&quot;}">11 (OK)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.offs_L&quot;}">a.offs_L</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.offs_H&quot;}">a.offs_H</td>
		<td bgcolor="#C6E0B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OK&quot;}">OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;...&quot;}">...</td>
	</tr>
	<tr>
		<td bgcolor="#FCE4D6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl ->m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#FCE4D6" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;11 (Err)&quot;}">11 (Err)</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.offs_L&quot;}">a.offs_L</td>
		<td bgcolor="#DDEBF7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.offs_H&quot;}">a.offs_H</td>
		<td bgcolor="#F07C7C" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;err&quot;}">err</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;# OK&quot;}"># OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data &yen;/?&quot;}">data /?</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data &yen;/?&quot;}">data /?</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;...&quot;}">...</td>
	</tr>
</table>

| Název       | Význam                                                                                   |
|-------------|------------------------------------------------------------------------------------------|
| group #     | Číslo skupiny parametrů                                                                  |
| param #     | Číslo parametru ve skupině                                                               |
| OK          | Zápis/Čtení OK ("= 0 ")                                                                   |
| Err         | Chybový kód ("≠ 0" 1 = chybný příkaz 2 = neplatná adresa, 3 = RO / mimo dosah, 4 = chyba v datovém firmwaru) |
| Number      | Číslo parametru (Int32) in a contiguous area                                              |
| # OK        | Číslo úspěšně zapsaného parametru                                                        |
| a.offs      | Ofset v oblasti 32bitových registrů (jeden 32bitový registr)                             |

Popis jednotlivých registrů s informacemi o `group #` a `param #` najdete [ZDE](../../../TGZ/TGZ_SW/GUI/md/parameters.md#GUIbasicParams)

**Žádost (master -> slave)**
Minimální délka dat UDP je pro čtení 2 + 3 bajty a 2 + 4 bajty pro zápis.
Paket může obsahovat několik požadavků.
Maximální celková délka paketu je 1470 bajtů + 2 (+2 označuje část identifikátoru).   

**Odezva (slave -> master)**
Příkaz, počet parametrů a číslo parametru ve skupině jsou stejné jako v případě žádosti.
Pro práci se spojitou oblastí registrů je nutné použít počet parametrů.
Délka odpovědi na požadavek na čtení je prodloužena o 4 bajtovou hodnotu parametru.
Odpověď na požadavek na zápis se rozšíří o výsledek write: = 0 - write OK, ≠ 0 - write error code.
Odpovědi jsou také seskupeny do jednoho paketu.
Master musí navrhnout aplikaci tak, aby bylo možné odesílat odpovědi s jedním paketem o celkové délce max. 2 + 1 470 bajtů (2+ označuje sekci identifikátoru).

##Příklad komunikace
*Požadavek*

<table>
    <tr>
        <td bgcolor="#005050" style="color: #FFFFFF;">identifier</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">identifier</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">write</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">group</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">element</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
    </tr>
    <tr>
        <td bgcolor="#DDEBF7"><b>0x47</b></td>
        <td bgcolor="#DDEBF7"><b>0x54</b></td>
        <td bgcolor="#FFFF00"><b>0x02</b></td>
        <td bgcolor="#C2D69B">0x03</td>
        <td bgcolor="#FABF8F">0x90</td>
        <td bgcolor="#D9D9D9">0x90</td>
        <td bgcolor="#D9D9D9">0x12</td>
        <td bgcolor="#D9D9D9">0x34</td>
        <td bgcolor="#D9D9D9">0x11</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td bgcolor="#005050" style="color: #FFFFFF;">read</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">group</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">element</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td bgcolor="#FFFF00"><b>0x01</b></td>
        <td bgcolor="#C2D69B">0x02</td>
        <td bgcolor="#FABF8F">0x45</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>

*Odpověď*

<table>
    <tr>
        <td bgcolor="#005050" style="color: #FFFFFF;">identifier</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">identifier</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">write</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">number</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">group</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">status</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td bgcolor="#ddebf7"><b>0x47</b></td>
        <td bgcolor="#ddebf7"><b>0x54</b></td>
        <td bgcolor="#ffff00"><b>0x02</b></td>
        <td bgcolor="#d9d9d9">0x03</td>
        <td bgcolor="#d9d9d9">0x90</td>
        <td bgcolor="#d9d9d9">0x00</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td bgcolor="#005050" style="color: #FFFFFF;">read</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">group</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">element</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">status</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
        <td bgcolor="#005050" style="color: #FFFFFF;">data</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td bgcolor="#ffff00"><b>0x01</b></td>
        <td bgcolor="#d9d9d9">0x02</td>
        <td bgcolor="#d9d9d9">0x45</td>
        <td bgcolor="#d9d9d9">0x00</td>
        <td bgcolor="#d9d9d9">0x72</td>
        <td bgcolor="#d9d9d9">0x12</td>
        <td bgcolor="#d9d9d9">0x34</td>
        <td bgcolor="#d9d9d9">0x56</td>
    </tr>
</table>

*Struktura dat UDP pro čtení textové zprávy*

<table>
	<tr>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"><b><i></i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 0&quot;}"><b><i>byte 0</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 1&quot;}"><b><i>byte 1</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 2&quot;}"><b><i>byte 2</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 3&quot;}"><b><i>byte 3</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 4&quot;}"><b><i>byte 4</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 5&quot;}"><b><i>byte 5</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 6&quot;}"><b><i>byte 6</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 7&quot;}"><b><i>byte 7</i></b></td>
		<td bgcolor="#005050" style="color: #FFFFFF;" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;byte 8&quot;}"><b><i>byte 8</i></b></td>
	</tr>
	<tr>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;request (m -&gt; sl)&quot;}">request (m -&gt; sl)</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;41 - reading messages&quot;}">41 - reading messages</td>
		<td bgcolor="#DAEEF3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.off&quot;}">a.off</td>
		<td bgcolor="#FBD4B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
		<td bgcolor="#D9D9D9" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;&quot;}"></td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl -&gt; m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;41 (OK)&quot;}">41 (OK)</td>
		<td bgcolor="#DAEEF3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.off&quot;}">a.off</td>
		<td bgcolor="#FBD4B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#92D050" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;OK&quot;}">OK</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;...&quot;}">...</td>
	</tr>
	<tr>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;response (sl -&gt; m)&quot;}">response (sl -&gt; m)</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;41 (Err)&quot;}">41 (Err)</td>
		<td bgcolor="#DAEEF3" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;a.off&quot;}">a.off</td>
		<td bgcolor="#FBD4B4" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;number&quot;}">number</td>
		<td bgcolor="#E5B8B7" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;err&quot;}">err</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;data&quot;}">data</td>
		<td bgcolor="#F2F2F2" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;...&quot;}">...</td>
	</tr>
</table>

| parametr | význam                                                                |
|----------|-----------------------------------------------------------------------|
| a.off    | offset první zprávy (řádku) 0..255                                    |
| number   | počet po sobě jdoucích zpráv (řádků) v telegramu 1..4 (délka zprávy je 256 bajtů) |
