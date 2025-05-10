# About My Project

Student Name:  Brayden Dawson
Student Email:  Bcdawson@syr.edu

### What it does
This is a weather dashboard that allows users to enter a city name and see a 5-day forecast for temperature and humidity. The app includes interactive line charts and weather condition icons. It uses the OpenWeatherMap API and includes caching to improve speed and reduce unnecessary API calls.

### How you run my project
1. Open a terminal and navigate to the project folder.

2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate

3. Run the Streamlit app:
    streamlit run streamlit_app.py
4. Type in a city and click "Get Weather" to see forecast charts and daily weather icons.

Optional: If you want to force new data from the API, check the "Force refresh from API" box.

5. To run the unit tests: 
        pytest tests/


### Other things you need to know

Cached data is saved in the cache/ folder, one file per city.

API requests use OpenWeatherMap’s free 5-day/3-hour forecast endpoint.

You can optionally store your API key in .streamlit/secrets.toml if preferred.

The app uses Python modules, pandas for data processing, Plotly for visualizations, and Streamlit for the interface.

