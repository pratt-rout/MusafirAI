import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

from scripts.ai_helper import generate_plan

# """ Optional: User Authentication (commented out for now)"""
# def login_screen():
#     st.header("This app is private.")
#     st.subheader("Please log in.")
#     st.button("Log in with Google", on_click=st.login)

# if not st.user.is_logged_in:
#     login_screen()
# else:
#     st.header(f"Welcome, {st.user.name}!")
#     st.button("Log out", on_click=st.logout)

st.set_page_config(page_title="MusafirAI", page_icon="assets/Musafir.png", layout="wide")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    st.image("assets/Musafir.png", width=200)
with col2:
    st.title("MusafirAI")

col1, col2, col3 = st.columns(3)

with col1:
    start_date = datetime.datetime.now()
    calendar_end_date = start_date + relativedelta(years=10)
    sample_end_date = start_date + relativedelta(days=10)

    date_range = st.date_input(
        "Your Duration*",
        (start_date, sample_end_date),
        min_value = start_date,
        max_value = calendar_end_date,
        format="DD.MM.YYYY",
    )

with col2:
    start_location = st.text_input(
        "Start location*",
        placeholder = "E.g - Mumbai",
    )

with col3:
    end_location = st.text_input(
        "Destination location (s)*",
        placeholder = "E.g - Rome.   If multiple locations, separate by commas. Eg - Rome, Florence",
    )



col1, col2 = st.columns(2)
with col1:
    theme = st.selectbox(
        label="Your Theme*",
        options=["Romantic", "Adventure", "Cultural", "Nature", "Relaxation"],
        index=1,
    )

with col2:
    budget = st.select_slider(
        "Your max budget (INR)*",
    options=list(range(1000,500100,100)),
    value=100000
)

special_request = st.text_input("Special requests (optional)", "", placeholder = "I want to include a spa day")

if date_range and theme and start_location and end_location and budget:
    if st.button("GENERATE ITINERARY", type="primary", width="stretch"):
        output = generate_plan(
            date_range=date_range, 
            theme=theme, 
            start_location=start_location, 
            end_location=end_location, 
            budget=budget, 
            special_request=special_request
        )

        st.markdown(output)




