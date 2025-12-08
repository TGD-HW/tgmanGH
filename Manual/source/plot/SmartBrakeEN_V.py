import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator  # shape-preserving interpolation

# ----- timing values -----
t_on   = 2.0
t_exc  = 5.0   # use 5.0 to match your xticks below (you had 5 in the code)
t_hold = 10.0

# original knots (levels)
t = np.array([0, t_on, 2.5, 5.0, 5.5, t_hold, 10.5, 12], dtype=float)
V = np.array([0, 0, 24, 24, 15, 15, 0, 0], dtype=float)

# dense time grid for smooth plotting
tt = np.linspace(t.min(), t.max(), 2000)

# shape-preserving interpolation for analog curve
p = PchipInterpolator(t, V)
V_smooth = p(tt)

# --- build digital control (0/1) on the same tt grid ---
# control is 1 from t_on to t_hold, else 0
ctrl_sig = np.where((tt >= t_on) & (tt <= t_hold), 1.0, 0.0)

# --- figure with 2 subplots sharing x-axis ---
fig, (ax_ctrl, ax_vbr) = plt.subplots(
    2, 1, sharex=True, figsize=(10, 5.5),
    gridspec_kw={'height_ratios': [1, 3]}
)

# =========================
# TOP: digital control (0/1)
# =========================
ax_ctrl.step(tt, ctrl_sig, where='post', color='#9467bd', lw=1.8, label='control')

# styling for control band
ax_ctrl.set_ylim(-0.2, 1.2)
ax_ctrl.set_yticks([0, 1])
ax_ctrl.set_yticklabels([r'$Brake$', r'$Release$'])
ax_ctrl.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax_ctrl.set_ylabel(r'$\mathrm{Control \ signal}$', fontsize=13, fontweight='bold')
ax_ctrl.set_axisbelow(True)
ax_ctrl.spines['top'].set_visible(False)
ax_ctrl.spines['right'].set_visible(False)
ax_ctrl.spines['bottom'].set_visible(False)  # cleaner connection to the bottom plot

# shade ON window
ax_ctrl.axvspan(t_on, t_hold, color='#9467bd', alpha=0.05)

# no x labels on the top subplot
ax_ctrl.tick_params(axis='x', labelbottom=False)



# =========================
# BOTTOM: analog brake voltage
# =========================
ax_vbr.plot(tt, V_smooth, lw=2, color='#1f77b4', label='brakeVoltage')

ax_vbr.set_xlabel(r'$\mathrm{time}$', fontsize=13, fontweight='bold')
ax_vbr.set_xlim(0, 14)
ax_vbr.set_xticks([t_on, t_exc, t_hold])
ax_vbr.set_xticklabels([r'$t_{ON}$', r'$t_{EXC}$', r'$t_{HOLD}$'])
ax_vbr.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='x')

ax_vbr.set_ylabel(r'$\mathrm{Brake \ voltage}$', fontsize=13, fontweight='bold')
ax_vbr.set_ylim(0, 32)
ax_vbr.set_yticks([0, 15, 24, 30])
ax_vbr.set_yticklabels([r'$V_{OFF}$', r'$V_{HOLD}$', r'$V_{EXC}$', r'$V_{ABSMAX}$'])
ax_vbr.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax_vbr.set_axisbelow(True)
ax_vbr.spines['top'].set_visible(False)
ax_vbr.spines['right'].set_visible(False)

# optionally shade the ON window here for visual alignment
ax_vbr.axvspan(t_on, t_hold, color='#9467bd', alpha=0.05)

plt.tight_layout()
plt.show()