<!--##Konektory-->
___
### Strana komunikace/ethernet/ethercat
___

<img src="../../../../../source/img/TGZ-D-48-13_26_enetCon.png" alt="ETH connectors" style="width:50%;">


<div class="grid cards" markdown>

-   **X11 - TGMotion systémový konektor**

    ---
	<!-- <img src="../../../../../source/img/RJ45_X11_service.png" alt="X11 service RJ45" style="width:60%;"> -->

-   RJ45

	---

	Port Ethernet se používá pro připojení grafického rozhraní TGZ prostřednictvím protokolu UDP.
	Používá se také pro připojení TGMotion (protokol TCP nebo UDP) pomocí Control Observeru a dalších uživatelských aplikací.
	Dalšími podporovanými protokoly jsou Modbus/TCP a Profinet IO.
		
-   **X12 - FSP port**

    ---
	<!-- <img src="../../../../../source/img/RJ45_X12_FSP.png" alt="X12 FSP RJ45" style="width:60%;"> -->

-   RJ45

	---

	Tento port se používá jako tzv. Fast Service Port. 
	Slouží pro velmi rychlé peer-to-peer spojení mezi TGMcontrollerem a PC.
	Používá se speciální protokol.
	V počítači musí být nainstalován ovladač [Winpcap](https://www.winpcap.org/) nebo [Npcap](https://npcap.com/). 
	Není nutné žádné nastavení, komunikační DLL sama najde správný síťový adaptér PC. 
	Pro dosažení nejlepšího výkonu použijte PCIe síťový adaptér.
	Adaptéry USB-Ethernet lze také použít, ale mají menší výkon.
	Některé levné adaptéry USB-Ethernet s protokolem FSP vůbec nefungují.
	Adaptér musí mít paměť pro alespoň 32 paketů najednou.
	
-   **X13 - EtherCAT master**

    ---
	<!-- <img src="../../../../../source/img/RJ45_X13_master.png" alt="X13 ECAT master RJ45" style="width:60%;"> -->

-   RJ45

	---

	Tento port slouží k připojení zařízení EtherCAT na sběrnici EtherCAT.
	Není nutné žádné nastavení.
	Port je schopen pracovat rychlostí 100 Mbit nebo 1 Gbit v závislosti na prvním připojeném zařízení.
	K dispozici je několik 1 Gbitových zařízení EtherCAT, např. servopohony TGZ nebo několik EtherCAT bridge zařízení od jiných výrobců.
	Při použití sběrnice 1 Gbit musí všechna zařízení v řetězci podporovat tuto rychlost.
	
</div>	