import streamlit as st
import pandas as pd
import altair as alt
from datetime import date
from data_handler import load_usage_data, save_usage_data

DAILY_LIMIT = 180  # 3 hours

def usage_form(username):
    st.markdown("### 🕒 Enter Today’s Usage")
    usage_df = load_usage_data()

    with st.form("usage_form"):
        today = date.today()
        instagram = st.number_input("📸 Instagram (mins)", min_value=0, max_value=1440)
        youtube = st.number_input("▶️ YouTube (mins)", min_value=0, max_value=1440)
        whatsapp = st.number_input("💬 WhatsApp (mins)", min_value=0, max_value=1440)
        others = st.number_input("🌐 Other Apps (mins)", min_value=0, max_value=1440)
        submit = st.form_submit_button("Save Data")

    if submit:
        new = pd.DataFrame([[username, today, instagram, youtube, whatsapp, others]],
                           columns=["username", "date", "instagram", "youtube", "whatsapp", "others"])
        usage_df = pd.concat([usage_df, new], ignore_index=True)
        save_usage_data(usage_df)
        st.success("✅ Your data has been saved!")


def show_analysis(username):
    st.markdown("### 📊 Your Screen Time Analysis")
    df = load_usage_data()
    user_data = df[df["username"] == username]

    if user_data.empty:
        st.info("No usage data found yet. Please add your records.")
        return

    user_data["total_time"] = user_data[["instagram", "youtube", "whatsapp", "others"]].sum(axis=1)
    avg_usage = user_data[["instagram", "youtube", "whatsapp", "others"]].mean().round(1)
    total_avg = avg_usage.sum()

    st.write("#### 📅 Average Daily Usage (minutes)")
    st.bar_chart(avg_usage)

    chart = alt.Chart(user_data).mark_line(point=True, color="#D3F149").encode(
        x="date:T", y="total_time:Q", tooltip=["date", "total_time"]
    ).properties(width=700, height=350, title="Daily Total Screen Time")

    st.altair_chart(chart, use_container_width=True)

    # Screen time messages
    st.write("#### 💬 Result:")
    if total_avg > DAILY_LIMIT:
        st.error("🚨 You are over the 3-hour daily limit! Try to reduce usage.")
    elif total_avg > 150:
        st.warning("⚠️ You are close to your daily limit. Be careful!")
    elif total_avg > 60:
        st.success("✅ You are maintaining a balanced usage!")
    else:
        st.balloons()
        st.success("🎉 Excellent! Very healthy screen habits.")
