import streamlit as st
import requests
import pandas as pd
import json

@st.cache_data(ttl=300)
def get_user_data(url):
    response = requests.get(url)
    json_data = response.json()
    return json_data

# Create dataframe from ckpool data
@st.cache_data(ttl=300)
def load_pool_data(pool_data):
    df = pd.read_json(pool_data, orient='index')
    return df

# Get ckpool data
@st.cache_data(ttl=300)
def get_pool_data(url):
    response = requests.get(url)

    data_list = []
    lines = response.text.splitlines()
    # lines = response.text.splitlines()[:2] grabs only first two lines

    # Convert each line of response text into a dictionary
    for line in lines:
        data_list.append(json.loads(line))

    # Combine all dictionaries into one
    combined_dict = {}
    for data in data_list:
        combined_dict.update(data)

    # Convert combined dictionary to JSON string
    json_data = combined_dict
    return json_data
