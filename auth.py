import streamlit as st
from database import add_user, validate_user

def login():
    st.subheader("🔐 Login")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_user(u, p):
            st.session_state["user"] = u
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

def signup():
    st.subheader("📝 Signup")
    u = st.text_input("Create Username")
    p = st.text_input("Create Password", type="password")

    if st.button("Signup"):
        add_user(u, p)
        st.success("Account created! Login now.")
