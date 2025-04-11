##3D view
![3D view control side](../img/IOside.en.webp){: style="width:80%;" }
<br>
<br>
![3D view PWR side](../img/MotSide.en.webp){: style="width:80%;" }

##Connectors
___
###Power connectors side
___

![PWR connections](../../../../source/img/TGS-560-25_50_PWRconns.webp){: style="width:70%;" }


<div class="grid cards" markdown>

-   **X1 - Mains connector**

    ---
	
	Cable side view
	
	![Mains IN](../../../../source/img/1930070000.webp){: style="width:70%;" }

-    WEIDMÜLLER BVZ 7.62HP/04/180F

	---
	
	--8<-- "md/X4_ACIN_4pin_TGS560_25.en.md"
	
-   **X4 - DC bus connector**

    ---
	
	Cable side view
	
	![DCbus out](../../../../source/img/1930090000.webp){: style="width:80%;" }

-    WEIDMÜLLER BVZ 7.62HP/06/180F

	---
	
	--8<-- "md/X1_DC_6pin_TGS560_25.en.md"
	
	
-   **X5 - Brake resistor**

    ---
		
	Cable side view
	
	![Brake res.](../../../../source/img/1095690000.webp){: style="width:60%;" }
		
	The X5 connector comes with jumper wires prepared for use with the internal chopper resistor.
	
	![PWR connector](../../../../source/img/1095690000jumper.svg){: style="width:60%;" }   
	
	If an external chopper (brake) resistor is used, the jumper wires must be removed from both X5 and X3 connectors and the resistor connected according to the [schematic](schematic.en.md).		

-   WEIDMÜLLER BLZ 7.62HP/03/180F

	---
	
	--8<-- "md/X5_RBR_3pin_TGS560_25.en.md"

</div>
  
___
### Logic power side
___

![Motor/Feedback connectors](../../../../source/img/TGS-560-25_50_24Vside.webp){: style="width:70%;" }

<div class="grid cards" markdown>

-   **X3 - Logic power**

    ---
	Cable side view   
	
	![1941040000](../../../../source/img/1941040000.webp){: style="width:60%;" }   
	
	![1941040000_1](../../../../source/img/1941040000_1.webp){: style="width:60%;" }	
	
	The X3 connector comes with jumper wires prepared for use with the internal chopper resistor.
	
	![1941040000_2](../../../../source/img/1941040000jumper.svg){: style="width:60%;" }   
	
	If an external chopper (brake) resistor is used, the jumper wires must be removed both from the X3 and X5 connectors and the resistor connected according to the [schematic](schematic.en.md).	  
	
-    Weidmüller BCZ 3.81/05/180F SN OR BX

	---

	--8<-- "md/X4_TGS560_24V_5pin_BCZ.en.md"

-   **X2 - Control outputs**

    ---
		
	Cable side view
	
	![DO](../../../../source/img/1792970000_1.webp){: style="width:60%;" }
	![DO1](../../../../source/img/1792970000_2.webp){: style="width:60%;" }
		
	Front view (TGS side)
	
	![DO2](../../../../source/img/1792970000_3.webp){: style="width:60%;" }
	
-    Weidmüller BCZ 3.81/04/180 SN BK BX

    ---

	--8<-- "md/X3_DO_4pin_BCZ.en.md"
	
</div>

___
### Mode selector side
___

![LED&DIP](../../../../source/img/TGS-560-25_50_DIPside.webp){: style="width:70%;" }

<div class="grid cards" markdown>

-   **S1 - Mode select**

    ---
	
	![DIP switch](../../../../source/img/DS03-254-04BE.webp){: style="width:70%;" }

-    4 position DIP switch

    ---

	--8<-- "md/S1_TGS560_DIP.en.md"

-   **LED signalization**

    ---
	
	![LED](../img/LED.webp){: style="width:90%;" }

-   LED 

    ---

	--8<-- "md/LED_TGS560.en.md"
	
</div>


