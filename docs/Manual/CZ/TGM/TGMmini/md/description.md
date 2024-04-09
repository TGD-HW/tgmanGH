##Spuštění TG Motion
Pro administraci TG Motion slouží program `tgm_control_panel`, který lze spustit přímo z pracovní plochy grafického systému Xfce (desktop).  
 
<img src="../../img/TGMcontrolPanel.jpg" alt="Control panel in Xfce" style="width:40%;">

Konfigurace je uložena v souborech `tgm_starter_service.ini` a `tgm_xeno_service.ini`. Pomocí položky ___Autostart___ lze nastavit automatické spuštění TG Motion po startu TGMmini.   
Standardně je povoleno vzdálené ovládání TG Motion po síti Ethernet z PC. Pokud toto ovládání není potřeba, lze jej vypnout v souboru `tgm_xeno_service.ini` nastavením
```
[Server]
Enabled=0
```   
a následným restartem TGMmini.

##Spuštění PLC
Uživatelský PLC program se spouští a zastavuje standardním způsobem, tak jako na PC. Nejdříve 
je nutno do registru `SYSTEM.Main.PLC_Name` uložit plnou cestu k souboru typu `.so`. Název souboru je vždy ve formátu UNICODE (kódování UTF-16) a maximální délka názvu včetně cesty je 512 znaků
(včetně koncové nuly). Poté lze spustit či zastavit PLC program nastavením bitů v registru SYSTEM.-Main.PLC_Ctrl. Podrobný popis viz manuál k TG Motion.   

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
Doporučený program je VNC Viewer (viz. [www.realvnc.com](https://www.realvnc.com/en/connect/download/viewer/) ).

##USB flash disky
Přenos dat mezi PC a TGMmini lze provést také pomocí USB disků. 
Pro použití na TGMmini musí být USB disk naformátován pro souborový systém FAT32. 
Po zasunutí do libovolného USB portu v TGMmini se disk a jeho obsah automaticky objeví ve správci souborů (File Manager), který se jmenuje Thunar. 
Před vyjmutím USB disku z portu je žádoucí disk odpojit, na Linuxu se tato operace jmenuje `unmount`. Stačí kliknout pravým tlačítkem myši na ikoně disku a zvolit položku menu _Unmount_. 
Vhodné nastavení v souboru `/etc/fstab` je pro USB disk (zařízení `/dev/sda`):
```
/dev/sda1 /media/usb auto sync,user,noauto 0 0
```
Velmi užitečný je též doplněk prostředí Xfce4 s názvem `xfce4-mount-plugin`, který lze nainstalovat pomocí příkazu
```
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
```
sudo mousepad /etc/network/interfaces.d/eth0
```
a soubor upravit.

###Přístup na internet
Přímo z TGMmini lze přistupovat na internet. 
Je nutno nastavit tzv. nameserver v souboru `/etc/resolv.conf`, opět jako administrátor. 
Číslo nameserveru pro konkrétní síť může být odlišné, s nastavením pomůže administrátor sítě.
Pokud je funkční přístup na internet, lze aktualizovat operační systém. V terminálu zadejte příkazy:
```
sudo apt-get update
sudo apt-get upgrade
```
případně i
```
sudo apt-get dist-upgrade
```
###MAC adresa
Každé zařízení na síti Ethernet musí mít jedinečnou adresu adaptéru, tzv. MAC adresu. 
TGMmini při startu čte jedinečné číslo přímo z procesoru a podle něho nastaví MAC adresu tak, aby byla pro každý vyrobený kus jedinečná. 
Pokud je přesto nutné MAC adresu změnit, lze to pomocí terminálu zápisem do flash paměti. 
Je nutné postupně zapsat všech 6 hodnot pomocí příkazu:
```
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