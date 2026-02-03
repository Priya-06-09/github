import streamlit as st
from database import save_patient_data, get_patient_data
from datetime import date

def patient_tracker(username):
    st.subheader("📅 Patient Treatment Tracker")

    condition = st.text_input("Condition")
    checkup = st.date_input("Next Checkup Date")

    if st.button("Save"):
        save_patient_data(username, str(checkup), condition)
        st.success("Saved successfully")

    records = get_patient_data(username)
    if records:
        st.warning("Upcoming Checkups:")
        for r in records:
            st.write(f"Condition: {r[2]} | Date: {r[1]}")
