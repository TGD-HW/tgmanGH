There are almost no changes in the servo amplifier part of the product.
The TGZ GUI service program is used for settings the parameters of the drive, motors, etc.
However, there are a few parameters, which are set up in the TGMotion’s `TGM.INI` file:

-	IP address of the device: TGZ+Motion uses static IP address in its Ethernet service connector X13.
	This address must be set in the `TgMotion5xx.ini` file:
	``` ini
	[DHCP]
	IPAddress=192.168.1.188
	Gateway=192.168.1.1 
	Mask=255.255.255.0 
	DNS=192.168.1.1
	```
	It is necessary to correctly set the Gateway, it must be in the same domain as the IP address.
	Note that the IP address in the TGZ GUI is read-only.
-	C-SetCycleTime:
	Cycle time is also set in the configuration file:
	``` ini
	[System]
	Cycle_Time=250
	```
	
TGMotion and TGZ servo are synchronous and run from cycle time of 100 µs.
The recommended value is 250 or 500 µs.
The TGZ GUI displays the `C-SetCycleTime` as read-only parameter.   

It is highly recommended to correctly set the MAC address using the TGZ GUI to a valid value.
The first hexadecimal digits should be `00`, the second and third could be 0a:35 and there is no restriction to the last three values.
It is only important that the MAC addresses of all the connected devices in one network domain are different.
Example of a valid MAC address: `00:0a:35:01:02:04`.

##Internal servo control source
The TGZ servo of the **TGZ+Motion** system can be controlled either from service port via UDP protocol (TGZ GUI – usually for motor and drive setup) or internally by the TGMotion.

##User program in TGZ (PLC)
The so-called user program (or PLC) found in standard TGZ servo drive is not supported.
The PLC is used with the TGMotion subsystem, allowing several program priorities, real-time behavior and better performance.

##Other diversions to standard TGZ servo amplifier
All the parameters are saved only to the SD card.
Saving the parameters to internal flash memory is not yet supported.
The firmware can be updated only by **Control Observer**, the TGZ GUI cannot be used for this action.
The format of the firmware file is completely different to the standard TGZ drive.