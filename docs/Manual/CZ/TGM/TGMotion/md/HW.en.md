## Hardware Solution Description

An industrial PC, which can communicate with up to 256 peripheries via EtherCAT, makes the heart of the hardware solution. The peripheries most frequently met are the servo drives, I/O units, or strain gauges. The user interface is managed by means of an operator panel. Classical control methods using a mouse, a keyboard, or tablet, can also be used. The PC can communicate with its environment from Windows applications through PROFINET, Ethernet, or Internet.

![Hardware solution of TG Motion](../img/HW_TGmotion.png){: style="width:100%;" }

!!! info "Note"

    With regard to the fact that the system is running on a PC with a Windows operating system, all connectivity options of this system can be used.

## PC – Computer

TG Drives delivers comprehensive systems with a PC-based control unit. The PC hardware requirements are given by the operating system. TG Motion system cooperates with Windows operating system (OS). 

Supported operating systems:

- Windows XP Embedded
- Windows 7
- Windows Embedded Standard 7
- Windows 8.1 (x64)
- Windows Embedded Standard 8.1 (x64)

Among the mostly required interfaces there are USB2 or USB3 and a network card for connecting to EtherCAT. Supported network cards are listed in the table below.

| Manufacturer | Driver    | Description                                                     | Trade Name                                    | Slot | Test | Support |
|--------------|-----------|-----------------------------------------------------------------|-----------------------------------------------|------|------|---------|
| Intel        | Rt8255x   | 82557/8/9/0/1 Intel PRO/100 S Server Adapter (82550EY)         |                                               | PCI  | yes  | yes     |
| Intel        | Rt8255x   | 82559 ER (8255xER/IT) Intel Fast Ethernet                      |                                               | PCI  | no   | yes     |
| Intel        | RtE1000   | Intel 82566 MM Gigabit Ethernet Controller                     |                                               | PCI  | yes  | no      |
| Intel        | RtE1000   | Intel 82566 DM Gigabit Ethernet Controller                     |                                               | PCI  | no   | no      |
| Intel        | RtE1000   | Intel 82574L Gigabit Ethernet Controller                       |                                               | PCI  | yes  | yes     |
| Intel        | RtIGB     | I210 T1 Ethernet Server Adapter                                |                                               | PCI  | yes  | yes     |
| Intel        | RtIGB     | I350 10/100/1000 Mb/s Ethernet Controller, x4 PCIe, Copper     |                                               | PCI  | no   | yes     |
| Realtek      | RtRtl81x9 | 8139 8100 8169 8110 GigaFast EE110-AXP, 8139(c) (non plus)     | TP-Link: TF-3239DL                            | PCI  | yes  | yes     |
| Realtek      | RtRtl81x9 | GigaFast GE1000-AXP 8169                                       |                                               | PCI  | yes  | yes     |
| Realtek      | RtRtl81x8 | RTL8168/8111(B, C, CP, D, DP)                                  | TP-Link: TG-3468                              | PCIe | yes  | yes     |

!!! info "Note"

    TG Motion could also be run on ordinary PCs. However, the comprehensive systems, which are delivered by TG Drives, do not prefer this variant.

## Servo Drives

TG Motion, which is running on an industrial PC, can separately communicate – via EtherCAT interface – with as many as 256 servo drives. It can read their positions, send the required positions, read input data, and set outputs (provided that they are available on the servo amplifiers). In the case of multi-axis servo drives, one servo amplifier can control two or more axes. See Chapter Servo structure.

| Manufacturer | Description        | Test | Support |
|--------------|--------------------|------|---------|
| Seidel       | TGP PowerStage     | yes  | yes     |
| Danaher      | ServoStar S300     | yes  | yes     |
| Danaher      | ServoStar S700     | yes  | yes     |
| Danaher      | AKD                | yes  | yes     |
| TG Drives    | TGZ-D              | yes  | yes     |

## I/O Units

TG Motion, which is running on an industrial PC, can communicate – via EtherCAT interface – separately with as many as 256 input/output units. It can read analog as well as digital input data and set analog as well as digital outputs, or, if need be, read strain gauge data.

## Supported and Tested I/O Unit Types

| Manufacturer | Description                                      | Test | Support |
|--------------|--------------------------------------------------|------|---------|
| TG Drives    | DIO Module (old)                                 | yes  | yes     |
| TG Drives    | DIO Module                                       | yes  | yes     |
| TG Drives    | Strain gauge (old)                               | yes  | yes     |
| TG Drives    | Strain gauge                                     | yes  | yes     |
| B&R          | X20BC00G3 – Coupler                              | yes  | yes     |
| B&R          | X20DI9371 – 12× Digital Input 24 V (0.2 ms)      | yes  | yes     |
| B&R          | X20DO9322 – 12× Digital Output 24 V (0.5 A for a channel) | yes  | yes     |
| B&R          | X20PS9400 – Power Supply 24 V (max. 10 A)        | yes  | yes     |
| B&R          | X20PS9402 – Power Supply 24 V (max. 10 A)        | yes  | yes     |
| B&R          | X20PS2100 – Power Supply 24 V (max. 10 A)        | yes  | yes     |
| B&R          | X20AI1744 – 1× Full bridge Input (24 bit, 5 kHz) | yes  | yes     |
| B&R          | X20AI2622 – 2× Analog Input ±10 V or 0–20 mA (13 bit, 300 μs) | yes  | yes     |
| B&R          | X20AI4632 – 4× Analog Input ±10 V or 0–20 mA (16 bit, 50 μs) | yes  | yes     |
| B&R          | X20AO2622 – 2× Analog Output ±10 V or 0–20 mA (13 bit, 200 μs) | yes  | yes     |
| B&R          | X20AO4622 – 4× Analog Output ±10 V or 0–20 mA (13 bit, 300 μs) | yes  | yes     |
| B&R          | X20AO4632 – 4× Analog Output ±10 V or 0–20 mA (16 bit, 50 μs) | yes  | yes     |
| B&R          | X20DC2395 – 2× PWM Output 24 V (1 Hz – 24 kHz)   | yes  | yes     |
| Beckhoff     | BK1120 – Coupler                                  | yes  | yes     |
| Beckhoff     | ET1100 chipset                                    | yes  | yes     |
| Beckhoff     | KL3404 – 4× Analog Input −10 V to 10 V (12 bit, 2 ms) | no   | yes     |
| Beckhoff     | KL3464 – 4× Analog Input 0–10 V (12 bit, 2 ms)      | yes  | yes     |
| Beckhoff     | KL3408 – 8× Analog Input −10 V to 10 V (12 bit, 4 ms) | no   | yes     |
| Beckhoff     | KL3468 – 8× Analog Input 0–10 V (12 bit, 4 ms)      | no   | yes     |
| Beckhoff     | KL3061 – 1× Analog Input 0–10 V (12 bit, 1 ms)      | yes  | yes     |
| Beckhoff     | KL3062 – 2× Analog Input 0–10 V (12 bit, 2 ms)      | no   | yes     |
| Beckhoff     | KL4001 – 1× Analog Output 0–10 V (12 bit, 1.5 ms)    | yes  | yes     |
| Beckhoff     | KL4002 – 2× Analog Output 0–10 V (12 bit, 1.5 ms)    | yes  | yes     |
| Beckhoff     | All simple digital terminals, such as:               |      |         |
| Beckhoff     | KL1418 – 8× Digital Input 24 V (0.2 ms)              | yes  | yes     |
| Beckhoff     | KL2408 – 8× Digital Output 24 V (0.5 A for a channel)| yes  | yes     |
| Beckhoff     | EK1100 – Coupler                                     | yes  | yes     |
| Beckhoff     | EL1008 – 8× Digital Input 24 V (3.0 ms)              | yes  | yes     |
| Beckhoff     | EL2008 – 8× Digital Output 24 V (0.5 A for a channel)| yes  | yes     |


## External Communication

The industrial PC runs the Windows operating system, offering users all types of communication available in this OS.
Windows applications can therefore communicate via PROFINET, Ethernet, or the Internet.
TG Motion provides communication with other systems using the CAN bus.

!!! info "Note"
    The communication of TG Motion via CAN operates independently of EtherCAT communication.

