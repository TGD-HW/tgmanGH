##Nastavení rychlosti komunikace CAN
Naleznete jej ve skupině registrů s názvem *Common*

<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Registr</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Popis</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">C-CAN_Baudrate</td>
        <td bgcolor="#F2F2F2" style="color: black;">Zaregistrujte se pro zadání rychlosti komunikace CAN v kilobaudech (20,50,100,125,250,500,800,1000).<br>Pro přijetí rychlosti musí být registr C-CAN_Settings 0. Bod vzorkování je pevně stanoven na 75%</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">C-CAN_Settings</td>
        <td bgcolor="#F2F2F2" style="color: black;">Registr pro podrobnější nastavení sběrnice CAN. Pokud je zadána nenulová hodnota, přepíše se registr C-CAN_Baudrate vypočítanou rychlostí.<br>Byte 0: TS1<br>Byte 1: TS2<br>Byte 2: SJ<br>Byte 3: Dělitel frekvence, základní frekvence je 16MHz.</td>
    </tr>
</table>

Příklad nastavení rychlosti na 500 kbaud:

| Parametr            |Hodnota      |
|----------------------|------------|
| SJ                   | 2          |
| TS1                  | 2          |
| SJ                   | 4          |
| Dělitel frekvence    | 11         |
| C-CAN_Settings       | **0x0202040b** |

##Příjem a odesílání zpráv

Nastavení pro příjem a odesílání zpráv prostřednictvím komunikace CAN.
Naleznete je ve skupině registrů *UserProg*.

###CAN status
<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Registr</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Popis</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Status</td>
        <td bgcolor="#F2F2F2" style="color: black;">bit 0: data odeslána, připravena na další.<br>bit 1 - bit8: nová data ve vyrovnávací paměti 1-8.</td>
    </tr>
</table>

###Posílání zpráv
<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Registr</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Popis</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_ID</td>
        <td bgcolor="#F2F2F2" style="color: black;">Zprávy CAN ID</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Len</td>
        <td bgcolor="#F2F2F2" style="color: black;">délka zprávy v bajtech</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Data_Lo</td>
        <td bgcolor="#F2F2F2" style="color: black;">Odesílá dolních 32 bitů zprávy</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Data_Hi</td>
        <td bgcolor="#F2F2F2" style="color: black;">Odesílá horních 32 bitů zprávy</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Transmit_Control</td>
        <td bgcolor="#F2F2F2" style="color: black;">bit 1: odešle zprávu<br>bit 2: odešle požadavek RTR (žádost o vzdálený přenos)<br>Poté musí být nastavena na 0</td>
    </tr>
</table>

Chcete-li zprávu odeslat, napište `1` do registru `CAN_Transmit_Control`.
Před odesláním další zprávy je nutné do tohoto registru napsat `0` a počkat na zpracování systémem.
Poté je možné odeslat další zprávu.

###Příjem zpráv
<table>
    <tr>
        <td bgcolor="#005050" style="color: white;"><b>Registr</b></td>
        <td bgcolor="#005050" style="color: white;"><b>Popis</b></td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Control</td>
        <td bgcolor="#F2F2F2" style="color: black;">Kontrolní registr příjmu.</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Recieve_Buffx_ID</td>
        <td bgcolor="#F2F2F2" style="color: black;">Příjem ID pro vyrovnávací paměť x (x = 1 - 8).</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Buffx_Len</td>
        <td bgcolor="#F2F2F2" style="color: black;">Počet bytů v přijaté zprávě.</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Buffx_Data_Lo</td>
        <td bgcolor="#F2F2F2" style="color: black;">Přijímá spodních 32 bitů zprávy</td>
    </tr>
    <tr>
        <td bgcolor="#F2F2F2" style="color: black;">CAN_Receive_Buffx_Data_Hi</td>
        <td bgcolor="#F2F2F2" style="color: black;">Přijímá horních 32 bitů zprávy</td>
    </tr>
</table>

K dispozici je 8 vyrovnávacích pamětí pro příjem zpráv.
Ne všechny zprávy z CAN jsou přijímány, ale pouze ty, na které jsou nastaveny vyrovnávací paměti.
`CAN_Recieve_Buff0_ID` (nebo jiná zvolená vyrovnávací paměť) je nastavena na požadované ID.
Do této vyrovnávací paměti se nahraje zpráva s odpovídajícím ID.
Následně zápis `0x1000` do registru `CAN_Receive_Control` resetuje příjem zpráv a přijme změny `CAN_Receive_Buffx_ID`.
Poté, co systém zprávu zpracuje, musí být hodnota registru `CAN_Receive_Control` nastavena na `0`.
Po přijetí zprávy se bit pro konkrétní vyrovnávací paměť nastaví v registru `CAN_Status`.
Pro potvrzení přijetí zprávy je v registru `AN_Recieve Control` nastaven odpovídající bit vyrovnávací paměti (stejný bit jako v `CAN_Status`).
Po zpracování systémem musí být registry znovu resetovány.

!!! Note "Poznámka"
	Standardizovaný protokol CAN pro TGZ je ve vývoji.