##Popis funkce {#SmartBrakeDesc}
Servozesilovač TGZ je vybaven vylepšenou funkcí ovládání statické motorové brzdy **Chytrá brzda**.
Tato funkce mimo jiné umožňuje snížit spotřebu statické brzdy po té, co již byla odbržděna (stav trvale odbržděno).
Snížení spotřeby je docíleno snížením přídržného napětí/proudu brzdy (V_HOLD, I_HOLD).
K dispozici jsou dva režimy ovládání statické brzdy.

Jedná se o ovládání napětím:

![Smart brake voltage mode](../img/SmartBrakeEN_V.webp){: style="width:70%;" }

 a ovládání proudem.
 
![Smart brake current mode](../img/SmartBrakeEN_I.webp){: style="width:70%;" }

##Nastavení a ovládání {#SmartBrakeUsage}
Uživatel může nastavit všechny potřebné parametry v programu [TGZ GUI](../../CZ/TGZ/TGZ_SW/GUI/md/intro.md#GUIstart).
Set parametrů je dostupný v sekci `Drive`.
![Smart brake GUI parameters](../img/SmartBrake_GUI1.webp){: style="width:100%;" }
U každé řízené osy je možné zvolit buď napěťové `voltage control` nebo proudové `current control` řízení brzdy pomocí parametru ** `D-Brake_mode` **.
Pro každý režim platí jiné provozní parametry.

##Parametry {#SmartBrakeParams}
V **napěťovém režimu** ovládání brzdy je možné nastavit následující parametry:

|  Č. parametru |  Název |  Označení v TGZ GUI | Jednotka | Rozsah | Popis |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  V<sub>EXC</sub>  | `D-BR_L2H_voltage` | V | 0~VCC<sub>BR</sub>  | Excitační napětí (napětí přítahu) |
| 2 |  V<sub>HOLD</sub>  | `D-BR_H_voltage` | V | 0~VCC<sub>BR</sub>  | Přídržné napětí (holding) |
| 3 |  τ<sub>EXC</sub>  | `D-BR_L2H_T_time` | 10 ms | 0~1000  | Doba excitace (Doba po kterou je na brzdě napětí V<sub>EXC</sub>) 0~10 s |

!!! warning "Maximální napětí brzdy"

	V<sub>ABSMAX</sub> lze zadat v rozsahu 0~50 V.
	Elektronicky je ale obvod spínání brzdy omezen na 30 VDC.
	Vyšší připojené napětí na napájecí pin VCC_BR může obvod nevratně poškodit!

V **proudovém režimu** ovládání brzdy je možné nastavit následující parametry:

|  Č. parametru |  Název |  Označení v TGZ GUI | Jednotka | Rozsah | Popis |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  I<sub>EXC</sub>  | `D-BR_L2H_voltage` | 100 mA | 0~30</sub>  | Excitační proud (proud přítahu) 0~3 A |
| 2 |  I<sub>HOLD</sub>  | `D-BR_H_voltage` | 100 mA | 0~30</sub>  | Přídržný proud (holding) 0~3 A |
| 3 |  τ<sub>EXC</sub>  | `D-BR_L2H_T_time` | 10 ms | 0~1000  | Doba excitace (Doba po kterou teče cívkou brzdy proud I<sub>EXC</sub>) 0~10 s |
