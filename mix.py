import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.gridspec as gridspec
from fractions import Fraction


# Initial values
initial_vinegar = 100
initial_oil = 10
max_oil = 200

# Set up grid layout
fig = plt.figure(figsize=(10, 5))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1.2])

ax_pie = fig.add_subplot(gs[0])
ax_bar = fig.add_subplot(gs[1])
plt.subplots_adjust(bottom=0.25)

def update_display(current_oil):
    ax_pie.clear()
    ax_bar.clear()

    total = current_oil + initial_vinegar
    sizes = [current_oil, initial_vinegar]
    labels = [f"Oil ({int(current_oil)})", f"Vinegar ({initial_vinegar})"]
    colors = ['goldenrod', 'saddlebrown']

    # Ratio calculations
    ratio_float = current_oil / initial_vinegar if initial_vinegar != 0 else float('inf')
    ratio_frac = Fraction(int(current_oil), initial_vinegar).limit_denominator()

    # Pie chart
    ax_pie.pie(sizes, labels=labels, colors=colors, startangle=90)
    ax_pie.axis('equal')
    ax_pie.set_title(f"Oil-to-Vinegar Ratio: {int(current_oil)}:{initial_vinegar} → {ratio_frac}")

    # Volume bar chart
    ax_bar.bar(['Total Volume'], [total], color='mediumslateblue')
    ax_bar.set_ylim(0, initial_vinegar + max_oil + 20)
    ax_bar.set_ylabel("Milliliters")
    ax_bar.set_title(f"Total Mixture: {total:.0f} mL")
    ax_bar.grid(axis='y', linestyle='--', alpha=0.6)

update_display(initial_oil)

# Slider
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
oil_slider = Slider(ax_slider, 'Oil Amount', 0, max_oil, valinit=initial_oil, valstep=1)

def on_slider_change(val):
    update_display(oil_slider.val)
    fig.canvas.draw_idle()

oil_slider.on_changed(on_slider_change)

plt.show()