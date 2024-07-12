##Necessary equipment:

- PC with installed TGZ GUI and Ethernet interface.
- Ethernet cable
- 24 VDC power supply
- TGZ servo amplifier
- `.TGZFW` file (firmware)

##Firmware change procedure:

1. Connect the TGZ to the computer (connector X11) via the Ethernet cable.
2. Connect + 24V and GND (connector X1) to the power supply.
3. Start the TGZ GUI, select the appropriate network adapter, select the appropriate device from the list and connect to the TGZ servo amplifier.
4. Back up the servo amplifier parameters by clicking on the icon
   ![Icon Save](../../../../../source/img/icoSave.png){: style="width:4%;" }
   in the right part of the menu at the top. Select all parameter groups and click the **Save** icon.
5. Click the icon
   ![Icon Memory](../../../../../source/img/icoMemory.png){: style="width:4%;" }
   in the right part of the menu at the top and select **Upload firmware**.
6. Open the firmware file (`*.TGZFW`).
7. Wait for the firmware download to complete.
8. When the flashing is complete, restart the TGZ servo amplifier by clicking **Yes**.
   ![FW upload complete](../../../../../source/img/GUIfwUploadComplete.png){: style="width:50%;" }   
   Reconnect to the TGZ servo amplifier.
9. If the new firmware has a different parameter structure than the previous firmware, an error will occur (*error 27 - parameter error, 0x08000000*).
   It is therefore necessary to load the parameters from the backup via the icon
   ![Icon Load](../../../../../source/img/icoLoad.png){: style="width:4%;" }
   in the right part of the menu at the top.
   Then it is necessary to save the parameters to the memory card by clicking on the icon
   ![Icon Save](../../../../../source/img/icoSave.png){: style="width:4%;" }
    again in the right part of the menu at the top and select **Save to memory**.
	After restarting the TGZ servo amplifier, the parameter error (error 27) no longer appears.

!!! warning "Attention!"
	Do not disturb the power supply until the flashing process is completed!
