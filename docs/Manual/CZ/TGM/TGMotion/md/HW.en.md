##Popis hardwarového řešení

Centrem hardwarového řešení je průmyslové PC, které prostřednictvím EtherCAT může komunikovat až s 256 periferiemi.
Periferiemi jsou nejčastěji servopohony, I/O jednotky nebo tenzometrické můstky.
Uživatelské rozhraní je zabezpečeno pomocí operátorského panelu.
Lze také využívat klasického ovládání pomocí myši, klávesnice nebo tabletu.
S okolím může PC komunikovat z Windows aplikací prostřednictvím PROFINETu, ethernetu nebo internetu.

<img src="../../img/HW_TGmotion.png" alt="Hardwarové řešení TG Motion"  style="width:100%;">

!!! info "Upozornění"
	
	Vzhledem k tomu, že systém běží na PC s nainstalovaným operačním systémem Windows, lze také využívat všech možností konektivity OS.
	
##PC – počítač

Společnost TG Drives dodává ucelené systémy s průmyslovým PC jako řídící jednotkou.
Hardwarové požadavky na PC jsou nejvíce dány operačním systémem.
Systém TG Motion spolupracuje s OS Windows.   

Podporované OS:

-	Windows XP Embedded
-	Windows 7
-	Windows Embedded Standard 7
-	Windows 8.1 (x64)
-	Windows Embedded Standard 8.1 (x64)

Mezi vyžadovaná rozhraní patří USB2 nebo USB3 a síťová karta pro připojení k EtherCAT.
Výčet podporovaných síťových karet je uveden v následující tabulce.

| Výrobce | Driver   | Popis                                                      | Obchodní označení                              | Slot   | Test  | Podpora |
|---------|----------|------------------------------------------------------------|-------------------------------------------------|--------|-------|---------|
| Intel   | Rt8255x  | 82557/8/9/0/1 Intel PRO/100 S Server Adapter (82550EY)    |                                                 | PCI    | ano   | ano     |
| Intel   | Rt8255x | 82559 ER (8255xER/IT) Intel Fast Ethernet                           |                                                 | PCI    | ne    | ano     |
| Intel   | RtE1000  | Intel 82566 MM Gigabit Ethernet Controller                |                                                 | PCI    | ano   | ne      |
| Intel	  | RtE1000 | Intel 82566 DM Gigabit Ethernet Controller                 |                                                 | PCI    | ne    | ne      |
| Intel   | RtE1000| Intel 82574L Gigabit Ethernet Controller                   |                                                 | PCI    | ano   | ano     |
| Intel   | RtIGB    | I210 T1 Ethernet Server Adapter                            |                                                 | PCI    | ano   | ano     |
| Intel   | RtIGB	| I350  10/100/1000 Mb/s Ethernet Controller, x4 PCIe, Copper     |                                                 | PCI    | ne    | ano     |
| Realtek | RtRtl81x9| 8139 8100 8169 8110 GigaFast EE110-AXP, 8139(c) (non plus)| TP-Link: TF-3239DL                              | PCI    | ano   | ano     |
| Realtek | RtRtl81x9 | GigaFast GE1000-AXP 8169                                   |                                                 | PCI    | ano   | ano     |
| Realtek | RtRtl81x8| RTL8168/8111(B, C, CP, D, DP)                              | TP-Link: TG-3468                                | PCIe   | ano   | ano     |

!!! info "Upozornění"
	System TG Motion by mohl být provozován i na běžných PC.
	Ucelené systémy dodávané firmou TG Drives ale tuto variantu nepreferují.
	
##Servopohony
TG Motion běžící na průmyslovém PC může po rozhraní EtherCAT nezávisle komunikovat až s 256 servopohony.
Může načítat jejich polohy, posílat požadované pozice, načítat data vstupů a nastavovat výstupy (pokud jimi servozesilovače disponují).
Pokud se jedná o víceosý servopohon, mohou být jedním servozesilovačem řízeny dvě osy (případně více os). Viz kapitolu Struktura Servo.

| Výrobce | Popis               | Test | Podpora |
|---------|---------------------|------|---------|
| Seidel  | TGP PowerStage      | ano  | ano     |
| Danaher | ServoStar S300      | ano  | ano     |
| Danaher | ServoStar S700      | ano  | ano     |
| Danaher | AKD                 | ano  | ano     |
| TG Drives | TGZ-D               | ano  | ano     |

##I/O jednotky
TG Motion běžící na průmyslovém PC může po rozhraní EtherCAT nezávisle komunikovat až s 256 I/O jednotkami.
Může načítat data analogových i digitálních vstupů a nastavovat analogové i digitální výstupy, případně načítat data tenzometrických můstků.

##Podporované a testované typy I/O jednotek

| Výrobce | Popis | Test | Podpora |
|---|---|---|---|
| TG Drives | DIO Module (old) | ano | ano |
| TG Drives | DIO Module | ano | ano |
| TG Drives | Tenzometer (old) | ano | ano |
| TG Drives | Tenzometer | ano | ano |
| B&R | X20BC00G3 – Coupler | ano | ano |
| B&R | X20DI9371 – 12× Digital Input 24 V (0,2 ms) | ano | ano |
| B&R | X20DO9322 – 12× Digital Output 24 V (0,5 A na kanál) | ano | ano |
| B&R | X20PS9400 – Power Supply 24 V (max. 10 A) | ano | ano |
| B&R | X20PS9402 – Power Supply 24 V (max. 10 A) | ano | ano |
| B&R | X20PS2100 – Power Supply 24 V (max. 10 A) | ano | ano |
| B&R | X20AI1744 – 1× Full bridge Input (24 bit, 5 kHz) | ano | ano |
| B&R | X20AI2622 – 2× Analog Input ±10 V nebo 0–20 mA (13 bit, 300 μs) | ano | ano |
| B&R | X20AI4632 – 4× Analog Input ±10 V nebo 0–20 mA (16 bit, 50 μs) | ano | ano |
| B&R | X20AO2622 – 2× Analog Output ±10 V nebo 0–20 mA (13 bit, 200 μs) | ano | ano |
| B&R | X20AO4622 – 4× Analog Output ±10 V nebo 0–20 mA (13 bit, 300 μs) | ano | ano |
| B&R | X20AO4632 – 4× Analog Output ±10 V nebo 0–20 mA (16 bit, 50 μs) | ano | ano |
| B&R | X20DC2395 – 2× PWM Output 24 V (1 Hz – 24 kHz) | ano | ano |
| Beckhoff | BK1120 – Coupler | ano | ano |
| Beckhoff | ET1100 chipset | ano | ano |
| Beckhoff | KL3404 – 4× Analog Input −10 až 10 V (12 bit, 2 ms) | ne | ano |
| Beckhoff | KL3464 – 4× Analog Input 0–10 V (12 bit, 2 ms) | ano | ano |
| Beckhoff | KL3408 – 8× Analog Input −10 V až 10 V (12 bit, 4 ms) | ne | ano |
| Beckhoff | KL3468 – 8× Analog Input 0–10 V (12 bit, 4 ms) | ne | ano |
| Beckhoff | KL3061 – 1× Analog Input 0–10 V (12 bit, 1 ms) | ano | ano |
| Beckhoff | KL3062 – 2× Analog Input 0–10 V (12 bit, 2 ms) | ne | ano |
| Beckhoff | KL4001 – 1× Analog Output 0–10 V (12 bit, 1,5 ms) | ano | ano |
| Beckhoff | KL4002 – 2× Analog Output 0–10 V (12 bit, 1,5 ms) | ano | ano |
| Beckhoff | Všechny jednoduché digitální terminály jako: | | |
| Beckhoff | KL1418 – 8× Digital Input 24 V (0,2 ms) | ano | ano |
| Beckhoff | KL2408 – 8× Digital Output 24 V (0.5 A na kanál) | ano | ano |
| Beckhoff | EK1100 – Coupler | ano | ano |
| Beckhoff | EL1008 – 8× Digital Input 24 V (3,0 ms) | ano | ano |
| Beckhoff | EL2008 – 8× Digital Output 24 V (0,5 A na kanál) | ano | ano |
| Festo | CPX-FB38 + Digital Input, Digital Output, … | ano | ano |

##Externí komunikace
Na průmyslovém PC běží OS Windows, pro uživatele jsou k dispozici všechny typy komunikací, které tento OS nabízí.
Windows aplikace tedy mohou komunikovat prostřednictvím PROFINETu, ethernetu nebo internetu.
TG Motion nabízí komunikaci s jinými systémy pomocí sběrnice CAN.

!!! info "Upozornění"
	Komunikace TG Motion po CAN funguje nezávisle na komunikaci prostřednictvím EtherCAT.
