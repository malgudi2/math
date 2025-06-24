import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_pie_charts(n1, d1, n2, d2):
    try:
        n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)
        if not (0 <= n1 <= d1 and 0 <= n2 <= d2 and d1 > 0 and d2 > 0):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid fractions (0 ≤ numerator ≤ denominator, denominator > 0).")
        return

    # Set up the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

    # First pie chart
    labels1 = [f"{n1}/{d1}", f"{d1-n1}/{d1}"]
    ax1.pie([n1, d1 - n1], labels=labels1, colors=['skyblue', 'lightgray'], startangle=90, counterclock=False)
    ax1.set_title(f"Fraction 1: {n1}/{d1}")

    # Second pie chart
    labels2 = [f"{n2}/{d2}", f"{d2-n2}/{d2}"]
    ax2.pie([n2, d2 - n2], labels=labels2, colors=['lightgreen', 'lightgray'], startangle=90, counterclock=False)
    ax2.set_title(f"Fraction 2: {n2}/{d2}")

    # Clear previous canvas if needed
    for widget in chart_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# GUI setup
window = tk.Tk()
window.title("Compare Two Fractions")

tk.Label(window, text="Fraction 1 - Numerator:").grid(row=0, column=0)
entry_n1 = tk.Entry(window)
entry_n1.grid(row=0, column=1)

tk.Label(window, text="Fraction 1 - Denominator:").grid(row=1, column=0)
entry_d1 = tk.Entry(window)
entry_d1.grid(row=1, column=1)

tk.Label(window, text="Fraction 2 - Numerator:").grid(row=2, column=0)
entry_n2 = tk.Entry(window)
entry_n2.grid(row=2, column=1)

tk.Label(window, text="Fraction 2 - Denominator:").grid(row=3, column=0)
entry_d2 = tk.Entry(window)
entry_d2.grid(row=3, column=1)

tk.Button(window, text="Compare Fractions", command=lambda: draw_pie_charts(
    entry_n1.get(), entry_d1.get(), entry_n2.get(), entry_d2.get())
).grid(row=4, column=0, columnspan=2, pady=10)

chart_frame = tk.Frame(window)
chart_frame.grid(row=5, column=0, columnspan=2)

window.mainloop()