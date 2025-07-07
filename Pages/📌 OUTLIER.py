import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm, zscore
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
import plotly.express as px

# Set page configuration for wide layout
st.set_page_config(layout="wide")

# Custom CSS for sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #103F7A;
    }
    [data-testid="stSidebar"] * {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with header
with st.sidebar:
    st.header("DASHBOARD")

# Main title and description
st.title('DATA SCIENCE')
st.title("Outlier Detection Techniques")
st.write("""
This app detects anomalies in the 'age' column of a dataset using multiple outlier detection techniques:
- **Isolation Forest | Contamination**
- **Local Outlier Factor (LOF)**
- **Normal Distributions and Z-scores (X~N(0:1))**
- **Quartiles**
- **Percentile-Based Method**
- **Outliers Treatment Techniques [Winsorization]**       
""")

### Normal Distribution & Z-Scores Section
st.success("## 1. Normal Distribution & Z-scores")

# Load dataset
df = pd.read_csv('dataset.csv')

# Get min and max age for plotting
max_age = df['age'].max()
min_age = df['age'].min()

# Create figure for PDF
fig_pdf = go.Figure()

# Plot Normal distribution curve
x_values = np.linspace(min_age, max_age, 100)
normal_pdf = norm.pdf(x_values, df['age'].mean(), df['age'].std())
fig_pdf.add_trace(go.Scatter(x=x_values, y=normal_pdf, mode='lines', name='Normal Distribution', line=dict(color='blue')))

# Highlight outliers using z-scores
z_scores = zscore(df['age'])
outliers = df[(z_scores < -3) | (z_scores > 3)]
fig_pdf.add_trace(go.Scatter(x=outliers['age'], y=[0]*len(outliers), mode='markers', name='Outliers', marker=dict(color='red', size=10)))

# Update PDF figure layout
fig_pdf.update_layout(title='Probability Density Function (PDF) of Age', xaxis_title='Age', yaxis_title='Density', showlegend=True)
st.plotly_chart(fig_pdf, use_container_width=True)

# Create layout for Box Plot and Outlier Values
a, b = st.columns([3, 1])

