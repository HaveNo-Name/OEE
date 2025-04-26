# app.py

import streamlit as st
import pandas as pd
import sqlite3
from llm_agent import generate_sql_from_nl
import pandas as pd
from oee_utils import calculate_oee

st.set_page_config(page_title="GenAI OEE Dashboard", layout="centered")

st.title("📊 GenAI OEE Conversational Dashboard")

# Step 1: Upload Excel File
st.header("1️⃣ Upload IoT Sensor Data")
uploaded_file = st.file_uploader("Upload .xlsx file", type=["xlsx"])


if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("Data uploaded & processed!")
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

     # Compute OEE for each row
    df["OEE"] = df.apply(calculate_oee, axis=1)

    # Save to session or temp file or database
    st.session_state["oee_df"] = df
    # Preview data
    st.dataframe(df.head())

    # Save to SQLite
    conn = sqlite3.connect("oee_data.db")
    df.to_sql("oee_data", conn, if_exists="replace", index=False)

    # Step 2: Ask NL Question
    st.header("2️⃣ Ask a question about the OEE data")
    user_query = st.text_input("e.g., What is the average OEE of all devices?")

    if st.button("Run Query"):
        with st.spinner("Generating SQL from your question..."):
            sql_query = generate_sql_from_nl(user_query)
        
        st.code(sql_query, language="sql")

        try:
            result_df = pd.read_sql_query(sql_query, conn)
            st.success("✅ Query successful!")
            st.dataframe(result_df)
        except Exception as e:
            st.error(f"❌ Failed to execute SQL: {e}")
