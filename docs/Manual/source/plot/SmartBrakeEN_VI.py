
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.interpolate import PchipInterpolator  # shape-preserving interpolation

# ----- timing values -----
t_on   = 2.0
t_exc  = 5.0   # excitation marker
t_hold = 10.0

# original knots (levels)
t = np.array([0, t_on, 2.5, 5.0, 5.5, t_hold, 10.5, 12], dtype=float)
V = np.array([0, 0, 24, 24, 15, 15, 0, 0], dtype=float)
I = np.array([0, 0, 2, 2, 1.2, 1.2, 0, 0], dtype=float)

# dense time grid for smooth plotting
tt = np.linspace(t.min(), t.max(), 2000)

# shape-preserving interpolation for analog curve
p = PchipInterpolator(t, V)
V_smooth = p(tt)
pI = PchipInterpolator(t, I)
I_smooth = pI(tt)

# --- build digital control (0/1) on the same tt grid ---
ctrl_sig = np.where((tt >= t_on) & (tt <= t_hold), 1.0, 0.0)

#################--------------------VOLTAGE-----------------######################
###################################################################################
# --- figure with 2 subplots sharing x-axis ---
fig, (ax_ctrl, ax_vbr) = plt.subplots(
    2, 1, sharex=True, figsize=(10, 5.8),
    gridspec_kw={'height_ratios': [1, 3]}
)

# =========================
# TOP: digital control (0/1)
# =========================
ax_ctrl.step(tt, ctrl_sig, where='post', color='#7f3fbf', lw=1.8, zorder=3)
ax_ctrl.set_ylim(-0.2, 1.2)
ax_ctrl.set_yticks([0, 1])
ax_ctrl.set_yticklabels([r'$Brake$', r'$Release$'])
ax_ctrl.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax_ctrl.set_ylabel(r'$\mathrm{Control \ signal}$', fontsize=13, fontweight='bold')
ax_ctrl.set_axisbelow(True)
ax_ctrl.spines['top'].set_visible(False)
ax_ctrl.spines['right'].set_visible(False)
ax_ctrl.spines['bottom'].set_visible(False)
# shade ON window (keep low zorder so it stays under arrows/line)
ax_ctrl.axvspan(t_on, t_hold, color='#7f3fbf', alpha=0.08, zorder=0)
ax_ctrl.tick_params(axis='x', labelbottom=False)

# =========================
# BOTTOM: analog brake voltage
# =========================
ax_vbr.plot(tt, V_smooth, lw=2.2, color='#1f77b4', zorder=4)

ax_vbr.set_xlabel(r'$\mathrm{time}$', fontsize=13, fontweight='bold')
ax_vbr.set_xlim(0, 12)
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
# shade ON window (low zorder)
ax_vbr.axvspan(t_on, t_hold, color='#7f3fbf', alpha=0.05, zorder=0)

# =========================
# Dimension callouts
# =========================
def add_dimension(ax, x0, x1, y, text, color='#333', tick_height=1.0,
                  lw=1.8, z=6, label_offset=0.35):
    """
    Draw a horizontal <-> dimension line from x0 to x1 at y,
    with short vertical ticks at the ends and a centered label.
    """
    # end ticks (small vertical lines)
    ax.vlines([x0, x1], y - tick_height/2, y + tick_height/2,
              color=color, lw=lw, zorder=z)
    # double arrow
    ax.annotate(
        "", xy=(x0, y), xytext=(x1, y),
        arrowprops=dict(arrowstyle="<->", lw=lw, color=color),
        zorder=z
    )
    # label slightly above the arrow
    ax.text((x0 + x1) / 2, y + label_offset, text,
            ha="center", va="bottom", color=color, fontsize=12,
            zorder=z)

# Place dimensions in the upper half, well above spans/waveform
ymin, ymax = ax_vbr.get_ylim()
# Put arrows at 60% and 78% of the y-range (adjust to taste)
y_dim1 = ymin + 0.8 * (ymax - ymin)
y_dim2 = ymin + 0.8 * (ymax - ymin)

# τ_EXC: t_ON ↔ t_EXC
add_dimension(ax_vbr, t_on, t_exc, y_dim1, r'$\tau_{\mathrm{EXC}}$', color='#6c3d00', lw=2.0, z=7)

# τ_HOLD: t_EXC ↔ t_HOLD
add_dimension(ax_vbr, t_exc, t_hold, y_dim2, r'$\tau_{\mathrm{HOLD}}$', color='#004d61', lw=2.0, z=7)

# Optional thin guides in both subplots (visible but subtle)
for x in (t_on, t_exc, t_hold):
    ax_vbr.axvline(x, color='#000', lw=0.8, ls=':', alpha=0.35, zorder=2)
    ax_ctrl.axvline(x, color='#000', lw=0.8, ls=':', alpha=0.35, zorder=2)

plt.tight_layout()
#plt.show()


# --- EXPORTS ---
out_svg  = "SmartBrakeEN_V_SVG.svg"
out_webp = "SmartBrakeEN_V_WEBP.webp"

mpl.rcParams["svg.fonttype"] = "none"

# Save SVG (best for MkDocs)
fig.savefig(out_svg, bbox_inches="tight")

# Save WEBP at 600 dpi
# Matplotlib 3.7+ supports WEBP directly via Pillow;
# we try savefig('...webp'), and if not available, we fall back to Pillow conversion.
try:
    # High-quality WEBP via Pillow backend
    fig.savefig(
        out_webp,
        dpi=600,
        bbox_inches="tight",
        pil_kwargs={
            "quality": 100,  # adjust 90–100 to taste
            "method": 6,    # 6 = best compression effort (if Pillow supports)
        },
    )
except Exception as e:
    print(f"[info] savefig WEBP failed ({e}); falling back to PNG->WEBP via Pillow...")
    # Fallback: save a high-dpi PNG and convert to WEBP
    tmp_png = "brake_timing_600dpi.png"
    fig.savefig(tmp_png, dpi=600, bbox_inches="tight")

    from PIL import Image
    im = Image.open(tmp_png)
    # Convert to lossless or near-lossless WEBP; you can pass quality for lossy
    # If you prefer near-lossless, use quality=95; for true lossless use lossless=True (larger file)
    im.save(out_webp, format="WEBP", quality=95, method=6)

#################--------------------CURRENT-----------------######################
###################################################################################
# --- figure with 2 subplots sharing x-axis ---
fig, (ax_ctrl, ax_ibr) = plt.subplots(
    2, 1, sharex=True, figsize=(10, 5.8),
    gridspec_kw={'height_ratios': [1, 3]}
)
# =========================
# TOP: digital control (0/1)
# =========================
ax_ctrl.step(tt, ctrl_sig, where='post', color='#7f3fbf', lw=1.8, zorder=3)
ax_ctrl.set_ylim(-0.2, 1.2)
ax_ctrl.set_yticks([0, 1])
ax_ctrl.set_yticklabels([r'$Brake$', r'$Release$'])
ax_ctrl.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax_ctrl.set_ylabel(r'$\mathrm{Control \ signal}$', fontsize=13, fontweight='bold')
ax_ctrl.set_axisbelow(True)
ax_ctrl.spines['top'].set_visible(False)
ax_ctrl.spines['right'].set_visible(False)
ax_ctrl.spines['bottom'].set_visible(False)
# shade ON window (keep low zorder so it stays under arrows/line)
ax_ctrl.axvspan(t_on, t_hold, color='#7f3fbf', alpha=0.08, zorder=0)
ax_ctrl.tick_params(axis='x', labelbottom=False)
# =========================
# BOTTOM: analog brake current
# =========================
ax_ibr.plot(tt, I_smooth, lw=2.2, color='#1f77b4', zorder=4)
ax_ibr.set_xlabel(r'$\mathrm{time}$', fontsize=13, fontweight='bold')
ax_ibr.set_xlim(0, 12)
ax_ibr.set_xticks([t_on, t_exc, t_hold])
ax_ibr.set_xticklabels([r'$t_{ON}$', r'$t_{EXC}$', r'$t_{HOLD}$'])
ax_ibr.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='x')
ax_ibr.set_ylabel(r'$\mathrm{Brake \ current}$', fontsize=13, fontweight='bold')
ax_ibr.set_ylim(0, 3)
ax_ibr.set_yticks([0, 1.2, 2, 2.5])
ax_ibr.set_yticklabels([r'$I_{OFF}$', r'$I_{HOLD}$', r'$I_{EXC}$', r'$I_{ABSMAX}$'])
ax_ibr.grid(True, alpha=0.3, linestyle='-', linewidth=0.5, axis='y')
ax_ibr.set_axisbelow(True)
ax_ibr.spines['top'].set_visible(False)
ax_ibr.spines['right'].set_visible(False)
# shade ON window (low zorder)
ax_ibr.axvspan(t_on, t_hold, color='#7f3fbf', alpha=0.05, zorder=0)

# =========================
# Dimension callouts
# =========================
def add_dimension(ax, x0, x1, y, text, color='#333', tick_height=1.0,
                  lw=1.8, z=6, label_offset=0.35):
    """
    Draw a horizontal <-> dimension line from x0 to x1 at y,
    with short vertical ticks at the ends and a centered label.
    """
    # end ticks (small vertical lines)
    ax.vlines([x0, x1], y - tick_height/2, y + tick_height/2,
              color=color, lw=lw, zorder=z)
    # double arrow
    ax.annotate(
        "", xy=(x0, y), xytext=(x1, y),
        arrowprops=dict(arrowstyle="<->", lw=lw, color=color),
        zorder=z
    )
    # label slightly above the arrow
    ax.text((x0 + x1) / 2, y + label_offset, text,
            ha="center", va="bottom", color=color, fontsize=12,
            zorder=z)

# Place dimensions in the upper half, well above spans/waveform
ymin, ymax = ax_ibr.get_ylim()
# Put arrows at 60% and 78% of the y-range (adjust to taste)
y_dim1 = ymin + 0.8 * (ymax - ymin)
y_dim2 = ymin + 0.8 * (ymax - ymin)

# τ_EXC: t_ON ↔ t_EXC
add_dimension(ax_ibr, t_on, t_exc, y_dim1, r'$\tau_{\mathrm{EXC}}$', color='#6c3d00', lw=2.0, z=7)

# τ_HOLD: t_EXC ↔ t_HOLD
add_dimension(ax_ibr, t_exc, t_hold, y_dim2, r'$\tau_{\mathrm{HOLD}}$', color='#004d61', lw=2.0, z=7)

# Optional thin guides in both subplots (visible but subtle)
for x in (t_on, t_exc, t_hold):
    ax_ibr.axvline(x, color='#000', lw=0.8, ls=':', alpha=0.35, zorder=2)
    ax_ctrl.axvline(x, color='#000', lw=0.8, ls=':', alpha=0.35, zorder=2)

plt.tight_layout()
#plt.show()


# --- EXPORTS ---
out_svg  = "SmartBrakeEN_I_SVG.svg"
out_webp = "SmartBrakeEN_I_WEBP.webp"

mpl.rcParams["svg.fonttype"] = "none"

# Save SVG (best for MkDocs)
fig.savefig(out_svg, bbox_inches="tight")

# Save WEBP at 600 dpi
# Matplotlib 3.7+ supports WEBP directly via Pillow;
# we try savefig('...webp'), and if not available, we fall back to Pillow conversion.
try:
    # High-quality WEBP via Pillow backend
    fig.savefig(
        out_webp,
        dpi=600,
        bbox_inches="tight",
        pil_kwargs={
            "quality": 100,  # adjust 90–100 to taste
            "method": 6,    # 6 = best compression effort (if Pillow supports)
        },
    )
except Exception as e:
    print(f"[info] savefig WEBP failed ({e}); falling back to PNG->WEBP via Pillow...")
    # Fallback: save a high-dpi PNG and convert to WEBP
    tmp_png = "brake_timing_600dpi.png"
    fig.savefig(tmp_png, dpi=600, bbox_inches="tight")

    from PIL import Image
    im = Image.open(tmp_png)
    # Convert to lossless or near-lossless WEBP; you can pass quality for lossy
    # If you prefer near-lossless, use quality=95; for true lossless use lossless=True (larger file)
    im.save(out_webp, format="WEBP", quality=95, method=6)