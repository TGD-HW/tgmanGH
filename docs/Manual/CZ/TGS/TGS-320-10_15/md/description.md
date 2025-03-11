<!--
# Popis zařízení   

## Konektory
-->
##3D náhled
![3D view IO side](../img/IOside.svg){: style="width:70%;" }
<br>
<br>
![3D view FB side](../img/MotSide.svg){: style="width:70%;" }

##Konektory
___
### Strana AC IN
___

![AC IN connector](../../../../source/img/TGS-320-10_15_ACside.png){: style="width:70%;" }


<div class="grid cards" markdown>

-   **X1 - Vstupní fázové napětí**

    ---
	
	![PWR connector](../../../../source/img/1778078.svg){: style="width:60%;" }

-    Phoenix PC 5/ 3-STCL1-7,62

	---
	
	--8<-- "md/X1_ACIN_PC5.md"

</div>

___
### Strana LED signalizace
___


![LEDs](../../../../source/img/TGS-320-10_15_LEDSide.png){: style="width:70%;" }

<div class="grid cards" markdown>

-	**status LEDs**

	---
	
	![status LEDs](../img/LEDs.svg){: style="width:100%;" }
	
-	LED diody

	---
	
	Status LED zrcadlí stav výstupních stavových kontaktů.
	Když je TGS připraven a nemá žádný chybový stav (přehřátí, přepětí, podpětí), svítí zelená LED.
	V opačném případě svítí červená LED.

</div>
   
   
___
### Strana výstup DC bus, Ready, Error
___

![Motor/Feedback connectors](../../../../source/img/TGS-320-10_15_DCbusSide.png){: style="width:70%;" }

<div class="grid cards" markdown>

-   **X2 - Výstup DC silového napájení**

    ---
	
	![DCout connector](../../../../source/img/1778120.svg){: style="width:85%;" }
	![DCout connector](../../../../source/img/TGS-320_Rb.png){: style="width:85%;" }	

-    Phoenix PC 5/ 8-STCL1-7,62

	---

	--8<-- "md/X2_DC_8pin_PC5.md"

-   **X3 - Kontrolní výstupy**

    ---
	
	![DO](../../../../source/img/1792790000.svg){: style="width:50%;" }

-    Weidmüller BCZ 3.81/04/180 SN BK BX

    ---

	--8<-- "md/X3_DO_4pin_BCZ.md"
	
	
	Výstupy RDY a ERR se chovají jako kontakty relé s maximálním přípustným externím napájením 28 VDC a maximálním zatížením 700 mA.
	Nejčastěji se používají pro signalizaci poruchy napájecího modulu do nadřazeného systému.
	
	| **Kontakt sepnut** | **Stav** | **Popis** |
	| :---: | :---: | :---: |
	| RDY | TGS OK | Modul nezaznamenal chybu, napětí i teploty jsou v pořádku |
	| ERR | TGS chyba | Modul zaznamenal jednu nebo více chyb |
	
</div>


