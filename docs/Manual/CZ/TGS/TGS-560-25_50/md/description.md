##3D náhled
![3D view IO side](../img/IOside.webp){: style="width:60%;" }
<br>
<br>
![3D view FB side](../img/MotSide.webp){: style="width:80%;" }

##Konektory
___
### Strana silových konektorů
___

![PWR connections](../../../../source/img/TGS-560-25_50_PWRconns.webp){: style="width:70%;" }


<div class="grid cards" markdown>

-   **X1 - Vstupní fázové napětí**

    ---
	
	Pohled na konektor zezadu (strana vodičů)
	
	![Mains IN](../../../../source/img/1930070000.webp){: style="width:70%;" }

-    WEIDMÜLLER BVZ 7.62HP/04/180F

	---
	
	--8<-- "md/X4_ACIN_4pin_TGS560_25.md"
	
-   **X4 - Výstup DC bus**

    ---
	
	Pohled na konektor zezadu (strana vodičů)
	
	![DCbus out](../../../../source/img/1930090000.webp){: style="width:80%;" }

-    WEIDMÜLLER BVZ 7.62HP/06/180F

	---
	
	--8<-- "md/X1_DC_6pin_TGS560_25.md"
	
	
-   **X5 - Brzdný odpor**

    ---
		
	Pohled na konektor zezadu (strana vodičů)
	
	![Brake res.](../../../../source/img/1095690000.webp){: style="width:60%;" }   
	
	Konektor X5 je standardně dodáván včetně propojovacího vodiče v konfiguraci pro použítí interního brzdného odporu.
	
	![PWR connector](../../../../source/img/1095690000jumper.svg){: style="width:60%;" }   
	
	V případě použití externího brzdného rezistoru je nutné odstranit propojovací vodiče z konektorů X5 a X3 (TERM) a rezistor připojit dle [schématu](schematic.md).	

-   WEIDMÜLLER BLZ 7.62HP/03/180F

	---
	
	--8<-- "md/X5_RBR_3pin_TGS560_25.md"

</div>
  
___
### Strana napájení řízení a kontrolních výstupů
___

![Motor/Feedback connectors](../../../../source/img/TGS-560-25_50_24Vside.webp){: style="width:70%;" }

<div class="grid cards" markdown>

-   **X3 - Napájení řídicí části**

    ---
	Pohled zezadu (strana vodičů)   
	
	![1941040000](../../../../source/img/1941040000.webp){: style="width:60%;" }   
	
	![1941040000_1](../../../../source/img/1941040000_1.webp){: style="width:60%;" }	
	
	Konektor X3 je standardně dodáván včetně propojovacího vodiče v konfiguraci pro použítí interního brzdného odporu.
	
	![1941040000_2](../../../../source/img/1941040000jumper.svg){: style="width:60%;" }   
	
	V případě použití externího brzdného rezistoru je nutné odstranit propojovací vodiče z konektorů X3 a X5 a rezistor připojit dle [schématu](schematic.md).		

-    Weidmüller BCZ 3.81/05/180F SN OR BX

	---

	--8<-- "md/X4_TGS560_24V_5pin_BCZ.md"

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
	
</div>

___
### Strana LED výstupů a voliče DIP
___

![LED&DIP](../../../../source/img/TGS-560-25_50_DIPside.webp){: style="width:70%;" }

<div class="grid cards" markdown>

-   **S1 - Výběr režimu zařízení**

    ---
	
	![DIP switch](../../../../source/img/DS03-254-04BE.webp){: style="width:70%;" }

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


