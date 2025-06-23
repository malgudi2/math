import streamlit as st
import matplotlib.pyplot as plt
from fractions import Fraction

# Initial values
initial_vinegar = 100
max_oil = 200

st.set_page_config(layout="wide")

# Inject CSS to style the slider label
st.markdown(
    """
    <style>
    div[class*="stSlider"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

oil_amount = st.slider("Adjust Oil Amount (mL)", 0, max_oil, 10)
total_volume = oil_amount + initial_vinegar
ratio_fraction = Fraction(oil_amount, initial_vinegar).limit_denominator()

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    sizes = [oil_amount, initial_vinegar]
    labels = [f"Oil ({oil_amount} mL)", f"Vinegar ({initial_vinegar} mL)"]
    colors = ['goldenrod', 'saddlebrown']
    ax1.pie(sizes, labels=labels, colors=colors, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    ax2.bar(['Mixture'], [total_volume], width=0.3, color='mediumslateblue')
    ax2.set_ylim(0, initial_vinegar + max_oil + 20)
    ax2.set_ylabel("Milliliters")
    ax2.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig2)

st.markdown(
    f"<div style='font-size:24px; font-weight:bold;'>Oil-to-Vinegar Ratio: {oil_amount}:{initial_vinegar} = {ratio_fraction}</div>",
    unsafe_allow_html=True
)