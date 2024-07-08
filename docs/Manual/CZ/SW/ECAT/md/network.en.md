Síť EtherCAT se připojuje pomocí konektoru X13 (Fieldbus IN) a konektoru X12 (Fieldbus OUT).
Konektor IN použijte ve směru k zařízení EtherCAT master a konektor OUT k připojení dalších zařízení EtherCAT v řetězci.
Standardní rychlost je 100Mbit/s, existuje také možnost použít připojení 1Gbit/s.
V takovém případě musí všechna zařízení (včetně mastera) používat gigabitovou rychlost.
Pro volbu požadované rychlosti komunikace použijte registr `C-Enable_1G`, viz. [Nastavení komunikace EtherCAT](EtherCAT.md#ECATcommSettings).
Při připojování síťových kabelů EtherCAT musí být napájení zařízení vypnuto.   

Sběrnice CAN je připojena pomocí konektoru X10. Není zde žádný zakončovací odpor 120Ω.
Servozesilovač TGZ podporuje všechny standardní rychlosti sběrnice CAN: 10, 20, 50, 100, 125, 250, 500, 800 a 1000 Kbit/s. Rychlost se volí pomocí registru CAN_BaudRate pomocí servisního programu TGZ_GUI.
Nastavení servozesilovače TGZ smí provádět pouze odborný pracovník s dostatečnými znalostmi techniky pohonů. Všechna elektrická zapojení musí být provedena v souladu s uživatelskou příručkou TGZ.