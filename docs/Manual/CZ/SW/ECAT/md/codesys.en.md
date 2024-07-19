## Profile Position (PP) and Profile Velocity (PV) Modes

The TGZ servo drive supports additional positioning modes – profile position and profile velocity. In such cases, it uses its internal profile generator. The controller only sets the desired target position (or velocity), and the servo drive performs all the necessary calculations (acceleration/deceleration) to create a position or velocity profile. Communication between the controller and the device does not need to be in real-time. This process works identically for both EtherCAT and CAN field buses.

- Prepare the servo drive using the TGZ_GUI service program: set the `D-Mode` register to `7`: position PG mode. This setting is the same for both PP and PV modes.

![Codesys img](../../../../source/img/codesys1.webp){: style="width:70%;" }

- Depending on the fieldbus used, select `EtherCAT` or `CAN` in the `UseCANbus` setting.

![Codesys img](../../../../source/img/codesys2.webp){: style="width:70%;" }

- If the fieldbus has been changed, save the parameters and restart the drive.
- Open the CODESYS development system and create a new **Standard project**.

![Codesys img](../../../../source/img/codesys3.webp){: style="width:50%;" }

- The Control Win device (soft real-time) is sufficient for PP and PV modes.

![Codesys img](../../../../source/img/codesys4.webp){: style="width:50%;" }

- Add the TGZ device description file (XML for EtherCAT, EDS for CANopen) to the device repository (if not yet done).

![Codesys img](../../../../source/img/codesys5.webp){: style="width:50%;" }

- Choose **Install** and select the correct description file.

![Codesys img](../../../../source/img/codesys6.webp){: style="width:50%;" }

- Right-click on **Device (CODESYS Control Win V3 x64)** and select **Add Device**.

![Codesys img](../../../../source/img/codesys7.webp){: style="width:50%;" }

- In the dialog that appears, select **EtherCAT Master SoftMotion** and click **Add Device**.

![Codesys img](../../../../source/img/codesys8.webp){: style="width:50%;" }

- Click on **EtherCAT_Master_SoftMotion** in the device tree. In the **Add Device** dialog, select the EtherCAT slave TGZ-Drives/TGZ/TGZ Drive V5 and add it to the project.

![Codesys img](../../../../source/img/codesys9.webp){: style="width:50%;" }

- Close the **Add Device** dialog and select **TGZ Drive** in the project device tree. Right-click and choose **Add SoftMotionLight CiA402 Axis**.

![Codesys img](../../../../source/img/codesys10.webp){: style="width:40%;" }

- Rename the added axis to **Drive** using the context menu **Refactoring**.

![Codesys img](../../../../source/img/codesys11.webp){: style="width:60%;" }
![Codesys img](../../../../source/img/codesys12.webp){: style="width:35%;" }

- Start **Control Win PLC** from the Windows system tray.

![Codesys img](../../../../source/img/codesys13.webp){: style="width:20%;" }

- Double-click on **Device (CODESYS Control Win V3 x64)** to open the communication settings window. Establish a connection by pressing Enter.

![Codesys img](../../../../source/img/codesys14.webp){: style="width:90%;" }

- Log in to the device using the username and password.

![Codesys img](../../../../source/img/codesys15.webp){: style="width:50%;" }

- After a successful login, the device icon should display a green light.

![Codesys img](../../../../source/img/codesys16.webp){: style="width:50%;" }

- Open the **EtherCAT_Master_SoftMotion** properties window by double-clicking on the item and select the network card used for the EtherCAT fieldbus by clicking the **Select** button.

![Codesys img](../../../../source/img/codesys17.webp){: style="width:80%;" }

- Check the **Use LRW instead of LWR/LRD** box.

![Codesys img](../../../../source/img/codesys18.webp){: style="width:50%;" }

- To assist the system in identifying the device on the fieldbus, set the correct device ID in the **TGZ_Drive properties** window. Enable **Expert settings**, then select **Configured station alias (ADO 0x0012)** and set the **Value** to the same number as in the `C-ID` register in the TGZ_GUI service program (5 in this example).

![Codesys img](../../../../source/img/codesys19.webp){: style="width:70%;" }

  Group **Common** in TGZ_GUI

  ![Codesys img](../../../../source/img/codesys20.webp){: style="width:80%;" }

- In the **TGZ_Drive properties** window, select the **Startup Parameters** tab and change the value of SDO objects `6060` and `6860` from `8` to `1`.

![Codesys img](../../../../source/img/codesys21.webp){: style="width:60%;" }

- The SoftMotion Lite can be easily tested and controlled using a prepared visualization named **VISU_SML_StartupDrive**. To use it, declare a helper variable in the PLC_PRG code of type `SML_StartupDrive` and name it **sml_visu**, and also set a pointer to the same object.

  
``` 
PROGRAM PLC_PRG
VAR
	sml_visu: SML_StartupDrive;
	p_sml_visu : POINTER TO SML_StartupDrive := ADR(sml_visu);
END_VAR
p_sml_visu^(Axis := Drive);
```

  ![Codesys img](../../../../source/img/codesys22.webp){: style="width:50%;" }
The statement `p_sml_visu^(Axis := Drive)` assigns the SoftMotion Lite Axis to the `sml_visu` variable. It could be run only once, e.g., in the **StartDone** event, but for simplicity, it is called periodically here. The `sml_visu` variable is needed in the visualization template (see below).

- Add a visualization to the application by right-clicking on the **Application** item and selecting **Add Object/Visualization menu item**.

![Codesys img](../../../../source/img/codesys23.webp){: style="width:45%;" }

- Keep the default name **Visualization** and click on the **Add** button.

![Codesys img](../../../../source/img/codesys24.webp){: style="width:30%;" }

- In the **Visualization Toolbox** window, select SML and then the **VISU_SML_StartupDrive** template.

![Codesys img](../../../../source/img/codesys25.webp){: style="width:20%;" }

- Drag and drop the template into the **Visualization** window and, in the following dialog box, assign **m_Startup** to the `sml_visu` variable created above.

![Codesys img](../../../../source/img/codesys26.webp){: style="width:80%;" }

- Position and resize the template as needed in the window.

![Codesys img](../../../../source/img/codesys27.webp){: style="width:80%;" }

- Login and start the PLC. Now interact with the visualization. Enable **bDriveStart**, **bRegulatorOn**, and then **Enable**. Try absolute and relative movements. The **MC_MoveVelocity_SML** block changes the drive mode to PV. Stop the movement at any time using **MC_Stop_SML**. **Read** and **Write** parameters are used to access the internal members of the **AXIS_REF_SML** function block.

- Observe the **Control word**, **Status word**, and **Mode of operation** in the TGZ_GUI.

!!! warning "Warning"
    Remember that the servo will position the motor, so be careful!
