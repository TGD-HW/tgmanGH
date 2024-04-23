##Stručný popis
<br>

<img src="../../img/3Dview.png" alt="Basic view" style="width:35%;">

<br>

**TGMmini** je plnohodnotný počítač s dvoujádrovým procesorem ARM. 
Obě jádra procesoru jsou využita pro operační sytém Linux (distribuce Debian 10 s real-time rozšířením Xenomai) s grafickou nadstavbou Xfce. 
Řídicí systém **TG&nbsp;Motion**, umožňující řízení servopohonů a I/O jednotek přes sběrnici EtherCAT, běží z části v real-time prostředí Linuxu a z části v samostatném procesoru s hardwarovým EtherCAT akcelerátorem (vše implementováno v FPGA). 
Ovládání **TG&nbsp;Motion** se provádí z linuxového prostředí, na všechny potřebné operace jsou k dispozici knihovny, jejichž API rozhraní je totožné s knihovnami DLL pro systém Windows na PC. 
Uživatelské virtuální PLC programy lze psát a vyvíjet na PC, zdrojový text se pouze přeloží kompilátorem pro procesor ARM a vytvořený binární soubor se přenese na **TGMmini**, kde se spustí. 
Pro přístup ke sdílené paměti systému **TG&nbsp;Motion** slouží knihovna TGM_Comm_Int_5, opět ve shodné verzi pro PC a **TGMmini**.

##Rozdíly vůči TG Motion na PC
TG Motion používaný na TGMmini je ve verzi 501 či vyšší. 
Verze pro PC i TGMmini jsou navzájem kompatibilní. 
Manuál pro systém TG Motion tuto verzi zahrnuje a je mj. k dispozici na [webových stránkách TG Drives](https://www.tgdrives.cz/). 
TGMmini podporuje až 64 servopohonů a 16 I/O jednotek na sběrnici EtherCAT.
Implementován jsou též až dva CNC moduly s interpolátorem. 
Přímo na hardwaru TGMmini se nachází 8 rychlých vstupů (použitelné např. i pro inkrementální snímač otáček IRC), 8 rychlých výstupů (programovatelné jako digitální nebo PWM výstupy) a sběrnice CAN.   

Na rozdíl od systému Windows systém Linux rozeznává velikost písmen v názvech souborů a proto soubory se stejným názvem, lišícím se pouze velikostí, jsou chápány jako dva různé soubory. 
Např. TG Motion používá pro vlastní nastavení soubor `TgMotion5xx.ini`. 
Pokud by byl tento soubor uložen na TGMmini např. jako `TGMotion5xx.INI`, systém jej bude ignorovat.


Před vlastní prací s TGMmini je vhodné si přečíst [manuály k TG Motion](https://www.tgdrives.cz/ke-stazeni/ridici-systemy-pc-a-panely-ke-stazeni/#c426).