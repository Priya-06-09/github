import streamlit as st
import sqlite3
from PIL import Image
from datetime import date

# ---------------- DATABASE ----------------
conn = sqlite3.connect("health_app.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS patient_data (
    username TEXT,
    condition TEXT,
    next_checkup TEXT
)
""")
conn.commit()

# ---------------- DATA ----------------
FIRST_AID = {
    "cut": [
        "Wash hands",
        "Clean wound with clean water",
        "Apply antiseptic",
        "Cover with bandage"
    ],
    "burn": [
        "Cool under running water for 10 minutes",
        "Apply aloe vera or burn ointment",
        "Cover loosely with sterile gauze",
        "Do not pop blisters"
    ],
    "fever": [
        "Check temperature",
        "Give paracetamol",
        "Drink plenty of fluids",
        "Consult doctor if fever persists"
    ]
}

VITAMINS = {
    "vitamin a": "Carrots, spinach, milk",
    "vitamin b": "Eggs, bananas, whole grains",
    "vitamin c": "Oranges, lemon, amla",
    "vitamin d": "Sunlight, fish, milk",
    "vitamin e": "Nuts, seeds, spinach"
}

WORKOUTS = {
    "weight loss": ["Walking", "Skipping", "Cycling", "Plank"],
    "muscle gain": ["Pushups", "Squats", "Deadlifts"],
    "general fitness": ["Yoga", "Stretching", "Jogging"]
}

# ---------------- FUNCTIONS ----------------
def add_user(u, p):
    c.execute("INSERT INTO users VALUES (?,?)", (u, p))
    conn.commit()

def validate_user(u, p):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    return c.fetchone()

def chatbot_response(text):
    text = text.lower()
    for injury in FIRST_AID:
        if injury in text:
            steps = FIRST_AID[injury]
            return "\n".join([f"{i+1}. {s}" for i, s in enumerate(steps)])
    return "Please consult a medical professional if symptoms are serious."

def save_patient_data(user, condition, checkup):
    c.execute("INSERT INTO patient_data VALUES (?,?,?)",
              (user, condition, str(checkup)))
    conn.commit()

def get_patient_data(user):
    c.execute("SELECT * FROM patient_data WHERE username=?", (user,))
    return c.fetchall()

# ---------------- UI ----------------
st.set_page_config(page_title="Health Assistant App")
st.title("🩺 Emergency First Aid & Health Assistant")

# -------- LOGIN / SIGNUP --------
if "user" not in st.session_state:

    option = st.selectbox("Choose", ["Login", "Signup"])

    if option == "Login":
        st.subheader("🔐 Login")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login"):
            if validate_user(u, p):
                st.session_state["user"] = u
                st.success("Login successful")
            else:
                st.error("Invalid credentials")

    else:
        st.subheader("📝 Signup")
        u = st.text_input("Create Username")
        p = st.text_input("Create Password", type="password")

        if st.button("Signup"):
            add_user(u, p)
            st.success("Account created! Login now.")

# -------- MAIN APP --------
else:
    user = st.session_state["user"]
    st.success(f"Welcome {user}")

    menu = st.sidebar.radio(
        "Menu",
        [
            "First Aid Chatbot",
            "Image Assistance",
            "Patient Checkup Tracker",
            "Vitamin Guide",
            "Workout Guide"
        ]
    )

    # ---- CHATBOT ----
    if menu == "First Aid Chatbot":
        st.subheader("💬 First Aid Chatbot")
        q = st.text_input("Describe the injury or problem")
        if st.button("Get Guidance"):
            st.write(chatbot_response(q))

    # ---- IMAGE ----
    elif menu == "Image Assistance":
        st.subheader("📸 Injury Image Assistance")
        img = st.file_uploader("Upload injury image", type=["jpg", "png"])
        if img:
            image = Image.open(img)
            st.image(image)
            st.info(
                "Clean the area, apply antiseptic, "
                "and consult a doctor if swelling or bleeding continues."
            )

    # ---- PATIENT TRACKER ----
    elif menu == "Patient Checkup Tracker":
        st.subheader("📅 Patient Treatment Tracker")

        condition = st.text_input("Condition")
        checkup = st.date_input("Next Checkup Date")

        if st.button("Save Checkup"):
            save_patient_data(user, condition, checkup)
            st.success("Checkup saved")

        records = get_patient_data(user)
        if records:
            st.warning("Upcoming Checkups")
            for r in records:
                st.write(f"Condition: {r[1]} | Date: {r[2]}")

    # ---- VITAMINS ----
    elif menu == "Vitamin Guide":
        st.subheader("🥗 Vitamin Deficiency Guide")
        v = st.selectbox(
            "Select Vitamin",
            ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "Vitamin E"]
        )
        st.info(VITAMINS[v.lower()])

    # ---- WORKOUT ----
    elif menu == "Workout Guide":
        st.subheader("🏋️ Gym Workout Guidance")
        goal = st.selectbox(
            "Select Goal",
            ["Weight Loss", "Muscle Gain", "General Fitness"]
        )
        for w in WORKOUTS[goal.lower()]:
            st.write("•", w)

    st.warning(
        "⚠️ This app provides guidance only. "
        "It does NOT replace professional medical advice."
    )
