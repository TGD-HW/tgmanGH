- Použijte nejnovější soubor EtherCAT XML pro TGZ a zkopírujte jej do složky TwinCAT (`TwinCAT\3.1\Config\Io\EtherCAT`).
- Vytvořte nový projekt\
- Připojte TGZ k síti EtherCAT
- Nastavte registr `D-Mode` servozesilovače TGZ na hodnotu 3 (režim polohy).
  Proveďte to pro první nebo obě osy (verze pohonu TGZ-D). 
  V případě potřeby nastavení uložte.
- Použijte příkaz **Scan** v kontextové nabídce `I/O | Zařízení`

![TwinCAT](../../../../source/img/twincat01devices.webp){: style="width: 35%;" }

- Připojte pohon ke konfiguraci **NC-Configuration**

![TwinCAT](../../../../source/img/twincat02drive.webp){: style="width: 35%;" }

- Dvojklikem na položku **TGZ Drive** ve stromu zařízení se otevře okno vlastností.

![TwinCAT](../../../../source/img/twincat03properties.webp){: style="width: 35%;" }

- PDO lze sledovat a měnit v kartě **Process Data**. Na obrázku níže je zobrazeno nastavení pro režim CST.

![TwinCAT](../../../../source/img/twincat04CSTset.webp){: style="width: 60%;" }

- Po dokončení nastavení aktivujte konfiguraci.

![TwinCAT](../../../../source/img/twincat05config.webp){: style="width: 35%;" }

- Pomocí stromové položky `MOTION | NC-Task 1 SAF | Axes | Axis 1` zobrazíte všechny vlastnosti osy. Vyberte kartu **Online** a klikněte na tlačítko **Set**.

![TwinCAT](../../../../source/img/twincat06motion.webp){: style="width: 60%;" }

- Kliknutím na tlačítko **All** zaškrtnětě všechna zaškrtávací políčka.

![TwinCAT](../../../../source/img/twincat07enableAll.webp){: style="width: 25%;" }

- Osa by nyní měla být povolena a připravena k pohybu v režimu cyklického synchronního polohování (CST). V případě potřeby použijte červené tlačítko F6 pro resetování chyby a/nebo modré tlačítko F8 pro referenci osy.
- Jak je popsáno v kapitole [Mapování PDO a varianty jednotky TGZ](objects.md#PDO_TGZ), jsou hodnoty PDO stejné pro jednoosou i dvouosou verzi TGZ. 
  Proto při použití varianty TGZ-S v systému TwinCAT nebude osa 2 použitelná a musí být ignorována.
  
##Nastavení režimu cyklické synchronní rychlosti (CSV)
- Použijte konfigurační režimu TwinCAT

- Aktivujte kartu **Process Data** jednotky TGZ a v kombinovaném poli vyberte položku **Cyclic synchronous velocity mode (CSV)**.

![TwinCAT](../../../../source/img/twincat08CSVitem.webp){: style="width: 60%;" }

- Znovu připojte data osy kliknutím na tlačítko **Yes** v následujícím dialogovém okně.

![TwinCAT](../../../../source/img/twincat09axisConfirm.webp){: style="width: 25%;" }

- Aktivujte kartu **Startup** a změňte hodnotu objektu `0x6060:00` (Mode of operation). Dvakrát klikněte na tuto položku.

![TwinCAT](../../../../source/img/twincat10startupTab.webp){: style="width: 50%;" }

- V následujícím dialogovém okně změňte hodnotu `Data` na `09` a klikněte na tlačítko OK.

![TwinCAT](../../../../source/img/twincat11data09.webp){: style="width: 50%;" }

- V případě potřeby proveďte totéž pro druhou osu (objekt `0x6860:00`).
- Nezapomeňte nastavit příslušný režim pohonu TGZ (registr `D-Mode`), jak je popsáno v kapitole [Režimy provozu 0x6060](objects.md#0x6060).
- Aktivujte konfiguraci a přepněte do režimu **Run**. 
  TwinCAT nyní používá regulátor otáček k provedení pohybu.
  Pro dosažení plynulého polohování je nutné správně nastavit parametry regulátoru.