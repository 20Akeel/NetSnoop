import streamlit as st
import pandas as pd

st.title("📊 NetSnoop Intrusion Detection Dashboard")

try:
    df = pd.read_csv("logs/netsnoop_log.csv", names=["Source IP", "Destination IP", "Port", "Status"])
    st.dataframe(df.tail(50))
    st.bar_chart(df["Status"].value_counts())
except Exception as e:
    st.error(f"Error reading log: {e}")
