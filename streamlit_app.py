import pandas as pd
import streamlit as st

# Load data
data = pd.read_csv('OWID_homicide-rate_1990-2019.csv')

# Display DataFrame
st.dataframe(data)

# Create a bar chart
# Replace 'Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate)' with the correct column name from your CSV
st.bar_chart(data['Deaths'].value_counts())

# Slider for filtering data by year
selected_range = st.slider('Select a range of years', int(data['Year'].min()), int(data['Year'].max()), (1990, 2019))

# Filter data based on selected year range
filtered_data = data[(data['Year'] >= selected_range[0]) & (data['Year'] <= selected_range[1])]

# You can add more Streamlit components to interact with filtered_data
