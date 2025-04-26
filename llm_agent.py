# llm_agent.py

import google.generativeai as genai
import os
import re
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Set your Gemini API Key (store in env var or paste directly for testing)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# You can load or pass your table schema here
schema_str = """
Table: oee_data
Columns:
- device_id (string)
- location (string)
- date (date)
- operating_time (float)
- planned_production_time (float)
- good_count (integer)
- reject_count (integer)
- ideal_cycle_time (float)
- oee (float)
"""

def extract_sql(text):
    """Extract a valid single-line SQL SELECT statement from the LLM response."""
    match = re.search(r"SELECT\s.+?;", text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(0).strip()
    else:
        return text.strip()  # fallback

def generate_sql_from_nl(question: str) -> str:
    prompt = (
        "You are a helpful assistant that converts natural language to SQL.\n\n"
        f"Table schema:\n{schema_str}\n\n"
        "Generate a valid SQL SELECT query (PostgreSQL style). "
        "Only output the SQL query, nothing else.\n\n"
        f"User question: {question}\nSQL:"
    )

    try:
        chat = genai.GenerativeModel("gemini-1.5-pro-latest").start_chat()
        response = chat.send_message(prompt)
        return extract_sql(response.text)
    except Exception as e:
        return f"-- Error generating SQL: {str(e)}"

