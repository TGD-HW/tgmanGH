#**Electrical installation of the device**
##Overview
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

![Shielding connection 1](../../../../source/img/TGZ-S-400_M1Shielding.webp){: style="width:60%;" }

- Use only original TG Drives cables - the shortest possible cables according to the mutual distance and arrangement of individual devices in the switchboard.
- Remove the outer (orange) insulation in length of 60 to 70 mm from the end of the cable. Be careful not to damage the shielding layer (mesh) of the cable.
- Strip the ends of all wires and fit the contact ferrules.
- At the point where the main shield (braid) of the motor cable will contact the ground terminal of the shielding fixture, carefully remove the main cable insulation across the width of the shielding fixture.
- Insert the wires with ferrules to the connector housings according the wiring diagram.
- Connect the connectors to the TGZ servo amplifier.
- Insert the motor cable into the prepared terminals on the steel plate.
- Secure the cable to the steel plate with tie wraps at the designated location.

![Shielding connection 2](../../../../source/img/TGZ-S-400_M1ShieldingDetail.webp){: style="width:30%;" }
![Shielding connection 3](../../../../source/img/TGZ-S-400_M1ShieldingDetail1.webp){: style="width:60%;" }

TGZ-S-400 assembly including the RWMO NCZx EMC filter overall view.

![Shielding connection 4](../../../../source/img/TGZ-S-400_shielding1.webp){: style="width:85%;" }   

Overall view of the TGZ-S-400 assembly, including the input EMI filter RWMO NCZx and the motor choke. 
The motor choke is recommended when using long motor cables to further reduce EMI.

![Shielding connection 5](../../../../source/img/TGZ-S-400_M1ShieldingChoke1.webp){: style="width:85%;" }
![Shielding connection 6](../../../../source/img/TGZ-S-400_M1ShieldingChoke2.webp){: style="width:85%;" }

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