![FW logo](../../../../source/img/icoLoad.png){: style="width:10%;" }
##Úvod
blabla
##Možné kombinace
všecky
##Mapa Firmware

<!--Office 365 table (login required)
<iframe width="700" height="850" frameborder="0" scrolling="no" src="https://tgdcz-my.sharepoint.com/personal/puczok_tgdrives_cz/_layouts/15/Doc.aspx?sourcedoc={0de87665-2f1c-4ce3-b1b4-cb91b06ba7bd}&action=embedview&wdAllowInteractivity=False&Item='FWmap'!A1%3AE37&wdInConfigurator=True&wdInConfigurator=True"></iframe>
-->

<iframe width="700" height="1000" frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRUP3JTuTrqm0LBUBqgM4X-KZXVA5KUPMZc72GPN_kC452TMLmDAt_H2FRl_ocReXk1ZogAalQpOWrF/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=true"></iframe>

##JS filtering
<div id="filters">
  <label for="filter-controlHW">Control HW:</label>
  <select id="filter-controlHW">
    <option value="">All</option>
    <option value="4">4</option>
    <option value="5">5</option>
    <!-- Add more options as needed -->
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
    <option value="CoE + CANOpen">CoE + CANOpen</option>
  </select>

  <label for="filter-FB">Feedback:</label>
  <select id="filter-FB">
    <option value="">All</option>
    <option value="Hiperface DSL">Hiperface DSL</option>
    <option value="Endat 2.2">Endat 2.2</option>
	<option value="Biss C, SSI">Biss C, SSI</option>
  </select>
</div>

<div id="firmware-list"></div>

