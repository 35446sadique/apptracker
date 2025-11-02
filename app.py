import streamlit as st
from auth import login_user, register_user
from ui_components import usage_form, show_analysis
from admin_panel import show_admin_panel

# ------------------------------------------
# Page setup
# ------------------------------------------
st.set_page_config(page_title="Social Media Usage Analyzer", page_icon="📱", layout="centered")

st.markdown("""
    <style>
        body {
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align:center;
            font-size: 35px;
            color: red;
            font-weight: 700;
            margin-bottom: -10px;
        }
        .subtitle {
            text-align:center;
            color: red;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: yellow;
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 8px;
            font-weight: 500;
        }
        .stButton>button:hover {
            background-color: red;
            transform: scale(1.02);
        }
        .stTextInput>div>div>input {
            border: 1px solid #0078D7;
            border-radius: 6px;
        }
        .footer {
            text-align:center;
            font-size: 13px;
            color: pink;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📱 Social Media Usage Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track • Analyze • Control Your Screen Time</div>", unsafe_allow_html=True)

menu = ["Login", "Sign Up", "Admin"]
choice = st.sidebar.selectbox("Menu", menu)

# ------------------------------------------
# Sign Up Page
# ------------------------------------------
if choice == "Sign Up":
    st.subheader("🆕 Create a New Account")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Register"):
        register_user(username, password)

# ------------------------------------------
# Login Page
# ------------------------------------------
elif choice == "Login":
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(username, password):
            st.success(f"Welcome, {username}! 👋")
            st.session_state["user"] = username
        else:
            st.error("Invalid username or password")

    if "user" in st.session_state:
        option = st.sidebar.radio("Select", ["Enter Usage", "View Analysis"])
        if option == "Enter Usage":
            usage_form(st.session_state["user"])
        else:
            show_analysis(st.session_state["user"])

# ------------------------------------------
# Admin Page
# ------------------------------------------
elif choice == "Admin":
    st.subheader("👑 Admin Panel")
    admin_pass = st.text_input("Enter Admin Password", type="password")
    if st.button("Access"):
        if admin_pass == "admin123":
            show_admin_panel()
        else:
            st.error("Incorrect Admin Password!")

st.markdown("<div class='footer'>Developed by Mohammed Sadique | BCA Project</div>", unsafe_allow_html=True)
