import streamlit as st
import pandas as pd
from data_handler import load_usage_data

def show_admin_panel():
    st.header("👑 Admin Dashboard")

    data = load_usage_data()
    if data.empty:
        st.info("No data available yet.")
        return

    st.dataframe(data)

    summary = data.groupby("username")[["instagram", "youtube", "whatsapp", "others"]].mean().round(1)
    summary["Total Avg"] = summary.sum(axis=1)

    st.subheader("📊 User Summary")
    st.dataframe(summary)

    st.bar_chart(summary["Total Avg"])
