V části výrobku týkající se servozesilovače nedošlo téměř k žádným změnám.
Pro nastavení parametrů pohonu, motorů atd. se používá servisní program `TGZ GUI`.
Existuje však několik parametrů, které se nastavují v souboru `TGM.INI` programu `TGMotion`:

-	IP adresa zařízení:
	TGZ+Motion používá statickou IP adresu ve svém servisním konektoru Ethernet X13. Tato adresa musí být nastavena v souboru `TgMotion5xx.ini`:
	``` ini
	[DHCP]
	IPAddress=192.168.1.188
	Gateway=192.168.1.1 
	Mask=255.255.255.0 
	DNS=192.168.1.1
	```
	Je nutné správně nastavit `Gateway`, musí být ve stejné doméně jako IP adresa. 
	IP adresa v TGZ GUI je určena pouze pro čtení.
-	C-SetCycleTime:
	V konfiguračním souboru se také nastavuje doba cyklu:
	``` ini
	[System]
	Cycle_Time=250
	```
	
Servozesilovač TGZ a systém TGMotion jsou synchronní a pracují s dobou cyklu 100&nbsp;µs.
Doporučená hodnota je 250 nebo 500&nbsp;µs. Grafické rozhraní TGZ zobrazuje `C-SetCycleTime` jako parametr pouze pro čtení.
Důrazně doporučujeme správně nastavit adresu MAC pomocí TGZ&nbsp;GUI na platnou hodnotu. 
První hexadecimální číslice by měla být `00`, druhá a třetí může být `0a:35` a na poslední tři hodnoty není žádné omezení.
Důležité je pouze to, aby se adresy MAC všech připojených zařízení v jedné síťové doméně lišily.
Příklad platné adresy MAC: `00:0a:35:01:02:04`.

## Interní zdroj řízení pohonu
Servozesilovače TGZ systému TGZ+Motion lze ovládat buď ze servisního portu prostřednictvím protokolu UDP (grafické rozhraní TGZ - obvykle pro nastavení motoru a pohonu), nebo interně pomocí TGMotion.

## Uživatelský program v TGZ (PLC)
Takzvaný uživatelský program (neboli PLC), který se nachází ve standardním servopohonu TGZ, není podporován.
PLC se používá se subsystémem TGMotion, což umožňuje několik programových priorit, chování v reálném čase a lepší výkon (viz níže).

##Další odchylky od standardního servozesilovače TGZ
Všechny parametry se ukládají pouze na SD kartu.
Ukládání parametrů do interní paměti flash zatím není podporováno.
Firmware lze aktualizovat pouze pomocí programu **Control Observer**, grafické rozhraní TGZ nelze pro tuto činnost použít.
Formát souboru firmwaru je zcela odlišný od standardní jednotky TGZ.