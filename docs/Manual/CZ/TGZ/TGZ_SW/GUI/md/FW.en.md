##Potřebné vybavení:

- PC s nainstalovaným TGZ GUI a Ethernetovým rozhraním. 
- Ethernetový kabel
- Napájecí zdroj 24VDC
- Servozesilovač TGZ
- Soubor `.TGZFW` (firmware)

##Postup přehrání firmware:

1. Přes ethernetový kabel řipojte TGZ k počítači (konektor X11).
2. Připojte 24VDC napájení k servozesilovači TGZ.
3. Spusťte TGZ GUI, vyberte příslušný síťový adaptér.
   Ze seznamu zvolte odpovídající zařízení a připojte k servozesilovači TGZ.
4. Zálohujte parametry servozesilovače kliknutím na ikonu
   <img src="../../../../../../source/img/icoSave.png" alt="Icon Save" style="width:4%;">
   v pravé části menu nahoře. Vyberte všechny skupiny parametrů a klikněte na ikonu **Save**.
5. Klikněte na ikonu
   <img src="../../../../../../source/img/icoMemory.png" alt="Icon Memory" style="width:4%;">
   v pravé části menu nahoře a vyberte **Upload firmware**.
6. Otevřete soubor s firmware (`*.TGZFW`).
7. Počkejte na dokončení nahrání firmware.
8. Po dokončení nahrávání restartujte servozesilovač TGZ kliknutím na Yes:
   <img src="../../../../../../source/img/GUIfwUploadComplete.png" alt="FW upload complete" style="width:50%;">   
   Znovu se připojte k servozesilovači TGZ.
9. Pokud má nový firmware jinou strukturu parametrů než firmware předchozí, dojde k chybě (*chyba 27 - parameter error, 0x08000000*).
   Je tedy nutné načíst parametry ze zálohy prostřednictvím ikony
   <img src="../../../../../../source/img/icoLoad.png" alt="Icon Load" style="width:4%;">
   v pravé části menu nahoře.
   Následně je nutné parametry uložit na paměťovou kartu kliknutím na ikonu
   <img src="../../../../../../source/img/icoSave.png" alt="Icon Save" style="width:4%;">
   opět v pravé části menu nahoře a zvolit **Save to memory**.
   Po restartování servozesilovače TGZ se již chyba parametrů (chyba 27) neobjeví.

!!! warning "Pozor"
	
	Neodpojujte napájení, dokud není proces nahrávání dokončen!
