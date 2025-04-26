# 📊 GenAI OEE Conversational Dashboard

## Overview

The GenAI OEE (Overall Equipment Efficiency) Conversational Dashboard is a web-based application built with Streamlit that allows users to upload IoT sensor data, calculate OEE for manufacturing devices, and ask natural language questions about the data. The application processes the uploaded data, calculates OEE, and enables users to query the results using natural language to generate SQL queries on the fly.

This tool uses Google Gemini's Generative AI to convert natural language queries into SQL queries, making it easy for users to interact with their OEE data and retrieve useful insights.

## Features

- **Data Upload**: Users can upload an `.xlsx` file containing IoT sensor data for different devices.
  
- **OEE Calculation**: The app computes OEE (Overall Equipment Efficiency) for each device based on the uploaded data, including parameters like Operating Time, Planned Production Time, Good Count, Reject Count, and Ideal Cycle Time.
  
- **SQL Query Generation**: Users can ask natural language questions about the OEE data. The app uses a Generative AI model to convert these questions into SQL queries and execute them on the uploaded data.
  
- **Interactive Dashboard**: The results of SQL queries are displayed interactively within the app, allowing users to explore the data with ease.

## Requirements

- Python 3.7 or higher
- Google Gemini API key (for using Generative AI)

Required Python libraries:

- Streamlit
- pandas
- sqlite3
- google-generativeai
- python-dotenv

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/genai-oee-dashboard.git
   cd genai-oee-dashboard
2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
4. **Set up environment variables:**

   GOOGLE_API_KEY=your_google_api_key_here
5. **Run the application:**

   ```bash
   streamlit run app.py
6. **Open your browser and navigate to http://localhost:8501 to view the app.**

## How to Use

### 1. Upload IoT Sensor Data:

- Click the "Upload .xlsx file" button to upload your IoT sensor data file. The file should contain columns like `Device ID`, `Location`, `Date`, `Operating Time`, `Planned Production Time`, `Good Count`, `Reject Count`, and `Ideal Cycle Time`.

### 2. Ask a Question:

- Once the data is uploaded and processed, you can type a question in the text box like:
  - "What is the average OEE of all devices?"
  - "Which device has the highest OEE?"

- The app will automatically generate the corresponding SQL query and execute it to fetch the results.

### 3. View Results:

- The results will be displayed below the query box, and you can interact with the output directly in the Streamlit interface.

## Sample Questions

- "What is the average OEE of all devices?"
- "Which device has the highest OEE?"
- "What is the total good count for all devices?"
- "Show the OEE values for all devices in Bangalore."
- "What is the OEE for device D024?"



   
