import streamlit as st
import datetime

st.title("MusafirAI")

col1, col2 = st.columns(2)

with col1:
    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    d = st.date_input(
        "Your Duration",
        (jan_1, datetime.date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )
    print(d)

with col1:
    option = st.selectbox(
        label="Your Theme",
        options=["Romantic", "Adventure", "Cultural", "Nature", "Relaxation"],
        index=1,
    )
with col2:
    text_entry = st.text_input(
        "Your location",
        placeholder="Rome"
    )

with col2:
    color = st.select_slider(
    "Your max budget",
    options=list(range(100,100000,100))
)


st.button("GENERATE PLAN", type="primary", width="stretch")

