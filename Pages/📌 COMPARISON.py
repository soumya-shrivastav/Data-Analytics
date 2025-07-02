
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
st.set_page_config(layout="wide")

def load_data():
    return pd.read_csv('dataset.csv')

st.sidebar.image("logo2.png",caption="EmployeeEcho Insights")
theme_plotly = None 

def load_data():
    # Load dataset
    return pd.read_csv('dataset.csv')

def plot_age_vs_fields(df):
    # Create a figure
    fig = go.Figure()

    # Plot age vs weight
    fig.add_trace(go.Bar(
        x=df['age'],
        y=df['Weight'],
        name='Weight',
        marker_color='blue'
    ))

    # Plot age vs height
    fig.add_trace(go.Bar(
        x=df['age'],
        y=df['Height'],
        name='Height',
        marker_color='green'
    ))

    # Plot age vs diabetes status (convert 'Diabetes' to numerical for plotting)
    df['Diabetes_Num'] = df['Diabetes'].map({'Yes': 1, 'No': 0})
    fig.add_trace(go.Bar(
        x=df['age'],
        y=df['Diabetes_Num'],
        name='Diabetes',
        marker_color='red'
    ))

    # Plot age vs sugar level
    fig.add_trace(go.Bar(
        x=df['age'],
        y=df['Sugar_Level'],
        name='Sugar Level',
        marker_color='orange'
    ))

    # Plot age vs gender (convert 'Gender' to numerical for plotting)
    df['Gender_Num'] = df['Gender'].map({'Male': 1, 'Female': 0})
    fig.add_trace(go.Bar(
        x=df['age'],
        y=df['Gender_Num'],
        name='Gender',
        marker_color='purple'
    ))

    # Update layout for stacked bar chart
    fig.update_layout(
        barmode='stack',
        title='age vs Various Health Metrics',
        xaxis_title='age',
        yaxis_title='Value',
        plot_bgcolor='rgba(0,0,0,0)',  # Set background transparency
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),  # Adjust legend position
        autosize=True,
        height=600
    )

    # Show plot
    st.plotly_chart(fig, use_container_width=True)


