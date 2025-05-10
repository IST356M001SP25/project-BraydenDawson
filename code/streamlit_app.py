import streamlit as st
from code.extract import get_weather_data
from code.transform import process_weather_data
import plotly.express as px

st.title("📈 Weather Forecast Dashboard")

city = st.text_input("Enter city", value="Syracuse")
api_key = "02551e4e2aae1c018ddfa4bc99aac05c"  # Use st.secrets in final version

# Refresh toggle
refresh_data = st.checkbox("Force refresh from API", value=False)

if st.button("Get Weather"):
    try:
        raw = get_weather_data(city, api_key, use_cache=not refresh_data)
        df = process_weather_data(raw)

        st.subheader("🌡️ Temperature Over Time")
        st.plotly_chart(px.line(df, x="datetime", y="temperature", title="Temperature (°C)"))

        st.subheader("💧 Humidity Over Time")
        st.plotly_chart(px.line(df, x="datetime", y="humidity", title="Humidity (%)"))

        st.subheader("🌦️ Weather Preview")
        for i in range(0, len(df), 8):  # One icon per day
            row = df.iloc[i]
            st.markdown(f"**{row['datetime'].strftime('%a %b %d %I:%M %p')}**")
            st.image(
                f"http://openweathermap.org/img/wn/{row['icon']}@2x.png",
                width=75,
                caption=row["description"].title()
            )

    except Exception as e:
        if "404" in str(e):
            st.error("❌ City not found. Please check the name and try again.")
        elif "401" in str(e):
            st.error("🔒 Unauthorized. Your API key might be incorrect or expired.")
        else:
            st.error(f"🚨 Something went wrong: {e}")
