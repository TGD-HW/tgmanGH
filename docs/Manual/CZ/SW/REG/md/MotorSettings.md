##Motor {#MotorSettings}
###Parametr `M-Inull` – trvalý efektivní proud motoru   

$$
M_{I,null} = 1000 \cdot I_{n} (A)
$$

, kde I<sub>n</sub> je jmenovitý proud motoru.

###Parametr `M-Ipeak` – špičkový proud motoru

$$
M_{I,peak} = 1414 \cdot I_{max} (A) \approx 2 \cdot 1414 \cdot I_{n} (A)
$$

, kde I<sub>n</sub> je jmenovitý proud motoru,
I<sub>max</sub> je maximální efektivní proud motoru.

##Proudový regulátor {#CurrentRegulatorSetting}
###Parametr `C-K` – proporcionální zesílení proudového regulátoru

$$
C_K = \frac{L_{2PH} (mH) \cdot 100000}{U_{DC}}
$$

, kde L<sub>2PH</sub> je indukčnost vinutí dvou fází motoru,
U<sub>DC</sub> je pracovní napětí meziobvodu měniče.

###Parametr `C-Ti` – integrační časová konstanta proudového regulátoru

$$
C_{Ti} = 1000 \cdot \tau_{el} (ms) = 1000 \cdot \frac{L_{2PH} (mH)}{R_{2PH} (Ω)}
$$

, kde L<sub>2PH</sub> je indukčnost vinutí dvou fází motoru,
R<sub>2PH</sub> je odpor vinutí dvou fází motoru,
τ<sub>el</sub> je elektrická časová konstanta vinutí.

###Parametr `C-LimN` – proudové omezení záporného proudu na výstupu z rychlostního regulátoru

**Výpočet limitu v mA**   

$$
\frac{- C_{Lim,N} \cdot M_{I,null}}{1000}
$$

Příklad: M<sub>I,null</sub> = 2000 mA,  C<sub>Lim,N</sub> = 3000 ‰   

**Záporný špičkový proud bude omezen hodnotou:**

$$
\frac{3000 \cdot 2000}{1000} = -6000 mA
$$

###Parametr `C-LimP` – proudové omezení kladného proudu na výstupu z rychlostního regulátoru

**Výpočet limitu v mA:**

$$
\frac{C_{Lim,P} \cdot M_{I,null}}{1000}
$$

Příklad: M<sub>I,null</sub> = 2000 mA,  C<sub>Lim,P</sub> = 3000 ‰

**Kladný špičkový proud bude omezen hodnotou:**

$$
\frac{3000 \cdot 2000}{1000} = 6000 mA
$$

