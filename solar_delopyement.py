#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import pickle
import  warnings
warnings.filterwarnings('ignore')


# In[21]:


model=pickle.load(open('solar.pkl','rb'))
model


# In[22]:


st.title("☀️ Solar Power Generation Prediction App using Random Forest Regressor")


# In[26]:


def user_input_variables():
    distance_to_solar_noon = st.number_input("Enter distance-to-solar-noon (in hours)", value=0.0 )
    temperature = st.number_input("Enter temperature (°C)", value=25.0)
    wind_direction = st.selectbox("Select wind direction", ["N", "NE", "E", "SE", "S", "SW", "W", "NW"])
    wind_direction_map = {"N": 0, "NE": 1, "E": 2, "SE": 3, "S": 4, "SW": 5, "W": 6, "NW": 7}
    wind_direction_encoded = wind_direction_map[wind_direction]
    wind_speed = st.number_input("Enter wind speed (m/s)", value=0.0, min_value=0.0)
    sky_cover = st.number_input("Enter sky cover (%)", min_value=0.0, max_value=100.0, value=0.0)
    visibility = st.number_input("Enter visibility (km)", min_value=0.0, value=10.0)
    humidity = st.number_input("Enter humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
    average_wind_speed_period = st.number_input("Enter average wind speed (m/s)", min_value=0.0, value=0.0)
    average_pressure_period = st.number_input("Enter average pressure (hPa)", min_value=0.0, value=1013.0)

    # Data dictionary must have numeric values
    data = {
        "distance_to_solar_noon": distance_to_solar_noon,
        "temperature": temperature,
        "wind_direction": wind_direction_encoded,  # encoded value
        "wind_speed": wind_speed,
        "sky_cover": sky_cover,
        "visibility": visibility,
        "humidity": humidity,
        "average_wind_speed_period": average_wind_speed_period,
        "average_pressure_period": average_pressure_period
    }
    features = pd.DataFrame(data, index=[0])
    return features


# Get user input
df = user_input_variables()

# Prediction
predicted = model.predict(df)

# Display
st.subheader("Predicted Value")
st.write(predicted[0])   # show single value


# In[16]:





# In[ ]:




