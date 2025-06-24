import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# App styling
st.set_page_config(layout="wide")
st.markdown(
    "<style>"
    "body, div, p, label, input, span, button, h1, h2, h3, h4 { font-size:24px !important; }"
    "</style>",
    unsafe_allow_html=True
)

st.markdown("<h2 style='text-align:center;'>Adding Two Decimal Numbers Visually</h2>", unsafe_allow_html=True)

# Input sliders
a = st.slider("Select first number (red)", 0.0, 1.0, 0.3, step=0.01)
b = st.slider("Select second number (blue)", 0.0, 1.0, 0.4, step=0.01)
total = a + b if a + b <= 1.0 else 1.0

# Grid settings: 10x10 (100 squares)
grid_size = 10
total_squares = int(total * 100)
a_squares = int(a * 100)
b_squares = int(b * 100)

# Draw tiny figure (1/16 area)
fig, ax = plt.subplots(figsize=(0.75, 0.75))  # Shrunk dimensions
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Populate grid squares
for i in range(100):
    row = 9 - i // 10
    col = i % 10
    if i < a_squares:
        color = 'red'
    elif i < a_squares + b_squares:
        color = 'blue'
    else:
        color = 'lightgray'
    rect = patches.Rectangle((col, row), 1, 1, facecolor=color, edgecolor='black', linewidth=0.3)
    ax.add_patch(rect)

# Center the tiny figure
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    st.pyplot(fig)

# Display result
st.markdown(f"<div style='font-size:24px; text-align:center;'>Sum: {a:.2f} + {b:.2f} = {a + b:.2f}</div>", unsafe_allow_html=True)