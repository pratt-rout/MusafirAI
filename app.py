import streamlit as st
import datetime
from ai_helper import generate_plan

st.set_page_config(page_title="MusafirAI", page_icon="Musafir.png", layout="wide")
st.title("MusafirAI")


col1, col2 = st.columns(2)

with col1:
    today = datetime.datetime.now()
    next_year = today.year + 1
    dec_31 = datetime.date(next_year, 12, 31)

    date_range = st.date_input(
        "Your Duration",
        (today, datetime.date(next_year, 1, 7)),
        today,
        dec_31,
        format="DD.MM.YYYY",
    )

with col1:
    theme = st.selectbox(
        label="Your Theme",
        options=["Romantic", "Adventure", "Cultural", "Nature", "Relaxation"],
        index=1,
    )
with col2:
    location = st.text_input(
        "Your location",
        "Rome"
    )

with col2:
    budget = st.select_slider(
    "Your max budget",
    options=list(range(1000,500100,100))
)


if st.button("GENERATE PLAN", type="primary", width="stretch"):
    output = generate_plan(date_range, theme, location, budget)
    st.markdown(output)


