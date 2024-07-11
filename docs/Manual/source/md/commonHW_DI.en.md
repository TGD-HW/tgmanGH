##Basic description {#commonDI1-8}
The TGZ servo amplifier has eight galvanically isolated fast digital inputs integrated on the **X8** connector in the standard (UNI) version.
Six of these (DI1-6) can be configured by the manufacturer either for classic digital input function or as direct inputs for Hall probes (24V voltage level).
In either case, a supply voltage must be connected to VDDIO or GNDIO, as the inputs are active and require power.
Simply connecting a supply voltage to one of the two VDDIO power inputs is sufficient for the active inputs to function properly.
The remaining digital inputs #7 and #8 are standard, passive, with a nominal input level of +24V and do not require a VDDIO supply.
All digital inputs 1-8 have built-in reverse polarity protection (down to -70V) and overvoltage protection (above 30V).

##DI parameters

--8<-- "md/X8_commonHW_DI_tab.en.md"

##Use with Hall sensors
If you want to use the direct connection of Hall probes for motor commutation to the **X8** connector on inputs `1,3,5` (axis 1) or `2,4,6` (axis 2), you must first ask the manufacturer for a properly HW-adapted version.
This version is different in both hardware and firmware.
Make sure that the Hall probes used in this way are **adapted for supply voltages up to 30V**, as the digital inputs of the TGZ servo amplifier operate at a nominal level of **24V**.
The use of Hall probes with 5V or 12V supply voltage will not work in this case.   

If for some reason it is not possible to provide suitable Hall probes and their 24V supply voltage, we recommend using voltage translation module [TGHall](../../CZ/ETC/TGHall/md/description.md#TGhall_1), which you can order at TG Drives.