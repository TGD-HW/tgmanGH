##Parameter settings
The settings of all parameters of the TGZ servo amplifier are available in the **Parameters** tab.
In addition to this detailed setting, it is also possible to find detailed information about the connected servo amplifier (type, serial number, etc.).

![TGZ GUI servo parameters](../img/GUIparams.png){: style="width:100%;" }

The open window also consists of several panes:

- BASIC GROUPS - list of parameter groups (in individual groups it is possible to find and set all parameters of the servo amplifier).
- USER GROUPS - user groups (allow setting the display of selected parameter groups).
- DRIVE INFO - displays information about the given servo amplifier (type, serial number, HW version, firmware version, etc.).
- PARAMETERS - display and edit parameters of the active group
- MONITORED VALUES - AXIS 1 - displays basic status information (position, speed, proud, etc.) of Axis 1 of the TGZ servo amplifier, displays a code of possible errors and allows its reset.
- MONITORED VALUES - AXIS 2 - displays basic status information (position, speed, proud, etc.) of Axis 2 of the TGZ servo amplifier, displays a code of possible errors and allows its reset.

At the bottom of the window there is an informative status bar with several function buttons:

<div class="grid cards" markdown>

-   **COMMON**

    ---
	![Icon Common](../../../../../source/img/icoCommon.png){: style="width:50%;" }

- 	HW ENABLE status information the Disable function key allows the HW ENABLE to be switched off simultaneously on both axes of the servo amplifier

-   **AXIS 1**

    ---
	![Icon Ax1](../../../../../source/img/icoAx1.png){: style="width:85%;" }

-	- display of information about the status of axis 1 (error, warning message SW Enable)
    - the function key Disable enables switching off the SW ENABLE for axis 1
    - the function key Enable allows to switch on SW ENABLE for axis 1
    
-   **AXIS 2**

    ---
	![Icon Ax2](../../../../../source/img/icoAx2.png){: style="width:85%;" }

-	- display of information about the status of axis 2 (error, warning message SW Enable)
    - the function key Disable enables switching off the SW ENABLE for axis 2
    - the function key Enable allows to switch on SW ENABLE for axis 2
		
</div>

##Description of parameters
A list of all parameters of the TGZ servo amplifier, including their description, is given in a special document [TGZ_registers_fw_build_1605.xlsx](https://www.tgdrives.cz/fileadmin/user_upload/download-TGZ/TGZ_registers_fw_build_1605.zip).

##Basic TGZ parameters in the TGZ GUI {#GUIbasicParams}
<table>
	<tr>
		<td colspan="10" bgcolor="#004F4F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Description of TGZ main parameters&quot;}">Description of TGZ main parameters</td>
	</tr>
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
		<td bgcolor="#92D04F" data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Description [EN]&quot;}">Description [EN]</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Servo drive hw type 1&yen;/5&quot;}">Servo drive hw type 1/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Servo drive hw type 2&yen;/5&quot;}">Servo drive hw type 2/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Servo drive hw type 3&yen;/5&quot;}">Servo drive hw type 3/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Servo drive hw type 4&yen;/5&quot;}">Servo drive hw type 4/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Servo drive hw type 5&yen;/5&quot;}">Servo drive hw type 5/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;HW version&quot;}">HW version</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Firmware version&quot;}">Firmware version</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Firmware build 1&yen;/5&quot;}">Firmware build 1/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Firmware build 2&yen;/5&quot;}">Firmware build 2/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Firmware build 3&yen;/5&quot;}">Firmware build 3/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Firmware build 4&yen;/5&quot;}">Firmware build 4/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Firmware build 5&yen;/5&quot;}">Firmware build 5/5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;IP address X11 service UDP chanel&quot;}">IP address X11 service UDP chanel</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ID fieldbus&quot;}">ID fieldbus</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Measured time between synchronization pulses&yen;u000a(only for DC functionality)&quot;}">Measured time between synchronization pulses<br>(only for DC functionality)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Enable 1G speed fieldbus (preparing)&quot;}">Enable 1G speed fieldbus (preparing)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired cycle time (used only without DC&yen;u000afunctionality)&quot;}">Desired cycle time (used only without DC<br>functionality)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Enable autostart of user program : 0 .. no autostart, 1 .. autostart from flash memory, (2 ..&yen;u000aautostart from SD .. preparing)&quot;}">Enable autostart of user program : 0 .. no autostart, 1 .. autostart from flash memory, (2 ..<br>autostart from SD .. preparing)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 1 1&yen;/6&quot;}">Motor name 1 1/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 2 1&yen;/6&quot;}">Motor name 2 1/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 1 2&yen;/6&quot;}">Motor name 1 2/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 2 2&yen;/6&quot;}">Motor name 2 2/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 1 3&yen;/6&quot;}">Motor name 1 3/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 2 3&yen;/6&quot;}">Motor name 2 3/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 1 4&yen;/6&quot;}">Motor name 1 4/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 2 4&yen;/6&quot;}">Motor name 2 4/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 1 5&yen;/6&quot;}">Motor name 1 5/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 2 5&yen;/6&quot;}">Motor name 2 5/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 1 6&yen;/6&quot;}">Motor name 1 6/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor name 2 6&yen;/6&quot;}">Motor name 2 6/6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Allowed stall rms current of motor 1&quot;}">Allowed stall rms current of motor 1</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Allowed stall rms current of motor 2&quot;}">Allowed stall rms current of motor 2</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Allowed peak current amplitude of motor 1&yen;u000a(Iamp = 1.41 * Irms)&quot;}">Allowed peak current amplitude of motor 1<br>(Iamp = 1.41 * Irms)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Allowed peak current amplitude of motor 2&yen;u000a(Iamp = 1.41 * Irms)&quot;}">Allowed peak current amplitude of motor 2<br>(Iamp = 1.41 * Irms)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximal mechanical speed of motor 1 - error&yen;u000alimit&quot;}">Maximal mechanical speed of motor 1 - error<br>limit</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximal mechanical speed of motor 2 - error&yen;u000alimit&quot;}">Maximal mechanical speed of motor 2 - error<br>limit</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of motor 1 polepairs (polepairs = poles&yen;u000a&yen;/ 2)&quot;}">Number of motor 1 polepairs (polepairs = poles<br>/ 2)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of motor 2 polepairs (polepairs = poles&yen;u000a&yen;/ 2)&quot;}">Number of motor 2 polepairs (polepairs = poles<br>/ 2)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Angle offset between zero of feedback encoder&yen;u000aand stator of motor 1&quot;}">Angle offset between zero of feedback encoder<br>and stator of motor 1</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Angle offset between zero of feedback encoder&yen;u000aand stator of motor 2&quot;}">Angle offset between zero of feedback encoder<br>and stator of motor 2</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Limit for overtemperature error - Minimal resistivity of motor 1 thermal sensor (used only for digital feedback with connected thermal&yen;u000asensor)&quot;}">Limit for overtemperature error - Minimal resistivity of motor 1 thermal sensor (used only for digital feedback with connected thermal<br>sensor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Limit for overtemperature error - Minimal resistivity of motor 2 thermal sensor (used only for digital feedback with connected thermal&yen;u000asensor)&quot;}">Limit for overtemperature error - Minimal resistivity of motor 2 thermal sensor (used only for digital feedback with connected thermal<br>sensor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Limit for overtemperature error - Maximal resistivity of motor 1 thermal sensor (used only for digital feedback with connected thermal&yen;u000asensor)&quot;}">Limit for overtemperature error - Maximal resistivity of motor 1 thermal sensor (used only for digital feedback with connected thermal<br>sensor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Limit for overtemperature error - Maximal resistivity of motor 2 thermal sensor (used only for digital feedback with connected thermal&yen;u000asensor)&quot;}">Limit for overtemperature error - Maximal resistivity of motor 2 thermal sensor (used only for digital feedback with connected thermal<br>sensor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor 1 static brake: 1 = yes , 0 = no&quot;}">Motor 1 static brake: 1 = yes , 0 = no</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Motor 2 static brake: 1 = yes , 0 = no&quot;}">Motor 2 static brake: 1 = yes , 0 = no</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ThermalTimeConstant of motor 1&quot;}">ThermalTimeConstant of motor 1</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;ThermalTimeConstant of motor 2&quot;}">ThermalTimeConstant of motor 2</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive 1 name 1&yen;/3&quot;}">Drive 1 name 1/3</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive 2 name 1&yen;/3&quot;}">Drive 2 name 1/3</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive 1 name 2&yen;/3&quot;}">Drive 1 name 2/3</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive 2 name 2&yen;/3&quot;}">Drive 2 name 2/3</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive 1 name 3&yen;/3&quot;}">Drive 1 name 3/3</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Drive 2 name 3&yen;/3&quot;}">Drive 2 name 3/3</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Mode of drive 1 - see manual&quot;}">Mode of drive 1 - see manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Mode of drive 2 - see manual&quot;}">Mode of drive 2 - see manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Delay enable drive 1 after HW enable signal&yen;u000arising edge X1&quot;}">Delay enable drive 1 after HW enable signal<br>rising edge X1</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Delay enable drive 2 after HW enable signal&yen;u000arising edge X1&quot;}">Delay enable drive 2 after HW enable signal<br>rising edge X1</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Delay release brake of motor 1 after enable&yen;u000adrive&quot;}">Delay release brake of motor 1 after enable<br>drive</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Delay release brake of motor 2 after enable&yen;u000adrive&quot;}">Delay release brake of motor 2 after enable<br>drive</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Delay disable drive 1 after activating brake&quot;}">Delay disable drive 1 after activating brake</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Delay disable drive 2 after activating brake&quot;}">Delay disable drive 2 after activating brake</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Minimal DC link voltage - low voltage error level&quot;}">Minimal DC link voltage - low voltage error level</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Maximal DC link voltage - high voltage error&yen;u000alevel&quot;}">Maximal DC link voltage - high voltage error<br>level</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current controller Q gain&quot;}">Current controller Q gain</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current controller Q gain&quot;}">Current controller Q gain</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current controller integral time&quot;}">Current controller integral time</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current controller integral time&quot;}">Current controller integral time</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current controller D relative gain to K&quot;}">Current controller D relative gain to K</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current controller D relative gain to K&quot;}">Current controller D relative gain to K</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Time constant of current command filter (not&yen;u000aused)&quot;}">Time constant of current command filter (not<br>used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Time constant of current command filter (not&yen;u000aused)&quot;}">Time constant of current command filter (not<br>used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Percentable value of current command (100 =&yen;u000a100% goes via filter) (not used)&quot;}">Percentable value of current command (100 =<br>100% goes via filter) (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Percentable value of current command (100 =&yen;u000a100% goes via filter) (not used)&quot;}">Percentable value of current command (100 =<br>100% goes via filter) (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current amplitude negative limit relatively to M- Inull (limiting output of speed controller)&quot;}">Current amplitude negative limit relatively to M- Inull (limiting output of speed controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current amplitude negative limit relatively to M- Inull (limiting output of speed controller)&quot;}">Current amplitude negative limit relatively to M- Inull (limiting output of speed controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current amplitude positive limit relatively to M- Inull (limiting output of speed controller)&quot;}">Current amplitude positive limit relatively to M- Inull (limiting output of speed controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current amplitude positive limit relatively to M- Inull (limiting output of speed controller)&quot;}">Current amplitude positive limit relatively to M- Inull (limiting output of speed controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Negative voltage limit (output of current&yen;u000acontroller)&quot;}">Negative voltage limit (output of current<br>controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Negative voltage limit (output of current&yen;u000acontroller)&quot;}">Negative voltage limit (output of current<br>controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Possitive voltage limit (output of current&yen;u000acontroller)&quot;}">Possitive voltage limit (output of current<br>controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Possitive voltage limit (output of current&yen;u000acontroller)&quot;}">Possitive voltage limit (output of current<br>controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cogging compensation factor 0 .. Off (Before&yen;u000ausing function must be measured compensation data of motor)&quot;}">Cogging compensation factor 0 .. Off (Before<br>using function must be measured compensation data of motor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Cogging compensation factor 0 .. Off (Before using function must be measured compensation&yen;u000adata of motor)&quot;}">Cogging compensation factor 0 .. Off (Before using function must be measured compensation<br>data of motor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity controller gain&quot;}">Velocity controller gain</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity controller gain&quot;}">Velocity controller gain</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity controller integral time&quot;}">Velocity controller integral time</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity controller integral time&quot;}">Velocity controller integral time</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity negative limit (limiting output of&yen;u000aposition controller)&quot;}">Velocity negative limit (limiting output of<br>position controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity negative limit (limiting output of&yen;u000aposition controller)&quot;}">Velocity negative limit (limiting output of<br>position controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity positive limit (limiting output of&yen;u000aposition controller)&quot;}">Velocity positive limit (limiting output of<br>position controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity positive limit (limiting output of&yen;u000aposition controller)&quot;}">Velocity positive limit (limiting output of<br>position controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Time constant of velocity feedback lowpass filter&yen;u000a(not used)&quot;}">Time constant of velocity feedback lowpass filter<br>(not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Time constant of velocity feedback lowpass filter&yen;u000a(not used)&quot;}">Time constant of velocity feedback lowpass filter<br>(not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Time constant of velocity command lowpass&yen;u000afilter (not used)&quot;}">Time constant of velocity command lowpass<br>filter (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Time constant of velocity command lowpass&yen;u000afilter (not used)&quot;}">Time constant of velocity command lowpass<br>filter (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity filter factor 0 .. not filtered (not used)&quot;}">Velocity filter factor 0 .. not filtered (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Velocity filter factor 0 .. not filtered (not used)&quot;}">Velocity filter factor 0 .. not filtered (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Position controller gain&quot;}">Position controller gain</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Position controller gain&quot;}">Position controller gain</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Speed feed forward&quot;}">Speed feed forward</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Speed feed forward&quot;}">Speed feed forward</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximal position error - angle part&quot;}">maximal position error - angle part</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximal position error - angle part&quot;}">maximal position error - angle part</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximal position error - revolution part&quot;}">maximal position error - revolution part</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;maximal position error - revolution part&quot;}">maximal position error - revolution part</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback type : 1.. Hiperface DSL, 2.. Endat 2,&yen;u000a3..SSI, 4.. Incremental&quot;}">Feedback type : 1.. Hiperface DSL, 2.. Endat 2,<br>3..SSI, 4.. Incremental</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback type : 1.. Hiperface DSL, 2.. Endat 2,&yen;u000a3..SSI, 4.. Incremental&quot;}">Feedback type : 1.. Hiperface DSL, 2.. Endat 2,<br>3..SSI, 4.. Incremental</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback resolution per revolution(read only for&yen;u000adigital feedbacks type 1 and 2)&quot;}">Feedback resolution per revolution(read only for<br>digital feedbacks type 1 and 2)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Feedback resolution per revolution(read only for&yen;u000adigital feedbacks type 1 and 2)&quot;}">Feedback resolution per revolution(read only for<br>digital feedbacks type 1 and 2)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Incremental encoder feedback resolution&quot;}">Incremental encoder feedback resolution</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Incremental encoder feedback resolution&quot;}">Incremental encoder feedback resolution</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;External incremental encoder resolution&quot;}">External incremental encoder resolution</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of resolver poles (not used - only for&yen;u000aoptional board)&quot;}">Number of resolver poles (not used - only for<br>optional board)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of resolver poles (not used - only for&yen;u000aoptional board)&quot;}">Number of resolver poles (not used - only for<br>optional board)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command bits[1,0]=01 .. SW enable bit[3] = 1 ..&yen;u000aClear errors&quot;}">Command bits[1,0]=01 .. SW enable bit[3] = 1 ..<br>Clear errors</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Command bits[1,0]=01 .. SW enable bit[3] = 1 ..&yen;u000aClear errors&quot;}">Command bits[1,0]=01 .. SW enable bit[3] = 1 ..<br>Clear errors</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required current (current mode = 1)&quot;}">Required current (current mode = 1)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required current (current mode = 1)&quot;}">Required current (current mode = 1)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required velocity (velocity mode = 2)&quot;}">Required velocity (velocity mode = 2)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required velocity (velocity mode = 2)&quot;}">Required velocity (velocity mode = 2)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required position - angle (position mode = 3)&quot;}">Required position - angle (position mode = 3)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required position - angle (position mode = 3)&quot;}">Required position - angle (position mode = 3)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required position - revolutions (position mode =&yen;u000a3)&quot;}">Required position - revolutions (position mode =<br>3)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required position - revolutions (position mode =&yen;u000a3)&quot;}">Required position - revolutions (position mode =<br>3)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;force outputs - set&quot;}">force outputs - set</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;force outputs - set&quot;}">force outputs - set</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;force outputs - clear&quot;}">force outputs - clear</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;force outputs - clear&quot;}">force outputs - clear</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Main counter&quot;}">Main counter</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current phase A&quot;}">Actual current phase A</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current phase A&quot;}">Actual current phase A</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current phase B&quot;}">Actual current phase B</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current phase B&quot;}">Actual current phase B</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current phase C&quot;}">Actual current phase C</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current phase C&quot;}">Actual current phase C</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current q&quot;}">Actual current q</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current q&quot;}">Actual current q</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current d&quot;}">Actual current d</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual current d&quot;}">Actual current d</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual position per revolution (resolution :&yen;u000a32bit per revolution)&quot;}">Actual position per revolution (resolution :<br>32bit per revolution)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual position per revolution (resolution :&yen;u000a32bit per revolution)&quot;}">Actual position per revolution (resolution :<br>32bit per revolution)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual number of revolutions&quot;}">Actual number of revolutions</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual number of revolutions&quot;}">Actual number of revolutions</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual motor speed&quot;}">Actual motor speed</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual motor speed&quot;}">Actual motor speed</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual speed error&quot;}">Actual speed error</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual speed error&quot;}">Actual speed error</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual angle error&quot;}">Actual angle error</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual angle error&quot;}">Actual angle error</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual revol error&quot;}">Actual revol error</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual revol error&quot;}">Actual revol error</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status of drive : bit[0] = 1 .. Enabled, bit[1] = 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6] = 1&yen;u000a..fieldbus mode, .............&quot;}">Status of drive : bit[0] = 1 .. Enabled, bit[1] = 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6] = 1<br>..fieldbus mode, .............</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status of drive : bit[0] = 1 .. Enabled, bit[1] = 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6] = 1&yen;u000a..fieldbus mode, ..............&quot;}">Status of drive : bit[0] = 1 .. Enabled, bit[1] = 1 .. HW Enable signal, bit[2] = 1 .. Software enable, bit[3] = 1 .. Brake released, bit [4] = 1 .. No error, bit[5] = 1 .. Initialization finished, bit[6] = 1<br>..fieldbus mode, ..............</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Error of drive (see manual)&quot;}">Error of drive (see manual)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Error of drive (see manual)&quot;}">Error of drive (see manual)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Warning (not used)&quot;}">Warning (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Warning (not used)&quot;}">Warning (not used)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analogue input 1&quot;}">Analogue input 1</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Analogue input 2&quot;}">Analogue input 2</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;DC-link voltage&quot;}">DC-link voltage</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;CPU temperature&quot;}">CPU temperature</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired position per revolution (fieldbus)&quot;}">Desired position per revolution (fieldbus)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired position per revolution (fieldbus)&quot;}">Desired position per revolution (fieldbus)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired number of revolutions (fieldbus)&quot;}">Desired number of revolutions (fieldbus)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired number of revolutions (fieldbus)&quot;}">Desired number of revolutions (fieldbus)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Fieldbus control register&quot;}">Fieldbus control register</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Fieldbus control register&quot;}">Fieldbus control register</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Fieldbus current setpoint&quot;}">Fieldbus current setpoint</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Fieldbus current setpoint&quot;}">Fieldbus current setpoint</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Fieldbus current limitation&quot;}">Fieldbus current limitation</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Fieldbus current limitation&quot;}">Fieldbus current limitation</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digital inputs : bit[0] .. IN1,bit[1] .. IN3,bit[2] ..&yen;u000aIN5,bit[3] .. IN7&quot;}">Digital inputs : bit[0] .. IN1,bit[1] .. IN3,bit[2] ..<br>IN5,bit[3] .. IN7</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digital inputs : bit[0] .. IN2,bit[1] .. IN4,bit[2] ..&yen;u000aIN6,bit[3] .. IN8&quot;}">Digital inputs : bit[0] .. IN2,bit[1] .. IN4,bit[2] ..<br>IN6,bit[3] .. IN8</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rezistivity of motor temperature sensor (only for&yen;u000adigital feedback with connected temperature sensor)&quot;}">Rezistivity of motor temperature sensor (only for<br>digital feedback with connected temperature sensor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Rezistivity of motor temperature sensor (only for&yen;u000adigital feedback with connected temperature sensor)&quot;}">Rezistivity of motor temperature sensor (only for<br>digital feedback with connected temperature sensor)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required current (input - current controller)&quot;}">Required current (input - current controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required current (input - current controller)&quot;}">Required current (input - current controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current Ia rms value&quot;}">Current Ia rms value</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current Ia rms value&quot;}">Current Ia rms value</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current Ib rms value&quot;}">Current Ib rms value</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current Ib rms value&quot;}">Current Ib rms value</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current Ic rms value&quot;}">Current Ic rms value</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Current Ic rms value&quot;}">Current Ic rms value</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Integrated value I2t&quot;}">Integrated value I2t</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Integrated value I2t&quot;}">Integrated value I2t</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required position per revolution (input -&yen;u000aposition controller)&quot;}">Required position per revolution (input -<br>position controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required position per revolution (input -&yen;u000aposition controller)&quot;}">Required position per revolution (input -<br>position controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required number of revolutions (input - position&yen;u000acontroller)&quot;}">Required number of revolutions (input - position<br>controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required number of revolutions (input - position&yen;u000acontroller)&quot;}">Required number of revolutions (input - position<br>controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required speed (input - speed controller)&quot;}">Required speed (input - speed controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Required speed (input - speed controller)&quot;}">Required speed (input - speed controller)</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status DSL fb encoder&quot;}">Status DSL fb encoder</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Status DSL fb encoder&quot;}">Status DSL fb encoder</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digital outputs: bit[0] .. Out1, bit[1] .. Out3,&yen;u000abit[2] .. Out5&quot;}">Digital outputs: bit[0] .. Out1, bit[1] .. Out3,<br>bit[2] .. Out5</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Digital outputs: bit[0] .. Out2, bit[1] .. Out4,&yen;u000abit[2] .. Out6&quot;}">Digital outputs: bit[0] .. Out2, bit[1] .. Out4,<br>bit[2] .. Out6</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Measured time between packets for fieldbus&yen;u000amode&quot;}">Measured time between packets for fieldbus<br>mode</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired acceleration of movement [ inc&yen;/s2 ] ..&yen;u000asee functional manual&quot;}">Desired acceleration of movement [ inc/s2 ] ..<br>see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired acceleration of movement [ inc&yen;/s2 ] ..&yen;u000asee functional manual&quot;}">Desired acceleration of movement [ inc/s2 ] ..<br>see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired deceleration of movenent [ inc&yen;/s2 ] ..&yen;u000asee functional manual&quot;}">Desired deceleration of movenent [ inc/s2 ] ..<br>see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired deceleration of movenent [ inc&yen;/s2 ] ..&yen;u000asee functional manual&quot;}">Desired deceleration of movenent [ inc/s2 ] ..<br>see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Actual position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Actual position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Actual position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Actual position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Destination position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Destination position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Destination position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Destination position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Destination position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Destination position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Destination position of movenent[ inc ] .. see&yen;u000afunctional manual&quot;}">Destination position of movenent[ inc ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual speed of movenent[ inc&yen;/s ] .. see&yen;u000afunctional manual&quot;}">Actual speed of movenent[ inc/s ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Actual speed of movenent[ inc&yen;/s ] .. see&yen;u000afunctional manual&quot;}">Actual speed of movenent[ inc/s ] .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired speed of movenent in position mode[&yen;u000ainc&yen;/s ] .. see functional manual&quot;}">Desired speed of movenent in position mode[<br>inc/s ] .. see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired speed of movenent in position mode[&yen;u000ainc&yen;/s ] .. see functional manual&quot;}">Desired speed of movenent in position mode[<br>inc/s ] .. see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired speed of movenent in speed mode[&yen;u000ainc&yen;/s ] .. see functional manual&quot;}">Desired speed of movenent in speed mode[<br>inc/s ] .. see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Desired speed of movenent in speed mode[&yen;u000ainc&yen;/s ] .. see functional manual&quot;}">Desired speed of movenent in speed mode[<br>inc/s ] .. see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Mode of profile generator 0 = speed mode, 1 = position mode, 2( only read ) = signalizing deceleration ramp in position mode .. see&yen;u000afunctional manual&quot;}">Mode of profile generator 0 = speed mode, 1 = position mode, 2( only read ) = signalizing deceleration ramp in position mode .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Mode of profile generator 0 = speed mode, 1 = position mode, 2( only read ) = signalizing deceleration ramp in position mode .. see&yen;u000afunctional manual&quot;}">Mode of profile generator 0 = speed mode, 1 = position mode, 2( only read ) = signalizing deceleration ramp in position mode .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Flag end of movemnet 1 = Destination position is reached .. see functional manual&quot;}">Flag end of movemnet 1 = Destination position is reached .. see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Flag end of movemnet 1 = Destination position is reached .. see functional manual&quot;}">Flag end of movemnet 1 = Destination position is reached .. see functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Type of speed profile 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. see functional&yen;u000amanual&quot;}">Type of speed profile 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. see functional<br>manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Type of speed profile 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. see functional&yen;u000amanual&quot;}">Type of speed profile 0 = harmonic non symetric, 1 = harmonic symetric, 2 = full harmonic, 3 = trapezoidal .. see functional<br>manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of bit per revolution for internal pg calculation. It take affect to resolution of speeds and accelerations (decelerations) .. see&yen;u000afunctional manual&quot;}">Number of bit per revolution for internal pg calculation. It take affect to resolution of speeds and accelerations (decelerations) .. see<br>functional manual</td>
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
		<td data-sheets-value="{ &quot;1&quot;: 2, &quot;2&quot;: &quot;Number of bit per revolution for internal pg calculation. It take affect to resolution of speeds and accelerations (decelerations) .. see&yen;u000afunctional manual&quot;}">Number of bit per revolution for internal pg calculation. It take affect to resolution of speeds and accelerations (decelerations) .. see<br>functional manual</td>
	</tr>
</table>
