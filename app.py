import streamlit as st

col1, col2 = st.columns(2)
with col1:
    option = st.selectbox(
        "Choose an option",
        ("Option 1", "Option 2", "Option 3"),
        label_visibility="collapsed"  # Hide label if you want a cleaner look
    )
with col2:
    text_entry = st.text_input(
        "",
        placeholder="Enter text here"
    )