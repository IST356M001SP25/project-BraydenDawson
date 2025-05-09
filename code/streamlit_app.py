import streamlit as st
from code.extract import get_weather_data
from code.transform import process_weather_data
import plotly.express as px

st.title("📈 Weather Forecast Dashboard")

city = st.text_input("Enter city", value="Syracuse")
api_key = st.secrets["OWM_API_KEY"]

if st.button("Get Weather"):
    try:
        raw = get_weather_data(city, api_key)
        df = process_weather_data(raw)

        st.subheader("Temperature Over Time")
        st.plotly_chart(px.line(df, x="datetime", y="temperature", title="Temperature (°C)"))

        st.subheader("Humidity Over Time")
        st.plotly_chart(px.line(df, x="datetime", y="humidity", title="Humidity (%)"))

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        
st.write("Using API key:", api_key)  # Add this just for debugging
