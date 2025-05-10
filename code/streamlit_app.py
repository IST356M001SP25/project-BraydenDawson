import streamlit as st
from code.extract import get_weather_data
from code.transform import process_weather_data
import plotly.express as px
import requests

st.title("📈 Weather Forecast Dashboard")

# Inputs
city = st.text_input("Enter city", value="Syracuse")
api_key = "02551e4e2aae1c018ddfa4bc99aac05c"  # Or use st.secrets["OWM_API_KEY"]
refresh_data = st.checkbox("Force refresh from API", value=False)

# Single button
if st.button("Get Weather"):
    use_cache = not refresh_data

    try:
        raw = get_weather_data(city, api_key, use_cache=use_cache)
        df = process_weather_data(raw)

        st.success(f"✅ Loaded weather for {city.title()} ({'cached' if use_cache else 'fresh from API'})")

        # Charts
        st.subheader("🌡️ Temperature Over Time")
        st.plotly_chart(px.line(df, x="datetime", y="temperature", title="Temperature (°C)"))

        st.subheader("💧 Humidity Over Time")
        st.plotly_chart(px.line(df, x="datetime", y="humidity", title="Humidity (%)"))

        # Icon Preview
        st.subheader("🌦️ Weather Preview")
        for i in range(0, len(df), 8):  # One icon per day
            row = df.iloc[i]
            st.markdown(f"**{row['datetime'].strftime('%a %b %d %I:%M %p')}**")
            st.image(
                f"http://openweathermap.org/img/wn/{row['icon']}@2x.png",
                width=75,
                caption=row["description"].title()
            )

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 404:
            st.error("❌ City not found. Please check the name and try again.")
        elif status_code == 401:
            st.error("🔒 Unauthorized. Please check your API key.")
        else:
            st.error(f"🌐 HTTP Error {status_code}")
    except Exception as e:
        st.error(f"🚨 Unexpected error: {e}")
