##3D náhled
![3D view IO side](../img/IOside.svg){: style="width:70%;" }
<br>
<br>
![3D view FB side](../img/MotSide.svg){: style="width:70%;" }

##Konektory
___
### Strana silových konektorů
___

![PWR connections](../../../../source/img/TGS-560-50_100_PWR.webp){: style="width:70%;" }


<div class="grid cards" markdown>

-   **X1 - Vstupní fázové napětí**

    ---
	
	![PWR connector](../../../../source/img/2636-1107.webp){: style="width:80%;" }

-   Wago 2636-1107

	---
	
	--8<-- "md/X1_ACIN_7pin_2636.md"
	
-   **X4 - DC bus konektor**

    ---
	![ENET/ECAT/LogicPWR connectors](../../../../source/img/D560DCbusCon.svg){: style="width:70%;" }

-    Šroubovací svorky M8

	---

	--8<-- "md/X4_D560DCbus.md"

</div>
  
___
### Strana napájení řízení, kontrolních výstupů, term.
___

![Motor/Feedback connectors](../../../../source/img/TGS-560-50_100_Topside.webp){: style="width:70%;" }

<div class="grid cards" markdown>

-   **X3 - Napájení řídicí části 24V**

    ---
	
	![24V connector](../../../../source/img/1941040000.webp){: style="width:50%;" }

-    Weidmüller BCZ 3.81/05/180F SN OR BX

    ---

	--8<-- "md/X3_TGS560_24V_5pin_BCZ.md"


-   **X2 - Kontrolní výstupy**

    ---
		
	Pohled na konektor zezadu (strana vodičů)
	
	![DO](../../../../source/img/1792970000_1.webp){: style="width:60%;" }
	![DO1](../../../../source/img/1792970000_2.webp){: style="width:60%;" }
		
	Pohled na konektor zepředu (z pohledu TGS)
	
	![DO2](../../../../source/img/1792970000_3.webp){: style="width:60%;" }
	
-    Weidmüller BCZ 3.81/04/180 SN BK BX

    ---

	--8<-- "md/X2_DO_4pin_BCZ.md"
	
-   **S1 - Výběr režimu zařízení**

    ---
	
	![DO](../../../../source/img/DS03-254-04BE.webp){: style="width:40%;" }

-    DIP switch 4 pozice

    ---

	--8<-- "md/S1_TGS560_DIP.md"
	
-   **LED signalizace**

    ---
	
	![LED](../img/LED.webp){: style="width:90%;" }

-   LED 

    ---

	--8<-- "md/LED_TGS560.md"
	
</div>


