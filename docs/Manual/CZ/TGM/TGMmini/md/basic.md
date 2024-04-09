##Stručný popis
**TGMmini** je plnohodnotný počítač s dvoujádrovým procesorem ARM. Obě jádra procesoru jsou využita pro operační sytém Linux (distribuce Debian 10 s real-time rozšířením Xenomai) s grafickou nadstavbou Xfce. 
Řídicí systém **TG&nbsp;Motion**, umožňující řízení servopohonů a I/O jednotek přes sběrnici
EtherCAT, běží z části v real-time prostředí Linuxu a z části v samostatném procesoru s hardwarovým
EtherCAT akcelerátorem (vše implementováno v FPGA). Ovládání **TG&nbsp;Motion** se provádí z linuxové-
ho prostředí, na všechny potřebné operace jsou k dispozici knihovny, jejichž API rozhraní je totožné
s knihovnami DLL pro systém Windows na PC. Uživatelské virtuální PLC programy lze psát a vyvíjet
na PC, zdrojový text se pouze přeloží kompilátorem pro procesor ARM a vytvořený binární soubor se
přenese na **TGMmini**, kde se spustí. Pro přístup ke sdílené paměti systému **TG&nbsp;Motion** slouží knihovna TGM_Comm_Int_5, opět ve shodné verzi pro PC a **TGMmini**.

##Rozdíly vůči TG Motion na PC
TG Motion používaný na TGMmini je ve verzi 501 či vyšší. Verze pro PC i TGMmini jsou navzá-
jem kompatibilní. Manuál pro systém TG Motion tuto verzi zahrnuje a je mj. k dispozici na webových
stránkách TGDrives. TGMmini podporuje až 64 servopohonů a 16 I/O jednotek na sběrnici EtherCAT.
Implementován jsou též až dva CNC moduly s interpolátorem. Přímo na hardwaru TGMmini se nachází 8 rychlých vstupů (použitelné např. i pro inkrementální snímač otáček IRC), 8 rychlých výstupů
(programovatelné jako digitální nebo PWM výstupy) a sběrnice CAN.


Na rozdíl od systému Windows systém Linux rozeznává velikost písmen v názvech souborů a proto soubory se stejným názvem, lišícím se pouze velikostí, jsou chápány jako dva různé soubory. Např.
TG Motion používá pro vlastní nastavení soubor TgMotion5xx.ini. Pokud by byl tento soubor
uložen na TGMmini např. jako TGMotion5xx.INI, systém jej bude ignorovat.


Před vlastní prací s TGMmini je vhodné si přečíst manuály k TG Motion.

##Adresář `/TGMotion`
Všechny systémové a konfigurační soubory TG Motion se nacházejí v adresáři `/TGMotion`. Struktura adresáře je následující:
`{++ /TGMotion/app/cnc++}` – knihovny CNC modulu (`libSF_xxx.so`) a testovací program `Qt_CNC_Tester_5`   
`{++ /TGMotion/bin ++}` – určen pro uživatelské PLC programy   
`{++ /TGMotion/rtss ++}` – obsahuje vlastní TG Motion (`tgm501-xeno`) a jeho konfiguraci `TgMotion5xx.ini`   
`{++ /TGMotion/system ++}` – obslužné programy pro ovládání TG Motion – spuštění, zastavení, reset: služby `tgm_starter_service`, a `tgm_xeno_service`, obslužný program `tgm_sc` a uživatelské rozhraní `tgm_control_panel`.
Dále jsou zde umístěny systémové knihovny `libTGM_Comm_Int_5.so` a `libTGM_OPC_Server_5.so`, které jsou zaregistrovány do systému Linux pomocí příkazu `ldconfig`.   
`{++ /TGMotion/tools/TGM_5xx/4034_905 ++}` – další pomocné utility, např. konzole pro zobrazení chybových a uživatelských zpráv `TGM5xxDebugConsole`, servery OPC UA, ModbusTCP, a server pro emulaci DNC na sériovém portu.   
`{++ /TGMotion/Windows ++}` – zde se nacházejí všechny utility, které lze použít pro práci s TGMmini. Tyto programy běží pod Windows a komunikují s TGMmini pomocí protokolu TCP/IP. K dispozici je mj.
Control Observer, konzole pro zobrazení chybových a uživatelských zpráv, DLL knihovny CNC modulu a testovací program `Qt_CNC_Tester_5.exe`.