import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

from ai_helper import generate_plan

st.set_page_config(page_title="MusafirAI", page_icon="Musafir.png", layout="wide")
st.title("MusafirAI")


col1, col2 = st.columns(2)

with col1:
    start_date = datetime.datetime.now()
    calendar_end_date = start_date + relativedelta(years=10)
    sample_end_date = start_date + relativedelta(days=10)

    date_range = st.date_input(
        "Your Duration",
        (start_date, sample_end_date),
        min_value = start_date,
        max_value = calendar_end_date,
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
        "Your location (s)",
        "Rome"
    )

with col2:
    budget = st.select_slider(
    "Your max budget",
    options=list(range(1000,500100,100)),
    value=100000
)

special_request = st.text_input("Special requests (optional)", "", placeholder = "I want to include a spa day")

if st.button("GENERATE ITINERARY", type="primary", width="stretch"):
    output = generate_plan(
        date_range=date_range, 
        theme=theme, 
        location=location, 
        budget=budget, 
        special_request=special_request
    )

    # st.markdown(output, unsafe_allow_html=True)
    st.markdown(output)



