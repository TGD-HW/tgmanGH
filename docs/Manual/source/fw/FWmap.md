![FW logo](../../../../source/img/icoLoad.png){: style="width:3%;" }
##Úvod
Update firmware (FW) u servozesilovače TGZ běžně probíhá pomocí software TGZ GUI. Je potřeba zvolit odpovídající firmware na základě konkrétního typu servozesilovače. Soubor firmware má příponu *.TGZFW.
##Možné kombinace
FW se dělí:

1) Podle typu řídicí desky. Starší verze vyráběná cca. do roku 2017 je označována jako "verze 4". Tento typ je pro speciální aplikace stále dostupný.
   Novější typ "verze 5" je standardní produkční a nejvíce rozšířená verze.   
2) Podle počtu řízených os pohonu. S - Single. Jedná se o jednoosou verzi servozesilovače. D - Double. Jedná se o dvouosou verzi servozesilovače.   
3) Podle typu řídicí komunikace. K dispozici jsou varianty EtherCAT, Profinet nebo CoE + CANOpen.   
4) Podle typu snímače polohy (zpětné vazby). K dispozici je standardní Hiperface DSL, nebo Endat 2.2 či BISS-C.   

##Filtr výběru firmware
<div id="filters">
  <label for="filter-controlHW">Control HW:</label>
  <select id="filter-controlHW">
    <option value="">All</option>
    <option value="4">4</option>
    <option value="5">5</option>
  </select>

  <label for="filter-NoAxis">No Axis:</label>
  <select id="filter-NoAxis">
    <option value="">All</option>
    <option value="S">S</option>
    <option value="D">D</option>
  </select>

  <label for="filter-Comm">Comm:</label>
  <select id="filter-Comm">
    <option value="">All</option>
    <option value="EtherCAT">EtherCAT</option>
    <option value="Profinet">Profinet</option>
    <option value="CoEcanopen">CoE + CANOpen</option>
  </select>

  <label for="filter-FB">Feedback:</label>
  <select id="filter-FB">
    <option value="">All</option>
    <option value="HiperfaceDSL">Hiperface DSL</option>
    <option value="Endat2_2">Endat 2.2</option>
    <option value="BissC_SSI">Biss C, SSI</option>
  </select>
</div>

<div id="firmware-list"></div>

