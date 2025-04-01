## Obecné

Síť PROFINET se připojuje pomocí konektoru X13 (Fieldbus IN) a konektoru X12 (Fieldbus OUT).
Konektor IN použijte směrem k PLC a konektor OUT k připojení dalších zařízení PROFINET v řetězci.
Servozesilovač TGZ má vestavěnou funkci PROFINET Bridge, takže pro malý počet zařízení a jednoduchou konfiguraci není potřeba speciální řízený PROFINET switch.
**Při připojování síťových kabelů PROFINET musí být vypnuto napájení zařízení**.   

!!! warning "Varování"
	Nastavení servozesilovače TGZ smí provádět pouze odborný pracovník s dostatečnými znalostmi techniky pohonů.
	Veškerá elektrická zapojení musí být provedena v souladu s [uživatelským manuálem HW TGZ](../../../../CZ/TGZ/TGZ-D-48-13_26/md/mark.md).
	
## Rychlý průvodce nastavením

- Zkontrolujte instalaci a montáž. Dodržujte všechny bezpečnostní pokyny uvedené v návodu k použití.
- Připojte počítač ke konektoru služby X11 Ethernet a spusťte program TGZ GUI.
- Nastavení adresy MAC zařízení:

![Profinet img](../../../../source/img/profinet1.webp){: style="width:90%;" }

- Adresa MAC začíná číslem `00` a `0A`.
  Poslední čtyři čísla mohou být libovolná, ale v síti PROFINET jedinečná.
  Kromě toho se poslední číslo musí lišit o 8, takže platné hodnoty pro poslední číslo jsou `00, 08, 10, 18, 20, 28, ..., 90, 98, A0, A8, B0, B8, ..., F0, F8`.
- Základní hodnota adresy MAC se používá pro servisní port X11.
  MAC adresa rozhraní PROFINET se vypočítá přičtením `4` k základní hodnotě, X13 (IN) má adresu `base + 5` a X12 (OUT) `base + 6`.
  Při uvádění zařízení PROFINET do provozu se obvykle používá pouze adresa MAC rozhraní PROFINET.
  První dvě hexadecimální čísla jsou vždy `00` a `0A` pro všechna rozhraní PROFINET a konektory X13 a X12 bez ohledu na hodnotu zadanou v grafickém rozhraní TGZ.
- Zvolte správné číslo telegramu podle projektu PROFINET a typu mechanismu ovládaného servopohonem TGZ.

![Profinet img](../../../../source/img/profinet2.webp){: style="width:90%;" }

- V případě dvouosé varianty servozesilovače nastavte typ telegramu pro obě osy.
- Uložte parametry do jednotky.

![Profinet img](../../../../source/img/profinet3.webp){: style="width:40%;" }

- Restartujte jednotku.

![Profinet img](../../../../source/img/profinet4.webp){: style="width:40%;" }

!!! note "Poznámka"
	Při změně adresy MAC a/nebo čísla telegramu je důležité vždy uložit parametry a restartovat servozesilovač.
	
## Název a IP adresa zařízení {#ProfinetIPsettings}

IP adresa je z výroby nastavena na `0.0.0.0` a název zařízení je prázdný.
V síti PROFINET je třeba přiřadit jedinečný název zařízení a IP adresu.
K tomu lze použít libovolný software PROFINET, například **TIA Portal**.

- Vyberte síťový adaptér PC, který je připojen k síti PROFINET, a dvakrát klikněte na řádek **Update accessible devices**.

![Profinet img](../../../../source/img/profinet5.webp){: style="width:40%;" }

- Připojená zařízení se po chvíli objeví:

![Profinet img](../../../../source/img/profinet6.webp){: style="width:40%;" }

- Měl by se zobrazit seznam všech připojených zařízení v síti PROFINET.
  Rozbalte zařízení s danou MAC adresou a dvojklikem zvolte **Online & diagnostics**.
  
![Profinet img](../../../../source/img/profinet7.webp){: style="width:40%;" }

- Zadejte jedinečnou IP adresu a vhodnou masku podsítě (obvykle `255.255.255.0`) a klikněte na tlačítko **Assign IP address**.

![Profinet img](../../../../source/img/profinet8.webp){: style="width:70%;" }

- Nastavte název zařízení, který musí být v síti PROFINET také jedinečný, a přiřaďte jej tlačítkem **Assign name**.

![Profinet img](../../../../source/img/profinet9.webp){: style="width:70%;" }

- Volitelně lze k lokalizaci zařízení v terénu použít blikání kontrolky LED zaškrtávacího políčka.
  TGZ bliká písmeny "Pd" na svém segmentovém LED displeji (Pd znamená PROFIdrive).
  
