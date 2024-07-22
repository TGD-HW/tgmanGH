## Using TGZ in TIA Portal
- Be careful that the drive can start to move without previous warning.
- Take the appropriate measures to ensure that the operating and service personnel is aware of this danger.
- Implement appropriate protections to ensure that any unintended movement of the machines cannot result in any dangerous situation.
- The user is responsible that, in the event of failure of the drive, the complete system is set to state that is safe for both the machinery and personnel.

## Positioning mode with telegram 111
The most used operating mode is the positioning mode using the basic positioner of TGZ and the TIA Portal function block SinaPos with telegram 111.
Following are the possible steps to create a new project with two TGZ servo amplifiers, both in two axes variant.

- Create a new project.

![Profinet img](../../../../source/img/profinet11.webp){: style="width:90%;" loading="lazy"}

- Open the project view.

![Profinet img](../../../../source/img/profinet12.webp){: style="width:90%;" loading="lazy"}

- Install the XML GSD files describing the TGZ device in PROFINET network.
  There are two types of files, one for the single axis variant, called `GSDML-V2.4-TGDrives-TGZ-S-xxxxx.xml` and the second for the double axis TGZ variant `GSDML-V2.4-TGDrives-TGZ-D-xxxxx.xml` (where `xxxxx` stands for file creation date).

<!-- add placeholders for GSDML-V2.4-TGDrives-TGZ-S-xxxxx.xml and GSDML-V2.4-TGDrives-TGZ-D-xxxxx.xml - direct download links from the web -->

  The files can be downloaded from the TG Drives website.

- Select menu item `Options|Manage general station description files (GSD)`.

![Profinet img](../../../../source/img/profinet13.webp){: style="width:90%;" loading="lazy"}

- Enter the source path where the GSDML files are stored, select the appropriate file and click on the **Install** button.

!!! note "Note"
    Both files can be installed simultaneously.

![Profinet img](../../../../source/img/profinet14.webp){: style="width:50%;" loading="lazy"}

- In the Project tree on left top, double click on the **Add new device item**.

![Profinet img](../../../../source/img/profinet15.webp){: style="width:30%;" loading="lazy"}

- Select the PLC controller used in the hardware project.
  For this tutorial, the PLC S7-1200 is used.

![Profinet img](../../../../source/img/profinet16.webp){: style="width:50%;" loading="lazy"}

!!! warning "Warning"
    Be careful to choose the right firmware version (V4.1 here).

- The **Devices & networks** window should open in the TIA portal.
  If not, use the tree view item **Devices & networks** in the Project view and open the window by double click.

![Profinet img](../../../../source/img/profinet17.webp){: style="width:90%;" loading="lazy"}

- Now it is time to add TGZ drives to the project.
  In the **Catalog pane**, open the **Other field devices** item, and navigate to `PROFINET IO|Drives|TGDrives|tgz-d|tgz-d`.
  Add the device to the project by double click.

![Profinet img](../../../../source/img/profinet18.webp){: style="width:50%;" loading="lazy"}

- Do it two times to add two TGZ servo drives.
  Use `tgz-s` item to work with single axis TGZ variant.
  The **Devices & network** window should look like:

![Profinet img](../../../../source/img/profinet19.webp){: style="width:90%;" loading="lazy"}

- Rename the drives in the **Network overview** pane according to the hardware project.
  The names must be the same as used during [preparing the devices](network.md#ProfinetIPsettings).

![Profinet img](../../../../source/img/profinet20.webp){: style="width:30%;" loading="lazy"}

- Connect the drives with PLC.
  Click on the blue text **Not assigned** and select the **PLC PROFINET interface_1**.

![Profinet img](../../../../source/img/profinet21.webp){: style="width:70%;" loading="lazy"}

- Do the same for the second TGZ.

![Profinet img](../../../../source/img/profinet22.webp){: style="width:70%;" loading="lazy"}

- Optionally use the **Topology** view and connect the PLC and TGZ devices by mouse in the same manner as in reality.
  This step is not necessary.

![Profinet img](../../../../source/img/profinet23.webp){: style="width:70%;" loading="lazy"}
![Profinet img](../../../../source/img/profinet24.webp){: style="width:70%;" loading="lazy"}

- Assign the right IP addresses to all devices in the project.
  The IP addresses and PROFINET device names must correspond to the values entered in the [Name and IP address of the device](network.md#ProfinetIPsettings).
  Activate the connection in the PLC box (green rectangle) and in the **Properties** pane below use the **Ethernet addresses** item.
  Enter the right IP address in the text box, together with the Subnet mask (usually 255.255.255.0).

![Profinet img](../../../../source/img/profinet25.webp){: style="width:70%;" loading="lazy"}

- In a similar way assign the IP addresses to other devices.

![Profinet img](../../../../source/img/profinet26.webp){: style="width:70%;" loading="lazy"}

- Switch to **Device view** (on the top right) and select the first TGZ device (`tgz_1`) by the combo box.
  In the hardware catalog on the right, double click on **Siemens telegram 111**.
  Do it twice for both axes (slot 1 and slot 2).

![Profinet img](../../../../source/img/profinet27.webp){: style="width:90%;" loading="lazy"}

- The result should look like:
![Profinet img](../../../../source/img/profinet28.webp){: style="width:60%;" loading="lazy"}

- Rename the axes (slots 1 and 2) according to the real hardware project.

![Profinet img](../../../../source/img/profinet29.webp){: style="width:60%;" loading="lazy"}

- Do the same for the second TGZ drive and get something like:

![Profinet img](../../../../source/img/profinet30.webp){: style="width:90%;" loading="lazy"}

- Download the project to the PLC by using the icon **Download** to device or by using menu command `Online|Download to device`.

![Profinet img](../../../../source/img/profinet31.webp){: style="width:60%;" loading="lazy"}

- It is necessary to find the PLC.
  Click on the **Start search** button in the following dialog.

![Profinet img](../../../../source/img/profinet32.webp){: style="width:70%;" loading="lazy"}

- After a while the PLC should appear in the list **Select target device**.
  Select it and click on the **Load** button.

![Profinet img](../../../../source/img/profinet33.webp){: style="width:70%;" loading="lazy"}

- The dialog box **Load preview** summarizes the load status.

![Profinet img](../../../../source/img/profinet34.webp){: style="width:70%;" loading="lazy"}

- Click on **Load** and then on the **Finish** button.

![Profinet img](../../../../source/img/profinet35.webp){: style="width:70%;" loading="lazy"}

- Check the hardware configuration.
  Click on the icon **Go online** in the command bar.

![Profinet img](../../../../source/img/profinet36.webp){: style="width:70%;" loading="lazy"}

- Wait for the green mark status in the project view.

![Profinet img](../../../../source/img/profinet37.webp){: style="width:30%;" loading="lazy"}

- Switch back to offline mode by the **Go offline** command.

![Profinet img](../../../../source/img/profinet38.webp){: style="width:70%;" loading="lazy"}

- Expand the item **Project view to Program blocks|Main [OB1]** and open it by double click.

![Profinet img](../../../../source/img/profinet39.webp){: style="width:30%;" loading="lazy"}

- A new window with PLC blocks will open.

![Profinet img](../../../../source/img/profinet40.webp){: style="width:90%;" loading="lazy"}

- Find the function block **SinaPos** (FB) in the **Instructions** pane on the right.
  The search edit box can be used for that.

![Profinet img](../../../../source/img/profinet41.webp){: style="width:30%;" loading="lazy"}

- Drag and drop the SinaPos block to the line **Network 1** and assign the Data block name.
  Preferably use the same name as for axes (slots) assigned in the previous steps.

![Profinet img](../../../../source/img/profinet42.webp){: style="width:90%;" loading="lazy"}

- Connect the telegram with the HWIDSTW and HWIDZSW inputs of the function block.

![Profinet img](../../../../source/img/profinet43.webp){: style="width:50%;" loading="lazy"}

- The result should be something like:

![Profinet img](../../../../source/img/profinet44.webp){: style="width:40%;" loading="lazy"}

- Repeat the SinaPos FB drag and drop and axis assignment for **Network 2** together with **Axis_2**.

![Profinet img](../../../../source/img/profinet45.webp){: style="width:40%;" loading="lazy"}

- The same process is for drive tgz_2 and **Axis_3** and **Axis_4**.

![Profinet img](../../../../source/img/profinet46.webp){: style="width:40%;" loading="lazy"}
![Profinet img](../../../../source/img/profinet47.webp){: style="width:40%;" loading="lazy"}

- Compile and download the modified project to the PLC by the command `Online|Download to device` and switch the TIA Portal back to online mode.
- The function block can be controlled by a watch table.
  Create a new table by `Project view item PLC_1|Watch and force tables|Add new watch table` and rename it to **Axis_1_Control**.

![Profinet img](../../../../source/img/profinet48.webp){: style="width:30%;" loading="lazy"}

- Add the following SinaPos function block inputs and outputs:

![Profinet img](../../../../source/img/profinet49.webp){: style="width:90%;" loading="lazy"}

- When the values are correctly set (ModePos, Position, Velocity, EnableAxis), by switching **ExecuteMode** from FALSE to TRUE the desired movement should start.
  The Status must be `16#7002` for the correct behavior of the function block.
  See the online [documentation for the SinaPos](https://cache.industry.siemens.com/dl/files/845/109736845/att_928039/v1/109736845_G120_CU250S2PN_at_S7_1200_SINA_POS_v10_DOCU_en.pdf) for additional information how to operate this FB.
- Optionally create additional watch tables for working with other axes.

![Profinet img](../../../../source/img/profinet50.webp){: style="width:90%;" loading="lazy"}

## Supported Control Bits in ConfigEPos

Additional bits can be used in **ConfigEPos** value to fine control the TGZ behavior.
When setting to `16#0000_0103` (bit 8 is also set), the constant setpoint transfer is activated.
When the traversing task is active, it is possible to change the target position or velocity, and the drive responds immediately without the need of toggling the ExecuteMode bit.
When the task finishes, the drive goes back to state `S41` (see PROFIdrive documentation) and waits for the rising edge of ExecuteMode bit.

It is also possible to set the **ConfigEPos** to `16#0010_0103` (set bits 8 and 20).
Then the drive keeps the state `S451` even if the task is finished, and a new task is immediately started when a new position arrives.
To exit from state `S451`, the **ConfigEPos** value must be changed to `16#0000_0103`.

!!! note "Note"

    Note that the value `16#0000_0103` or `16#0010_0103` can be used only for absolute positioning, i.e., when ModePos = 2.
    As the minimal cycle time is 1 ms, it is possible to achieve constant positioning by PLC.
    It is necessary to correctly set acceleration and speed values.
    Also, the trapezoidal speed profile is recommended (Profile generator type 3).

Bit 8 of the **ConfigEPos** is internally mapped to bit 12 of the POS_STW1 control word in the telegram (MdiTrTyp).
Bit 20 is mapped to bit 11 of the POS_STW1.

## Using S7-300 or S7-400 PLC with Telegram 111

To use the older PLCs, download a DriveLib library from the internet.
At the time of writing this manual, the filename was `Drive_Lib_V62_S7_300_400.zip`.
Extract it and install it to TIA portal.
After that, the steps to create a project will be the same as above, only use the **Libraries** tab and there find the **SINA_POS** function to add it to the **Main’s Network** line.

![Profinet img](../../../../source/img/profinet51.webp){: style="width:30%;" loading="lazy"}

The TGZ servo drive now supports startup modes Advanced and Legacy.
The Legacy mode is used for S7-300 or S7-400.
The modified GSDML files (PNIO version 2.4) are available at the [TGDrives website](https://www.tgdrives.cz/ke-stazeni/digitalni-servozesilovace-ke-stazeni/#c425).
There are also GSDML files of version V2.2 for use in older software packages.

## Speed Mode Using Standard Telegram 3

- Create a new project and name it *TGZ-S-Tele3*.

![Profinet img](../../../../source/img/profinet52.webp){: style="width:90%;" loading="lazy"}

- Open the project view.

![Profinet img](../../../../source/img/profinet53.webp){: style="width:90%;" loading="lazy"}

- Double click on **Add new device**.

![Profinet img](../../../../source/img/profinet54.webp){: style="width:30%;" loading="lazy"}

- Select the right PLC controller and its version.

![Profinet img](../../../../source/img/profinet55.webp){: style="width:50%;" loading="lazy"}

- Select **Network view** and expand the tree in `Hardware catalog to item Other field devices|PROFINET IO|Drives|TGDrives|tgz-s|tgz-s`.

![Profinet img](../../../../source/img/profinet56.webp){: style="width:70%;" loading="lazy"}

- Double click on tgz-s, the device will be added to the project in **Network view**.

![Profinet img](../../../../source/img/profinet57.webp){: style="width:70%;" loading="lazy"}

- Rename the TGZ device and give it a name of the device – the same which was set during commissioning as described in [Name and IP address of the device](network.md#ProfinetIPsettings).

![Profinet img](../../../../source/img/profinet58.webp){: style="width:70%;" loading="lazy"}

- For this example, we use the name tgz_2.

![Profinet img](../../../../source/img/profinet59.webp){: style="width:70%;" loading="lazy"}

- Connect the TGZ drive to PLC by clicking on the **Not assigned** blue text and selecting `PLC_1 PROFINET interface_1`.

![Profinet img](../../../../source/img/profinet60.webp){: style="width:70%;" loading="lazy"}

- The result should look like this:

![Profinet img](../../../../source/img/profinet61.webp){: style="width:70%;" loading="lazy"}

- Assign the IP address to the PLC.
  Use the address described in the section [Name and IP address of the device](network.md#ProfinetIPsettings).

![Profinet img](../../../../source/img/profinet62.webp){: style="width:70%;" loading="lazy"}

- Assign the IP address to the TGZ servo drive. Again, use the address already stored in the TGZ device.

![Profinet img](../../../../source/img/profinet63.webp){: style="width:70%;" loading="lazy"}

- Select telegram 3 for slot 1 of the TGZ.

![Profinet img](../../../../source/img/profinet64.webp){: style="width:70%;" loading="lazy"}

- Double click on the **Standard telegram 3** item to set the telegram automatically.

![Profinet img](../../../../source/img/profinet65.webp){: style="width:70%;" loading="lazy"}

- Download the hardware configuration to PLC:

![Profinet img](../../../../source/img/profinet66.webp){: style="width:70%;" loading="lazy"}

- Click on the **Start search** button.

![Profinet img](../../../../source/img/profinet67.webp){: style="width:70%;" loading="lazy"}

- The PLC should appear in the list box.

![Profinet img](../../../../source/img/profinet68.webp){: style="width:70%;" loading="lazy"}

- Click on the **Load** button, wait for compilation to finish, and in the following dialog box select **Stop all modules** and click on the **Load** button again.

![Profinet img](../../../../source/img/profinet69.webp){: style="width:70%;" loading="lazy"}

- Finish the loading by clicking on the **Finish** button.

![Profinet img](../../../../source/img/profinet70.webp){: style="width:70%;" loading="lazy"}

- If not yet selected, choose telegram number 3 in the TGZ GUI service program.

![Profinet img](../../../../source/img/profinet71.webp){: style="width:70%;" loading="lazy"}

- Save parameters and restart the TGZ drive.

![Profinet img](../../../../source/img/profinet72.webp){: style="width:70%;" loading="lazy"}

- Switch TIA portal to **Online mode**, there should be green check marks in the project view.

![Profinet img](../../../../source/img/profinet73.webp){: style="width:30%;" loading="lazy"}

- If there are any errors, stop and start the PLC.
  Also, check that the `PD_SetDataCounter` parameter is increasing in the TGZ GUI service program.

![Profinet img](../../../../source/img/profinet74.webp){: style="width:30%;" loading="lazy"}

- Expand the `PLC_1|Technology object|Add new object` item and double-click on it.

![Profinet img](../../../../source/img/profinet75.webp){: style="width:30%;" loading="lazy"}

- Select **Motion control** and **TO_PositioningAxis**. Optionally, give a suitable name for the object.

![Profinet img](../../../../source/img/profinet76.webp){: style="width:70%;" loading="lazy"}

- In the `Axis_1` window under `Basic parameters|General`, select the **PROFIdrive** radio button.

![Profinet img](../../../../source/img/profinet77.webp){: style="width:70%;" loading="lazy"}

- Switch to `Basic parameters|Drive` and select the right drive.

![Profinet img](../../../../source/img/profinet78.webp){: style="width:70%;" loading="lazy"}

- Update the **Reference speed** and **Maximum speed** if necessary, according to the machinery.

![Profinet img](../../../../source/img/profinet79.webp){: style="width:50%;" loading="lazy"}

- Select `Basic parameters|Encoder` and switch to **Encoder on drive**.

![Profinet img](../../../../source/img/profinet80.webp){: style="width:70%;" loading="lazy"}

- Optionally, set up other parameters in the **Extended parameters** items according to the hardware project.
- When finished, switch to offline mode and download the modified project to the PLC using the menu command `Online|Download to device`. The process is the same as described above.
- Switch back to online mode and double-click on the **Commissioning** item in the project view.

![Profinet img](../../../../source/img/profinet81.webp){: style="width:30%;" loading="lazy"}

- Click on the **Activate** button at the top of the window.

![Profinet img](../../../../source/img/profinet82.webp){: style="width:70%;" loading="lazy"}

- Enable the axis using the **Enable** button.

![Profinet img](../../../../source/img/profinet83.webp){: style="width:70%;" loading="lazy"}

- Now you can Jog the axis, perform Homing, and/or Positioning depending on the selected command.

![Profinet img](../../../../source/img/profinet84.webp){: style="width:70%;" loading="lazy"}

  For a detailed description of the technology object, refer to the online documentation.
