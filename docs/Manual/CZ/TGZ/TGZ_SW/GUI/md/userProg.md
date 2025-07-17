V programu **TGZ GUI** je možné spustit testovací uživatelský program. Jeho tvorba je možná například v prostředí **Visual Studio** či **Code::Blocks**.

---

## Popis spuštění uživatelského programu

Připojte se pomocí **TGZ GUI II** k zařízení **TGZ**, do kterého chcete nahrát **PLC**.

V horní části programu v záložkách zvolte záložku **`Uživatelský program`**.

![TGZ GUI UPL 01](../img/GUI_UPL_01.webp){: style="width:100%;" }

V dolní části programu zvolte záložku **`Ovládání`**.

![TGZ GUI UPL 02](../img/GUI_UPL_02.webp){: style="width:100%;" }

Pod touto záložkou v poli **`Soubor s programem`**

![TGZ GUI UPL 03](../img/GUI_UPL_03.webp){: style="width:100%;" }

stiskněte na konci řádku tlačítko **`…`**.

![TGZ GUI UPL 41](../img/GUI_UPL_04.webp){: style="width:100%;" }

Vyberte požadované **PLC** a volbu potvrďte. Nyní se v poli **`Soubor s programem`**

![TGZ GUI UPL 05](../img/GUI_UPL_05.webp){: style="width:100%;" }

objeví cesta k vybranému **PLC**.

Stiskněte tlačítko **`Nahrátí`**.

![TGZ GUI UPL 06](../img/GUI_UPL_06.webp){: style="width:100%;" }

Nyní se objeví zpráva nahraného **PLC**.

![TGZ GUI UPL 07](../img/GUI_UPL_07.webp){: style="width:100%;" }

Pokud vše proběhlo v pořádku a nedošlo k žádnému problému, text v pravém dolním rohu v části **`Ovládání`**

![TGZ GUI UPL 08](../img/GUI_UPL_08.webp){: style="width:100%;" }

se změní z **`Program není načten`** na **`Program spuštěn`** a tlačítka, včetně pozadí textu, změní barvy.

Nyní stiskem tlačítka **`Uložení do paměti`**

![TGZ GUI UPL 09](../img/GUI_UPL_09.webp){: style="width:100%;" }

uložíte **PLC** do flash paměti zařízení.

---

## Nastavení parametrů

V horní části **TGZ GUI** zvolte záložku **`Parametry`**.

![TGZ GUI UPL 10](../img/GUI_UPL_10.webp){: style="width:100%;" }

V rozbalovací nabídce parametru **`CO-UserProgStart`**

![TGZ GUI UPL 11](../img/GUI_UPL_11.webp){: style="width:100%;" }

vyberte možnost **`1: Yes – from flash`**

![TGZ GUI UPL 12](../img/GUI_UPL_12.webp){: style="width:100%;" }

, pokud chcete, aby se **PLC** automaticky spustilo při startu zařízení.