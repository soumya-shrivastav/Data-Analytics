import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, norm
import plotly.graph_objects as go
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
st.set_page_config(layout="wide")

def load_data():
    return pd.read_csv('dataset.csv')

st.sidebar.image("logo2.png",caption="EmployeeEcho Insights")
theme_plotly = None 

# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def calculate_age_intervals(max_age):
    intervals = np.arange(0, max_age + 11, 10)  # Adjusted to include maximum age
    labels = [f'{i}-{i+10}' for i in range(0, max_age + 1, 10)]  # Adjusted to include maximum age
    return intervals, labels

def calculate_grouped_statistics(freq_table):
    # Convert 'Age Interval' to numerical midpoints
    def get_midpoint(interval):
        start, end = map(int, interval.split('-'))
        return (start + end) / 2
    
    # Apply midpoint function and ensure numerical type
    freq_table['Midpoint'] = freq_table['Age Interval'].apply(get_midpoint).astype(float)

    # Calculate cumulative frequency
    freq_table['Cumulative Frequency'] = freq_table['Frequency'].cumsum()

    # Calculate mean
    mean_grouped = (freq_table['Midpoint'] * freq_table['Frequency']).sum() / freq_table['Frequency'].sum()

    # Calculate mode class
    mode_class = freq_table.loc[freq_table['Frequency'].idxmax()]['Age Interval']
    mode_class_start, mode_class_end = map(int, mode_class.split('-'))
    mode_freq = freq_table.loc[freq_table['Age Interval'] == mode_class, 'Frequency'].values[0]
    cumulative_freq_before = freq_table['Frequency'].cumsum().loc[freq_table['Age Interval'] == mode_class].values[0] - mode_freq
    mode = mode_class_start + ((mode_freq - cumulative_freq_before) / (2 * mode_freq)) * (mode_class_end - mode_class_start)

    # Calculate median
    total_freq = freq_table['Frequency'].sum()
    cumulative_freq = freq_table['Cumulative Frequency']
    median_class = freq_table.loc[cumulative_freq >= (total_freq / 2)].iloc[0]['Age Interval']
    median_class_start, median_class_end = map(int, median_class.split('-'))
    median_freq = freq_table.loc[freq_table['Age Interval'] == median_class, 'Frequency'].values[0]
    cumulative_freq_before = cumulative_freq[freq_table['Age Interval'] == median_class].values[0] - median_freq
    median = median_class_start + ((total_freq / 2 - cumulative_freq_before) / median_freq) * (median_class_end - median_class_start)

    # Calculate variance
    variance = ((freq_table['Midpoint'] - mean_grouped)**2 * freq_table['Frequency']).sum() / freq_table['Frequency'].sum()
    std_dev = np.sqrt(variance)

    # Calculate skewness
    skewness_grouped = skew(freq_table['Midpoint'].repeat(freq_table['Frequency']))

    # Calculate kurtosis
    kurtosis_value = kurtosis(freq_table['Midpoint'].repeat(freq_table['Frequency']))

    # Calculate IQR
    Q1 = freq_table.loc[freq_table['Frequency'].cumsum() >= (total_freq * 0.25)].iloc[0]['Midpoint']
    Q3 = freq_table.loc[freq_table['Frequency'].cumsum() >= (total_freq * 0.75)].iloc[0]['Midpoint']
    IQR = Q3 - Q1

    # Calculate standard error
    standard_error = std_dev / np.sqrt(freq_table['Frequency'].sum())

    return mean_grouped, mode, mode_class, median, skewness_grouped, kurtosis_value, IQR, std_dev, standard_error, median_class, variance


