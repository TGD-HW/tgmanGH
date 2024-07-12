![uSD card connector](../../../../../source/img/uSD.png){: style="width:30%;" }

##Saved parameters {#SDparams}
The SD card with stored parameters is only compatible with the same TGZ model and the same firmware version (displayed in the TGZ GUI).
If the TGZ firmware is upgraded or a card is taken from another TGZ that has a different version of the FW (even the exact same model), it reports a parameter error after starting the TGZ.
The parameter error is eliminated by loading the factory settings in the TGZ GUI and setting the required parameters again.
When using a card from another TGZ model but with the same FW version, a parameter error may not be reported, but in this case, we recommend resetting the TGZ to the factory settings in the TGZ GUI and resetting the necessary parameters.
If it is necessary to transfer the settings from TGZ to TGZ of the same model, but with a different version of FW, we recommend saving the settings to a file via TGZ GUI on the TGZ from which the data we want to transfer and then to read and save settings from the file again from TGZ GUI. 
If the TGZ GUI displays a message when writing parameters to the card that it was not possible to write, please check that the SD card in the SD slot is inserted correctly and is functional (for example, by writing to it in another device).