##Použití TGZ v TIA portálu
- Buďte opatrní, aby se pohon nezačal pohybovat bez předchozího varování.
- Přijměte příslušná opatření, aby obsluha a servisní pracovníci byli o tomto nebezpečí informováni.
- Zaveďte vhodná ochranná opatření, která zajistí, že jakýkoli neúmyslný pohyb pohonů nemůže vést k nebezpečným situacím.
- Uživatel je zodpovědný za to, že v případě poruchy pohonu bude celý systém nastaven do stavu, který je bezpečný pro zařízení i personál.

##Režim polohování s telegramem 111
Nejpoužívanějším provozním režimem je režim polohování pomocí základního polohování TGZ a funkčního bloku SinaPos TIA portálu s telegramem 111.
Následují možné kroky pro vytvoření nového projektu se dvěma servozesilovači TGZ, a to ve variantě se dvěma osami.

- Vytvořte nový projekt.

<img src="../../../../../source/common/img/profinet11.webp" alt="Profinet img" style="width:70%;">

- Otevřete projekt.

<img src="../../../../../source/common/img/profinet12.webp" alt="Profinet img" style="width:70%;">

- Nainstalujte soubory XML GSD popisující zařízení TGZ v síti PROFINET.
  Existují dva typy souborů, jeden pro jednoosou variantu s názvem `GSDML-V2.4-TGDrives-TGZ-S-xxxxx.xml` a druhý pro dvouosou variantu TGZ `GSDML-V2.4-TGDrives-TGZ-D-xxxxx.xml` (kde `xxxxx` znamená datum vytvoření souboru).



<!--vložit placeholdery na GSDML-V2.4-TGDrives-TGZ-S-xxxxx.xml a GSDML-V2.4-TGDrives-TGZ-D-xxxxx.xml - linky pro přímé stažení z webu-->



  Soubory lze stáhnout z webových stránek TG Drives.

- Zvolte položku nabídky `Options|Manage general station description files (GSD)`.

<img src="../../../../../source/common/img/profinet13.webp" alt="Profinet img" style="width:70%;">

- Zadejte zdrojovou cestu, kde jsou uloženy soubory GSDML, vyberte příslušný soubor a klikněte na tlačítko **Install**.

!!! note "Poznámka"
	Oba soubory lze instalovat současně.
	
<img src="../../../../../source/common/img/profinet14.webp" alt="Profinet img" style="width:70%;">

- Ve stromu projektů vlevo nahoře dvojklikem zvolte položku **Add new device item**.

<img src="../../../../../source/common/img/profinet15.webp" alt="Profinet img" style="width:70%;">

- Vyberte PLC controller použitý v hardwarovém projektu.
  V tomto výukovém programu je použit PLC S7-1200.

!!! warning "Pozor"
	Dbejte na výběr správné verze firmwaru (zde V4.1).
	
- Na portálu TIA by se mělo otevřít okno **Devices & networks**.
  Pokud ne, použijte položku stromového zobrazení **Devices & networks** v zobrazení projektu a otevřete okno dvojklikem.

<img src="../../../../../source/common/img/profinet16.webp" alt="Profinet img" style="width:70%;">

- Nyní je čas přidat do projektu jednotky TGZ.
  V podokně **Catalog pane** otevřete položku **Other field devices** a přejděte na `PROFINET IO|Pohony|TGPohony|tgz-d|tgz-d`.
  Zařízení přidejte do projektu dvojklikem.

<img src="../../../../../source/common/img/profinet17.webp" alt="Profinet img" style="width:70%;">

- Chcete-li přidat dva servopohony TGZ, proveďte to dvakrát.
  Pro práci s jednoosou variantou TGZ použijte položku tgz-s.
  Okno **Devices & network** by mělo vypadat následovně:

<img src="../../../../../source/common/img/profinet18.webp" alt="Profinet img" style="width:70%;">

- Přejmenujte jednotky v podokně **Network overview** podle projektu hardwaru.
  Názvy musí být stejné jako při [přípravě zařízení](TIA.md#prepDevice).

<img src="../../../../../source/common/img/profinet19.webp" alt="Profinet img" style="width:70%;">

- Připojte pohony k PLC.
  Klikněte na modrý text **Not assigned** a zvolte **PROFINET interface_1**.
  
<img src="../../../../../source/common/img/profinet20.webp" alt="Profinet img" style="width:70%;">


















##Příprava zařízení {#prepDevice}

