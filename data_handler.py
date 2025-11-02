import pandas as pd
import os

USAGE_FILE = "usage_data.csv"

def load_usage_data():
    if os.path.exists(USAGE_FILE):
        return pd.read_csv(USAGE_FILE)
    else:
        return pd.DataFrame(columns=["username", "date", "instagram", "youtube", "whatsapp", "others"])

def save_usage_data(df):
    df.to_csv(USAGE_FILE, index=False)
