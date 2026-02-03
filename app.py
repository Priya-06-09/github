import streamlit as st
from auth import login, signup
from chatbot import chatbot_response
from image_helper import image_assistance
from patient_tracker import patient_tracker
from vitamin_guide import vitamin_help
from workout_guide import workout_goal

st.set_page_config("Health Assistant")

st.title("🩺 Emergency First Aid & Health Assistant")

if "user" not in st.session_state:
    option = st.selectbox("Choose", ["Login", "Signup"])
    login() if option == "Login" else signup()

else:
    user = st.session_state["user"]
    st.success(f"Welcome {user}")

    menu = st.sidebar.radio("Menu", [
        "First Aid Chatbot",
        "Image Assistance",
        "Patient Tracker",
        "Vitamin Guide",
        "Workout Guide"
    ])

    if menu == "First Aid Chatbot":
        q = st.text_input("Describe your problem")
        if st.button("Get Help"):
            st.write(chatbot_response(q))

    elif menu == "Image Assistance":
        image_assistance()

    elif menu == "Patient Tracker":
        patient_tracker(user)

    elif menu == "Vitamin Guide":
        v = st.selectbox("Select Vitamin", ["Vitamin A","Vitamin B","Vitamin C","Vitamin D","Vitamin E"])
        st.info(vitamin_help(v.lower()))

    elif menu == "Workout Guide":
        goal = st.selectbox("Goal", ["Weight Loss","Muscle Gain","General Fitness"])
        st.write(workout_goal(goal.lower()))

    st.warning("⚠️ This app provides guidance only, not medical diagnosis.")
