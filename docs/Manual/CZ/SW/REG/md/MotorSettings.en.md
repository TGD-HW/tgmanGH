##Motor {#MotorSettings}
###Parameter `M-Inull` – continuous effective motor current   

$$
M_{I,null} = 1000 \cdot I_{n} (A)
$$

, where I<sub>n</sub> is the nominal motor current.

###Parameter `M-Ipeak` – peak motor current

$$
M_{I,peak} = 1414 \cdot I_{max} (A) \approx 2 \cdot 1414 \cdot I_{n} (A)
$$

, where I<sub>n</sub> is the nominal motor current,
I<sub>max</sub> is maximum efective motor current.

##Current regulator {#CurrentRegulatorSetting}
###Parameter `C-K` – current controller proportional gain

$$
C_K = \frac{L_{2PH} (mH) \cdot 100000}{V_{DC}}
$$

, where L<sub>2PH</sub> is two phase motor inductance,
V<sub>DC</sub> is working DC bus voltage of the servo amplifier.

###Parameter `C-Ti` – current controller integration time constant

$$
C_{Ti} = 1000 \cdot \tau_{el} (ms) = 1000 \cdot \frac{L_{2PH} (mH)}{R_{2PH} (Ω)}
$$

, where L<sub>2PH</sub> is two phase motor inductance,
R<sub>2PH</sub> is two phase motor resistance,
τ<sub>el</sub> is electrical winding time constant.

###Parameter `C-LimN` – speed controller output negative current limit

**Limit calculation in mA**   

$$
\frac{- C_{Lim,N} \cdot M_{I,null}}{1000}
$$

Example: M<sub>I,null</sub> = 2000 mA,  C<sub>Lim,N</sub> = 3000 ‰   

**Peak negative current is limited to:**

$$
\frac{3000 \cdot 2000}{1000} = -6000 mA
$$

###Parameter `C-LimP` – speed controller output positive current limit

**Limit calculation in mA**   

$$
\frac{C_{Lim,P} \cdot M_{I,null}}{1000}
$$

Example: M<sub>I,null</sub> = 2000 mA,  C<sub>Lim,P</sub> = 3000 ‰

**Peak positive current is limited to:**

$$
\frac{3000 \cdot 2000}{1000} = 6000 mA
$$

