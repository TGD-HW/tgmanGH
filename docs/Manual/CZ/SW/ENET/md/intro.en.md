Servozesilovač lze monitorovat a ovládat přes Ethernet UDP.
Ethernetový kabel musí být připojen ke konektoru RJ45 (X11).
Podporované rychlosti jsou 100 Mb/s a 1 000 Mb/s.
MAC adresu může nastavit uživatel.
Všechny kontrolní součty (IP, UDP) musí být platné, jinak bude paket ignorován.
Port UDP je pevný a nastavený na 0x1F6.
IP adresa servozesilovače TGZ je statická, výchozí je `192.168.1.200`.
Servozesilovač funguje v komunikaci jako "slave" (tj. reaguje pouze na požadavky).
Odešle paket odpovědi pro každý přijatý paket ve správném formátu.
Master (PC) musí vždy čekat na odpověď od servozesilovače před odesláním dalšího dotazu.
Pokud PC neobdrží odpověď ve stanovené lhůtě, může se pokusit odeslat další požadavek.