#**Electrical installation of the device**
##Overview
![Shielding connection of the DCbus](../../../../source/img/TGZ-D-560-30_50_shielding1.webp){: style="width:85%;" }   

During the electrical installation of the servo amplifier, the safety instructions must be observed and the following principles must be observed:

- The servo amplifier may only be installed by qualified personnel for the installation of electrical equipment.
- Improper mains voltage, incorrect motor or incorrect connection can damage the servo amplifier. Check that the servo amplifier is suitable for the motor. Compare the rated voltage and current of the connected devices. Connect the device according to the relevant wiring diagrams (chapter "Description of connectors").
- Make sure that the maximum permissible rated voltage at the terminals is not exceeded by more than 10% even in the most unfavorable situations (see ČSN EN 60204-1).
- Excessive current rating of the external fuse will endanger cables and equipment. The supply voltage fuse and the 24 VDC control circuit supply must be installed by the user.
- The status of the servo amplifier must be monitored to identify critical situations.
- Configuration software can be used to change the servo amplifier settings. Any changes or interventions not previously consulted and approved by the equipment manufacturer will void the warranty.

Install the servo amplifier electrical system as follows:

- Select cables in accordance with the ČSN EN 60204 standard.
- Install a servo amplifier shield and ground that meets EMC requirements. Ground the mounting plate and motor cover.
- Connect the servo amplifier and connectors according to common principles and recommendations for suppressing electromagnetic interference.

##Shield connection procedure
###Motor cable connection procedure with shield connection:

- Remove a suitable length of outer motor cable insulation so that the outer cable shield can be conveniently attached to the prepared clamp on the servo amplifier cover.
- Do not shorten the shielding of the feedback pair and, if applicable, the shielding of the brake connection wires.
- Fit the contact sleeves to the prepared stripped ends of the wires.
- Connect the connectors according to the wiring diagram and connect to the&nbsp;device.
- Insert the prepared power wires fitted with the sleeves into the terminals for motor connection 1 or 2.
- Insert the prepared cable with the outer braid into the shield clamp on the cover.
- Insert the remaining parts (feedback pair + brake pair) including their shielding into the prepared earth terminals.

![Shielding connection motor 1](../../../../source/img/TGZ-D-560-30_50_shielding2.webp){: style="width:60%;" }

###Shielding technology
The figures show an unsuitable and suitable shield connection:

<br>

![Shielding connection technology](../../../../source/img/cableShielding4.en.png){: style="width:70%;" }

###Reducing EMI

**The following guidelines will help you reduce electrical interference problems in your application:**

- Ensure a good connection between the parts in the cabinet. Connect the rear panel and the cabinet door to the cabinet body using stranded wires. Never rely on hinges or mounting screws to provide grounding. Ensure that the entire rear surface of the servo amplifier panel is electrically connected. It is recommended to use electrically conductive panels, for example made of aluminum alloys or galvanized steel. For metal panels with a coating or other finish, remove the non-conductive layer behind the servo amplifier.
- Ensure a good ground connection. Connect the switchboard to a good ground. The earth conductors should have the same cross-section as the supply conductors, or one degree smaller.
- Use the cables provided by the manufacturer. If a cable is used which also contains the brake control wires, the brake control wires must have a separate shield.
- Ground the shield at both ends. Ground all shields with as large an area as possible (to achieve low impedance). Connect them to the metal cover of the connectors or shield terminals wherever possible. For cables entering the switchboard, connect the shield around the entire cable circumference (360 °). Never connect just one "wire".
- The cables should not be extended, as this could disturb the shielding and thus the signal processing. To achieve the maximum cable length, use cables with the appropriate cross-section according to ČSN EN 60204 and made of the recommended material.
- Connect the cables correctly. If split cables need to be used, use connectors with a metal cover to connect them. Ensure that both covers are connected to the shield around the entire circumference of the cable (360 °). No part of the cable should remain unshielded. Never connect a split cable using a terminal block.
- The wires between the individual servo amplifiers must also be shielded.

###Recommended cabling

The figures below show the recommended cabling:

![Cable management technology](../../../../source/img/cableMan.en.png){: style="width:80%;" }