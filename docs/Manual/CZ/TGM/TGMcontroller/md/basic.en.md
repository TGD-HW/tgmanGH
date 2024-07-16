![Basic view](../img/3Dview.png){: style="width:35%;" }

As software and operating systems evolve, it is becoming increasingly difficult to run real-time extensions on PCs.
On the other hand the communication speeds are more than sufficient using standard Ethernet gigabit connection.
An external device with a powerful real-time processor and a fast connection can easily replace the hard to maintain software extension to an operating system.
The **TGMcontroller** device perfectly meets the above mentioned requirements and features.


##Features
The **TGMcontroller** implements the complete TGMotion control system – version 502 or higher.
It works as EtherCAT master and through the fieldbus supports up to:

- 64 servo axes 
- 16 I/O units 
- 16 additional user defined devices
- 3 independent CNC interpolators, each with 10 axes.

The oscilloscope memory has size of 32 MB, which allows storing information about a very large process.
The virtual PLC programs are programmed in C or C++ language, complete gnu tool chain is available.
PLC development can be done in any popular IDE system, like Visual Studio or VS Code.   

The minimal cycle time is 100 µs.   

EtherCAT master has extremely low jitter of several nanoseconds.
It means that the EtherCAT packets are sent to the fieldbus very precisely in time domain and allow controlling the motion process with very high quality.   

Full set of communication and diagnostics tools are available – Windows and partially Linux.
The TGMotion control system is described in [TG Motion operation manual](../../TGMotion/md/PLC.md#MotionPLC).

##Hardware
The system is based on the proven and powerful FPGA Zynq processor system – a double core Cortex A9 processor running at 667 MHz.
The device has 128 MB of RAM memory and 16 MB of flash storage (used for the safety golden firmware version).
The actual firmware, configuration, and user-defined PLC are stored on an 8 GB SD card.
Communication with other devices can be done by 3 Ethernet ports and/or CAN bus.
The system has 10 digital inputs, 6 digital outputs and 2 analog inputs.
There are also 3 feedback connectors for a movement monitoring.
The supported digital interfaces are Hiperface DSL, EnDAT 2.2, SSI and incremental encoder IRC.
