##Význam LED indikátorů a stavového displeje {#LED_sigs}
<img src="../../img/TGZ_LED1.png" alt="TGZ LED display" style="width:25%;">

Integrované LED indikátory a dvoumístný sedmisegmentový LED displej zobrazují stav servozesilovače po zapnutí napájení 24V.
LED indikátory jsou vždy dva (červená LED a zelená LED) pro každou řízenou osu plus jedna společná zelená LED pro signalizaci stavu sběrnice EtherCAT - signál EtherCAT RUN.
Indikátory detekují stav jednotlivých řízených os a pokud nastane porucha nebo chyba, zobrazí se příslušné kódy poruchy na stavovém displeji.
Možné stavy LED indikátorů a jejich význam, stejně jako signalizace chyb a jejich popis, jsou uvedeny v tabulkách níže.

**Po restartování servozesilovače TGZ**

| Chybový kód | Popis |
|---|---|
| Bu | Datum a čas vytvoření Firmware |
| iP | IP adresa servozesilovače TGZ pro protokol UDP |
| id | Identifikace servozesilovače TGZ (“slave alias” pro EtherCat) |

**Signalizace chyby / poruchy**

| Chybový kód | Popis |
|---|---|
| F.1 | Chyba osy 1 |
| F.2 | Chyba osy 2 |

Po kódu `F.1` popř. `F.2` se zobrazí sekvence čísel. Tato čísla jsou bitová čísla v chybovém registru, viz. [Popis chybových hlášení TGZ](description.md#errors)

**LED indikátory**   

<img src="../../../../../../source/img/statusLedsECAT.svg" alt="TGZ status LEDs" style="width:70%;">

Možné stavy servozesilovače signalizují LED diody **Ready** a **Error**:   

| Servozesilovač TGZ | Červená LED | Zelená LED |
|---|---|---|
| Režim = 0 (vypnuto) | Krátce problikává | Krátce problikává |
| Chyba servozesilovače | Svítí | Nesvítí |
| Servozesilovač připraven, není sepnutý HW ENABLE | Nesvítí | Pomalu bliká |
| Servozesilovač připraven, je sepnutý HW ENABLE | Nesvítí | Bliká |
| Servozesilovač připraven, ve stavu ENABLED | Nesvítí | Svítí |

V případě, že je v servozesilovači nahrán vhodný firmware s podporou sběrnice EtherCAT je pomocí LED diody **ECAT RUN** signalizován stav sběrnice.
Detailní popis jednotlivých stavů EtherCAT naleznete v dokumentaci [ EtherCAT Indicator and Labeling - ETG.1300 S](https://www.ethercat.org/memberarea/download/ETG1300_V1i1i1_S_R_IndicatorLabelingSpecification.pdf).

| Stavy indikátoru | Stav zařízení       | Popis                                |
|------------------|------------------|--------------------------------------|
| Vypnuto          | INITIALISATION   | Zařízení je ve stavu INIT            |
| Bliká            | PRE-OPERATIONAL  | Zařízení je ve stavu PRE-OPERATIONAL |
| Jeden záblesk    | SAFE-OPERATIONAL | Zařízení je ve stavu SAFE-OPERATIONAL|
| Zapnuto          | OPERATIONAL      | Zařízení je ve stavu OPERATIONAL     |

##Popis chybových hlášení {#errors}

| Druh chyby                 | Hodnota chyby v registru `aDriveError` | Číslo chyby na displeji | Popis chyby / možná příčina / řešení |
|----------------------------|----------------------------------------|-------------------------|-------------------------------------|
| Interní chyba              | 0x00000004                             | 02                      | **Příčina**: Interní hardwarová chyba.<br>**Řešení**: Kontaktujte dodavatele zařízení (servis). |
| Přepětí                    | 0x00000008                             | 03                      | Napětí meziobvodu (konektor X2) je příliš vysoké.<br>**Příčina 1**: Napájecí zdroj (DC) je špatně dimenzován nebo špatně nastaven nebo je v poruše.<br>**Řešení 1**: Zkontrolujte napájecí zdroj a jeho parametry.<br>**Příčina 2**: Rekuperační energie servopohonu je vyšší, než může zdroj přijmout.<br>**Řešení 2a**: Upravte hodnotu decelerační rampy na vyšší číslo.<br>**Řešení 2b**: Připojte jiný napájecí zdroj nebo připojte vhodné brzdné rezistory.<br>**Příčina 3**: Nízká hodnota parametru D – VoltDCLinkMaxErrLim.<br>**Řešení 3**: Upravte hodnotu D – VoltDCLinkMaxErrLim. |
| Podpětí                    | 0x00000010                             | 04                      | Napětí meziobvodu (konektor X2) je příliš nízké.<br>**Příčina 1**: Napájecí zdroj (DC) není připojen, je v poruše, je vypnutý nebo nemá dostatečný výkon.<br>**Řešení 1**: Zkontrolujte napájecí zdroj.<br>**Příčina 2**: Vysoká hodnota parametru D – VoltDCLinkMinErrLim.<br>**Řešení 2**: Upravte hodnotu D – VoltDCLinkMinErrLim.<br>**Příčina 3**: Zkrat na meziobvodu.<br>**Řešení 3**: Kontaktujte dodavatele zařízení (servis). |
| Chyba diag. STO            | 0x00000020                             | 05                      | Diagnostika vyhodnotila chybu v obvodech bezpečného přerušení točivého momentu.<br>**Příčina**: Interní hardwarová chyba.<br>**Řešení**: Kontaktujte servisní oddělení. |
| Chyba statické brzdy       | 0x00000040                             | 06                      | Diagnostika vyhodnotila chybu statické brzdy.<br>**Příčina 1**: Brzda je odpojena nebo je nesprávně zadán parametr M-StaticBrake v TGZ GUI.<br>**Řešení 1a**: Ověřte typ motoru a dle něj nastavte parametr M-StaticBrake.<br>**Řešení 1b**: Překontrolujte zapojení kabelů brzdy a zapojení napájení brzdy na měniči. |
| Chyba měření proudu        | 0x00000100                             | 08                      | Obvody měření proudu motoru mají poruchu.<br>**Příčina**: Interní hardwarová chyba.<br>**Řešení**: Kontaktujte servisní oddělení. |
| Přehřátý motor             | 0x00000200                             | 09                      | Motor je přehřátý.<br>**Příčina 1**: Teplota okolí je moc vysoká nebo jsou nevhodné podmínky chlazení.<br>**Řešení 1**: Zvažte zlepšení podmínek chlazení.<br>**Příčina 2**: Motor je výkonově přetěžován.<br>**Řešení 2**: Ověřte dimenzování pohonu a nastavení parametrů motoru dle dat od výrobce motoru.<br>**Příčina 3**: Chyba v zapojení teplotního čidla.<br>**Řešení 3**: Pokud to lze, ověřte zapojení čidla teploty, případně kontaktujte servisní oddělení.<br>**Příčina 4**: Chyba nastavení parametrů.<br>**Řešení 4**: Ověřte nastavení parametrů teplotních limitů a konzultujte se servisním oddělením. Ověřte parametry motoru podle dat od výrobce.<br>**Příčina 5**: Mechanická nebo elektrická závada na motoru.<br>**Řešení 5**: Kontaktujte servisní oddělení. |
| Přehřátý servozesilovač    | 0x00000800                             | 11                      | Servozesilovač TGZ je přehřátý.<br>**Příčina 1**: Teplota okolí je moc vysoká nebo jsou nevhodné podmínky chlazení.<br>**Řešení 1**: Zvažte zlepšení podmínek chlazení.<br>**Příčina 2**: Chyba nastavení parametrů.<br>**Řešení 2**: Ověřte nastavení parametrů teplotních limitů.<br>**Příčina 3**: Závada servozesilovače.<br>**Řešení 3**: Kontaktujte servisní oddělení. |
| Chyba zpětné vazby         | 0x00001000                             | 12                      | Chyba zpětné vazby polohy.<br>**Příčina 1**: Chyba v kabeláži a připojení konektorů.<br>**Řešení 1**: Překontrolujte a opravte kabeláž a připojení konektorů X6, X7.<br>**Příčina 2**: Chyba snímače polohy motoru.<br>**Řešení 2**: Kontaktujte servisní oddělení.<br>**Příčina 3**: Chyba v obvodech servozesilovače.<br>**Řešení 3**: Kontaktujte servisní oddělení. |
| Překročena rychlost        | 0x00004000                             | 14                      | Rychlost změřená snímačem polohy je větší než hodnota parametru M-Nmax.<br>**Příčina 1**: Nevhodně nastavený parametr M-Nmax.<br>**Řešení 1**: Upravte parametr podle dat dodaných výrobcem motoru.<br>**Příčina 2**: Špatně nastavený regulátor rychlosti.<br>**Řešení 2**: Upravte nastavení rychlostního a podružných regulátorů, aby nedocházelo ke kmitání.<br>**Příčina 3**: Chyba měření polohy (rychlosti).<br>**Řešení 3**: Kontaktujte servisní oddělení dodavatele motoru. |
| Poziční chyba              | 0x00008000                             | 15                      | Odchylka žádané a skutečné polohy polohového regulátoru překročila zadanou mez.<br>**Příčina 1**: Nevhodně nastavené parametry regulační struktury.<br>**Řešení 1**: Prověřte a upravte nastavení regulátorů v rámci pracovního cyklu, aby nedocházelo ke kmitání a byla minimální poziční chyba.<br>**Příčina 2**: Servozesilovač není schopen dodat potřebný moment pro dodržení žádané polohy. Může jít i o mechanickou závadu na poháněném systému.<br>**Řešení 2**: Ověřte dimenzování pohonu z hlediska dynamiky a momentu. Případně upravte zrychlení, zpomalení systému. Ověřte, že nejde o mechanickou závadu poháněného systému, zda se nevyskytuje nadměrné tření nebo není zařízení na mechanickém dorazu atd. |
| Chyba trajektorie          | 0x00010000                             | 16                      | Odchylka žádané polohy z nadřazeného systému (ethercat) od skutečné polohy překročila zadanou mez.<br>**Příčina 1**: Nespojitost v poloze zasílané nadřazeným systémem.<br>**Řešení 1**: Kontaktujte dodavatele nadřazeného systému.<br>**Příčina 2**: Souvislost s poziční chybou.<br>**Řešení 2**: Viz. **Řešení** poziční chyby. |
| Chyba průmyslové sběrnice  | 0x00020000                             | 17                      | Nedorazila platná data po průmyslové sběrnici ve stanoveném čase.<br>**Příčina 1**: Závada kabeláže.<br>**Řešení 1**: Překontrolujte kabeláž, konektory.<br>**Příčina 2**: Závada nadřazeného systému.<br>**Řešení 2**: Kontaktujte dodavatele nadřazeného systému.<br>**Příčina 3**: Chyba hardwaru servozesilovače.<br>**Řešení 3**: Kontaktujte servisní oddělení. |
| Chyba parametrů            | 0x00040000                             | 18                      | Při verifikaci sady parametrů došlo k chybě.<br>**Příčina**: Nesprávná sada parametrů.<br>**Řešení**: Kontaktujte dodavatele zařízení. |
