##Nastavení komunikace {#ECATcommSettings}
Servozesilovač TGZ je schopen komunikovat s ostatními zařízeními průmyslové sběrnice rychlostí 100 Mbit/s nebo 1 Gbit/s.
Zatímco standard 100 Mbit/s podporují všechna zařízení EtherCAT a je povinný, gigabitová rychlost je určena pro budoucnost a zatím ji podporuje jen několik zařízení.
Všechny podřízené jednotky EtherCAT v řetězci musí používat stejnou rychlost.
Servozesilovač TGZ používá pro volbu správného komunikačního režimu svůj registr s názvem `C-Enable_1G`.
Po výběru správného režimu se doporučuje uložit nastavení a restartovat pohon.

| Hodnota | Popis | Využití |
|-------------|-----------|--------------|
| 0 | 100Mbit/s force full duplex | výchozí hodnota pro vestavěné EtherCAT mastery |
| 1 | Automatické vyjednávání 1 Gbit/s | pro gigabitovou sběrnici musí všechna zařízení (včetně masteru) používat gigabitovou rychlost. |
| 2 | 100Mbit/s force half duplex (bez MDI-X) | pro testování nebo ladění |
| 3 | 100Mbit/s force full duplex (bez MDI-X) | pro testování nebo ladění |
| 4 | Automatické vyjednávání 100Mbit/s (bez záměny vodičů) | pro testování nebo ladění |
| 5 | Automatické vyjednávání 100Mbit/s | výchozí hodnota pro EtherCAT mastery na bázi PC |
| 6 | 100Mbit/s force half duplex (bez záměny vodičů) | pro testování nebo ladění |
| 7 | 100Mbit/s force full duplex (bez záměny vodičů) | pro testování nebo ladění |
 
###Rychlost 100 Mbit/s 
Doporučená hodnota je 0 pro vestavěné EtherCAT mastery nebo pokud servo TGZ není prvním zařízením v řetězci sběrnice.
U PC masteru vybaveného kartou Ethernet s gigabitovou podporou je nutné použít režim 5, a to alespoň pro první TGZ připojené k masteru.
Ostatní popsané režimy se používají především pro testování nebo ladění a je nutné nastavit stejný režim pro všechny servozesilovače TGZ v řetězci fieldbus.

###Rychlost 1 Gbit/s
Jediná možná hodnota je 1. Automatické vyjednávání (autonego) je pro gigabitovou rychlost povinné.

##Profil EtherCAT
V následující tabulce jsou uvedeny nejpoužívanější registry EtherCAT.
Podrobný popis všech registrů naleznete v [dokumentaci EtherCAT](https://www.ethercat.org/default.htm).

| Adresa | Délka bajtu | Popis | Master přístup | TGZ přístup |
|--------|-------------|-------|----------------|---------------|
| 0x120  | 2           | Kontrola AL | rw             | ro            |
| 0x130  | 2           | Stav AL     | ro             | rw            |
| 0x134  | 2           | Kód stavu AL | ro             | rw            |
| 0x220  | 2           | Událost IRQ | ro             | rw            |
| 0x600  | 16          | FMMU 0 (výstupy) | rw         | ro            |
| 0x610  | 16          | FMMU 1 (vstupy) | rw         | ro            |
| 0x800  | 8           | Správce synchronizace 0 (mailbox out) | rw | ro |
| 0x808  | 8           | Správce synchronizace 1 (mailbox in) | rw | ro |
| 0x810  | 8           | Správce synchronizace 2 (PDO out) | rw | ro |
| 0x818  | 8           | Správce synchronizace 3 (PDO in) | rw | ro |
| 0x1000 | 40 nebo 44  | PDO out (nastavené hodnoty) | rw | ro |
| 0x1400 | 40 nebo 44  | PDO in (skutečné hodnoty) | ro | rw |
| 0x1800 | 16 nebo 32  | SDO out (požadavky) | rw | ro |
| 0x1C00 | 16 nebo 32  | SDO in (odpovědi od TGZ) | ro | rw |

##Node-ID

Sítě EtherCAT i CAN vyžadují jedinečné identifikační číslo uzlu přiřazené každému zařízení.
TGZ k tomuto účelu používá registr `C-ID`.
Identifikaci uzlu může přečíst EtherCAT master:
- Nakonfigurovaný alias stanice (adresa `0x12`) (podporován pouze 8bitový Node-Id, tj. hodnoty 1 - 255)
- Nastavením bitu 5 (`0x20`) do řízení AL se Node-Id zkopíruje do stavového kódu AL `0x134`.
- Oblast EEPROM s offsetem 4 obsahuje také hodnotu Configured station alias (plná 16bitová hodnota, tj. hodnoty 1 - 65535).

!!! Note "Poznámka"
	Node-Id nemůže být nulový
	
##Ovládání AL `0x120`
Podporované stavy řízení AL jsou INIT (`0x01`), PRE-OPERATIONAL (`0x02`), SAFE-OPERATIONAL (`0x04`), OPERATIONAL (`0x08`). 
Navíc je podporován bit 4 (potvrzení) a bit 5 (požadavek na Node-Id zařízení).
Požadavek BOOTSTRAP (`0x03`) není podporován.

##Stav AL `0x130`

| Bit   | Popis                                     |
|-------|-------------------------------------------|
| 3:0   | aktuální stav zařízení (0x01, 0x02, 0x04, 0x08) |
| 4     | Indikace chyby                            |
| 5     | Identifikace zařízení                     |

##4.6 Stavový kód AL `0x134`
Podporované stavové kódy:

| Hodnota | Popis                                              |
|---------|----------------------------------------------------|
| 0x0000  | Žádná chyba                                        |
| 0x0011  | Neplatná požadovaná změna stavu                    |
| 0x0012  | Neznámý požadovaný stav                            |
| 0x0013  | Bootstrap není podporován                          |
| 0x0016  | Neplatná mailbox konfigurace (stav PRE-OP) |
| 0x001B  | Správce synchronizace watchdog                     |
| 0x001D  | Nesprávná konfigurace výstupu                      |
| 0x001E  | Neplatná konfigurace vstupu                        |
