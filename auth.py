import streamlit as st
import pandas as pd
import os

USER_FILE = "users.csv"

def load_users():
    if os.path.exists(USER_FILE):
        return pd.read_csv(USER_FILE)
    else:
        return pd.DataFrame(columns=["username", "password"])

def save_users(df):
    df.to_csv(USER_FILE, index=False)

def register_user(username, password):
    users = load_users()
    if username in users["username"].values:
        st.warning("Username already exists. Please choose another.")
    else:
        new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
        users = pd.concat([users, new_user], ignore_index=True)
        save_users(users)
        st.success("Registration successful! Please go to Login page.")

def login_user(username, password):
    users = load_users()
    user = users[(users["username"] == username) & (users["password"] == password)]
    return not user.empty
