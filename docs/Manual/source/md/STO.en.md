##Safe Torque Off (STO)
Funkce STO je základní bezpečnostní funkce integrovaná do servozesilovače. 
Zajišťuje, že žádná energie vytvářející točivý moment nemůže v případě nouzového stavu dále působit na motor a současně zabraňuje neúmyslnému spuštění.   
Vstupní svorky pro STO jsou součástí konektoru X1, prostřednictvím kterého je realizováno také napájení řídící části a spínače brzdy motoru. 
Pro korektní elektrické zapojení servozesilovače je nutné přivést na vstupy STO A a STO B napětí +24 V DC. 
V případě odpojení napájení od vstupu STO A nebo STO B dojde k okamžitému přerušení napájení motoru, který nebude dále pod momentem. 
V případě, že je motor v pohybu dojde vlivem setrvačných sil k dotočení motoru do klidového stavu.

<img src="../../../../../source/img/STOpins.png" alt="STO connection" style="width:15%;">

K vstupům STO A a STO B je možné připojit uživatelský bezpečnostní systém v závislosti na konkrétní aplikaci a potřebách zákazníka.
Po vybavení ochrany STO je nutné provést reset systému a opětovně povolit SW ENABLE. 
Ochrana STO je redundantní a vyznačuje se vysokou mírou spolehlivosti.

<img src="../../../../../source/img/STOschematic.png" alt="STO schematic" style="width:80%;">

!!! info "Norma STO"

	**Systém STO (Safety Torque Off) související s bezpečností servozesilovačů posuzované typové řady TGZ splňuje podle norem ČSN EN 61508-1 ed.2, ČSN EN 61508-2 ed.2, ČSN EN 61508-6 ed.2 požadavky
	úroveň integrity bezpečnosti SIL 3 v režimu provozu s vysokým vyžádáním, podle norem ČSN EN ISO 13849-1  požadavky kategorie 3 a úrovně vlastností PL e.**

