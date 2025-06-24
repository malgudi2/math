import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from random import randint

st.set_page_config(layout="wide")
st.markdown("<h2 style='text-align:center;'>Explore Subtracting a Negative Number</h2>", unsafe_allow_html=True)

# Session state
if "a" not in st.session_state:
    st.session_state.a = 3
    st.session_state.b = -3
    st.session_state.score = 0
    st.session_state.revealed = False
    st.session_state.feedback = ""

# Try This! button
if st.button("🎲 Try This!"):
    st.session_state.a = randint(-10, 10)
    st.session_state.b = randint(-10, 10)
    st.session_state.revealed = False
    st.session_state.feedback = ""

# Sliders (adjustable)
a = st.slider("Choose the first number (a)", -10, 10, st.session_state.a, key="slider_a")
b = st.slider("Choose the second number to subtract (b)", -10, 10, st.session_state.b, key="slider_b")

# Expression and result
expression = f"{a} - ({b})"
result = a - b

# Guess input
guess = st.number_input("What’s your guess for the result?", step=1, format="%d")

# Submit answer
if st.button("Submit Answer"):
    if guess == result:
        st.session_state.score += 1
        st.session_state.feedback = "✅ Correct! Streak: " + str(st.session_state.score)
    else:
        st.session_state.score = 0
        st.session_state.feedback = f"❌ Oops! The correct answer was {result}. Try again!"
    st.session_state.revealed = True

# Feedback
if st.session_state.feedback:
    st.markdown(f"<div style='font-size:20px; font-weight:bold; color:#333;'>{st.session_state.feedback}</div>", unsafe_allow_html=True)

# Number line plot
x_range = np.arange(min(a, result) - 3, max(a, result) + 4)
fig, ax = plt.subplots(figsize=(10, 2))
ax.axhline(0, color='black')
ax.set_xticks(x_range)
ax.set_yticks([])
ax.set_ylim(-1, 1)

# Annotate movement
ax.annotate("", xy=(result, 0), xytext=(a, 0),
            arrowprops=dict(arrowstyle="->", lw=2, color="blue"))
ax.plot(a, 0, 'o', color='blue')
ax.plot(result, 0, 'o', color='green')
ax.text(a, 0.3, f"Start: {a}", ha='center')
ax.text(result, 0.3, f"Result: {result}", ha='center')
ax.text((a + result) / 2, -0.5, f"Move {'right' if b < 0 else 'left'} by {abs(b)}", ha='center', fontsize=12, color='blue')

st.pyplot(fig)

# Final reveal
if st.session_state.revealed:
    st.markdown(
        f"<div style='font-size:24px;'><b>Expression:</b> {expression} = {result}</div>",
        unsafe_allow_html=True
    )

