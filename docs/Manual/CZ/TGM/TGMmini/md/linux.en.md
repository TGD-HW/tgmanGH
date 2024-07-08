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

##Spuštění TG Motion
Pro administraci TG Motion slouží program `tgm_control_panel`, který lze spustit přímo z pracovní plochy grafického systému Xfce (desktop).  
 
<img src="../../img/TGMcontrolPanel.png" alt="Control panel in Xfce" style="width:40%;">

Konfigurace je uložena v souborech `tgm_starter_service.ini` a `tgm_xeno_service.ini`. Pomocí položky `Autostart` lze nastavit automatické spuštění TG Motion po startu TGMmini.   
Standardně je povoleno vzdálené ovládání TG Motion po síti Ethernet z PC. Pokud toto ovládání není potřeba, lze jej vypnout v souboru `tgm_xeno_service.ini` nastavením
```
[Server]
Enabled=0
```   
a následným restartem TGMmini.

##Spuštění PLC
Uživatelský PLC program se spouští a zastavuje standardním způsobem, tak jako na PC. Nejdříve 
je nutno do registru `SYSTEM.Main.PLC_Name` uložit plnou cestu k souboru typu `.so`. Název souboru je vždy ve formátu UNICODE (kódování UTF-16) a maximální délka názvu včetně cesty je 512 znaků
(včetně koncové nuly). Poté lze spustit či zastavit PLC program nastavením bitů v registru `SYSTEM.Main.PLC_Ctrl`. Podrobný popis viz. manuál k TG Motion.   

Pokud běží server pro vzdálený přístup, ovládání PLC lze provádět i pomocí programu Control Observer na PC. V něm je nutno ručně zadat plný název souboru PLC (přípona `.so`). 
Jméno i cesta k souboru se udává jako lokální název, např. `/TGMotion/bin/Universal_PLC.so`.   

Cesta k uživatelskému PLC programu se neukládá. Je nutno ji ručně upravit přímo v konfiguračním souboru `TgMotion5xx.ini`, např. pomocí editoru Mousepad z okna terminálu příkazem:
```
mousepad /TGMotion/rtss/TgMotion5xx.ini
```

##Připojení ke sdílené paměti
Pro připojení ke sdílené paměti slouží knihovna DLL `TGM_Comm_Int_5`. 
Na TGMmini se soubor jmenuje `libTGM_Comm_Int_5.so` a je standardně umístěn v adresáři `/TGMotion/system`. 
Pomocné programy a utility systému TG Motion tuto knihovnu také využívají. 
Popis knihovny a její použití je uveden v samostatném návodu. Knihovna je zaregistrovaná v systému Linux pomocí příkazu `ldconfig`.

##Vzdálené připojení z PC
Pokud je na TGMmini spuštěn server pro vzdálený přístup, lze ke sdílené paměti TGMmini přistupovat vzdáleně z PC. 
Pomocí knihovny `TGM_Comm_Int_5.DLL` a její pomocné komponenty `TGM_Mini_5.DLL` lze pracovat s lokální sdílenou pamětí (TG Motion na PC) transparentně, stejně jako se vzdálenou sdílenou pamětí (TG Motion na TGMmini). 
Stejně tak lze přímo pracovat s programem Control Observer na PC a pomocí něj číst a zapisovat hodnoty do sdílených pamětí TGMmini.
Pro úspěšné vzdálené připojení je pouze nutné znát IP adresu TGMmini na lokální síti. 
Nastavení IP adresy je popsáno v kapitole _IP adresa_.

##Přenos souborů do TGMmini po síti Ethernet
Soubory mezi PC a TGMmini lze snadno přenášet pomocí protokolu SCP. 
Na PC s Windows je vhodné použít uživatelsky příjemný program WinSCP. 
Po nastavení IP adresy, přihlašovacího jména a hesla (není vhodné používat uživatele root) se WinSCP připojí, v levém panelu zobrazuje lokální soubory na PC a v pravém panelu soubory TGMmini.
K dispozici jsou všechny potřebné operace: kopírování, přesun, mazání a editace souborů, stejně tak nastavování atributů a přístupových práv.
Program WinSCP lze stáhnout z internetu např. z adresy [www.winscp.net](https://winscp.net/eng/download.php).

##Vzdálená správa TGMmini
TGMmini může běžet v tzv. headless režimu, tj. bez monitoru, klávesnice a myši. 
Připojení ke grafickému rozhraní TGMmini je možné pomocí VNC protokolu. VNC server na TGMmini je standardně spuštěn, stačí proto na PC pouze spustit vhodný klient VNC. 
Doporučený program je VNC Viewer (viz. [www.realvnc.com](https://www.realvnc.com/CZ/connect/download/viewer/) ).

##USB flash disky
Přenos dat mezi PC a TGMmini lze provést také pomocí USB disků. 
Pro použití na TGMmini musí být USB disk naformátován pro souborový systém FAT32. 
Po zasunutí do libovolného USB portu v TGMmini se disk a jeho obsah automaticky objeví ve správci souborů (File Manager), který se jmenuje Thunar. 
Před vyjmutím USB disku z portu je žádoucí disk odpojit, na Linuxu se tato operace jmenuje `unmount`. Stačí kliknout pravým tlačítkem myši na ikoně disku a zvolit položku menu _Unmount_. 
Vhodné nastavení v souboru `/etc/fstab` je pro USB disk (zařízení `/dev/sda`):
``` bash
/dev/sda1 /media/usb auto sync,user,noauto 0 0
```
Velmi užitečný je též doplněk prostředí Xfce4 s názvem `xfce4-mount-plugin`, který lze nainstalovat pomocí příkazu
``` bash
sudo apt-get install xfce4-mount-plugin
```
##Další nastavení TGMmini
###IP adresa
Důležitá informace pro práci s TGMmini je jeho IP adresa v lokální síti. 
Je vhodné nastavit IP adresu jako statickou, tj. při každém spuštění se TGMmini přiřadí stejná adresa. 
Samozřejmě musí být tato adresa v lokální síti volná, tj. neobsazena jiným počítačem. 
Výchozí adresa je `192.168.1.220`. 
Vše se nastavuje v souboru `/etc/network/interfaces.d/eth0`. 
Přístup je nutný s administrátorskými právy, tj. v terminálu zadat příkaz: 
``` bash
sudo mousepad /etc/network/interfaces.d/eth0
```
a soubor upravit.

###Přístup na internet
Přímo z TGMmini lze přistupovat na internet. 
Je nutno nastavit tzv. nameserver v souboru `/etc/resolv.conf`, opět jako administrátor. 
Číslo nameserveru pro konkrétní síť může být odlišné, s nastavením pomůže administrátor sítě.
Pokud je funkční přístup na internet, lze aktualizovat operační systém. V terminálu zadejte příkazy:
``` bash
sudo apt-get update
sudo apt-get upgrade
```
případně i
``` bash
sudo apt-get dist-upgrade
```
###MAC adresa
Každé zařízení na síti Ethernet musí mít jedinečnou adresu adaptéru, tzv. MAC adresu. 
TGMmini při startu čte jedinečné číslo přímo z procesoru a podle něho nastaví MAC adresu tak, aby byla pro každý vyrobený kus jedinečná. 
Pokud je přesto nutné MAC adresu změnit, lze to pomocí terminálu zápisem do flash paměti. 
Je nutné postupně zapsat všech 6 hodnot pomocí příkazu:
``` bash
sudo ethtool -E eth0 magic 0x9500 offset 0x01 value 0xff
```
kde hexadecimální hodnota za parametrem `offset` musí postupně nabývat hodnot `0x01, 0x02, …, 0x06` a hodnoty za parametrem `value` určují MAC adresu. 
V případě chyby, či pokud je třeba nastavit zpět výchozí MAC adresu, je nutné do všech offsetů `0x01..0x06` zapsat hodnoty `0xff`.
Výchozí MAC adresa je uvedena na spodní straně TGMmini spolu s výrobním číslem a dalšími údaji.

###Spořič obrazovky, vypínání monitoru
Ve výchozím nastavení je TGMmini nastaven tak, že nikdy nevypíná monitor ani nespouští spořič obrazovky. 
To je zajištěno skriptem `/home/shareman/autostart.sh` a jeho příkazy `xset`. 
Toto chování lze v souboru `autostart.sh` lehce upravit podle potřeby. 
Návod k programu `xset` se zobrazí po zadání příkazu `xset` v příkazové řádce terminálu.

###Autostart aplikací
Grafické prostředí Xfce umožňuje jednoduše nastavit, které aplikace se spouští při startu. 
Kromě již zmíněného skriptu `autostart.sh`, který je nezbytný pro správnou práci TG Motion, lze zadat libovolné množství dalších programů, které mají být spuštěny při startu systému. 
Pomocí položky menu `Start|Settings|Session and Startup` lze vše potřebné nastavit.
Připraveny jsou položky pro autostart serverů OPC UA, Modbus TCP a emulaci DNC přes sériový port. 
Není vhodné spouštět všechny tyto servery, vždy jen jeden podle potřeby.

###Rozlišení obrazovky
TGMmini umožňuje použít pro monitor připojený přes HDMI následující rozlišení:

| **Rozlišení** | **Obnovovací frekvence** |
| :--- | :---: |
| 800 × 600 | 60 Hz |
| 1024 × 600 | 75 Hz |
| 1024 × 768 | 60 Hz |
| 1280 × 720 | 60 Hz |
| 1280 × 800 | 60 Hz |
| 1280 × 1024 | 60 Hz |
| 1368 × 768 | 60 Hz |
| 1400 × 1050 | 60 Hz |
| 1440 × 900 | 60 Hz |
| 1600 × 900 | 60 Hz |
| 1600 × 1200 | 50 Hz |
| 1680 × 1050 | 50 Hz |
| 1920 × 1080 | 47 Hz |

Barevná hloubka je vždy 16 bitů na pixel (16 bpp).   

Pro změnu rozlišení lze použít program `screen_resolution`, který lze spustit pomocí položky menu `Start|Settings|Set Screen Resolution`.   

Rozlišení 1400 × 1050 a vyšší používají tzv. potlačení zatmívacích intervalů CVT, tak aby bylo možno zobrazit vysoké rozlišení při výstupních kmitočtech do 1 GHz. 
Pro tato rozlišení je nutné použít kvalitní monitor. 
Full HD rozlišení 1920 x 1080 používá snímkový kmitočet pouze 47 Hz, což zvládnou jen některé monitory.   

Rozlišení lze měnit též pomocí konzole, po příhlášení jako root je v adresáři `/root` připravena sada skriptů, kterými lze rozlišení nastavit. 
Po spuštění příslušného skritpu je nutné TGMmini restartovat pomocí příkazu `reboot`. 
Tento postup je vhodný v případě, že nastavené rozlišení připojený displej nepodporuje. 
Jako konzoli lze použít připojení přes USB kabel nebo SSH terminál, viz. níže v kapitole Administrace TGMmini.

###Hardwarový kurzor myši
Firmware v2.2 a vyšší obsahuje podporu hardwarového kurzoru myši. 
Ukazatel je vykreslován přímo do obrazových dat, což přináší výhody menší zátěže procesoru a odstranění blikání kurzoru při změně jeho tvaru. 
Maximální velikost hardwarového kurzoru je 32 × 32 pixelů. 
Pro větší ukazatele (prostředí Xfce podporuje maximální velikost 48 × 48) se automaticky aktivuje softwarové vykreslování. 
Běžná velikost kurzoru je 16 × 16 pixelů.
Nastavení lze provést v souboru `/usr/share/X11/xorg.conf.d/99-fbdev.conf`. Standardní volby jsou

```
Option "HWCursor" "true"
Option "GlobalHWCursorDisable" "false"
Option "InverseHWCursorColors" "false"
```

Nastavením položky "`HWCursor5`" na "`false`" lze hardwarový kurzor vypnout a bude se používat pouze softwarové vykreslování ukazatele. 
Pro použití v kiosk módu lze kurzor úplně vypnout pomocí "`HWCursor`" "`true`" a "`GlobalHWCursorDisable`" "`true`". 
Poslední položka "`InverseHWCursorColors`" umožňuje prohodit černou a bílou barvu u monochromatických kurzorů.
Podporovány jsou monochromatické a barevné ARGB styly kurzorů. 
Uživatelské soubory popisující tvar ukazatelů (vizuální styly) lze najít na internetu, umísťují se do adresáře `~/.icons/<název stylu>/cursors`. 
Přepnutí stylu lze provést v grafickém prostředí Xfce pomocí položky menu `Start|Settings|Mouse and Touchpad`, záložka `Themes`.

###Vizuální styly
Grafické prostředí Xfce je propracovaný systém pro správu oken a programů v sytému Linux Debian. 
Lze mj. též měnit vizuální styly, např. velikost a barvy ikon pro práci s okny. 
Standardní nastavení používá styl optimalizovaný pro dotykové zobrazení, nazvaný `TG_Flat`. 
K dispozici jsou ale i další styly, vše lze nastavit pomocí `Start|Settings|Window Manager`.

###Kalibrace dotykové obrazovky
Pro kalibraci slouží příkaz menu `Start|Calibration|Calibrate touchscreen`. 
Po úspěšné kalibraci se kalibrační data objeví v okně terminálu. 
Je nutné je přenést do schránky a zkopírovat do kalibračního souboru. 
Ten lze otevřít a editovat příkazem `Start|Calibration|Edit calibration data`.

###Administrace TGMmini
TGMmini lze připojit k PC pomocí USB kabelu, pak se z hlediska počítače chová jako sériový port.
Při použití vhodného terminálového programu, např. Putty nebo Tera Term, lze nastavovat a ovládat TGMmini pomocí konzole. 
Stejně tak je i možný přístup pomocí protokolu SSH přes rozhraní Ethernet. Nutná je pouze znalost IP adresy.

###Význam stavové LED diody STS
1. Krátce po zapnutí TGMmini se rozsvítí červená LED dioda.

2. Po spuštění operačního systému Linux se rozbliká zelená LED dioda, červená zhasne.
3. Následně se spustí řídicí systém TGMotion a zelená LED dioda svítí trvale.
4. Pokud je aktivován interní I/O modul, tj. používají se vstupy a výstupy na konektorech X5 a X10, červená LED dioda slouží k indikaci stavu výstupů:
	1. je-li výstupní obvod v chybě (tj. špatné napájení, přepětí nebo zkrat na výstupech, atd.), bliká střídavě zelená a červená LED dioda,
	2. v opačném případě (tj. výstupní obvod je v pořádku), svítí trvale zelená LED dioda.
5. Po spuštění procesu vypínání operačního systému se rozsvítí červená LED dioda. Ta trvale svítí do odpojení napájení TGMmini.

| **Stav LED** | **Význam** |
| :--- | :---: |
| Červená svítí | Start nebo ukončování operačního systému |
| Zelená bliká | Operační systém spuštěn, TGMotion neběží |
| Zelená svítí | TGMotion běží, stav bez chyb |
| Červená bliká se zelenou | TGMotion běží, výstupní modul v chybě |

Výše uvedené chování stavové LED diody lze vypnout v souboru `/TGMotion/system/tgm_xeno_service.ini` pomocí zápisu
```
[LED]
Control=0
```

V tom případě se rozsvítí pouze červená LED po startu TGMmini. 
LED diody lze ovládat pomocí sběrnice i2c (adresa `0x28` na sběrnici i2c-1). 
Sekvence příkazů pomocí terminálu:

``` bash
/usr/local/sbin/i2cset 1 0x28 0xF6 0xC # (1)
/usr/local/sbin/i2cset 1 0x28 0xF7 0x50 # (2)
/usr/local/sbin/i2cset 1 0x28 0xF4 0x4 # (3)
/usr/local/sbin/i2cset 1 0x28 0xF4 0x8 # (4)
/usr/local/sbin/i2cset 1 0x28 0xF4 0x0 # (5)
```

1.	piny `SS2` a `SS3` jako GPIO
2.	GPIO jako push-pull
3.	Rozsvícení červené LED :red_circle:
4.	Rozsvícení zelené LED :green_circle:
5.	Rozsvícení obou LED :orange_circle:


Je nutné nainstalovat [I2C-tools](https://www.mankier.com/package/i2c-tools), [i2c-tools-4.1.tar.gz](https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git/snapshot/i2c-tools-4.1.tar.gz).   
Samostatné ovládání LED diody mimo TGMotion je nutné pro některé speciální uživatelské programy, jako např. Profinet I/O device.