🌞 Solar Power Generation Prediction App
This project is a Streamlit web application that predicts solar power generation using a Random Forest Regressor model trained on weather and environmental data.
📖Description
"Streamlit app for predicting solar power generation using a Random Forest Regressor. Users can input weather conditions (temperature, wind, humidity, visibility, sky cover, pressure, etc.) to estimate solar output. Includes deployment script, dataset, and trained model."
📖 Dataset
The dataset solarpowergeneration.csv contains historical weather and environmental features used to train the model for predicting solar power generation.
Columns include:
⏱️ distance-to-solar-noon – time difference from solar noon (hours)
🌡️ temperature – ambient temperature (°C)
🧭 wind-direction – wind direction (encoded from N, NE, E, …)
💨 wind-speed – wind speed (m/s)
☁️ sky-cover – percentage of sky covered by clouds (%)
👁️ visibility – visibility distance (km)
💧 humidity – relative humidity (%)
💨 average-wind-speed-(period) – average wind speed over a period (m/s)
📈 average-pressure-(period) – average air pressure over a period (hPa)
🔋 Target – solar power generation (output variable, continuous)
