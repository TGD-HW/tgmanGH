## General

The PROFINET network is connected using the X13 (Fieldbus IN) connector and X12 (Fieldbus OUT) connector.
Use the IN connector in the direction to the PLC and the OUT connector to connect other PROFINET devices in the chain.
The TGZ servo amplifier has built-in PROFINET bridge functionality, so for a small number of devices and simple configuration a dedicated PROFINET managed switch is not needed.
**When connecting the PROFINET network cables, the supply of the equipment must be switched off.**   

!!! warning "Warning"
    Only professional staff member with sufficient knowledge of drive technology is allowed to set up the TGZ servo amplifier.
    All the electrical connections must be done in conformance with the [TGZ user’s manual](../../../../CZ/TGZ/TGZ-D-48-13_26/md/mark.md).

## Fast Guide to Setup

- Check the installation and assembly. Consult all the safety instructions in the user’s manual.
- Connect PC to X11 Ethernet service connector and start TGZ GUI service program.
- Setup the MAC address of the device:

![Profinet img 1](../../../../source/img/profinet1.webp){: style="width:90%;" }

- The MAC address shall start with `00` (two zeros) and `0A`.
  The last four numbers could be arbitrary, but unique in the PROFINET network.
  In addition, the last number must vary by 8, so the valid values for the last number are `00, 08, 10, 18, 20, 28, ..., 90, 98, A0, A8, B0, B8, ..., F0, F8`.
- The MAC address base value is used for the service port X11.
  The PROFINET interface MAC address is calculated by adding `4` to the base value, X13 (IN) has address `base + 5` and X12 (OUT) `base + 6`.
  Usually only the PROFINET interface MAC address is used during PROFINET device commissioning.
  The first two hexadecimal numbers are always `00` and `0A` for all the PROFINET interface and connectors X13 and X12 regardless of the value entered in the TGZ GUI.
- Select the right telegram number according to the PROFINET project and type of the mechanism controlled by the TGZ servo.

![Profinet img 2](../../../../source/img/profinet2.webp){: style="width:90%;" }

- Set the telegram type for both axes in the case of the two axes servo amplifier variant.
- Save the parameters to the drive.

![Profinet img 3](../../../../source/img/profinet3.webp){: style="width:40%;" }

- Restart the drive.

![Profinet img 4](../../../../source/img/profinet4.webp){: style="width:40%;" }

!!! note "Note"
    It is important to always save parameters and restart the drive when the MAC address and/or the telegram number is changed.

	
## IP address and device name {#ProfinetIPsettings}

The factory setting of the IP address is `0.0.0.0` and the device name is empty. There is a need to assign a unique device name and IP address in the PROFINET network. Any commissioning PROFINET software can be used for that, for example **TIA Portal**.

- Select the PC network adapter which is connected to the PROFINET network and double click on line **Update accessible devices**.

![Profinet img 5](../../../../source/img/profinet5.webp){: style="width:40%;" }

- Connected devices will appear after a while:

![Profinet img 6](../../../../source/img/profinet6.webp){: style="width:40%;" }

- There should be a list of all connected PROFINET devices on the network. Expand the device with a given MAC address and double click on **Online & diagnostics**.

![Profinet img 7](../../../../source/img/profinet7.webp){: style="width:40%;" }

- Enter a unique IP address and appropriate subnet mask (usually `255.255.255.0`) and click the **Assign IP address** button.

![Profinet img 8](../../../../source/img/profinet8.webp){: style="width:70%;" }

- Set the device name, which must be also one and only in the PROFINET network and assign it by button **Assign name**.

![Profinet img 9](../../../../source/img/profinet9.webp){: style="width:70%;" }

- Optionally, the check box LED flashes can be used to locate the device in the field. TGZ blinks with letters "Pd" on its segment LED display (Pd stands for PROFIdrive).

