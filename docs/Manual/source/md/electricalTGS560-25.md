#**Elektrická instalace**
##Instalace zařízení
![Shielding connection of the DCbus](../../../../source/img/TGS-560-25_50_shielding.webp){: style="width:85%;" }   

Během elektrické instalace servozesilovače je nutné se řídit bezpečnostními pokyny a dbát na dodržení těchto zásad:

- Instalaci servozesilovače smí provádět pouze odborní pracovníci s příslušnou kvalifikací pro montáž elektrických zařízení.
- Nesprávné síťové napětí, nevhodný motor nebo chybné zapojení mohou servozesilovač poškodit. Zkontrolujte, zda je servozesilovač vhodný pro daný motor. Porovnejte jmenovité napětí a proud připojovaných zařízení. Zapojte zařízení podle příslušných schémat zapojení (kap. „Popis zařízení“).  
- Ujistěte se, že maximální přípustné jmenovité napětí na svorkách nebude překročeno o více než 10&nbsp;% ani v nejvíce nepříznivých situacích (viz ČSN&nbsp;EN&nbsp;60204-1).
- Příliš vysoký jmenovitý proud externího jištění ohrozí kabely a zařízení. Jištění napájecího napětí a napájení ovládacích obvodů 24&nbsp;VDC musí nainstalovat uživatel.
- Stav servozesilovače musí být monitorován tak, aby byly rozpoznány kritické situace.
- Pro změnu nastavení servozesilovače lze používat konfigurační software. Jakékoli změny nebo zásahy, které nebyly předem konzultovány a odsouhlaseny výrobcem zařízení, způsobí zneplatnění záruky.

Nainstalujte elektrický systém servozesilovače následovně:

- Zvolte kabely v souladu s normou ČSN&nbsp;EN&nbsp;60204.
- Nainstalujte stínění a zemnění servozesilovače vyhovující požadavkům na elektromagnetickou kompatibilitu. Uzemněte montážní desku a kryt motoru.
- Zapojte servozesilovač a konektory s ohledem na běžné zásady a doporučení pro potlačení elektromagnetického rušení. 

##Stínění
###Postup zapojení kabelu pro DC BUS (napájení výkonové části) s&nbsp;připojením stínění

- Používejte pokud možno co nejkratší kabely dle vzájemné vzdálenosti a&nbsp;uspořádání jednotlivých zařízení v&nbsp;rozvaděči.
- Z obou konců kabelu odstraňte vnější izolaci&nbsp;délce 25 až 35 mm včetně stínění a zakončete smršťovací bužírkou, aby části stínění nemohly tvořit nežádoucí kontakt se živými částmi zapojení.
- Odizolujte konce všech vodičů a&nbsp;nasaďte na ně kontaktní dutinky.
- Přibližně uprostřed kabelu odstraňte vnější izolaci v&nbsp;šířce odpovídající kabelovému oku (obvykle 15 – 20 mm). 
  Dávejte pozor, abyste nepoškodili síťku stínění kabelu.
- Zapojte konektory dle schématu zapojení a&nbsp;připojte k&nbsp;zařízení.
- Na odizolovanou část kabelu (viz předchozí bod) nasaďte stínicí sponu a upevněte ji včetně kabelu k desce rozvaděče pomocí předem připraveného otvoru se závitem.
- Stínění kabelu musí po dotažení šroubu doléhat na desku rozvaděče. Jen tak je zaručen kvalitní kontakt.

![Shielding connection of the DCbus](../../../../source/img/TGZ-D-560-3_9_shielding1.webp){: style="width:85%;" }

###Technologie stínění

Uvedené ilustrace ukazují nevhodné a&nbsp;vhodné připojení stínění:

<br>

![Shielding connection technology](../../../../source/img/cableShielding4.svg){: style="width:70%;" }

###Potlačení rušení

**Následující pokyny vám pomohou omezit problémy s elektrickým rušením ve Vaší aplikaci:**

- Zajistěte dobré připojení mezi díly v&nbsp;rozvaděči. Propojte zadní panel a&nbsp;dveře rozvaděče s&nbsp;tělem skříně pomocí lankových vodičů. Při zajištění uzemnění nikdy nespoléhejte na propojení přes závěsy (panty) nebo montážní šrouby. Zajistěte elektrické připojení celého zadního povrchu panelu servozesilovače. Doporučuje se použít elektricky vodivé panely, například ze slitin hliníku nebo pozinkované oceli. U kovových panelů s&nbsp;nátěrem nebo jinou povrchovou úpravou odstraňte nevodivou vrstvu za servozesilovačem.
- Zajistěte dobré připojení na zem. Připojte rozvaděč na dobré uzemnění. Zemnicí vodiče by měly mít stejný průřez, jako napájecí vodiče, nebo o&nbsp;jeden stupeň menší.
- Použijte kabely dodané výrobcem. Je-li použit kabel, který obsahuje také vodiče pro ovládání brzdy, musí mít vodiče pro ovládání brzdy samostatné stínění.
- Uzemněte stínění na obou koncích. Uzemněte všechna stínění s&nbsp;co největší plochou (pro dosažení nízké impedance). Připojte je na kovový kryt konektorů nebo svorky pro stínění všude, kde je to možné. U kabelů, které vstupují do rozvaděče, připojte stínění po celém obvodu kabelu (360°). Nikdy nepřipojujte jen jeden „drátek“.
- Kabely by se neměly prodlužovat, protože by mohlo dojít k&nbsp;narušení stínění a&nbsp;tím také k&nbsp;rušení zpracování signálu. Pro dosažení maximální délky kabelu použijte kabely s&nbsp;odpovídajícím průřezem podle ČSN EN 60204 a&nbsp;z&nbsp;doporučeného materiálu.
- Spojujte kabely správným způsobem. Pokud je zapotřebí použít rozdělené kabely, použijte pro jejich spojení konektory s&nbsp;kovovým krytem. Zajistěte, aby byly oba kryty spojeny se stíněním po celém obvodu kabelu (360°). Žádná část kabelu by neměla zůstat nestíněná. Nikdy nespojujte rozdělený kabel pomocí svorkovnice.
- Vodiče mezi jednotlivými servozesilovači musí být rovněž stíněné.

###Vedení kabeláže

Na níže uvedených obrázcích je zobrazeno doporučené vedení kabeláže:

![Cable management technology](../../../../source/img/cableMan.svg){: style="width:80%;" }